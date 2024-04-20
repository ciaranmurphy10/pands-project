import pandas as pd

# Although our data file is in .data format, the underlying data is in .csv format. 
# We can use read_csv() function from the pandas to import our data into a pandas DataFrame. 
iris_df = pd.read_csv("C:\\Users\\ciara\\Documents\\college\\pands-project\\iris.data", names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])