# Prompt Engineering Playbook - Structure and Table of Contents

## Playbook Organization

The Prompt Engineering Playbook is organized into logical sections that build upon each other:

## Table of Contents

### 1. Overview
- [00-overview.md](00-overview.md) - Introduction and getting started

### 2. Structure and Organization
- [01-structure-and-toc.md](01-structure-and-toc.md) - This document

### 3. Patterns and Anti-patterns
- [02-patterns-and-anti-patterns.md](02-patterns-and-anti-patterns.md)
  - Instruction-based prompts
  - Role-based prompts
  - RAG (Retrieval-Augmented Generation) patterns
  - Chain-of-thought scaffolding
  - Evaluation prompts
  - Common anti-patterns to avoid

### 4. Templates
- [03-templates.md](03-templates.md)
  - Summarization templates
  - Classification templates
  - Extraction templates
  - Transformation templates
  - Code-generation templates

### 5. Governance
- [04-governance.md](04-governance.md)
  - Review workflows
  - Storage strategy
  - Safety considerations
  - Quality guidelines
  - Versioning approach

### 6. Evaluation and Testing
- [05-evaluation-and-testing.md](05-evaluation-and-testing.md)
  - Testing methodologies
  - Evaluation metrics
  - Quality assurance processes

## Code Examples

Code integration examples are provided in the `src/` directory:

- **Python**: `src/python/` - Azure OpenAI SDK examples
- **C#**: `src/csharp/` - .NET SDK examples
- **Postman**: `src/postman/` - REST API examples

## Documentation

Additional documentation and architecture diagrams are available in:

- `docs/` - Additional documentation
- `infra/` - Azure infrastructure guidance

## Navigation

- **Previous**: [Overview](00-overview.md)
- **Next**: [Patterns and Anti-patterns](02-patterns-and-anti-patterns.md)
