'''
Gordon Doore
06/14/2023
csv_process.py
This script is the main entry point for the CSV processing workflow.
'''


import os
import shutil
from csv_to_sql import increment_csv_ids
import sort_csv as sort

def main():
    # Sort CSVs
    analysis_folder_path = '/Users/gordondoore/Documents/GitHub/DairyOne-csv-to-db/csv/analysis_csv/'
    sort.sort_files_by_naming_convention(analysis_folder_path)
    
    # Iterate through folders in 'csv' directory
    for folder in os.listdir('csv'):
        if folder.startswith("."):
            continue #ignore hidden files
        if len(os.listdir("csv/"+folder)) ==0:
            continue #ignore empty folders
        if folder.startswith("C3Macro"):
            sort.sort_macro_files("csv/C3Macro/")
        elif folder.startswith("C3TFA"):
            continue
        else:
            path = "csv/" + folder + "/"
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
        csv_paths["csv/" + table_name + "/data/"] = table_name
    
    # Iterate through csv_paths and increment csv ids for each file
    print("before loop")
    for path, table in csv_paths.items():
        print(path)
        if not os.path.exists(path):
            continue
        for file in os.listdir(path):
            file_path = path + file
            print("Appending " + file_path + " to table: " + table)
            increment_csv_ids(table, file_path, db)
            shutil.move(file_path, 'csv/used_csvs/')
    
if __name__ == "__main__":
    main()
