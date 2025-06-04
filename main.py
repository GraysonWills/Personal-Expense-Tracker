import UIPrompts
from UIManager import UIManager


def main():
    
    ui_manager = UIManager()
    print(UIPrompts.UI_INITIAL_PROMPT)
    
    while(True):
        print(UIPrompts.UI_QUESTION_FLOW)
        choice = input(UIPrompts.UI_SELECT_AN_OPTION)
        
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
 