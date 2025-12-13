# GitHub Copilot Instructions for Prompt Engineering Playbook

**Version**: 1.0  
**Last Updated**: December 2025  
**Repository**: `prompt-engineering-playbook`

---

## 🎯 Repository Purpose

**Prompt Engineering Playbook** is a comprehensive playbook that standardizes how prompts are designed, developed, tested, and integrated across C#, Python, and Postman workflows using Azure OpenAI.

### What This Repository Provides

- **Standard Prompt Patterns**: Instruction-based, role-based, RAG, chain-of-thought, evaluation prompts
- **Reusable Templates**: Summarization, classification, extraction, transformation, code-generation
- **Governance Guidelines**: Review workflows, storage strategy, safety considerations, quality guidelines
- **Code Integration Examples**: Working samples in Python, C#, and Postman for Azure OpenAI
- **Infrastructure Guidance**: Azure OpenAI setup and configuration

### Target Audience

- Engineering teams working with Azure OpenAI
- Prompt engineers
- AI application developers
- Technical leads and architects

### Business Value

- Ensures uniformity across prompt engineering practices
- Reduces model misbehaviour through tested patterns
- Accelerates onboarding for new team members
- Improves productivity with reusable templates
- Provides consistent framework for enterprise-grade Azure OpenAI development

---

## 📁 Repository Structure

```text
prompt-engineering-playbook/
├── .github/
│   ├── workflows/
│   │   ├── ci-python.yml              # Python linting and testing
│   │   ├── ci-dotnet.yml              # .NET build and testing
│   │   └── validate-postman.yml       # Postman collection validation
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── copilot-instructions.md        # THIS FILE
├── playbook/                          # Core playbook framework
│   ├── 01-overview.md                 # Introduction and getting started
│   ├── 02-structure-and-toc.md        # Table of contents
│   ├── 03-patterns-and-anti-patterns.md  # Prompt patterns
│   ├── 04-templates.md                # Reusable templates
│   ├── 05-governance.md               # Governance guidelines
│   └── 06-evaluation-and-testing.md   # Testing approaches
├── src/                               # Code examples
│   ├── python/
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── samples/                   # Python sample scripts
│   ├── csharp/
│   │   ├── README.md
│   │   └── samples/                   # C# sample projects
│   └── postman/
│       ├── README.md
│       ├── prompt-playbook.postman_collection.json
│       └── prompt-playbook.postman_environment.json
├── infra/                             # Infrastructure guidance
│   └── azure-guidance.md
├── docs/                              # Additional documentation
│   └── architecture-diagrams/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
└── CODE_OF_CONDUCT.md
```

---

## 🔧 Development Guidelines

### When Working with Prompts

1. **Follow Established Patterns**: Use patterns from `playbook/02-patterns-and-anti-patterns.md`
2. **Use Templates**: Leverage templates from `playbook/03-templates.md`
3. **Apply Governance**: Follow guidelines in `playbook/04-governance.md`
4. **Test Thoroughly**: Use evaluation approaches from `playbook/05-evaluation-and-testing.md`

### When Writing Code Examples

#### Python Examples (`src/python/`)

- Use Azure OpenAI SDK (`openai` package with Azure configuration)
- Follow PEP 8 style guidelines
- Include proper error handling and logging
- Use environment variables for configuration (never hardcode keys)
- Include docstrings and type hints

#### C# Examples (`src/csharp/`)

- Use Azure.AI.OpenAI NuGet package
- Follow .NET coding conventions
- Implement proper exception handling
- Use configuration providers (appsettings.json, environment variables)
- Include XML documentation comments

#### Postman Examples (`src/postman/`)

- Use environment variables for endpoints and keys
- Include pre-request scripts for authentication
- Add test scripts for response validation
- Document expected responses

### Security Best Practices

- ❌ **NEVER** commit API keys or secrets
- ✅ **ALWAYS** use environment variables or Azure Key Vault
- ✅ **ALWAYS** add `.env` files to `.gitignore`
- ✅ **ALWAYS** use GitHub Secrets for CI/CD workflows

### Configuration Management

```bash
# Required environment variables
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_KEY=your-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

---

## 📋 Code Quality Standards

### Markdown Files

- Use proper heading hierarchy (H1 → H2 → H3)
- Include code fence language specifications
- Follow markdownlint rules
- Use UTF-8 encoding

### Python Code

- Run `flake8` for linting
- Run `pytest` for testing
- Use `black` for formatting
- Maintain `requirements.txt` with pinned versions

### C# Code

- Build with `dotnet build`
- Run tests with `dotnet test`
- Follow .NET naming conventions
- Keep NuGet packages updated

### Postman Collections

- Validate with Newman
- Include comprehensive test scripts
- Document all variables
- Use collection-level authentication

---

## 🚀 CI/CD Workflows

### Python CI (`ci-python.yml`)

- Triggered on push/PR to `main`
- Sets up Python environment
- Installs dependencies
- Runs linting (flake8)
- Runs tests (pytest)

### .NET CI (`ci-dotnet.yml`)

- Triggered on push/PR to `main`
- Sets up .NET SDK
- Restores NuGet packages
- Builds solution
- Runs tests

### Postman Validation (`validate-postman.yml`)

- Triggered on push/PR to `main`
- Installs Newman
- Validates collection structure
- Runs collection tests (with mock or staging endpoint)

---

## 📝 Local Quality Checks

### Markdown Linting

Run markdownlint to check all markdown files for style and formatting issues:

```bash
npx markdownlint-cli2 "**/*.md" --config .markdownlint.json
```

### Link Checking (Lychee via Docker)

Run Lychee via Docker to check for broken links in markdown files:

```bash
docker run --rm -v "${PWD}:/input:ro" lycheeverse/lychee --config /input/lychee.toml "/input/**/*.md"
```

**Note**: Requires Docker to be installed and running.

---

## �📝 Prompt Engineering Best Practices

### Prompt Structure

1. **Role Definition**: Define the AI's role and expertise
2. **Context Setting**: Provide relevant background information
3. **Task Description**: Clearly state what needs to be done
4. **Output Format**: Specify expected response format
5. **Constraints**: Define limitations and guardrails
6. **Examples**: Provide few-shot examples when helpful

### Common Patterns

| Pattern           | Use Case               | Example                                |
| ----------------- | ---------------------- | -------------------------------------- |
| Instruction-based | Direct task completion | "Summarize the following text..."      |
| Role-based        | Specialized expertise  | "You are a senior code reviewer..."    |
| Chain-of-thought  | Complex reasoning      | "Think step by step..."                |
| RAG               | Knowledge-grounded     | "Based on the following context..."    |
| Evaluation        | Quality assessment     | "Rate the following on a scale..."     |

### Anti-Patterns to Avoid

- ❌ Vague or ambiguous instructions
- ❌ Missing output format specification
- ❌ No error handling guidance
- ❌ Overly complex single prompts
- ❌ Hardcoded values instead of variables

---

## 🔗 Quick Links

- [Playbook Overview](../playbook/01-overview.md)
- [Prompt Patterns](../playbook/03-patterns-and-anti-patterns.md)
- [Templates](../playbook/04-templates.md)
- [Governance](../playbook/05-governance.md)
- [Python Examples](../src/python/README.md)
- [C# Examples](../src/csharp/README.md)
- [Azure Setup](../infra/azure-guidance.md)

---

## 📞 Support

- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Contributing**: See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines
