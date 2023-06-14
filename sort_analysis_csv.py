import os
import re 

def sort_files_by_naming_convention(folder_path):
    file_types = {
        "_m.csv": "Manure",
        "_o.csv": "Other",
        "_d.csv": "DryAE",
        "_t.csv": "TMR",
        "_g.csv": "Grain",
        "_?.csv": "Unrecognized"
    }
    
    for filename in os.listdir(folder_path):
        f_path = os.path.join(folder_path, filename)
        file_type = None

        for suffix, filetype in file_types.items():
            #match filetype
            if filename.endswith(suffix):
                file_type = filetype
                break
        
        #set paths
        destination_folder = f"csv/C3Analysis{file_type}"
        destination_path = os.path.join(destination_folder, filename)

        # Move the file to the corresponding destination folder
        os.makedirs(destination_folder, exist_ok=True)
        os.rename(f_path, destination_path)

def sort_sample_from_analysis(folder):
    sample_folder = folder+"/sample/"
    analysis_folder = folder+"/analysis/"
    for file in os.listdir(folder):
        f_path = os.path.join(folder, file)
        if re.search('_a_.\.csv', file):
            destination_path = os.path.join(analysis_folder, file)
            os.makedirs(analysis_folder, exist_ok=True)
            os.rename(f_path, destination_path)
        elif re.search('_s_.\.csv', file):
            destination_path = os.path.join(sample_folder, file)
            os.makedirs(sample_folder, exist_ok=True)
            os.rename(f_path, destination_path)

if __name__ == "__main__":
    # Usage example
    folder_path = '/Users/gordondoore/Documents/GitHub/DairyOne-csv-to-db/csv/analysis_csv/'
    sort_files_by_naming_convention(folder_path)
    for folder in os.listdir('csv'):
        print(folder)
        if not folder.startswith('.DS'):
            path = "csv/"+folder+"/"
            print(path)
            sort_sample_from_analysis(path)
