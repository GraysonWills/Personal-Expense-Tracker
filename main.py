from StateManager import StateManager
from CSVService import CSVService
import UIPrompts

class UIManager(CSVService, StateManager):
    def __init__(self):
        CSVService.__init__(self)
        StateManager.__init__(self)

    def create_an_expense(self):
        date = input("Enter date (YYYY-MM-DD): ")

        category = input("Enter category: ")
        
        amount = float(input("Enter amount: $"))
        
        description = input("Enter description: ")
        
        print(self.create_expense(date=date, category=category, amount=amount, description=description))
        
        self.check_budget()

    def display_expenses(self):
        
        expenses = self.get_expenses()
        
        print("\n{:<12} {:<15} {:<10} {:<20}".format("Date", "Category", "Amount", "Description"))
        
        print("-" * 57)
        
        for expense in expenses:

            print("{:<12} {:<15} ${:<9.2f} {:<20}".format(
                expense.get_key('date'),
                expense.get_key('category'),
                expense.get_key('amount'),
                expense.get_key('description')
            ))

    def set_a_budget(self) -> str:
        
            print(UIPrompts.UI_BUDGET_CHOICE)
        
            budget_choice = input("Select an option: ")
            
            if budget_choice == '1':
                budget = float(input("Enter your budget: "))
                self.set_budget(budget)
            
            elif budget_choice == '2':
                print("Current budget:", self.get_budget())

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
            choice = input("Select an option: ")

            if choice == '1':
        
                print(UIPrompts.UI_SAVE_FILE_PROMPT)
        
                if input("Press 1 to cancel, or any other key to continue: ") == '1':
                    print("Save operation cancelled.")
                    return
        
                self.write_csv_async(self.get_expenses())
        
                self._writeThread.join()
        
                print("Expenses saved successfully.")

            elif choice == '2':
        
                try:
        
                    self.load_csv_async()
        
                    print(UIPrompts.UI_LOAD_FILE_PROMPT)
        
                    choice = input("Select an option: ")
        
                    self._loadThread.join()  # Wait for the thread to finish loading
        
                    if choice == '1':
                        self.set_expenses(list(set(self.get_expenses()) | set(self.asyncQueue.get())))
        
                    elif choice == '2':
                        self.set_expenses(self.asyncQueue.get())
        
                    elif choice == '3':
                        return  # Cancel the operation
        
                    else:
                        print(UIPrompts.UI_IMPROPER_INPUT)
        
                except Exception as e:
                    print(UIPrompts.UI_LOAD_FILE_ERROR)

            elif choice == '3':
                return
            
            else:
                print(UIPrompts.UI_IMPROPER_INPUT)



def main():
    
    ui_manager = UIManager()
    print(UIPrompts.UI_INITIAL_PROMPT)
    while(True):
        print(UIPrompts.UI_QUESTION_FLOW)
        choice = input("Select an option: ")
        
        if choice == '1':
            ui_manager.create_an_expense()
 
        elif choice == '2':
            ui_manager.display_expenses()

        elif choice == '3':
            ui_manager.set_a_budget()
        
        elif choice == '4':
            ui_manager.save_or_load_expenses()

        elif choice == '5':
            print(UIPrompts.UI_EXIT_MESSAGE)
            break

        else:
            print(UIPrompts.UI_IMPROPER_INPUT)

if __name__ == "__main__":
    main()
 