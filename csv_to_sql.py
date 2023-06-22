'''
Gordon Doore
06/14/2023
csv_to_sql.py
This script provides a function for incrementing CSV IDs and 
inserting the updated data into a MySQL database table.
'''

import csv
import mysql.connector

def increment_csv_ids(table_name, csv_file_path, db_config):
    # Establish a connection to the database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    print("connection success")
    # Step 1: Retrieve the maximum value of the id column from the table
    select_query = f"SELECT MAX(id) FROM {table_name}"
    cursor.execute(select_query)
    max_id = cursor.fetchone()[0]
    if max_id is None:
        max_id = -1
    print("max_id is"+str(max_id))

    # Step 2: Read the CSV file and update the id column values
    updated_rows = []
    with open(csv_file_path, 'r') as file:
        csv_data = csv.reader(file)
        next(csv_data)  # Skip the header row

        for row in csv_data:
            row[0] = int(row[0]) + max_id + 1 # Increment the id value
            updated_rows.append(row)

    # Step 3: Insert the updated data from the CSV into the table
    placeholders = ','.join(['%s'] * len(updated_rows[0]))
    insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.executemany(insert_query, updated_rows)

    # Commit the changes
    cnx.commit()
    print("committed")
    # Close the cursor and connection
    cursor.close()
    cnx.close()

def sample_to_db(table_name, csv_file_path, db_config):
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    print("connection success")

    #now need to see if 
if __name__ == "__main__":
    # Database credentials
    db = {
    'user': 'doadmin',
    'password': 'AVNS_UXdKjBYJzYULsF8uJnC',
    'host': 'c3-database-do-user-914951-0.b.db.ondigitalocean.com',
    'database': 'C3_Database',
    'port': 25060
    }
    TABLE = 'C3Macro'
    CSV = 'test.csv'
    increment_csv_ids(TABLE,CSV,db)