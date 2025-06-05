import os
import tempfile
import unittest

from ExpenseClass import Expense
from StateManager import StateManager
from CSVService import CSVService
from UIManager import UIManager

class TestExpense(unittest.TestCase):
    def test_get_key(self):
        exp = Expense({'date': '2024-01-01', 'category': 'Food', 'amount': '10', 'description': 'Lunch'})
        self.assertEqual(exp.get_key('amount'), '10')
        self.assertIsNone(exp.get_key('nonexistent'))

class TestStateManager(unittest.TestCase):
    def test_add_expense_and_budget(self):
        sm = StateManager()
        sm.set_budget(5)
        sm.add_expense({'date': '2024-01-01', 'category': 'Food', 'amount': '10', 'description': 'Lunch'})
        self.assertEqual(len(sm.get_expenses()), 1)
        self.assertAlmostEqual(sm.get_total_spent(), 10.0)
        self.assertFalse(sm.check_budget())

class TestCSVService(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.service = CSVService()
        self.service._csvFilePath = self.temp_file.name

    def tearDown(self):
        try:
            os.unlink(self.temp_file.name)
        except FileNotFoundError:
            pass

    def test_convert_and_io(self):
        expenses = [Expense({'date': '2024-01-01', 'category': 'Food', 'amount': '12.34', 'description': 'Lunch'})]
        csv_str = self.service.convert_listdict_to_csv(expenses)
        self.assertIn('2024-01-01', csv_str)

        # Write and read back
        self.service.write_csv(expenses)
        self.service.read_csv()
        result = self.service._asyncQueue.get_nowait()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_key('amount'), '12.34')

class TestUIManager(unittest.TestCase):
    def test_validate_number_input(self):
        ui = UIManager()
        ui.validate_number_input('10.55')  # should not raise
        with self.assertRaises(ValueError):
            ui.validate_number_input('-1')
        with self.assertRaises(ValueError):
            ui.validate_number_input('1.999')

if __name__ == '__main__':
    unittest.main()
