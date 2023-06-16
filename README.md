
# CSV Processing Scripts

Gordon Doore
C3 Database Team
Last Updated 05/14/2023
#### Info


This repository contains Python scripts for processing CSV files and performing various operations on them. Below is an overview of each script and its purpose.

### Dependencies

1. os module
2. shutil module
3. csv module
4. mysql.connector module: `pip install mysql-connector-python`
5. os module
6. re module


### File: `csv_process.py`

This script is the main entry point for the CSV processing workflow. It performs the following tasks:

1. Sorts CSV files in a specified folder based on a naming convention.
2. Moves the sorted files to corresponding destination folders.
3. Configures database connection details.
4. Defines a list of tables to process.
5. Increments CSV IDs and inserts the updated data into the respective tables.
6. Moves processed CSV files to a separate folder.

### File: `csv_to_sql.py`

This script provides a function for incrementing CSV IDs and inserting the updated data into a MySQL database table. The function `increment_csv_ids` accepts the following parameters:

- `table_name` (string): The name of the table where the data will be inserted.
- `csv_file_path` (string): The path to the CSV file containing the data.
- `db_config` (dict): The database connection configuration, including user, password, host, database, and port.

The script performs the following steps:

1. Establishes a connection to the MySQL database using the provided configuration.
2. Retrieves the maximum value of the `id` column from the specified table.
3. Reads the CSV file, increments the `id` values, and stores the updated rows.
4. Inserts the updated data into the table using prepared statements.
5. Commits the changes to the database.
6. Closes the database connection.

### File: `sort_csv.py`

This script contains helper functions for sorting and organizing CSV files. The main functions are:

1. `sort_files_by_naming_convention(folder_path)`: This function sorts files in a given folder based on their naming convention. It defines a dictionary `file_types` that maps file suffixes to corresponding folder names. It iterates through the files in the folder and checks each file type to find a match. It then moves the file to the corresponding destination folder based on its type.

2. `sort_sample_from_analysis(folder)`: This function sorts files in a given folder into separate sample and analysis folders. It iterates through the files in the folder and checks if the file matches the pattern for analysis or sample files. If it matches, it moves the file to the respective folder.

3. `sort_tfa(folder)`: This function moves files with a suffix "_t.csv" from a given folder to a "data" folder within that folder. It creates the "data" folder if it doesn't exist already.

4. `sort_macro_files(csv_folder_path)`: This function sorts files in a given folder into separate "data" and "sample" folders based on their suffixes. It iterates through the files and checks if the file ends with "_m.csv" or "_ms.csv". It then moves the file to the corresponding destination folder based on its type.

The file also includes an example usage section that demonstrates how to use the functions by providing a folder path and sorting the files accordingly.

Please note that the file should be executed as the main script to trigger the example usage.
---

Feel free to customize the README file further by adding additional sections, including installation instructions, usage examples, or any other relevant information.

Let me know if there's anything else I can assist you with!

## File:  `execute_csv_process.php`

This script runs the main function of csv_process.py from php allowing server use.  The server must have python 3 and the proper dependencies of the existing files.