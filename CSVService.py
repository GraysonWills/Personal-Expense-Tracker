from threading import Thread
import queue
class CSVService:
    def __init__(self):
        self.csv_file_path = 'expenseTracker.csv'
        self.async_queue = queue.Queue()

    def convert_listdict_to_csv(self, data: list[dict]) -> str:
        """Convert a list of dictionaries to a CSV string."""
        csv_string = 'Date,Category,Amount,Description\n'
        for item in data:
            csv_string += f'{item["Date"]},{item["Category"]},{item["Amount"]},{item["Description"]}\n'
        return csv_string
    
    def convert_csv_to_listdict(self, csv_data: str) -> list[dict]:
        """Convert a CSV string to a list of dictionaries."""
        lines = csv_data.strip().split('\n')
        headers = lines[0].split(',')
        data = []
        for line in lines[1:]:
            values = line.split(',')
            item = {headers[i]: values[i] for i in range(len(headers))}
            data.append(item)
        return data
    
    def read_csv(self):
        """Read the CSV file and return its content."""
        with open(self.csv_file_path, 'r') as file:
            fullCSV = file.read()
        self.async_queue.put(self.convert_csv_to_listdict(fullCSV))

    def write_csv(self, data):
        """Write data to the CSV file."""
        csv_string = self.convert_listdict_to_csv(data)
        with open(self.csv_file_path, 'w') as file:
            file.writelines(csv_string)
    
    def load_csv_async(self):
        """Load CSV data asynchronously."""
        Thread(target=self.read_csv).start()
        
    def write_csv_async(self, data):
        """Write data to the CSV file asynchronously."""
        Thread(target=self.write_csv, args=(data,)).start()
