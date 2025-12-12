// Azure OpenAI Chat Completion Example
// This demonstrates how to use Azure OpenAI for chat completions
// with proper configuration, error handling, and best practices.

using Azure;
using Azure.AI.OpenAI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;

namespace PromptPlaybook.Samples;

/// <summary>
/// Azure OpenAI configuration settings
/// </summary>
public class AzureOpenAISettings
{
    public string Endpoint { get; set; } = string.Empty;
    public string Key { get; set; } = string.Empty;
    public string DeploymentName { get; set; } = string.Empty;
}

/// <summary>
/// Service for interacting with Azure OpenAI chat completions
/// </summary>
public class ChatCompletionService
{
    private readonly OpenAIClient _client;
    private readonly string _deploymentName;
    private readonly ILogger<ChatCompletionService> _logger;

    public ChatCompletionService(AzureOpenAISettings settings, ILogger<ChatCompletionService> logger)
    {
        _client = new OpenAIClient(
            new Uri(settings.Endpoint),
            new AzureKeyCredential(settings.Key));
        _deploymentName = settings.DeploymentName;
        _logger = logger;
    }

    /// <summary>
    /// Send a chat completion request to Azure OpenAI
    /// </summary>
    /// <param name="userMessage">The user's input message</param>
    /// <param name="systemPrompt">Optional system prompt to set AI behavior</param>
    /// <param name="temperature">Sampling temperature (0.0 to 2.0)</param>
    /// <param name="maxTokens">Maximum tokens in the response</param>
    /// <returns>The AI's response content</returns>
    public async Task<string> GetChatCompletionAsync(
        string userMessage,
        string? systemPrompt = null,
        float temperature = 0.7f,
        int maxTokens = 1000)
    {
        _logger.LogInformation("Sending chat completion request to deployment: {Deployment}", _deploymentName);

        var chatOptions = new ChatCompletionsOptions
        {
            DeploymentName = _deploymentName,
            Temperature = temperature,
            MaxTokens = maxTokens
        };

        if (!string.IsNullOrEmpty(systemPrompt))
        {
            chatOptions.Messages.Add(new ChatRequestSystemMessage(systemPrompt));
        }

        chatOptions.Messages.Add(new ChatRequestUserMessage(userMessage));

        try
        {
            Response<ChatCompletions> response = await _client.GetChatCompletionsAsync(chatOptions);
            
            var result = response.Value.Choices[0].Message.Content;
            var usage = response.Value.Usage;
            
            _logger.LogInformation(
                "Received response with {TotalTokens} total tokens (Prompt: {PromptTokens}, Completion: {CompletionTokens})",
                usage.TotalTokens, usage.PromptTokens, usage.CompletionTokens);

            return result;
        }
        catch (RequestFailedException ex)
        {
            _logger.LogError(ex, "Azure OpenAI request failed with status {Status}", ex.Status);
            throw;
        }
    }

    /// <summary>
    /// Summarize the given text using Azure OpenAI
    /// </summary>
    public async Task<string> SummarizeTextAsync(string text, int maxSentences = 3)
    {
        var systemPrompt = $"""
            You are a skilled summarizer. 
            Create a concise summary of the provided text in {maxSentences} sentences or fewer.
            Focus on the key points and main ideas.
            """;

        var userMessage = $"Please summarize the following text:\n\n{text}";

        return await GetChatCompletionAsync(userMessage, systemPrompt, temperature: 0.3f);
    }

    /// <summary>
    /// Classify the given text into one of the provided categories
    /// </summary>
    public async Task<string> ClassifyTextAsync(string text, IEnumerable<string> categories)
    {
        var categoriesStr = string.Join(", ", categories);

        var systemPrompt = $"""
            You are a text classifier.
            Classify the given text into exactly one of these categories: {categoriesStr}
            Respond with only the category name, nothing else.
            """;

        var userMessage = $"Classify this text:\n\n{text}";

        return await GetChatCompletionAsync(userMessage, systemPrompt, temperature: 0.0f);
    }
}

class Program
{
    static async Task Main(string[] args)
    {
        // Build configuration
        var configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("appsettings.json", optional: true)
            .AddJsonFile("appsettings.Development.json", optional: true)
            .AddEnvironmentVariables()
            .Build();

        // Setup logging
        using var loggerFactory = LoggerFactory.Create(builder =>
        {
            builder.AddConsole();
            builder.SetMinimumLevel(LogLevel.Information);
        });

        var logger = loggerFactory.CreateLogger<ChatCompletionService>();

        // Get Azure OpenAI settings
        var settings = new AzureOpenAISettings
        {
            Endpoint = configuration["AzureOpenAI:Endpoint"] 
                ?? Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT") 
                ?? throw new InvalidOperationException("Azure OpenAI endpoint not configured"),
            Key = configuration["AzureOpenAI:Key"] 
                ?? Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY") 
                ?? throw new InvalidOperationException("Azure OpenAI key not configured"),
            DeploymentName = configuration["AzureOpenAI:DeploymentName"] 
                ?? Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT_NAME") 
                ?? throw new InvalidOperationException("Azure OpenAI deployment name not configured")
        };

        var chatService = new ChatCompletionService(settings, logger);

        try
        {
            // Example 1: Simple chat completion
            Console.WriteLine(new string('=', 50));
            Console.WriteLine("Example 1: Simple Chat Completion");
            Console.WriteLine(new string('=', 50));

            var response = await chatService.GetChatCompletionAsync(
                userMessage: "What are the key principles of prompt engineering?",
                systemPrompt: "You are a helpful AI assistant specializing in prompt engineering.");
            
            Console.WriteLine($"Response:\n{response}\n");

            // Example 2: Text summarization
            Console.WriteLine(new string('=', 50));
            Console.WriteLine("Example 2: Text Summarization");
            Console.WriteLine(new string('=', 50));

            var sampleText = """
                Prompt engineering is the practice of designing and refining input prompts 
                to effectively communicate with AI language models. It involves understanding 
                how models interpret instructions, structuring prompts for clarity, and 
                iterating based on outputs. Good prompt engineering can significantly improve 
                the quality, relevance, and accuracy of AI-generated responses. Key techniques 
                include providing context, specifying output formats, using examples (few-shot 
                learning), and applying chain-of-thought reasoning for complex tasks.
                """;

            var summary = await chatService.SummarizeTextAsync(sampleText);
            Console.WriteLine($"Summary:\n{summary}\n");

            // Example 3: Text classification
            Console.WriteLine(new string('=', 50));
            Console.WriteLine("Example 3: Text Classification");
            Console.WriteLine(new string('=', 50));

            var categories = new[] { "Technical", "Business", "Creative", "Support" };
            var textToClassify = "How do I configure Azure OpenAI endpoints in my application?";

            var category = await chatService.ClassifyTextAsync(textToClassify, categories);
            Console.WriteLine($"Text: {textToClassify}");
            Console.WriteLine($"Category: {category}\n");
        }
        catch (InvalidOperationException ex)
        {
            Console.WriteLine($"Configuration error: {ex.Message}");
            Console.WriteLine("Please ensure Azure OpenAI settings are configured correctly.");
        }
        catch (RequestFailedException ex)
        {
            Console.WriteLine($"Azure OpenAI error: {ex.Message}");
        }
    }
}
