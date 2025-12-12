# Postman Examples

This directory contains Postman collections and environment files for testing Azure OpenAI REST APIs.

## Setup

1. Import the collection:
   - Open Postman
   - Click "Import"
   - Select `prompt-playbook.postman_collection.json`

2. Import the environment:
   - Click "Environments" in Postman
   - Click "Import"
   - Select `prompt-playbook.postman_environment.json`

3. Configure environment variables:
   - Select the imported environment
   - Update the following variables:
     - `azure_openai_endpoint` - Your Azure OpenAI endpoint
     - `azure_openai_key` - Your Azure OpenAI API key
     - `azure_openai_deployment` - Your deployment name
     - `azure_openai_api_version` - API version (e.g., "2024-02-15-preview")

## Collection Structure

The collection includes examples for:

- Chat Completions
- Embeddings
- Function Calling
- Error Handling

## Running Requests

1. Select the environment
2. Choose a request from the collection
3. Review and update request body if needed
4. Click "Send"

## Testing with Newman

You can also run the collection using Newman (Postman CLI):

```bash
npm install -g newman
newman run prompt-playbook.postman_collection.json -e prompt-playbook.postman_environment.json
```

## Environment Variables

Required variables:
- `azure_openai_endpoint` - Azure OpenAI endpoint URL
- `azure_openai_key` - API key
- `azure_openai_deployment` - Deployment name
- `azure_openai_api_version` - API version

Optional variables:
- `model` - Model name (if different from deployment)
- `temperature` - Temperature setting
- `max_tokens` - Maximum tokens

