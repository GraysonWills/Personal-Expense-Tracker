import os
from StateManager import StateManager
from CSVService import CSVService
import UIPrompts

class UIManager(CSVService, StateManager):
    def __init__(self):
        CSVService.__init__(self)
        StateManager.__init__(self)

    def create_an_expense(self):
        while True:
            try:
                date_input = input(UIPrompts.UI_EXPENSE_DATE_PROMPT)
                from datetime import datetime
                date = datetime.strptime(date_input, '%Y-%m-%d').strftime('%Y-%m-%d') # Throws an error if the date is invalid
                break
            except ValueError:
                print(UIPrompts.UI_INVALID_DATE_FORMAT)

        category = input(UIPrompts.UI_EXPENSE_CATEGORY_PROMPT)
    
        while True:
            try:
                amount = input(UIPrompts.UI_EXPENSE_AMOUNT_PROMPT)
                self.validate_number_input(amount)
                break
            except ValueError:
                print(UIPrompts.UI_INVALID_AMOUNT)
    
        description = input(UIPrompts.UI_EXPENSE_DESCRIPTION_PROMPT)

        expenseDictionary = {
                    'date': date,
                    'category': category,
                    'amount': amount,
                    'description': description
                }
        
        self.add_expense(expenseDictionary)
        print(UIPrompts.UI_EXPENSE_CREATED)
        self.check_budget()

    def display_expenses(self):
        expenses = self.expenses
        dictionaryKeys = list(expenses[0]._expense.keys())
        
        print("\n{:<12} {:<15} {:<10} {:<20}".format(*[key.title() for key in dictionaryKeys])) # Table headers        
        print(UIPrompts.UI_EXPENSE_TABLE_SEPARATOR)
        
        for expense in expenses: 
            print("{:<12} {:<15} ${:<9.2} {:<20}".format( # Pythonic comprehension to format the output
                *[expense.get_key(key) for key in dictionaryKeys]
            ))
        
    def set_a_budget(self) -> str:
        
            print(UIPrompts.UI_BUDGET_CHOICE)
        
            budget_choice = input(UIPrompts.UI_SELECT_AN_OPTION)
            
            if budget_choice == '1':
                while True:
                    try:
                        budget = input(UIPrompts.UI_BUDGET_PROMPT)
                        self.validate_number_input(budget)
                        self.budget = float(budget)
                        print(UIPrompts.UI_BUDGET_SET % float(budget))
                        break
                    except ValueError:
                        print(UIPrompts.UI_INVALID_BUDGET)

            elif budget_choice == '2':
                if self.budget == float('inf'):
                    print(UIPrompts.UI_NO_BUDGET_SET)
                    return
                print(UIPrompts.UI_CURRENT_BUDGET % self.budget)

            elif budget_choice == '3':
                return
            
            else:
                print(UIPrompts.UI_IMPROPER_INPUT)
                return
            
            self.check_budget()

            
    def check_budget(self):
        if self.total_spent > self.budget:
                total_spent = self.total_spent
                budget = self.budget
                over_budget_amount = total_spent - budget
                recommended_budget = budget + over_budget_amount
                print(UIPrompts.UI_TRACK_BUDGET_ERROR % (over_budget_amount, total_spent, budget, recommended_budget))
        

    def save_or_load_expenses(self):
            print(UIPrompts.UI_SAVE_LOAD_CHOICE)
            choice = input(UIPrompts.UI_SELECT_AN_OPTION)

            if choice == '1':
                print(UIPrompts.UI_SAVE_FILE_PROMPT)
        
                if input(UIPrompts.UI_SAVE_LOAD_OVERWRITE_CHOICE) == '?':
                    print(UIPrompts.UI_OPERATION_CANCELLED)
                    return
        
                self.write_csv_async(self.expenses)
                self._writeThread.join()
                print(UIPrompts.UI_EXPENSES_SAVED)

            elif choice == '2':
                if not os.path.exists(self._csvFilePath):
                    print(UIPrompts.UI_NO_SAVED_EXPENSES)
                    return

                try:
                    self.load_csv_async()
        
                    if input(UIPrompts.UI_SAVE_LOAD_OVERWRITE_CHOICE) == '?':
                        print(UIPrompts.UI_OPERATION_CANCELLED)
                        return
        
                    self._loadThread.join()  # Wait for the thread to finish loading
                    if not self._asyncQueue.empty():
                        self.expenses = self._asyncQueue.get()
                    else:
                        print(UIPrompts.UI_CORRUPT_DATA_WARNING)
                        return
        
                    self.recalculate_total_spent()
        
                except Exception as e:
                    print(UIPrompts.UI_CORRUPT_DATA_WARNING)

            elif choice == '3':
                return
            
            else:
                print(UIPrompts.UI_IMPROPER_INPUT)

    def validate_number_input(self, value: str):

        try:
            value = float(value)
        except ValueError:
            raise ValueError()
        
        if value <= 0:
            raise ValueError()
        
        if isinstance(value, float) and len(str(value).split('.')[-1]) > 2: # Checks if the number has more than 2 decimal places
            raise ValueError()
