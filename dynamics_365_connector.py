import pyodbc
import pandas as pd

class Dynamics365Connector:
    """Class to handle connection and data retrieval from Dynamics 365."""
    
    def __init__(self, server, database, username, password):
        self.connection_string = (
            f'DRIVER={{SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password}'
        )
        
    def get_data(self, query):
        """Connects to the Dynamics 365 database and retrieves data based on the provided query."""
        conn = pyodbc.connect(self.connection_string)
        data = pd.read_sql(query, conn)
        conn.close()
        return data
