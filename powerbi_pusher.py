import requests
import json

class PowerBIPusher:
    """Class to handle pushing data to Power BI."""
    
    def __init__(self, push_url):
        self.push_url = push_url
    
    def push_data(self, data):
        """Pushes data to Power BI dataset."""
        data_json = json.loads(data.to_json(orient='records'))
        response = requests.post(
            self.push_url,
            headers={'Content-Type': 'application/json'},
            data=json.dumps(data_json)
        )
        
        if response.status_code == 200:
            print("Data pushed successfully to Power BI.")
        else:
            print(f"Failed to push data to Power BI. Status code: {response.status_code}")
