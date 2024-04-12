import pyodbc

class Database:
    def __init__(self):
        self.server = 'your_server_name'
        self.database = 'your_database_name'
        self.port = '1433'
        self.username = 'your_username'
        self.password = 'your_password'
        self.trusted_connection = 'yes'

    def connect(self):
        """
        Establece la conexion con la base de datos.
        
        Returns:
            pyodbc.Connection: Objeto de conexion a la base de datos.
        """
        try:
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                        SERVER='+self.server+';\
                        DATABASE='+self.database+';\
                        PORT='+self.port+';\
                        UID='+self.username+';\
                        Trusted_Connection='+self.trusted_connection+';\
                        PWD='+ self.password)
            return conn
        except pyodbc.Error as ex:
            print(f"Error de conexion a la base de datos: {ex}")
            return None
