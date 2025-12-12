# C# Examples

This directory contains C# examples for integrating with Azure OpenAI using the .NET SDK.

## Setup

1. Ensure .NET SDK is installed (version 8.0 or later)

2. Restore NuGet packages:

   ```bash
   dotnet restore
   ```

3. Configure app settings:
   - Update `appsettings.json` or `appsettings.Development.json`
   - Add your Azure OpenAI configuration:

     ```json
     {
       "AzureOpenAI": {
         "Endpoint": "your-endpoint",
         "Key": "your-key",
         "DeploymentName": "your-deployment"
       }
     }
     ```

## Examples

See the `samples/` directory for example projects demonstrating:

- Chat completions
- Embeddings
- Function calling
- Structured responses
- Error handling and retry logic
- Configuration management

## Running Examples

```bash
dotnet run --project samples/ChatExample
```

## NuGet Packages

- `Azure.AI.OpenAI` - Azure OpenAI .NET SDK
- `Microsoft.Extensions.Configuration` - Configuration management
- `Microsoft.Extensions.Logging` - Logging
