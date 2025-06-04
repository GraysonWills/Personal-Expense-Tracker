class Expense:
    def __init__(self, expenseDictionary):
        self._expense = expenseDictionary

    def get_key(self, key: str):
        return self._expense.get(key)
        
    def __str__(self): # For debugging purposes
        return ', '.join(f"{key.capitalize()}: {self._expense[key]}" for key in self._expense)
    

    