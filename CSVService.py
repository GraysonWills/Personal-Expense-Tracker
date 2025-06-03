from threading import Thread
import queue
from ExpenseClass import Expense
class CSVService:
    def __init__(self):
        self.csvFilePath = 'expenseTracker.csv'
        self.asyncQueue = queue.Queue()
        self.loadThread = None
        self.writeThread = None

    def convert_listdict_to_csv(self, data: list[Expense]) -> str:
        """Convert a list of dictionaries to a CSV string."""
        csvString = 'date,category,amount,description\n'
        for item in data:
            csvString += f'{item.get_key("date")},{item.get_key("category")},{item.get_key("amount")},{item.get_key("description")}\n'
        return csvString
    
    def convert_csv_to_listdict(self, csv_data: str) -> list[Expense]:
        """Convert a CSV string to a list of dictionaries."""
        lines = csv_data.strip().split('\n')
        headers = lines[0].split(',')
        data = []
        for line in lines[1:]:
            values = line.split(',')
            item = Expense(
                date=values[0],
                category=values[1],
                amount=float(values[2]),
                description=values[3]
            )
            data.append(item)
        return data
    
    def read_csv(self):
        """Read the CSV file and return its content."""
        with open(self.csvFilePath, 'r') as file:
            fullCSV = file.read()
        self.asyncQueue.put(self.convert_csv_to_listdict(fullCSV))

    def write_csv(self, data):
        """Write data to the CSV file."""
        csvString = self.convert_listdict_to_csv(data)
        with open(self.csvFilePath, 'w') as file:
            file.writelines(csvString)
    
    def load_csv_async(self):
        """Load CSV data asynchronously."""
        self.loadThread = Thread(target=self.read_csv)
        self.loadThread.start()
        
    def write_csv_async(self, data):
        """Write data to the CSV file asynchronously."""
        self.writeThread = Thread(target=self.write_csv, args=(data,))
        self.writeThread.start()
