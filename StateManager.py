import datetime
class StateManager:

    def __init__(self):
        self._expenses = []
        self._budget = int.MAX_VALUE
        self._totalSpent = 0

    def get_expenses(self) -> list[dict]:
        return self._expenses
    
    def create_expense(self, **kwargs): # Wanted to practice using **kwargs, should be guaranteed to receive these keys
        
        reason, isValid = self.validate_expense(**kwargs)
        if not isValid:
            return f"Invalid expense data: {reason}"
        
        expense = {
            'date': kwargs.get('date', ''),
            'category': kwargs.get('category', ''),
            'amount': kwargs.get('amount', 0),
            'description': kwargs.get('description', '')
        }
        self._expenses.append(expense)
        self._totalSpent += expense['Amount']
        return "You're expense has been added successfully."
    
    def validate_expense(self, **kwargs) -> tuple[str, bool]:
        """Validate if the expense is valid."""
        if not kwargs.get('date'):
            return "Date is required.", False
        try: # Validate Date Format
            datetime.datetime.strptime(kwargs['date'], '%Y-%m-%d')
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD.", False      
        if not kwargs.get('category'):
            return "Category is required.", False
        if not isinstance(kwargs.get('amount'), (int, float)):
            return "Invalid amount. Amount must be a number.", False
        if kwargs['amount'] <= 0:
            return "Invalid amount. Amount must be positive.", False
        if isinstance(kwargs['amount'], float) and len(str(kwargs['amount']).split('.')[-1]) > 2:
            return "Invalid amount. Amount cannot have more than 2 decimal places.", False        
        if not kwargs.get('description'):
            return "Description is required.", False
        return 0, True