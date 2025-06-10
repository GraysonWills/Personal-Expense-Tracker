import datetime
from ExpenseClass import Expense

class StateManager:

    def __init__(self):
        self._expenses = []
        self._budget = float('inf') # Set to infinity by default to mean that no budget is set
        self._totalSpent = 0.0 # Set to 0.0 to avoid issues with float precision
    
    @property
    def expenses(self) -> list[Expense]:
        return self._expenses
    
    @expenses.setter
    def expenses(self, expenses: list[Expense]):
        self._expenses = expenses    
    
    @property
    def budget(self) -> float:
        return self._budget
    
    @budget.setter
    def budget(self, budget: float):
        self._budget = budget
    
    @property
    def total_spent(self) -> float:
        return self._totalSpent
    
    def recalculate_total_spent(self):
        self._totalSpent = sum(float(expense.get_key('amount')) for expense in self._expenses) # Pythonic comprehension to sum amounts
    
    def check_budget(self) -> bool:        
        if self._totalSpent > self._budget:
            return False
        return True
    
    def add_expense(self, expenseDictionary):
        expense = Expense(expenseDictionary)
        self._expenses.append(expense)
        self._totalSpent += float(expense.get_key('amount'))

    def set_budget(self, budget: float):
        """Set a numeric budget for expenses."""
        self._budget = float(budget)

    def get_expenses(self) -> list[Expense]:
        """Return the current list of Expense objects."""
        return self._expenses

    def get_total_spent(self) -> float:
        """Return the total amount spent across all expenses."""
        return self._totalSpent
