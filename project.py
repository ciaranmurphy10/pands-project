import pandas as pd

# Determine a directory to use for reading and writing text. 
# Will need add functionality for other users to run this file. 
iris_dir = "C:\\Users\\ciara\\Documents\\college\\pands-project"

# Although our data file is in .data format, the underlying data is in .csv format. 
# Use the read_csv() function from the pandas library to import our data into a pandas DataFrame. 
iris_df = pd.read_csv(f"{iris_dir}\\iris.data", names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species_type"])

# Open a file called iris_summary.txt, creating it if necessary, in write mode. 
with open(f"{iris_dir}\\iris_summary.txt", "w") as file:  
    # Write some placeholder text to confirm this section is working. 
    file.write("Placeholder text.")