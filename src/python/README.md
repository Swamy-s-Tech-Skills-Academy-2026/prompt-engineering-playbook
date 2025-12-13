# Python Examples

This directory contains Python examples for integrating with Azure OpenAI.

## Setup

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Create a `.env` file (not committed to Git)
   - Add your Azure OpenAI credentials:

     ```text
     AZURE_OPENAI_ENDPOINT=your-endpoint
     AZURE_OPENAI_KEY=your-key
     AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment
     ```

## Examples

See the `samples/` directory for example scripts demonstrating:

- Chat completions
- Embeddings
- Function calling
- Error handling
- Configuration management

## Running Examples

```bash
python samples/chat_example.py
```

## Requirements

See `requirements.txt` for required packages.
