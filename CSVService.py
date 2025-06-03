from threading import Thread
import queue
class CSVService:
    def __init__(self):
        self.__csvFilePath = 'expenseTracker.csv'
        self._asyncQueue = queue.Queue()
        self._loadThread = None
        self._writeThread = None

    def convert_listdict_to_csv(self, data: list[dict]) -> str:
        """Convert a list of dictionaries to a CSV string."""
        csvString = 'Date,Category,Amount,Description\n'
        for item in data:
            csvString += f'{item["date"]},{item["category"]},{item["amount"]},{item["description"]}\n'
        return csvString
    
    def convert_csv_to_listdict(self, csv_data: str) -> list[dict]:
        """Convert a CSV string to a list of dictionaries."""
        lines = csv_data.strip().split('\n')
        headers = lines[0].lower().split(',')
        data = []
        for line in lines[1:]:
            values = line.split(',')
            item = {headers[i]: values[i] for i in range(len(headers))}
            data.append(item)
        return data
    
    def read_csv(self):
        """Read the CSV file and return its content."""
        with open(self.__csvFilePath, 'r') as file:
            fullCSV = file.read()
        self._asyncQueue.put(self.convert_csv_to_listdict(fullCSV))

    def write_csv(self, data):
        """Write data to the CSV file."""
        csvString = self.convert_listdict_to_csv(data)
        with open(self.__csvFilePath, 'w') as file:
            file.writelines(csvString)
    
    def load_csv_async(self):
        """Load CSV data asynchronously."""
        self._loadThread = Thread(target=self.read_csv)
        self._loadThread.start()
        
    def write_csv_async(self, data):
        """Write data to the CSV file asynchronously."""
        self._writeThread = Thread(target=self.write_csv, args=(data,))
        self._writeThread.start()
