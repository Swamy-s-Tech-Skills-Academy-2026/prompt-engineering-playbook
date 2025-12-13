"""
Azure OpenAI Chat Completion Example

This module demonstrates how to use Azure OpenAI for chat completions
with proper configuration, error handling, and best practices.
"""

import os
import logging
from typing import Optional

from openai import AzureOpenAI
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_azure_openai_client() -> AzureOpenAI:
    """
    Create and return an Azure OpenAI client with configuration from environment variables.
    
    Returns:
        AzureOpenAI: Configured Azure OpenAI client
        
    Raises:
        ValueError: If required environment variables are not set
    """
    load_dotenv()
    
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    
    if not endpoint or not api_key:
        raise ValueError(
            "AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY environment variables must be set"
        )
    
    return AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version=api_version
    )


def chat_completion(
    client: AzureOpenAI,
    user_message: str,
    system_prompt: Optional[str] = None,
    deployment_name: Optional[str] = None,
    temperature: float = 0.7,
    max_tokens: int = 1000
) -> str:
    """
    Send a chat completion request to Azure OpenAI.
    
    Args:
        client: Azure OpenAI client instance
        user_message: The user's input message
        system_prompt: Optional system prompt to set AI behavior
        deployment_name: Azure OpenAI deployment name (defaults to env var)
        temperature: Sampling temperature (0.0 to 2.0)
        max_tokens: Maximum tokens in the response
        
    Returns:
        str: The AI's response content
        
    Raises:
        Exception: If the API call fails
    """
    deployment = deployment_name or os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    
    if not deployment:
        raise ValueError("Deployment name must be provided or set in AZURE_OPENAI_DEPLOYMENT_NAME")
    
    messages = []
    
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    
    messages.append({"role": "user", "content": user_message})
    
    logger.info(f"Sending chat completion request to deployment: {deployment}")
    
    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        result = response.choices[0].message.content
        logger.info(f"Received response with {response.usage.total_tokens} total tokens")
        
        return result
        
    except Exception as e:
        logger.error(f"Chat completion failed: {e}")
        raise


def summarize_text(client: AzureOpenAI, text: str, max_sentences: int = 3) -> str:
    """
    Summarize the given text using Azure OpenAI.
    
    Args:
        client: Azure OpenAI client instance
        text: The text to summarize
        max_sentences: Maximum number of sentences in the summary
        
    Returns:
        str: Summarized text
    """
    system_prompt = f"""You are a skilled summarizer. 
Create a concise summary of the provided text in {max_sentences} sentences or fewer.
Focus on the key points and main ideas."""

    user_message = f"Please summarize the following text:\n\n{text}"
    
    return chat_completion(client, user_message, system_prompt, temperature=0.3)


def classify_text(client: AzureOpenAI, text: str, categories: list[str]) -> str:
    """
    Classify the given text into one of the provided categories.
    
    Args:
        client: Azure OpenAI client instance
        text: The text to classify
        categories: List of possible categories
        
    Returns:
        str: The classified category
    """
    categories_str = ", ".join(categories)
    
    system_prompt = f"""You are a text classifier.
Classify the given text into exactly one of these categories: {categories_str}
Respond with only the category name, nothing else."""

    user_message = f"Classify this text:\n\n{text}"
    
    return chat_completion(client, user_message, system_prompt, temperature=0.0)


def main():
    """Main function demonstrating Azure OpenAI usage."""
    try:
        # Initialize client
        client = get_azure_openai_client()
        logger.info("Azure OpenAI client initialized successfully")
        
        # Example 1: Simple chat completion
        print("\n" + "=" * 50)
        print("Example 1: Simple Chat Completion")
        print("=" * 50)
        
        response = chat_completion(
            client,
            user_message="What are the key principles of prompt engineering?",
            system_prompt="You are a helpful AI assistant specializing in prompt engineering."
        )
        print(f"Response:\n{response}")
        
        # Example 2: Text summarization
        print("\n" + "=" * 50)
        print("Example 2: Text Summarization")
        print("=" * 50)
        
        sample_text = """
        Prompt engineering is the practice of designing and refining input prompts 
        to effectively communicate with AI language models. It involves understanding 
        how models interpret instructions, structuring prompts for clarity, and 
        iterating based on outputs. Good prompt engineering can significantly improve 
        the quality, relevance, and accuracy of AI-generated responses. Key techniques 
        include providing context, specifying output formats, using examples (few-shot 
        learning), and applying chain-of-thought reasoning for complex tasks.
        """
        
        summary = summarize_text(client, sample_text)
        print(f"Summary:\n{summary}")
        
        # Example 3: Text classification
        print("\n" + "=" * 50)
        print("Example 3: Text Classification")
        print("=" * 50)
        
        categories = ["Technical", "Business", "Creative", "Support"]
        text_to_classify = "How do I configure Azure OpenAI endpoints in my application?"
        
        category = classify_text(client, text_to_classify, categories)
        print(f"Text: {text_to_classify}")
        print(f"Category: {category}")
        
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        print(f"Error: {e}")
        print("Please ensure environment variables are set correctly.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
