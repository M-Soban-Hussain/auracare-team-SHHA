# AuraCare Health System Core

**Class Activity 2: Team Collaboration Class Task**
**Scenario:** The AuraCare Feature Release Sprint

This repository is designed to practice Git workflow, branch protection, code reviews, and merge conflict resolution.

## Team Structure
*   **Engineering Lead / Repo Manager:** M. Soban Hussain
*   **Developer A (Patient Triage):** [Hamza Mudassir]
*   **Developer B (Doctor Schedule):** [Hamza Imran]
*   **Developer C (Conflict Specialist):** [Muhammad Ali]

## Role Responsibilities

### 1. Engineering Lead
*   Initialize the repository and `main.py` core file.
*   Configure branch protection rules on `main` requiring 1 PR approval.
*   Act as the primary code reviewer to comment on and approve team Pull Requests.

### 2. Developer A
*   **Branch:** `feature/triage-module`
*   **Task:** Add patient triage logic to `main.py`.
*   **Commit:** `git commit -m "PROJ-1: add patient triage logic"`
*   **Deliverable:** Push branch and open PR #1.

### 3. Developer B
*   **Branch:** `feature/doctor-schedule`
*   **Task:** Add doctor schedule lookup logic to the bottom of `main.py`.
*   **Commit:** `git commit -m "PROJ-2: add doctor schedule lookup"`
*   **Deliverable:** Push branch and open PR #2.

### 4. Developer C
*   **Branch:** `feature/app-config`
*   **Task:** Modify the exact same lines as Developer A in `main.py` (e.g., change `APP_VERSION = "2.0.0-Beta"`) to create an intentional merge conflict.
*   **Deliverable:** Push branch and open PR #3.

## Submission Deliverables
*   **Network Graph:** Must display 3 feature branches merging cleanly into `main`.
*   **Pull Requests Tab:** Must display 3 merged PRs containing code review comments.
