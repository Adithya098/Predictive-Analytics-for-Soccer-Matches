import sqlite3 

class DatabaseConnection:
    def __init__(self) -> None:
        self.__connection = sqlite3.connect('my_database.db')
        self.__cursor = self.__connection.cursor()

    def get_player_by_name(self, long_name : str):
        self.__cursor.execute("SELECT * FROM my_table WHERE long_name = ?", (long_name,))
        row = self.__cursor.fetchone()
        columns = [column[0] for column in self.__cursor.description]
        row_dict = dict(zip(columns, row))
        return row_dict
    
    def __del__(self):
        self.__connection.close()