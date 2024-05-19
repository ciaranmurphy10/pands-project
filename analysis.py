import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Determine a directory to use for reading and writing text. 
iris_dir = os.path.dirname(__file__)

# Create a list of numerical variables for use later. 
numerical_vars = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# Create a list of required subdirectories. This can be added to over time as more directories are needed.  
required_subdirectories = [
    f"{iris_dir}\\plots\\histograms",
    f"{iris_dir}\\plots\\pair_plots",
    f"{iris_dir}\\plots\\scatter_plots",
    f"{iris_dir}\\summary"
]

for directory in required_subdirectories: # Cycle through each element in the list of directories.
    if not os.path.exists(directory): # If the directory doesn't exist, create the directory. 
        os.makedirs(directory)
        

# Although our data file is in .data format, the underlying data is in .csv format. 
# Use the read_csv() function from the pandas library to import our data into a pandas DataFrame. 
iris_df = pd.read_csv(f"{iris_dir}\\data\\iris.data", names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species_type"])


# Open a file called iris_summary.txt, creating it if necessary, in write mode. 
with open(f"{iris_dir}\\summary\\iris_summary.txt", "w") as file:  
    file.write("Iris Dataset Summary\n\n") # Write a title to the text file. 

    file.write("First five rows of data:\n\n") # Write a string to the file. 
    file.write(iris_df.head().to_string()) # Write iris_df head to file. 
    file.write("\n\n") # Add empty lines. 

    file.write("Species counts:\n\n") # Write a string to the file. 
    file.write(iris_df["species_type"].value_counts().to_string()) # Write iris_df species counts to file. 
    file.write("\n\n") # Add empty lines. 

    file.write("Summary statistics of numerical variables:\n\n")
    file.write(iris_df.describe().to_string())
    file.write("\n\n") # Add empty lines. 


sns.pairplot(iris_df) # Create a scatter plot matrix using Seaborn's pairplot function. 
plt.savefig(f"{iris_dir}\\plots\\pair_plots\\iris_pair_plot.png") # Save the plot to a png file. 

# To create and write histograms to png files for each variable, we could use the same code multiple times. 
# Alternatively, a more efficient way would be to write a function which creates a custom histogram and outputs it to a png file. 
# We can then loop the function over each variable to achieve consistent histograms with less code. 

# Define a function to create a custom histogram and save it to a png file.
def custom_hist(variable, output_dir, number_of_bins = 30, bin_colour = "lightsteelblue"):
    """
    This function creates a custom styled histogram and outputs it to a png file.  

    Args:
        variable (str): The numerical variable you would like to use for your histogram. 
        output_dir (str): The directory to save the histogram png to. 
        number_of_bins (int): Number of bins you would like in your histogram. The default is 30. 
        bin_colour (str): The colour you would like the histogram bins to be. The default is lightsteelblue. 
        
    Output:
        matplotlib.figure.Figure: The fig object that we created. 
    """
    # Create the figure and axes.
    fig, ax = plt.subplots()

    # Create a histogram of the inputted variable using the seaborn library.
    sns.histplot(iris_df[variable], 
                 bins = number_of_bins, # Divide the histogram into the chosen number of bins. 
                 color = bin_colour, # Set the bin colour. 
                 ax = ax # Specify that the histogram is to be drawn on the ax that we already created. 
                 )
    
    # Remove spaces and use title case of variable name for the plot title and x-axis label. 
    ax.set_title(f"{variable.replace("_", " ").title()} Histogram")
    ax.set_xlabel(f"{variable.replace("_", " ").title()}")

    # Drop top and right spines. 
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)  

    # Save the plot to the chosen directory, creating a dynamic name based on the variable. 
    plt.savefig(f"{output_dir}\\plots\\histograms\\{variable}_histogram.png") 

    return fig

# Using a for loop and the custom_hist() function, create a histogram of each numerical variable. 
for i in numerical_vars:
    custom_hist(i, iris_dir)

# We can use the same approach for scatter plots, creating a function and running it with each pair of variables. 

# Define a function to create a custom scatter plot and save it to a png file.
def custom_scatter(x_variable, y_variable, output_dir):
    """
    This function creates a custom styled scatter plot and outputs it to a png file.  

    Args:
        x_variable (str): The x-axis variable to use for the scatter plot. 
        y_variable (str): The y-axis variable to use for the scatter plot. 
        output_dir (str): The directory to save the scatter plot png to. 
        
    Output:
        matplotlib.figure.Figure: The fig object that we created.
    """

    # Create the figure and axes.
    fig, ax = plt.subplots()

    # Create a scatter plot of the chosen variables using the seaborn library.
    sns.scatterplot(
        x = x_variable, y = y_variable, # Choose x-axis and y-axis variables.
        hue = "species_type", # Add a hue based on species type. 
        data = iris_df, # Use the iris dataset. 
        ax = ax # Specify that the scatter plot is to be drawn on the ax that we already created.
    )
    
    # Remove spaces and use title case of variable names for the plot title, x-axis label, and y-axis label.
    ax.set_title(f"{x_variable.replace("_", " ").title()} vs. {y_variable.replace("_", " ").title()} Scatter Plot")
    ax.set_xlabel(f"{x_variable.replace("_", " ").title()}")
    ax.set_ylabel(f"{y_variable.replace("_", " ").title()}")

    # Drop the top and right spines. 
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)   

    # Save the plot to the chosen directory, creating a dynamic name based on the variables. 
    plt.savefig(f"{output_dir}\\plots\\scatter_plots\\{x_variable}_vs_{y_variable}_scatter_plot.png") 

    return fig

# In order to run custom_scatter() on each pair of variables, we can create an algorithm using nested for loops. 
# The algorithm will cycle through each unique unordered pair of elements in a list and run custom_scatter() on them. 
# We will use unordered pairs since ordered pairs will douple the amount of plots without adding any extra utility.

for i in range(0, len(numerical_vars)): # Cycle through a range the length of the list. 
    a = numerical_vars[i] # Assign the list value at the current index i to the variable a. 
    for j in range(i + 1, len(numerical_vars)): # Cycle through a range the length of the rest of the list. 
        b = numerical_vars[j] # Assign the list value at the current index j to the variable a. 
        custom_scatter(x_variable = a, y_variable = b, output_dir = iris_dir) # Run custom_scatter() on the current values of a and b, and then repeat the for loop again until all unique unordered pairs have been cycled through. 