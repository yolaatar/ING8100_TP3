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

### Description

**Original prompt:**

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

**Context the AI already had (not visible in the prompt above):**

The prompt reads as vague on its own, but it was not sent cold. Claude Code automatically loads a persistent instruction file (`~/.claude/CLAUDE.md`) at the start of every session, and that file was already in place when this prompt was run. It is personal and shared across all my projects, so it is not part of this repository, but it gave the AI a lot of the context the prompt seems to skip:

- **Who I am**: research master's student at NeuroPoly (Polytechnique Montréal), working on axon segmentation in electron microscopy with AxonDeepSeg. This is why the AI already knew what a TEM dataset of myelinated axons is and did not need it explained.
- **Git and GitHub conventions**: concise, descriptive commit messages; short, casual PR descriptions; no AI attribution lines or "generated with" footers in commits, PRs or comments.
- **Writing style**: short and human, no em dashes.
- **Project-specific rules**: other repositories I work in have their own `CLAUDE.md` with branch naming conventions (e.g. `yl/feature-name`), one feature per branch/PR, PR workflow, and analysis conventions (figure format, which venv to use). These shaped the habits the AI applied here (branch naming in CONTRIBUTING.md, PR-based workflow).

So the short prompt only had to cover what was specific to this lab: the source of truth (the lab page), the deliverables and the stop condition. The trade-off is reproducibility: someone else running the same prompt without that file would get a different result, which is why the improved prompt below spells the context out explicitly.

What worked: a link to the source of truth (the lab page), an explicit list of deliverables, and a stop condition ("stop after these items"), so the AI did not invent analysis code for a dataset it knows nothing about.

What was missing: even with the persistent instructions, nothing told the AI about this specific course and team: the course and lab number, the teammates, which dataset from lab 2 we are using, the repository name and visibility, who the reviewers are, and what "done" means. The AI had to ask for the repo name, teammates and license before starting, and left the dataset as placeholders.

**Improved prompt** (what we would send now):

```text
Context: ING8100 (Polytechnique Montréal), lab 3, team of 3. We build a
reproducible project around the TEM dataset (mouse optic nerve, TEM1) we
published on Borealis in lab 2. Lab instructions:
https://reproducible-research.polymtl.ca/fr/lab3/ (read them first).

Task: set up everything that does not depend on the data:
- public GitHub repo yolaatar/ING8100_TP3, teammate <login> invited with
  write access,
- README.md following the World Bank template linked in the lab, describing
  the current state of the project only,
- LICENSE (MIT, the data keeps its Borealis license),
- CONTRIBUTING.md with our branch naming convention and PR workflow,
- CODE_OF_CONDUCT.md (Contributor Covenant),
- AI_Prompts.md structured with the 4D framework,
- protection of main: no direct push (admins included), PR with at least one
  approval from another team member.

Constraints: documents in English, short and readable. Do not invent anything
about the dataset or the research question: use clearly marked TODO
placeholders. Do not write the download/preprocessing/analysis scripts.

Done when: everything is pushed in one commit before main is protected, and a
direct push to main is rejected. Tell me what you could not do or verify.
```

What the improved version adds:

- **Context** (course, team, dataset), so the AI does not have to ask or guess, and so the prompt works on its own without my personal `CLAUDE.md`.
- **Concrete parameters** (repo name and visibility, teammate, exact protection rules) instead of leaving them to be asked.
- **Constraints on format and honesty**: language, style, and no invented content about the data.
- **A definition of done** that can be checked (push rejected on main), including asking the AI to report what it could not verify.

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
