import pandas as pd

# Although our data file is in .data format, the underlying data is in .csv format. 
# Use the read_csv() function from the pandas library to import our data into a pandas DataFrame. 
iris_df = pd.read_csv("C:\\Users\\ciara\\Documents\\college\\pands-project\\iris.data", names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

# Open a file called iris_summary.txt, creating it if necessary, in write mode. 
with open("C:\\Users\\ciara\\Documents\\college\\pands-project\\iris_summary.txt", "w") as file:  
    # Write some placeholder text to confirm this section is working. 
    file.write("Placeholder text.")