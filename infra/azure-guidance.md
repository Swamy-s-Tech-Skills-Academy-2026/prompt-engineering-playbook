# Azure Infrastructure Guidance

This document provides guidance for setting up and configuring Azure OpenAI resources.

## Prerequisites

- Azure subscription
- Appropriate permissions to create Azure resources
- Azure CLI or Azure Portal access

## Azure OpenAI Resource Setup

### 1. Create Azure OpenAI Resource

Using Azure Portal:
1. Navigate to Azure Portal
2. Create a new resource
3. Search for "Azure OpenAI"
4. Create the resource with appropriate configuration

Using Azure CLI:
```bash
az cognitiveservices account create \
  --name your-openai-resource \
  --resource-group your-resource-group \
  --kind OpenAI \
  --sku S0 \
  --location eastus
```

### 2. Deploy a Model

1. Navigate to Azure OpenAI Studio
2. Go to "Deployments"
3. Create a new deployment
4. Select model and configure settings

### 3. Get Endpoint and Key

1. Navigate to your Azure OpenAI resource
2. Go to "Keys and Endpoint"
3. Copy the endpoint URL
4. Copy one of the keys (Key 1 or Key 2)

## Configuration

### Environment Variables

Set the following environment variables:

```bash
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_KEY=your-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
```

### Security Best Practices

1. **Never commit keys**: Use environment variables or secure configuration
2. **Use managed identity**: When possible, use Azure Managed Identity
3. **Rotate keys regularly**: Implement key rotation policies
4. **Limit access**: Use role-based access control (RBAC)
5. **Monitor usage**: Set up monitoring and alerts

## Cost Management

1. **Monitor usage**: Track token usage and costs
2. **Set budgets**: Configure budget alerts
3. **Optimize prompts**: Reduce token usage where possible
4. **Use appropriate models**: Choose models based on requirements

## Networking

### Private Endpoints

For enhanced security, configure private endpoints:

1. Navigate to your Azure OpenAI resource
2. Go to "Networking"
3. Configure private endpoint settings

### Firewall Rules

Configure firewall rules to restrict access:

1. Navigate to "Networking" settings
2. Configure allowed IP addresses
3. Enable virtual network integration if needed

## Monitoring and Logging

### Application Insights

Integrate Application Insights for monitoring:

1. Create Application Insights resource
2. Configure logging in your application
3. Set up dashboards and alerts

### Logging Best Practices

- Log API calls (without sensitive data)
- Track token usage
- Monitor error rates
- Track latency metrics

## Troubleshooting

### Common Issues

1. **Authentication errors**: Verify endpoint and key
2. **Rate limiting**: Check quota and limits
3. **Model not found**: Verify deployment name
4. **Network issues**: Check firewall and network settings

### Support Resources

- Azure OpenAI documentation
- Azure support
- Community forums

## Next Steps

- Review code examples in `src/` directory
- Follow governance guidelines in playbook
- Set up monitoring and alerts
- Implement security best practices
