# AI Prompts

This file documents how generative AI was used in this project: which model, for what, and the most effective prompts. It is structured around the **4D framework** from Anthropic's [AI Fluency: Framework & Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations) course:

- **Delegation**: deciding what to hand to the AI and what to keep.
- **Description**: describing the product, the process and the expected performance clearly.
- **Discernment**: critically evaluating what the AI produced.
- **Diligence**: taking responsibility for what ends up in the repository.

## Models used

| Model | Interface | Used for |
|-------|-----------|----------|
| Claude Opus 5.5 (Anthropic) | Claude Code (CLI agent with access to the repo and the GitHub CLI) | Repository setup: README skeleton, LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, this file, branch protection |

## Entry 1: repository setup

### Delegation

Delegated: the "administrative" part of the lab that requires no knowledge of our dataset (creating the repo, boilerplate documents, branch protection settings).
Kept for the team: the research question, the dataset description, the scripts, the analysis and the report.

### Description (most effective prompt)

The prompt that worked best was the one that clearly described the **product** (the list of deliverables), the **process** (what to do, what to leave alone, when to push) and the **performance** expected (respect the lab instructions, ask when information is missing instead of inventing it):

```text
Help me set up this lab: https://reproducible-research.polymtl.ca/fr/lab3/

Product: set up everything that does not require real work on the data:
- the GitHub repository,
- a README.md reflecting the current state of the project (based on the
  World Bank template the lab links to),
- a LICENSE (MIT),
- CONTRIBUTING.md,
- a code of conduct,
- the AI_Prompts.md file,
- the protection rules on main (no direct pushes, PR reviewed by at least
  one other team member, consistent branch naming convention).

Process: read the lab page first and follow its requirements. Stop after
these items, do not write the download/preprocessing/analysis scripts.
Push as you go or all at once at the end.

Performance: if information is missing (repo name, teammates, dataset,
license), ask me instead of guessing, and leave clearly marked TODO
placeholders for what only the team can fill in.
```

What made it effective:

- **Explicit scope with a stop condition** ("stop after these items"): the AI did not start inventing analysis code for a dataset it knows nothing about.
- **A reference to the source of truth** (the lab URL): the AI read the actual requirements (e.g. that `main` needs reviews from another team member, the World Bank README template) instead of relying on generic defaults.
- **Permission to ask**: the AI asked for the repo name, teammates and license before acting, and used placeholders for the dataset.

### Discernment

Checked after generation:

- README follows the World Bank template sections and does not claim anything that does not exist yet (scripts, results are marked TODO).
- Code of conduct is the unmodified Contributor Covenant 2.1, with our own reporting contact.
- Branch protection was verified in the repository settings and by trying to push directly to `main` (rejected).

### Diligence

All generated files were reviewed by the team before being considered final. The AI is listed here as a tool, not as an author; the team is responsible for the content of the repository.

## Template for new entries

```markdown
## Entry N: <task>

### Delegation
What was delegated to the AI and what was kept.

### Description (prompt)
The prompt, in a code block.

### Discernment
How the output was checked, what was corrected or rejected.

### Diligence
What the team takes responsibility for.
```
