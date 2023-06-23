'''
Gordon Doore
06/21/2023
csv_process.py
This script is takes sample data, creates a conglomerate set, and then imports it into table in database
'''
import mysql.connector
import csv
from mysql.connector import errorcode

def process_sample(table_name, database_info, csv_file):
    '''database info of form:        
        'user': 'doadmin',
        'password': 'AVNS_UXdKjBYJzYULsF8uJnC',
        'host': 'c3-database-do-user-914951-0.b.db.ondigitalocean.com',
        'database': 'C3_Database',
        'port': 25060 
    '''

    try:
        cnx = mysql.connector.connect(**database_info)
        cursor = cnx.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print("Error:", err)
        exit()
    #sample_num is primary key
    columns = ['sample_number', 'sample_type','code','description','date_sampled', 'date_received', 'date_printed','ST','CO','institution', 'address1','address2','investigator', 'comments']


    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    for row in data:
        columns_sql = ', '.join(row.keys())
        values_sql = ', '.join(['%s'] * len(row))
        query = f"INSERT INTO {table_name} ({columns_sql}) VALUES ({values_sql}) " \
                f"ON DUPLICATE KEY UPDATE {', '.join([f'{col} = VALUES({col})' for col in columns])}"
        print("inserted")
        cursor.execute(query, list(row.values()))

    cnx.commit()
    cursor.close()
    cnx.close()
