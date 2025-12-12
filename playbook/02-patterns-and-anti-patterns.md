# Prompt Engineering Playbook - Patterns and Anti-patterns

## Prompt Patterns

### Instruction-Based Prompts

Instruction-based prompts provide clear, direct instructions to the model.

**Structure:**
```
[Clear instruction]
[Context if needed]
[Expected output format]
```

**Example:**
```
Summarize the following text in 2-3 sentences.
[Text to summarize]
```

### Role-Based Prompts

Role-based prompts assign a specific role or persona to the model.

**Structure:**
```
You are a [role].
[Role-specific context]
[Task description]
```

**Example:**
```
You are a senior software architect with expertise in cloud-native applications.
Review the following architecture and provide recommendations for improvement.
[Architecture description]
```

### RAG (Retrieval-Augmented Generation) Patterns

RAG patterns combine retrieval of relevant information with generation.

**Structure:**
```
[Context from retrieval]
[Question or task]
[Instructions for using context]
```

### Chain-of-Thought Scaffolding

Chain-of-thought prompts encourage step-by-step reasoning.

**Structure:**
```
[Problem statement]
Let's think step by step:
1. [First step]
2. [Second step]
...
[Final answer]
```

### Evaluation Prompts

Evaluation prompts assess the quality or correctness of outputs.

**Structure:**
```
Evaluate the following [output type] based on:
- [Criterion 1]
- [Criterion 2]
...
[Output to evaluate]
```

## Anti-patterns

### ❌ Vague Instructions

**Bad:**
```
Make it better.
```

**Good:**
```
Improve the code readability by:
1. Adding meaningful variable names
2. Breaking complex functions into smaller ones
3. Adding comments for complex logic
```

### ❌ Overly Complex Prompts

**Bad:**
```
[Very long prompt with multiple nested instructions and unclear structure]
```

**Good:**
```
[Clear, concise prompt with logical structure]
```

### ❌ Missing Context

**Bad:**
```
Classify this.
```

**Good:**
```
Classify the following customer feedback as positive, negative, or neutral.
[Feedback text]
```

### ❌ Inconsistent Formatting

**Bad:**
```
prompt without clear structure or formatting
```

**Good:**
```
[Well-structured prompt with clear sections]
```

## Best Practices

1. **Be Specific**: Clear, specific instructions produce better results
2. **Provide Context**: Include relevant context for the task
3. **Use Examples**: Few-shot examples improve performance
4. **Test Iteratively**: Refine prompts based on results
5. **Document Patterns**: Document successful patterns for reuse

## Navigation

- **Previous**: [Structure and Table of Contents](01-structure-and-toc.md)
- **Next**: [Templates](03-templates.md)

