'''
Gordon Doore
06/14/2023
csv_process.py
This script is the main entry point for the CSV processing workflow.
'''


import os
import shutil
from csv_to_sql import increment_csv_ids
import sort_analysis_csv as sort

def main():
    # Sort CSVs
    folder_path = '/Users/gordondoore/Documents/GitHub/DairyOne-csv-to-db/csv/analysis_csv/'
    sort.sort_files_by_naming_convention(folder_path)
    
    # Iterate through folders in 'csv' directory
    for folder in os.listdir('csv'):
        print(folder)
        if not folder.startswith('.DS'):  # Ignore hidden files
            path = "csv/" + folder + "/"
            print(path)
            sort.sort_sample_from_analysis(path)

    # Database configuration
    db = {
        'user': 'doadmin',
        'password': 'AVNS_UXdKjBYJzYULsF8uJnC',
        'host': 'c3-database-do-user-914951-0.b.db.ondigitalocean.com',
        'database': 'C3_Database',
        'port': 25060
    }
    
    tables = ["C3AnalysisDryAE", "C3AnalysisGrain", "C3AnalysisManure", "C3AnalysisOther", "C3AnalysisTMR", "C3AnalysisUnrecognized", "C3Macro", "C3TFA"]
    csv_paths = {}

    for table_name in tables:
        # Configure csv paths
        csv_paths["csv/" + table_name + "/analysis/"] = table_name
    
    # Iterate through csv_paths and increment csv ids for each file
    for path, table in csv_paths.items():
        if not os.path.exists(path):
            continue
        for file in os.listdir(path):
            file_path = path + file
            table = table
            print("Appending " + file_path + " to table: " + table)
            increment_csv_ids(table, file_path, db)
            shutil.move(file_path, 'csv/used_csvs/')
    
if __name__ == "__main__":
    main()
