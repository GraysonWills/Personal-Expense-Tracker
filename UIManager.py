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
                date_input = input("Enter date (YYYY-MM-DD): ")
                from datetime import datetime
                date = datetime.strptime(date_input, '%Y-%m-%d').strftime('%Y-%m-%d') # Throws an error if the date is invalid
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")

        category = input("Enter category: ")
    
        while True:
            try:
                amount = float(input("Enter amount: "))
                self.validate_number_input(amount)
                break
            except ValueError:
                print("Invalid amount. Please enter a valid input. It must be a positive number with up to two decimal places.")
    
        description = input("Enter description: ")

        self.create_expense(date=date, category=category, amount=amount, description=description)
        print(f"Expense created: {date}, {category}, ${amount:.2f}, {description}")
        self.check_budget()

    def display_expenses(self):
        expenses = self.get_expenses()
        
        print("\n{:<12} {:<15} {:<10} {:<20}".format("Date", "Category", "Amount", "Description")) # Table headers
        print("-" * 57)
        
        for expense in expenses: 
            print("{:<12} {:<15} ${:<9.2f} {:<20}".format( # Pythonic comprehension to format the output
                *[expense.get_key(key) for key in ['date', 'category', 'amount', 'description']]
            ))
        
    def set_a_budget(self) -> str:
        
            print(UIPrompts.UI_BUDGET_CHOICE)
        
            budget_choice = input(UIPrompts.UI_SELECT_AN_OPTION)
            
            if budget_choice == '1':
                while True:
                    try:
                        budget = float(input("Enter your budget: "))
                        self.validate_number_input(budget)
                        self.set_budget(budget)
                        print(f"Budget set to: ${budget:.2f}")
                        break
                    except ValueError:
                        print("Invalid budget. Please enter a valid input. It must be a positive number with up to two decimal places.")

            elif budget_choice == '2':
                if self.get_budget() == float('inf'):
                    print("No budget has been set yet.")
                    return
                print(f"Current budget: ${self.get_budget():.2f}")

            elif budget_choice == '3':
                return
            
            else:
                print(UIPrompts.UI_IMPROPER_INPUT)
                return
            
            self.check_budget()

            
    def check_budget(self):
        if self.get_total_spent() > self.get_budget():
                total_spent = self.get_total_spent()
                budget = self.get_budget()
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
        
                self.write_csv_async(self.get_expenses())
                self._writeThread.join()
                print("Expenses saved successfully.")

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
                        self.set_expenses(self._asyncQueue.get())
                    else:
                        print(UIPrompts.UI_CORRUPT_DATA_WARNING)
                        return
        
                    self.recalculate_total_spent()
        
                except Exception as e:
                    print(UIPrompts.UI_LOAD_FILE_ERROR)

            elif choice == '3':
                return
            
            else:
                print(UIPrompts.UI_IMPROPER_INPUT)

    def validate_number_input(self, value: float):
        if value <= 0:
            raise ValueError()
        
        if isinstance(value, float) and len(str(value).split('.')[-1]) > 2: # Checks if the number has more than 2 decimal places
            raise ValueError()