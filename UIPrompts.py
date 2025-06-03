UI_INITIAL_PROMPT = """
Welcome to your expense tracker!
"""

UI_QUESTION_FLOW = """
Please select an option to proceed:
1. Create an Expense
2. View Expenses
3. Track Budget
4. Save/Load Expense Report
5. Exit
"""

UI_EXPENSE_CREATION_PROMPT = """
Please enter the details for your expense:
"""

TRACK_BUDGET_ERROR = """
You have exceeded your budget! Please review your expenses.
"""

UI_LOAD_FILE_PROMPT = """
Would you like append to your existing session or overwrite it?

1. Append
2. Overwrite
3. Cancel
"""
UI_LOAD_FILE_ERROR = """
Uh oh! Looks like you don't have a saved file to load from.
Try saving your expenses first before loading them.
"""
UI_EXIT_MESSAGE = """
Thank you for using the expense tracker! Goodbye!
"""

UI_IMPROPER_INPUT = """
Invalid choice. Please select a number from the given list.
"""

