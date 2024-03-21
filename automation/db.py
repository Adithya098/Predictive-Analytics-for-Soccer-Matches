import sqlite3 
from pprint import pprint

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

    def get_players_by_club(self, club_name : str):
        self.__cursor.execute("SELECT long_name FROM my_table WHERE club_name = ?", (club_name,))
        rows = self.__cursor.fetchall()
        return [row[0] for row in rows]

    def get_all_clubs(self):
        self.__cursor.execute("SELECT DISTINCT club_name FROM my_table")
        rows = self.__cursor.fetchall()
        return rows
    
    
    def test(self):
        self.__cursor.execute('SELECT mentality_composure FROM my_table WHERE mentality_composure == 0')
        rows = self.__cursor.fetchall()
        pprint(rows)
    def __del__(self):
        self.__connection.close()


if __name__ == "__main__":
    db = DatabaseConnection()
    pprint(db.test())