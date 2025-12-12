# Prompt Engineering Playbook Repository Verification and Content Enhancement

## Context

You are working with **Prompt Engineering Playbook**, a comprehensive playbook repository that standardizes how prompts are designed, developed, tested, and integrated across C#, Python, and Postman workflows using Azure OpenAI. The repository provides prompt structures, reusable patterns, templates, governance guidelines, and code integration examples.

**Repository Structure:**
- `playbook/` - Core playbook framework and documentation
- `examples/` - Code examples in Python, C#, and Postman
- `infra/` - Azure infrastructure guidance
- `docs/` - Additional documentation and architecture diagrams
- `.github/` - GitHub workflows and templates

**Primary Objective:**
Perform a COMPREHENSIVE audit of the repository using Prompt Engineering Playbook standards and quality criteria. Verify file contents, run structured checks, and produce actionable reports with suggestions and fixes.

---

## Prompt Engineering Playbook Verification Checks

### A. **File Content Inspection**

- Open and verify every file (no file skipped)
- Ensure markdown formatting compliance
- Check for completeness and consistency with learning objectives

### B. **Learning Path Alignment**

- Verify content aligns with correct Level (1-9) or Phase (01-09)
- Validate prerequisites are appropriate and documented
- Check learning progression is logical and sequential
- Ensure cross-references between levels/phases are accurate

### C. **Content Accuracy & Quality**

- Verify technical correctness and architectural soundness
- Ensure completeness for stated learning objectives
- Check alignment with architectural best practices and design patterns
- Validate examples are current, relevant, and runnable

### D. **Prompt Engineering Playbook Metadata Requirements**

Check for presence of:

- Learning Level / Phase designation (e.g., Level 3, Phase 02)
- Prerequisites and dependencies
- Learning Objectives (clear, measurable, specific)
- Core Topics and Practical Projects
- Related Topics and cross-references to other levels/phases
- Estimated Learning Time (where applicable)

### E. **Naming Convention Compliance**

- Use kebab-case for filenames
- Use consistent naming patterns within domain folders
- Verify folder structure follows repository standards
- Check zero-padded numeric prefixes (01_, 02_, not 00_)

### F. **Broken Links & References**

- Verify all internal cross-references work correctly
- Check README files and navigation structure
- Validate external resource links and references
- Ensure level/phase navigation links are accurate

### G. **Content Quality Standards**

- Spellcheck and grammar verification
- Character encoding validation (UTF-8 only)
- Markdown formatting compliance (markdownlint standards)
- Code example correctness and completeness
- Proper code fence language specification

### H. **Domain Organization**

- Verify proper placement in correct domain folder
- Check cross-domain references are accurate
- Validate level/phase organization is clear and discoverable
- Ensure no content duplication across domains

### I. **Repository Structure Clarity**

- Verify folder organization is intuitive
- Check navigability and discoverability
- Validate table of contents accuracy
- Ensure README files guide users through content

### J. **Content Currency & Relevance**

- Verify content reflects current technologies and practices
- Check for deprecated patterns or outdated information
- Validate relevance to stated learning objectives
- Assess alignment with industry trends in architecture

### K. **Practical Application**

- Verify examples are runnable and technically correct
- Check projects align with learning objectives
- Validate edge cases and error handling coverage
- Ensure code examples follow best practices for their language/framework

### L. **Educational Effectiveness**

- Assess clarity and readability for target audience
- Verify learning progression (simple → complex)
- Check engagement through practical relevance
- Validate use of multiple learning modalities (text, code, diagrams, examples)

### M. **Architecture Pattern Documentation**

- Verify pattern intent and participants are clearly explained
- Check when/when-not-to-use guidance is present
- Validate trade-offs are discussed
- Ensure implementation examples are provided in multiple languages where relevant

### N. **Diagram & Visual Quality**

- Verify ASCII diagrams are provided as fallback
- Check Mermaid diagrams are well-structured
- Validate visual clarity and accuracy
- Ensure diagrams support learning objectives

### O. **Cross-Domain Integration**

- Check proper references between domains
- Verify content connections across levels
- Validate integration between reference library and LeadArchitect tracks
- Ensure consistency in terminology and concepts

---

## Prompt Engineering Playbook Content Standards

### Playbook Structure

- **Prompt Patterns**: Instruction-based, role-based, RAG, chain-of-thought, evaluation prompts
- **Templates**: Reusable templates for summarization, classification, extraction, transformation, code-generation
- **Governance**: Review workflows, storage strategy, safety considerations, quality guidelines
- **Code Integration**: Examples in Python, C#, and Postman for Azure OpenAI integration

### Content Organization

- **By Pattern Type**: Content organized by prompt pattern (instruction, role-based, RAG, etc.)
- **By Use Case**: Templates organized by task type (summarization, classification, extraction, etc.)
- **By Language**: Code examples organized by implementation language (Python, C#, Postman)
- **By Integration**: Examples show Azure OpenAI SDK and REST API patterns

### Quality Requirements

- **Accuracy**: Technically correct and architecturally sound
- **Completeness**: Addresses stated learning objectives fully
- **Clarity**: Clear explanations with practical examples and runnable code
- **Relevance**: Directly applicable to architecture practice and decision-making
- **Currency**: Reflects current technologies and best practices
- **Practicality**: Includes actionable guidance, patterns, and examples
- **Pedagogy**: Uses appropriate learning techniques for target audience

### File Standards

- **Naming**: kebab-case filenames, descriptive names indicating content focus
- **Structure**: Clear sections, logical flow, easy navigation
- **Metadata**: Learning level, prerequisites, objectives, topics, estimated time
- **References**: Cross-references to related content with working links
- **Examples**: Runnable code with multiple language implementations where relevant
- **Visuals**: ASCII diagrams and Mermaid diagrams where helpful
- **Length**: Focused, modular content (typically 100-300 lines for reference materials, scalable for complex topics)

---

## Output Requirements

### 1. SUMMARY (Top-level)

```json
{
  "repo_name": "prompt-engineering-playbook",
  "total_files_checked": 0,
  "total_issues_found": 0,
  "playbook_compliance_percentage": 0.0,
  "high_severity_count": 0,
  "medium_severity_count": 0,
  "low_severity_count": 0,
  "suggested_next_steps": ["step1", "step2", "step3"]
}
```

### 2. DETAILED_REPORT (array of file reports)

For each file:

```json
{
  "file_path": "string",
  "level_phase_designation": "string (e.g., Level 3 or Phase 02 - Cluster C)",
  "domain_category": "string (e.g., Development Fundamentals, AI-ML, Leadership & Strategy)",
  "checks_passed": ["list of check keys, e.g., A,B,C,F,G,I"],
  "learning_metadata_present": true/false,
  "content_quality_score": "0-100",
  "practical_application_score": "0-100",
  "issues": [
    {
      "id": "string (unique, e.g., AJ-001)",
      "severity": "high|medium|low",
      "line_start": 0,
      "line_end": 0,
      "description": "string",
      "suggested_fix": "string",
      "fix_type": "replace|delete|add|rename|format|link-fix|metadata-add",
      "violation_type": "string (e.g., missing-objectives, broken-link, outdated-pattern)"
    }
  ],
  "overall_status": "compliant|needs_updates|remove",
  "quick_fix_patch": "string or null"
}
```

### 3. PATTERN_COVERAGE_ANALYSIS

```json
{
  "pattern_coverage": { "instruction-based": 0, "role-based": 0, "rag": 0, "chain-of-thought": 0, "evaluation": 0 },
  "template_coverage": { "summarization": 0, "classification": 0, "extraction": 0, "transformation": 0, "code-generation": 0 },
  "language_coverage": { "python": 0, "csharp": 0, "postman": 0 },
  "completeness_score": "0-100",
  "gap_analysis": ["missing patterns", "missing templates", "missing language examples"]
}
```

### 4. CONTENT_QUALITY_ANALYSIS

```json
{
  "technical_accuracy_score": "0-100",
  "clarity_and_readability_score": "0-100",
  "practical_application_score": "0-100",
  "learning_effectiveness_score": "0-100",
  "examples_quality_score": "0-100",
  "pattern_documentation_score": "0-100"
}
```

### 5. METADATA_COMPLIANCE_SUMMARY

```json
{
  "files_with_complete_metadata": 0,
  "files_missing_learning_objectives": 0,
  "files_missing_prerequisites": 0,
  "files_missing_core_topics": 0,
  "files_with_incorrect_naming": 0,
  "metadata_compliance_percentage": "0-100"
}
```

### 6. CROSS_REFERENCE_VALIDATION

```json
{
  "internal_links_valid": 0,
  "broken_internal_links": 0,
  "domain_cross_references": 0,
  "level_cross_references": 0,
  "phase_cross_references": 0,
  "external_link_validation": "needs_verification"
}
```

### 7. IMPROVEMENT_RECOMMENDATIONS

```json
{
  "structural_improvements": ["recommendation1"],
  "content_enhancements": ["recommendation2"],
  "metadata_additions": ["recommendation3"],
  "domain_reorganization": ["recommendation4"],
  "pattern_documentation": ["recommendation5"]
}
```

Formatting rules for output:

- Output only JSON (no prose outside JSON) so it can be parsed by automation.
- JSON must be UTF-8, compact but human-readable (use 2-space indentation).
- If you include patches, ensure diffs use unified diff format and are properly escaped inside JSON strings.

Strict privacy & reasoning constraint:

- Use ReAct-style internal reasoning and actions to determine findings BUT DO NOT OUTPUT ANY CHAIN-OF-THOUGHT, internal logs, or private reasoning. Only provide the JSON structured output described above.
- If you cannot confirm something (e.g., external API version), mark it "needs_verification" and state what command or URL the operator should run to confirm.

Deliverables:

- The complete JSON report as described above.
- For each suggested_fix that is small (<= 30 lines), include a quick_fix_patch.
- For larger fixes, include exact instructions and code snippets for maintainers to apply the change.
- A final top-level "suggested_next_steps" with three clear actions (e.g., run linter, open PR with patches, run link-checker CI).

Formatting rules for output:

- Output only JSON (no prose outside JSON) so it can be parsed by automation.
- JSON must be UTF-8, compact but human-readable (use 2-space indentation).
- If you include patches, ensure diffs use unified diff format and are properly escaped inside JSON strings.

Strict privacy & reasoning constraint:

- Use ReAct-style internal reasoning and actions to determine findings BUT DO NOT OUTPUT ANY CHAIN-OF-THOUGHT, internal logs, or private reasoning. Only provide the JSON structured output described above.
- If you cannot confirm something (e.g., external API version), mark it “needs_verification” and state what command or URL the operator should run to confirm.

Deliverables:

- The complete JSON report as described above.
- For each suggested_fix that is small (<= 30 lines), include a quick_fix_patch.
- For larger fixes, include exact instructions and code snippets for maintainers to apply the change.
- A final top-level "suggested_next_steps" with three clear actions (e.g., run linter, open PR with patches, run link-checker CI).

Behavioral expectations:

- **Prompt Engineering Focus**: Prioritize prompt quality, effectiveness, and alignment with Azure OpenAI best practices
- **Template Quality**: Flag content that doesn't meet prompt engineering excellence standards
- **Pattern Integrity**: Ensure prompt patterns are well-documented with clear use cases and examples
- **Practical Relevance**: Verify content provides actionable prompt engineering guidance and integration examples
- **Cross-Language Integration**: Validate proper examples across Python, C#, and Postman
- **Code Quality**: Validate examples follow best practices, are runnable, and demonstrate proper Azure OpenAI integration
- **Governance Compliance**: Ensure governance guidelines are clear and actionable
- **Template Completeness**: Verify templates include all necessary components (system prompts, user prompts, examples)
- **Testing Coverage**: Check that evaluation and testing approaches are documented
- **Documentation Quality**: Ensure all examples are well-documented with setup instructions

---

## Formatting Rules

- Output as JSON (no prose outside JSON blocks)
- Use 2-space indentation for readability
- Escape patches in unified diff format
- UTF-8 encoding only
- Quote all JSON keys and string values

---

## Deliverables

1. Complete JSON report following Prompt Engineering Playbook output requirements
2. Compliance scoring and prompt engineering quality assessment
3. Pattern and template coverage analysis with gap identification
4. Cross-reference validation results
5. Content quality analysis by pattern type and language
6. Three clear next steps to improve repository and prompt engineering effectiveness

---

## Start Now

Open every file in the repository tree, run Prompt Engineering Playbook-specific checks, and produce the structured JSON report following these requirements. Focus on prompt quality, template completeness, code example correctness, and alignment with Azure OpenAI best practices.
