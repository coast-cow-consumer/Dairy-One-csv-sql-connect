'''
Gordon Doore
06/14/2023
sort_analysis_csv.py
This script contains helper functions for sorting and organizing analysis CSV files in target directory
'''


import os
import re
import shutil

def sort_files_by_naming_convention(folder_path):
    # Define the file types and their corresponding folder names
    file_types = {
        "_m.csv": "Manure",
        "_o.csv": "Other",
        "_d.csv": "DryAE",
        "_t.csv": "TMR",
        "_g.csv": "Grain",
        "_?.csv": "Unrecognized"
    }

    # Iterate through files in the given folder path
    for filename in os.listdir(folder_path):
        f_path = os.path.join(folder_path, filename)
        file_type = None

        # Check each file type to find a match
        for suffix, filetype in file_types.items():
            # Match filetype based on the suffix
            if filename.endswith(suffix):
                file_type = filetype
                break

        # Set paths for the destination folder and path
        destination_folder = f"csv/C3Analysis{file_type}"
        destination_path = os.path.join(destination_folder, filename)

        # Move the file to the corresponding destination folder
        os.makedirs(destination_folder, exist_ok=True)
        os.rename(f_path, destination_path)

def sort_sample_from_analysis(folder):
    # Define the paths for sample and analysis folders
    sample_folder = folder + "/sample/"
    analysis_folder = folder + "/data/"
    # Iterate through files in the given folder
    for file in os.listdir(folder):
        f_path = os.path.join(folder, file)
        if re.search('_a_.\.csv', file):
            # Move the file to the analysis folder if it matches the pattern
            destination_path = os.path.join(analysis_folder, file)
            os.makedirs(analysis_folder, exist_ok=True)
            os.rename(f_path, destination_path)
        elif re.search('_s_.\.csv', file):
            # Move the file to the sample folder if it matches the pattern
            destination_path = os.path.join(sample_folder, file)
            os.makedirs(sample_folder, exist_ok=True)
            os.rename(f_path, destination_path)

def sort_tfa(folder):
    # Create the 'data' folder if it doesn't exist
    data_folder = os.path.join(folder, 'data')
    os.makedirs(data_folder, exist_ok=True)

    # Get the list of files in the given folder
    files = os.listdir(folder)

    for file in files:
        if file.endswith('_t.csv'):
            # Construct the source and destination paths
            source_path = os.path.join(folder, file)
            destination_path = os.path.join(data_folder, file)

            # Move the file to the 'data' folder
            shutil.move(source_path, destination_path)


def sort_macro_files(csv_folder_path):

    files = os.listdir(csv_folder_path)
    for file in files:
        f_path = os.path.join(csv_folder_path, file)
        file_type = None
        if file.endswith("_m.csv"):
            file_type = "data"
        elif file.endswith("_ms.csv"): 
            file_type = "sample"

        # Set paths for the destination folder and path
        destination_folder = f"csv/C3Macro/{file_type}"
        destination_path = os.path.join(destination_folder, file)

        # Move the file to the corresponding destination folder
        if file_type == None: 
            continue
        os.makedirs(destination_folder, exist_ok=True)
        os.rename(f_path, destination_path)

if __name__ == "__main__":
    # Usage example
    folder_path = '/Users/gordondoore/Documents/GitHub/DairyOne-csv-to-db/csv/analysis_csv/'

    # Sort files based on naming convention
    sort_files_by_naming_convention(folder_path)

    # Iterate through folders in the 'csv' directory
    for folder in os.listdir('csv'):
        print(folder)
        if not folder.startswith('.DS'):
            path = "csv/" + folder + "/"
            print(path)
            # Sort samples from analysis in each folder
            sort_sample_from_analysis(path)
