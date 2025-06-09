# Welcome and Navigation
UI_INITIAL_PROMPT = """
Welcome to your expense tracker!"""

UI_QUESTION_FLOW = """
Please select an option to proceed:
1. Create an Expense
2. View Expenses
3. Track Budget
4. Save/Load Expense Report
5. Exit"""

UI_SELECT_AN_OPTION = """
Select an option: """

UI_INPUT_TO_CANCEL = """
Input '?' to cancel"""

UI_OPERATION_CANCELLED = """
Operation cancelled"""

UI_IMPROPER_INPUT = """
Invalid choice. Please select a number from the given list."""

UI_EXIT_MESSAGE = """
Thank you for using the expense tracker! Goodbye!"""

# Expense Creation
UI_EXPENSE_CREATION_PROMPT = """
Please enter the details for your expense:"""

UI_EXPENSE_DATE_PROMPT = "Enter date (YYYY-MM-DD): "

UI_EXPENSE_CATEGORY_PROMPT = "Enter category: "

UI_EXPENSE_AMOUNT_PROMPT = "Enter amount: "

UI_EXPENSE_DESCRIPTION_PROMPT = "Enter description: "

UI_EXPENSE_CREATED = "Expense created!"

UI_INVALID_DATE_FORMAT = "Invalid date format. Please use YYYY-MM-DD format."

UI_INVALID_AMOUNT = "Invalid amount. Please enter a valid input. It must be a positive number with up to two decimal places."

# Budget Management
UI_BUDGET_CHOICE = """
Would you like to set a budget for your expenses, or see your current budget?

1. Set Budget
2. See Budget
3. Cancel"""

UI_BUDGET_PROMPT = "Enter your budget: "

UI_BUDGET_SET = "Budget set to: $%.2f"

UI_NO_BUDGET_SET = "No budget has been set yet."

UI_CURRENT_BUDGET = "Current budget: $%.2f"

UI_INVALID_BUDGET = "Invalid budget. Please enter a valid input. It must be a positive number with up to two decimal places."

UI_TRACK_BUDGET_ERROR = """
You have exceeded your budget by $%.2f! Your total amount is $%.2f and your budget is $%.2f. Please set a budget amount higher than $%.2f."""

# Save/Load Operations
UI_SAVE_LOAD_CHOICE = """
Would you like to save your expenses to a file, or load them from a file?
1. Save Expenses
2. Load Expenses
3. Cancel"""

UI_SAVE_FILE_PROMPT = """
Your current save file (if you have one) will be overwritten."""

UI_SAVE_LOAD_OVERWRITE_CHOICE = f"""
{UI_INPUT_TO_CANCEL}, or any other key to continue: """

UI_LOAD_FILE_PROMPT = """
Your current session will be overwritten if you load from a file."""

UI_EXPENSES_SAVED = "Expenses saved successfully."

UI_CORRUPT_DATA_WARNING = """
The file you are trying to load is corrupted or not in the correct format.
Please check the file and try again."""

UI_NO_SAVED_EXPENSES = """
Uh oh! Looks like you don't have a saved file to load from.
Try saving your expenses first before loading them."""

# Display formatting
UI_EXPENSE_TABLE_SEPARATOR = "-" * 57
