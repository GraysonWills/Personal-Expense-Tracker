# Personal Expense Tracker Writeup

This document provides an overview of the project located in this repository. The application is a small command line tool written in Python that allows a user to record day‑to‑day expenses, optionally set a budget and persist data to a CSV file.
It targets Python 3.11 but should work on any recent Python 3 release.

## Structure
The main modules are:

- `ExpenseClass.py` – simple wrapper around a single expense entry.
- `StateManager.py` – keeps track of the list of expenses, the running total and the active budget.
- `CSVService.py` – handles reading and writing the expenses list to disk using a background thread.
- `UIManager.py` – coordinates user interaction, utilising the other classes.
- `UIPrompts.py` – central location for all displayed strings.
- `main.py` – entry point containing the menu loop.

Unit tests reside in `tests/` and cover the core behaviour of each component.

## Running the Application
1. Create a virtual environment and install dependencies (none by default):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Launch the tracker using:
   ```bash
   python main.py
   ```
   Follow the prompts to add expenses, view them, configure a budget and save or load data.

## Tests
The repository includes a small unit test suite under `tests/`.
It can be executed using Python's standard `unittest` runner:
```bash
python -m unittest discover -v
```
All tests currently pass and validate the behaviour of each module.

## Notes
The design deliberately splits functionality into multiple small classes to keep concerns separate. `StateManager` tracks domain data while `CSVService` focuses on persistence. `UIManager` inherits from both to combine their capabilities, presenting a simple interface for the CLI defined in `main.py`.

