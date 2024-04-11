import sqlite3 
from pprint import pprint

class DatabaseConnection:
    def __init__(self) -> None:
        self.__connection = sqlite3.connect('my_database2.db')
        self.__cursor = self.__connection.cursor()

    def get_player_by_name(self, long_name : str):
        self.__cursor.execute("SELECT * FROM my_table WHERE long_name = ?", (long_name,))
        row = self.__cursor.fetchone()
        columns = [column[0] for column in self.__cursor.description]
        row_dict = dict(zip(columns, row))
        return row_dict

    def get_players_by_club(self, club_name : str):
        self.__cursor.execute("SELECT * FROM my_table WHERE club_name = ?", (club_name,))
        rows = self.__cursor.fetchall()
        processed_rows = []
        for row in rows:
            processed_rows.append([0 if value is None else value for value in row])


        columns = [column[0] for column in self.__cursor.description]
        
        
        return [dict(zip(columns, processed_row) )for processed_row in processed_rows]

    def get_all_clubs(self):
        self.__cursor.execute("SELECT DISTINCT club_name FROM my_table")
        rows = self.__cursor.fetchall()
        return rows
    
    def test(self):
        self.__cursor.execute("SELECT DISTINCT unnest(string_to_array(elements, ', ')) AS element FROM my_table;")
        rows = self.__cursor.fetchall()
        columns = [column[0] for column in self.__cursor.description]
        

        return [dict(zip(columns, row) )for row in rows]
    
    
 
    def __del__(self):
        self.__connection.close()


if __name__ == "__main__":
    db = DatabaseConnection()
    my_dict = db.get_players_by_club('Paris Saint Germain')[0]
    
    for key in my_dict.keys():
        print(key, "->", my_dict[key])