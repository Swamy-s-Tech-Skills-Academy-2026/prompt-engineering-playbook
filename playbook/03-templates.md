# Prompt Engineering Playbook - Templates

This section provides reusable prompt templates for common tasks.

## Summarization Template

```
Summarize the following [content type] in [length] sentences.

Focus on:
- [Key point 1]
- [Key point 2]
- [Key point 3]

[Content to summarize]
```

## Classification Template

```
Classify the following [item type] into one of these categories:
- [Category 1]: [Description]
- [Category 2]: [Description]
- [Category 3]: [Description]

[Item to classify]

Provide:
1. The selected category
2. Confidence level (high/medium/low)
3. Brief reasoning
```

## Extraction Template

```
Extract the following information from the text below:
- [Field 1]: [Description]
- [Field 2]: [Description]
- [Field 3]: [Description]

[Text to extract from]

Format the output as JSON with the specified fields.
```

## Transformation Template

```
Transform the following [input type] into [output type].

Requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

[Input content]

Provide the transformed output.
```

## Code Generation Template

```
You are a [programming language] expert.

Generate [type of code] that:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

[Additional context or specifications]

Include:
- Clear variable names
- Comments for complex logic
- Error handling
```

## Customization Guidelines

When using templates:

1. **Replace placeholders** with specific values
2. **Add context** relevant to your use case
3. **Specify output format** clearly
4. **Include examples** if needed (few-shot learning)
5. **Test and refine** based on results

## Template Parameters

Common parameters to customize:

- `[content type]` - Type of content (text, code, data, etc.)
- `[length]` - Desired output length
- `[item type]` - Type of item to classify
- `[input type]` - Type of input
- `[output type]` - Type of output
- `[programming language]` - Target programming language

## Navigation

- **Previous**: [Patterns and Anti-patterns](02-patterns-and-anti-patterns.md)
- **Next**: [Governance](04-governance.md)

