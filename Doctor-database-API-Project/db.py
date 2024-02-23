# Import all necessary libraries
import sqlite3
from sqlite3 import Error
import os
from typing import List, Dict, Tuple

# Create a  class to handle the database connection


class DB:
    db_url: str  # Database url to connect to the database

# Create a constructor to initialize the database url
    def __init__(self, db_url: str):
        self.db_url = db_url
# If the database does not exist, create it
        if not os.path.exists(self.db_url):
            self.create_db()

# Create a method to create the database
    def create_db(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_url)
            print("Database created successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()

# Create a method to insert data into the database
    def insert(self, table: str, data: Dict):
        conn = None
        try:
            conn = sqlite3.connect(self.db_url)
            cursor = conn.cursor()
            columns = ", ".join(data.keys())
            values = ", ".join([f"'{value}'" for value in data.values()])
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            cursor.execute(query)
            conn.commit()
            print("Data inserted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()

# Create a method to get data from the database
    def get(self, table: str, where: Tuple = None):
        conn = None
        try:
            conn = sqlite3.connect(self.db_url)
            cursor = conn.cursor()
            if where:
                query = f"SELECT * FROM {table} WHERE {where[0]} = {where[1]}"
            else:
                query = f"SELECT * FROM {table}"
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()

# Create a method to update data in the database
    def update(self, table: str, data: Dict, where: Tuple):
        conn = None
        try:
            conn = sqlite3.connect(self.db_url)
            cursor = conn.cursor()
            columns = ", ".join(
                [f"{key} = '{value}'" for key, value in data.items()])
            query = f"UPDATE {table} SET {columns} WHERE {where[0]} = {where[1]}"
            cursor.execute(query)
            conn.commit()
            print("Data updated successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()

# Create a method to delete data from the database
    def delete(self, table: str, where: Tuple):
        conn = None
        try:
            conn = sqlite3.connect(self.db_url)
            cursor = conn.cursor()
            query = f"DELETE FROM {table} WHERE {where[0]} = {where[1]}"
            cursor.execute(query)
            conn.commit()
            print("Data deleted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()

# Create a method to create a table in the database
    def create_table(self, table: str, columns: List):
        conn = None
        try:
            conn = sqlite3.connect(self.db_url)
            cursor = conn.cursor()
            columns = ", ".join(
                [f"{key} {value}" for key, value in columns.items()])
            query = f"CREATE TABLE {table} ({columns})"
            cursor.execute(query)
            conn.commit()
            print("Table created successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()

# Create a method to drop a table from the database
    def drop_table(self, table: str):
        conn = None
        try:
            conn = sqlite3.connect(self.db_url)
            cursor = conn.cursor()
            query = f"DROP TABLE {table}"
            cursor.execute(query)
            conn.commit()
            print("Table dropped successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()

# Create a method to get the table names from the database
    def get_table_names(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_url)
            cursor = conn.cursor()
            query = "SELECT name FROM sqlite_master WHERE type = 'table'"
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()

# Create a method to get the column names from the database table
    def get_column_names(self, table: str):
        conn = None
        try:
            conn = sqlite3.connect(self.db_url)
            cursor = conn.cursor()
            query = f"PRAGMA table_info({table})"
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()

# create a method to delate table / column from the database
    def delete_table_column(self, table: str, column: str):
        conn = None
        try:
            conn = sqlite3.connect(self.db_url)
            cursor = conn.cursor()
            query = f"ALTER TABLE {table} DROP COLUMN {column}"
            cursor.execute(query)
            conn.commit()
            print("Column deleted successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()
