import os 
import shutil
from csv_to_sql import increment_csv_ids
import sort_analysis_csv as sort

def main():
    #sort csvs
    folder_path = '/Users/gordondoore/Documents/GitHub/DairyOne-csv-to-db/csv/analysis_csv/'
    sort.sort_files_by_naming_convention(folder_path)
    for folder in os.listdir('csv'):
        print(folder)
        if not folder.startswith('.DS'):
            path = "csv/"+folder+"/"
            print(path)
            sort.sort_sample_from_analysis(path)



    db = {
        'user': 'doadmin',
        'password': 'AVNS_UXdKjBYJzYULsF8uJnC',
        'host': 'c3-database-do-user-914951-0.b.db.ondigitalocean.com',
        'database': 'C3_Database',
        'port': 25060
        }
    
    tables = ["C3AnalysisDryAE","C3AnalysisGrain","C3AnalysisManure","C3AnalysisOther","C3AnalysisTMR", "C3AnalysisUnrecognized", "C3Macro", "C3TFA"]
    csv_paths = {}

    for table_name in tables: 
        #configure csv paths
        csv_paths["csv/"+table_name+"/analysis/"] = table_name
    

    #for each folder, for each file, increment csv ids

    for path, table in csv_paths.items():
        if not os.path.exists(path):
            continue
        for file in os.listdir(path):
            file_path = path+file
            table = table
            print("appending "+file_path+" to table: "+table)
            increment_csv_ids(table, file_path, db)
            shutil.move(file_path, 'csv/used_csvs/')
    
if __name__=="__main__":
    
    main()