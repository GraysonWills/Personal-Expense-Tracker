# Personal Expense Tracker

This project is a command line based application for tracking daily expenses. It was created as a school project to practice Python programming and version control workflows.

## Purpose
The tracker lets users enter expenses, keep an optional budget and store or load the data from a CSV file. It was built as an exercise in breaking down a larger program into small components and planning the overall architecture before writing the code.

## Project Approach
1. **Planning the components** – I started by mapping out the pieces the tracker would need, including how expenses are represented, how state is stored, and how to interact with the user.
2. **Coding step by step** – Each component (expense representation, state management, CSV utilities, and user interface) was implemented individually and tested in isolation before being tied together in `main.py`.
3. **Branching strategy** – After establishing the core functionality I planned a branching workflow in Git. Each new feature or refactor went into its own branch and was merged once complete, resulting in the final history you see in this repository.

Through this process I learned how valuable up‑front planning can be and how to keep code changes isolated with branches.

## Installation
1. Clone the repository.
2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install required packages (there are none by default, but this ensures consistency):
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Codebase Structure
- `main.py` – Entry point. Provides the command line loop.
- `UIManager.py` – Handles user interactions and coordinates actions.
- `CSVService.py` – Asynchronous read/write helper for the CSV file.
- `StateManager.py` – Keeps the list of expenses and budget in memory.
- `ExpenseClass.py` – Simple wrapper around a single expense record.
- `UIPrompts.py` – Holds strings used for prompts and messages.
- `expenseTracker.csv` – Example CSV data file.

## Lessons Learned
Working on this project taught me how to organize a small codebase, design functions that work together cleanly and keep track of work with branches. Building from a clear design document helped me turn ideas into a finished Python program.
