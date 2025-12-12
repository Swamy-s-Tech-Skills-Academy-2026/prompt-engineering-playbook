# Contributing to Prompt Engineering Playbook

Thank you for your interest in contributing to the Prompt Engineering Playbook! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone git@github.com:YOUR_USERNAME/prompt-engineering-playbook.git
   cd prompt-engineering-playbook
   ```
3. **Set up the development environment**:
   - For Python examples: Create a virtual environment and install dependencies
   - For C# examples: Ensure .NET SDK is installed
   - For Postman: Import the collection and environment files

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or suggest enhancements
- Include clear descriptions, steps to reproduce, and expected vs. actual behavior
- Use appropriate issue templates when available

### Contributing Code

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Test your changes**:
   - Run existing tests
   - Add new tests for new functionality
   - Ensure all tests pass

4. **Commit your changes** with clear, descriptive commit messages

5. **Push to your fork** and create a Pull Request

## Development Workflow

### Branch Strategy

- `main` - Stable, production-ready code
- `feature/*` - New features or enhancements
- `bugfix/*` - Bug fixes
- `docs/*` - Documentation updates

### Task Branches

As per the project structure, create branches for specific tasks:

```bash
git checkout -b task/design-playbook-day1
git checkout -b task/design-playbook-day2
git checkout -b task/implement-python-postman
git checkout -b task/implement-csharp
```

## Coding Standards

### Python

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Include docstrings for functions and classes
- Run `flake8` and `pytest` before committing

### C#

- Follow C# coding conventions
- Use XML documentation comments
- Ensure code compiles with zero warnings
- Run `dotnet test` before committing

### Postman

- Follow Postman collection structure guidelines
- Include clear descriptions for requests
- Use environment variables for configuration
- Test collections with Newman before committing

### Markdown Documentation

- Follow markdownlint standards
- Use clear headings and structure
- Include code examples where relevant
- Keep line length reasonable (~120 characters)

## Pull Request Process

1. **Update documentation** if you've changed functionality
2. **Ensure all tests pass** and CI checks succeed
3. **Update CHANGELOG.md** if applicable
4. **Request review** from maintainers
5. **Address feedback** and make requested changes
6. **Wait for approval** before merging

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Tests added/updated and passing
- [ ] Documentation updated
- [ ] No breaking changes (or documented if necessary)
- [ ] CI checks passing
- [ ] Reviewed by at least one maintainer

## Security

- **Never commit secrets** (API keys, passwords, etc.)
- Use environment variables or secure configuration
- Report security vulnerabilities privately to maintainers

## Questions?

If you have questions, please:
- Open an issue for discussion
- Check existing documentation
- Contact maintainers

Thank you for contributing to the Prompt Engineering Playbook!

