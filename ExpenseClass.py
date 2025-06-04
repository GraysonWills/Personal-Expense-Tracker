class Expense:
    def __init__(self, date, category, amount, description):
        self._expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }

    def get_key(self, key: str):
        return self._expense.get(key)
        
    def __str__(self):
        return f"Date: {self._expense['date']}, Category: {self._expense['category']}, Amount: {self._expense['amount']}, Description: {self._expense['description']}"
