from threading import Thread
import queue
from ExpenseClass import Expense
class CSVService:

    def __init__(self):
        self._csvFilePath = 'expenseTracker.csv'
        self._asyncQueue = queue.Queue()
        self._loadThread = None
        self._writeThread = None

    def convert_listdict_to_csv(self, data: list[Expense]) -> str:
        csvString = 'date,category,amount,description\n'
        
        for item in data:
            csvString += f'{item.get_key("date")},{item.get_key("category")},{item.get_key("amount")},{item.get_key("description")}\n'
        
        return csvString
    
    def convert_csv_to_listdict(self, csv_data: str) -> list[Expense]:
        lines = csv_data.strip().split('\n')
        headers = lines[0].split(',')
        data = []

        for line in lines[1:]:
            values = line.split(',')
            expenseDictionary = dict(map(lambda x, y: (x, y), headers, values))            
            data.append(Expense(expenseDictionary))
        
        return data
    
    def read_csv(self):
        try:
            with open(self._csvFilePath, 'r') as file:
                fullCSV = file.read()
            
            if not fullCSV.strip():
                return
            
            data = self.convert_csv_to_listdict(fullCSV)
            self._asyncQueue.put(data)

        except:
            return
    
    def write_csv(self, data):
        csvString = self.convert_listdict_to_csv(data)
        with open(self._csvFilePath, 'w') as file:
            file.writelines(csvString)
    
    def load_csv_async(self):
        self._loadThread = Thread(target=self.read_csv)
        self._loadThread.start()
        
    def write_csv_async(self):
        self._writeThread = Thread(target=self.write_csv)
        self._writeThread.start()

