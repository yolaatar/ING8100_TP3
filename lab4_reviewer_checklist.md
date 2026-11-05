## Review checklist by @mathisors, @Ananelle8

### AI usage

- [x] I understand that:
  - AI may only be used for **non-substantive assistance** (e.g., grammar checking my review text, contextualizing public materials)
  - **All evaluative decisions**—including scoring, accept/reject recommendations, and assessments of correctness, quality, and reproducibility—must be made exclusively by me, not AI
  - I bear full responsibility for all judgments, recommendations, and technical claims in this review
  - I will disclose any AI assistance at the conclusion of my review

### Code of Conduct

- [x] The repository contains a Code of Conduct. 
  - R: The file is present and filled. 
- [x] I confirm that I have read and will adhere to the Code of Conduct of the repository under review. 

### General checks

- [x] **Repository:** Is the source code for this software available at [{{target-repository}}]({{target-repository}})? 
  - R: The code is present in the scripts, thought there is no source code per say. The code is structured in functions and is easy to read.
- [x] **License:** Does the repository contain a plain-text LICENSE or COPYING file with an open-source license? 
  - R: An MIT license is present
- [ ] **How to cite:** Does the repository provide instructions on how to cite the project? 
  - R: No the README and the contributing files does not explain how to cite this repo. 
- [x] **Repository organization:** Is the repository structure clear and easy to navigate?
  - R: Yes the folder structure is explained in the readme, and follows a clear and simple naming.
- [x] **README.md:** Does the repository contain a README describing the project and installation procedure in a sufficient but synthetic manner?
  - R: Yes the README is there, and the desciption is complete.
- [x] **Research artifacts:** Are research artifacts (code, data, documentation, notebooks, etc.) openly available? 
  - R: Yes, repo is public, data is available on Borealis, figures are also commited

### Reproducibility

- [x] **Dependencies:** Are all required dependencies clearly documented? 
  - R: Depencies are shown the readme, thought python libraries are only show in the requirement.tx
- [x] **Functionality documentation:** Is the core functionality of the software documented to a satisfactory level (e.g., API method documentation)? 
  -  R: Yes all files are open.
- [x] **Example usage:** Do the authors provide working examples demonstrating how to run the software?
  - R: In the README, there is an instruction for replications, however it is only for one participant, one image. There is no explanation on how to do it for the whole dataset.
- [x] **Functionality:** Does the software execute successfully following the documentation (without errors)?
  - R: Yes software executed on the first try, however the GPU option was not working, an issue was raised.
- [x] **Correctness of claims:** Does the software behave as described and produce the expected outputs/results?
  - R: Yes the figure were identical from my reproducibility attemp and their figures.
- [x] **Performance claims:** If performance claims exist, have they been verified? (If none exist, check this item.)
  - R: Storage claim is verified, the runtime is also good, but only for macbook.
- [x] **Reproducibility of results:** Can the project be reproduced using only the information provided in the repository?
  - R: Yes, without asking questions,raising issues, I was able to reproduce the results. Thought replicating the results would be slightly harder, since the code is specific to this dataset and participant.

### Open-source development history

- [x] **Open development:** Does the repository show evidence of public and iterative development (issues, pull requests, commits)?
  - R: Yes I see 11 resolved issues, 13 PR with a review and multiple commits.

### Community guidelines

- [x] The repository includes guidelines for:
  1. Contributing to the software  
  2. Reporting issues or bugs  
  3. Seeking support or help