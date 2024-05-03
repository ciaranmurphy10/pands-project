import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Determine a directory to use for reading and writing text. 
# Will need add functionality later for other users to run this file. 
iris_dir = "C:\\Users\\ciara\\Documents\\college\\pands-project"

# Although our data file is in .data format, the underlying data is in .csv format. 
# Use the read_csv() function from the pandas library to import our data into a pandas DataFrame. 
iris_df = pd.read_csv(f"{iris_dir}\\iris.data", names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species_type"])

# Open a file called iris_summary.txt, creating it if necessary, in write mode. 
with open(f"{iris_dir}\\iris_summary.txt", "w") as file:  
    file.write("Iris Dataset Summary\n\n") # Write a title to the text file. 

    file.write("First five rows of data:\n\n") 
    file.write(iris_df.head().to_string()) # Write iris_df head to file. 
    file.write("\n\n") # Add empty lines. 

    file.write("Summary statistics of numerical variables:\n\n")
    file.write(iris_df.describe().to_string())
    file.write("\n\n") # Add empty lines. 

sns.pairplot(iris_df) # Create a scatter plot matrix using Seaborn's pairplot function. 
plt.savefig(f"{iris_dir}\\iris_pair_plot.png") # Save the plot to a png file. 

# Define a custom function to create a custom histogram and save it to a png file.
def custom_hist(variable, output_dir):

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Create a histogram of the inputted variable.
    sns.histplot(iris_df[variable], 
                 bins = 30, # Divide the histogram into 30 bins. 
                 ax = ax) # Specify that the histogram is to be drawn on the ax that we already created.
    
    # Save the plot to the chosen directory, creating a dynamic name based on the variable. 
    plt.savefig(f"{output_dir}\\{variable}_histogram.png") 