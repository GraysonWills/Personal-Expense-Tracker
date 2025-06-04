import datetime
from ExpenseClass import Expense

class StateManager:

    def __init__(self):
        self._expenses = []
        self._budget = float('inf') # Set to infinity by default to mean that no budget is set
        self._totalSpent = 0.0 # Set to 0.0 to avoid issues with float precision


    def get_expenses(self) -> list[Expense]:
        return self._expenses

    
    def set_expenses(self, expenses: list[Expense]) -> str:
        self._expenses = expenses
        return "Expenses set successfully"
    
    
    def get_budget(self) -> float:
        return self._budget
    
    
    def set_budget(self, budget: float) -> tuple[str, bool]:
        
        reason, isValid = self.validate_budget(budget)
        
        if not isValid:
            return reason, False
        
        self._budget = budget
        
        return "Budget set successfully", True

    
    def validate_budget(self, budget: float) -> tuple[str, bool]:
        return self.validate_amount(budget)

    
    def get_total_spent(self) -> float:
        return self._totalSpent
    
    def recalculate_total_spent(self) -> float:
        self._totalSpent = sum(expense.get_key('amount') for expense in self._expenses)
    
    def check_budget(self) -> bool:
        """Check if the budget has been exceeded."""
        
        if self._totalSpent > self._budget:
            return False
        
        return True
    
    
    def create_expense(self, **kwargs) -> str: # Wanted to practice using **kwargs, should be guaranteed to receive these keys
        
        reason, isValid = self.validate_expense(**kwargs)
        if not isValid:
            return f"Invalid expense data: {reason}"
        
        expense = Expense(
            date=kwargs.get('date'), 
            category=kwargs.get('category'), 
            amount=kwargs.get('amount'), 
            description=kwargs.get('description')
            )

        self._expenses.append(expense)
        self._totalSpent += expense.get_key('amount')

        return reason
    
    
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
        
        reason, isValid = self.validate_amount(kwargs.get('amount', 0))
        
        if not isValid:
            return reason, False

        if not kwargs.get('description'):
            return "Description is required.", False
        
        return "You're expense has been added successfully", True
    
    def validate_amount(self, value: float) -> tuple[str, bool]:

        if not isinstance(value, (int, float)):
            return "Invalid amount. Amount must be a number.", False
        
        if value <= 0:
            return "Invalid amount. Amount must be positive.", False
        
        if isinstance(value, float) and len(str(value).split('.')[-1]) > 2:
            return "Invalid amount. Amount cannot have more than 2 decimal places.", False     

        return "Valid amount.", True
        