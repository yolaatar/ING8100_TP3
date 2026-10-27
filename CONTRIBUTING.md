# Contributing

Thanks for contributing! This file explains how we work on this repository. By participating, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Reporting issues

Every piece of work starts with a GitHub issue.

1. Check the [existing issues](https://github.com/yolaatar/ING8100_TP3/issues) first to avoid duplicates.
2. Open a new issue with:
   - a short, explicit title (e.g. `Add Borealis download script`),
   - a description of the task or bug, and what "done" looks like,
   - for a bug: steps to reproduce, expected vs actual behavior, and your environment (OS, Python version).
3. Assign the issue to whoever takes it.

## Workflow

`main` is protected: nobody can push to it directly. All changes go through a pull request.

1. Pick or create an issue and assign it to yourself.
2. Update your local `main`:
   ```bash
   git checkout main
   git pull
   ```
3. Create a branch following the naming convention below:
   ```bash
   git checkout -b feature/12-download-script
   ```
4. Commit small, focused changes with meaningful messages.
5. Push your branch and open a pull request against `main`.
6. Link the issue in the PR description with `Closes #<issue>` so it closes automatically on merge.
7. Get **at least one approving review** from another team member. Address review comments by pushing new commits to the same branch.
8. Once approved and up to date, merge the PR and delete the branch.

## Branch naming convention

```
<type>/<issue-number>-<short-description>
```

- lowercase, words separated by hyphens
- `<type>` is one of:

| Type        | Use for                                        | Example                          |
|-------------|------------------------------------------------|----------------------------------|
| `feature/`  | new script, analysis or functionality          | `feature/12-download-script`     |
| `fix/`      | bug fix                                        | `fix/18-missing-values-crash`    |
| `docs/`     | README, report, documentation only             | `docs/7-update-readme`           |
| `env/`      | environment, dependencies, `.gitignore`, CI    | `env/9-environment-yml`          |
| `refactor/` | code reorganization with no behavior change    | `refactor/21-split-preprocess`   |

## Commit messages

- Imperative mood, short summary line (around 50 characters max): `Add preprocessing for missing values`
- Optionally a blank line followed by more context on *why* the change was made.
- Reference the issue when relevant: `Add download script (#12)`
- One logical change per commit; avoid `wip`, `fix`, `update` with no context.

## Pull requests

- Title: clear summary of the change.
- Description: what changed, why, and `Closes #<issue>`.
- Keep PRs small and focused on a single issue.
- Make sure the scripts still run from a fresh environment before asking for review.

## Reviewing

- Reviewers check that the code runs, is readable and commented, and that documentation (README, report) is updated when needed.
- Be constructive and specific: suggest, explain, and point to lines.
- Approve only when you would be comfortable having the change in `main`.

## Code conventions

- Python, following [PEP 8](https://peps.python.org/pep-0008/).
- Comments explain *why*, not just *what* (see the [MIT Communication Lab guide](https://mitcommlab.mit.edu/broad/commkit/coding-and-comment-style/)).
- Never commit data files: data is downloaded from Borealis by the download script.
- Add any new dependency to the environment file in the same PR.
