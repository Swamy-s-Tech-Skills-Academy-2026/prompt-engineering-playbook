# Prompt Engineering Playbook

**Description:**
As an engineering team, we need a comprehensive Prompt Engineering Playbook that standardizes how prompts are designed, developed, tested, and integrated across C#, Python, and Postman workflows using Azure OpenAI. The playbook should define prompt structures, reusable patterns, templates, governance guidelines, and code integration examples so teams can consistently produce high-quality, reliable, and maintainable prompt-driven solutions.

**Business Value:**
This playbook ensures uniformity, reduces model misbehaviour, accelerates onboarding, improves productivity, and provides a consistent framework for enterprise-grade Azure OpenAI development.

---

## Task Descriptions

### Task 1: Design and Author Prompt Engineering Playbook Framework – Day 1 (6.5 hours)

**Description:**
Establish the foundational structure and outline of the Prompt Engineering Playbook. Define the overall sections, chapter hierarchy, layout conventions, and documentation standards. Identify prompt types, use-case categories, and conceptual areas that will be covered across the playbook. Draft the governance scope, naming conventions, versioning approach, and documentation guidelines. Produce the initial skeleton document and high-level content architecture.

---

### Task 2: Design and Author Prompt Engineering Playbook Framework – Day 2 (6.5 hours)

**Description:**
Expand the framework by creating standard prompt patterns (instruction-based, role-based, RAG, chain-of-thought scaffolding, evaluation prompts). Develop reusable prompt templates for summarization, classification, extraction, transformation, and code-generation tasks. Define governance rules—including review workflows, storage strategy, safety considerations, and quality guidelines. Refine and complete the full framework document that will serve as the blueprint for the detailed playbook content.

---

### Task 3: Implement Azure OpenAI Integration Using Python and Postman (6.5 hours)

**Description:**
Implement working examples that demonstrate how to interact with Azure OpenAI using Python and Postman. Develop sample scripts using the Azure OpenAI SDK and REST APIs, including chat completions, embeddings, and model configuration. Create Postman collections with environment variables, authentication setup, and test calls. Document recommended project structure, error-handling, logging, and configuration approaches. Integrate these examples into the playbook framework for cross-language reference.

---

### Task 4: Implement Azure OpenAI Integration Using C# (6.5 hours)

**Description:**
Develop C# examples that illustrate Azure OpenAI usage through the Azure OpenAI .NET SDK and REST API patterns. Implement demonstration code for chat completions, embeddings, function calling, and structured responses. Set up recommended client initialization patterns, retry logic, configuration handling, and logging. Document these patterns and incorporate them into the playbook framework to ensure consistency across supported languages.

---

## Repository Contents

This repository contains:

* **Playbook Framework**: Complete playbook structure with markdown sections covering patterns, templates, governance, and evaluation.
* **Prompt Templates**: Reusable prompt templates for common tasks (summarization, classification, extraction, transformation, code generation).
* **Code Examples**: Working examples in multiple languages:
  * Python: Azure OpenAI SDK examples with configuration and authentication
  * C#: .NET SDK examples with proper client initialization and error handling
  * Postman: REST API collection with environment variables and test cases
* **CI/CD Workflows**: GitHub Actions workflows for:
  * Lint and format checks for Python and C#
  * Unit test execution (pytest / dotnet test)
  * Postman collection validation (using Newman)
* **Documentation**: Setup guides, contribution guidelines, and infrastructure guidance
* **Governance**: Review workflows, storage strategy, safety considerations, and quality guidelines

---

## Repository Structure

```text
prompt-engineering-playbook/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── .github/
│   ├── workflows/
│   │   ├── ci-python.yml
│   │   ├── ci-dotnet.yml
│   │   └── validate-postman.yml
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── copilot-instructions.md
│   └── prompts/
│       ├── smart-prompt-framework-guide.md
│       └── task-prompt.md
├── playbook/
│   ├── 01-overview.md
│   ├── 02-structure-and-toc.md
│   ├── 03-patterns-and-anti-patterns.md
│   ├── 04-templates.md
│   ├── 05-governance.md
│   └── 06-evaluation-and-testing.md
├── src/
│   ├── python/
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── samples/
│   ├── csharp/
│   │   ├── README.md
│   │   └── samples/
│   └── postman/
│       ├── README.md
│       ├── prompt-playbook.postman_collection.json
│       └── prompt-playbook.postman_environment.json
├── infra/
│   └── azure-guidance.md
└── docs/
    └── architecture-diagrams/
```

---

## Initial Setup — exact steps (copy/paste)

1. Create repo on GitHub (name: `prompt-engineering-playbook`).
1. Clone locally:

```bash
git clone git@github.com:<your-org>/prompt-engineering-playbook.git
cd prompt-engineering-playbook
```

1. Create default branch & initial commit:

```bash
git checkout -b main
# create files README.md, .gitignore
git add README.md .gitignore
git commit -m "Initial repo skeleton"
git push -u origin main
```

1. Create feature branches for tasks:

```bash
git checkout -b task/design-playbook-day1
git checkout -b task/design-playbook-day2
git checkout -b task/implement-python-postman
git checkout -b task/implement-csharp
```

---

## Security and Secrets

**Important**: Never commit API keys or sensitive credentials to the repository.

### GitHub Secrets

For CI/CD pipelines, use GitHub repository secrets:

* `AZURE_OPENAI_ENDPOINT`
* `AZURE_OPENAI_KEY`
* `POSTMAN_API_KEY` (if needed)

### Local Development

For local development:

* Use `.env` files (already added to `.gitignore`)
* Configure environment variables in `config.py` (Python) or `appsettings.Development.json` (C#)
* Never commit files containing actual credentials

---

## CI/CD Workflows

The repository includes GitHub Actions workflows:

* **`ci-python.yml`**: Sets up Python environment, installs dependencies, runs tests with pytest, and performs linting with flake8
* **`ci-dotnet.yml`**: Builds the C# solution and runs unit tests with dotnet test
* **`validate-postman.yml`**: Validates Postman collections using Newman against configured endpoints

---

## Getting Started

### Quick Start

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd prompt-engineering-playbook
   ```

2. **Review the playbook**: Start with `playbook/01-overview.md` to understand the framework

3. **Explore examples**: Check out code examples in `src/python/`, `src/csharp/`, and `src/postman/`

4. **Set up your environment**: Follow the setup instructions in each example directory's README

### Key Files

* **Playbook Framework**: `playbook/` - Complete playbook documentation
* **Code Examples**: `src/` - Working examples in Python, C#, and Postman
* **Infrastructure**: `infra/azure-guidance.md` - Azure OpenAI setup guide
* **Contributing**: `CONTRIBUTING.md` - Guidelines for contributing

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Process

1. Create a feature branch from `main`
2. Make your changes following the coding standards
3. Add tests for new functionality
4. Ensure all tests pass and CI checks succeed
5. Submit a pull request with a clear description

### Branch Strategy

* `main` - Stable, production-ready code
* `feature/*` - New features or enhancements
* `bugfix/*` - Bug fixes
* `task/*` - Task-specific branches (e.g., `task/design-playbook-day1`)

---

## Additional Resources

* **Playbook Documentation**: See `playbook/` directory for complete framework documentation
* **Code Examples**: Working examples available in `src/python/`, `src/csharp/`, and `src/postman/`
* **Azure Setup**: Follow `infra/azure-guidance.md` for Azure OpenAI resource configuration
* **Issues**: Report bugs or request features via GitHub Issues
* **Discussions**: Join discussions about prompt engineering best practices

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
