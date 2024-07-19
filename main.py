from dynamics365_connector import Dynamics365Connector
from powerbi_pusher import PowerBIPusher
import pandas as pd

def main():
    # Define your connection details and query
    server = 'your_server_name'
    database = 'your_database_name'
    username = 'your_username'
    password = 'your_password'
    query = "SELECT * FROM your_table_name"
    
    # Initialize Dynamics365Connector
    dynamics_connector = Dynamics365Connector(server, database, username, password)
    
    # Retrieve data from Dynamics 365
    data = dynamics_connector.get_data(query)
    
    # Manipulate and format your data using pandas
    data.rename(columns={
        'old_column_name1': 'new_column_name1',
        'old_column_name2': 'new_column_name2'
    }, inplace=True)
    
    filtered_data = data[data['column_name'] > some_value]
    
    # Define your Power BI push URL
    power_bi_push_url = 'https://api.powerbi.com/beta/your_workspace_id/datasets/your_dataset_id/rows?key=your_push_key'
    
    # Initialize PowerBIPusher
    power_bi_pusher = PowerBIPusher(power_bi_push_url)
    
    # Push data to Power BI
    power_bi_pusher.push_data(filtered_data)

if __name__ == '__main__':
    main()
