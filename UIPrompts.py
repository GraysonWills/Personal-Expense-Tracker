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

UI_BUDGET_CHOICE ="""
Would you like to set a budget for your expenses, or see your current budget?

1. Set Budget
2. See Budget
3. Cancel
"""

UI_TRACK_BUDGET_ERROR = """
You have exceeded your budget by %.2f! Your total amount is %.2f and your budget is %.2f. Please set a budget amount higher than %.2f.
"""

UI_SAVE_LOAD_CHOICE = """
Would you like to save your expenses to a file, or load them from a file?
1. Save Expenses
2. Load Expenses
3. Cancel
"""
UI_SAVE_FILE_PROMPT = """
Your current save file (if you have one) will be overwritten. Press 1 to cancel, or any other key to continue.
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

UI_SELECT_AN_OPTION = """
Select an option: 
"""




