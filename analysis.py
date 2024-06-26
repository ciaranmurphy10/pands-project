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
    f"{iris_dir}\\plots\\kde_plots",
    f"{iris_dir}\\summary"
]

for directory in required_subdirectories: # Cycle through each element in the list of directories.
    if not os.path.exists(directory): # If the directory doesn't exist, create the directory. 
        os.makedirs(directory)
        
# Although our data file is in .data format, the underlying data is in .csv format. 
# Use the read_csv() function from the pandas library to import our data into a pandas DataFrame. 
iris_df = pd.read_csv(f"{iris_dir}\\data\\iris.data", names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species_type"])

# Define a custom palette dictionary which can be used for adding species hues. 
custom_palette = {
    'Iris-setosa': 'salmon',
    'Iris-versicolor': 'lightskyblue',
    'Iris-virginica': 'lightgreen'
}

# Open a file called iris_summary.txt, creating it if necessary, in write mode. 
with open(f"{iris_dir}\\summary\\iris_summary.txt", "w") as file:  
    file.write("Iris Dataset Summary\n\n") # Write a title to the text file. 

    file.write("First five rows of data:\n\n") # Write a string to the file. 
    file.write(iris_df.head().to_string()) # Write iris_df head to file. 
    file.write("\n\n") # Add empty lines. 

    file.write("Species counts:\n\n") # Write a string to the file. 
    file.write(iris_df["species_type"].value_counts().to_string()) # Write iris_df species counts to file. 
    file.write("\n\n") # Add empty lines. 

    file.write("Summary statistics of numerical variables:\n\n") # Write a string to the file.
    file.write(iris_df.describe().to_string()) # Write iris_df summary statistics to file. 
    file.write("\n\n") # Add empty lines. 

    file.write("Data set medians:\n\n") # Write a string to the file.
    file.write(iris_df.median(numeric_only=True).to_string()) # Write iris_df medians to file. 
    file.write("\n\n") # Add empty lines. 

    file.write("Data set modes:\n\n") # Write a string to the file.
    file.write(iris_df.mode(numeric_only=True).to_string()) # Write iris_df modes to file. 
    file.write("\n\n") # Add empty lines. 

sns.pairplot(iris_df, hue = "species_type", palette = custom_palette) # Create a scatter plot matrix using Seaborn's pairplot function. 
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
def custom_scatter(x_variable, y_variable, output_dir, hue = "species_type", palette = custom_palette):
    """
    This function creates a custom styled scatter plot and outputs it to a png file.  

    Args:
        x_variable (str): The x-axis variable to use for the scatter plot. 
        y_variable (str): The y-axis variable to use for the scatter plot. 
        output_dir (str): The directory to save the scatter plot png to. 
        hue (str): The dataset variable to use to determine the hue. 
        palette (dict): The custom colour palette to use for the hues. 
        
    Output:
        matplotlib.figure.Figure: The fig object that we created.
    """

    # Create the figure and axes.
    fig, ax = plt.subplots()

    # Create a scatter plot of the chosen variables using the seaborn library.
    sns.scatterplot(
        x = x_variable, y = y_variable, # Choose x-axis and y-axis variables.
        hue = "species_type", # Add a hue based on species type. 
        palette = custom_palette, # Use the custom palette defined earlier. 
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
# The algorithm will cycle through each unique ordered pair of elements in a list and run custom_scatter() on them. 

for i in range(0, len(numerical_vars)): # Cycle through a range the length of the list. 
    a = numerical_vars[i] # Assign the list value at the current index i to the variable a. 
    for j in range(0, len(numerical_vars)): # Cycle through a range the length of the list. 
        if not i == j: # Exclude a variable being paired with itself. 
            b = numerical_vars[j] # Assign the list value at the current index j to the variable a. 
            custom_scatter(x_variable = a, y_variable = b, output_dir = iris_dir) # Run custom_scatter() on the current values of a and b, and then repeat the for loop again until all unique ordered pairs have been cycled through. 

# We can use the same functional approach again to create KDE plots. 

def custom_kde(variable, output_dir, hue = "species_type", palette = custom_palette):
    """
    This function creates a custom styled KDE plot and outputs it to a png file.  

    Args:
        variable (str): The numerical variable you would like to use for your KDE plot. 
        output_dir (str): The directory to save the KDE plot png to. 
        hue (str): The dataset variable to use to determine the hue. 
        palette (dict): The custom colour palette to use for the hues.  
        
    Output:
        matplotlib.figure.Figure: The fig object that we created. 
    """
    # Create the figure and axes.
    fig, ax = plt.subplots()

    # Create a KDE plot of the inputted variable using the seaborn library.
    sns.kdeplot(data = iris_df, 
                x = variable, # Choose the variable to use. 
                hue = "species_type", # Add a hue based on species type. 
                palette = custom_palette) # Use the custom palette defined earlier. 

    # Remove spaces and use title case of variable name for the plot title and x-axis label. 
    ax.set_title(f"{variable.replace("_", " ").title()} KDE Plot")
    ax.set_xlabel(f"{variable.replace("_", " ").title()}")

    # Drop top and right spines. 
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)  

    # Save the plot to the chosen directory, creating a dynamic name based on the variable. 
    plt.savefig(f"{output_dir}\\plots\\kde_plots\\{variable}_kde_plot.png") 

# Using a for loop and the custom_kde() function, create a KDE plot of each numerical variable. 
for i in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:
    custom_kde(i, iris_dir)

# To calculate a Pearson correlation matrix, we can use the pandas .corr() method.
# This computes a correlation matrix from a DataFrame, with a default method of Pearson. 
# First calculate a matrix without separating species.  
iris_corr_matrix = iris_df[numerical_vars].corr()

# Output it to a markdown file in the summary folder. 
with open(f"{iris_dir}\\summary\\iris_corr_matrix.md", "w") as file:  
    file.write(iris_corr_matrix.to_markdown()) # Use the .to_markdown() method to convert the DataFrame to a markdown string. 

# To examine correlation between variables broken out into species, use .loc to filter based on species_type column. 
# Drop the species_type column as we no longer need it. 
iris_df_setosa = iris_df.loc[iris_df['species_type'] == 'Iris-setosa'].drop(columns = 'species_type')

# Using list comprehension, add the setosa species suffix to all column names.
iris_df_setosa.columns = [f"{column}_setosa" for column in iris_df_setosa.columns]

# Calculate the correlation matrix for our new DataFrame. 
iris_setosa_corr_matrix = iris_df_setosa.corr()

# As before, output it to a markdown table. 
with open(f"{iris_dir}\\summary\\iris_setosa_corr_matrix.md", "w") as file:  
    file.write(iris_setosa_corr_matrix.to_markdown()) 

# Perform the same steps for versicolor.
iris_df_versicolor = iris_df.loc[iris_df['species_type'] == 'Iris-versicolor'].drop(columns = 'species_type')
iris_df_versicolor.columns = [f"{column}_versicolor" for column in iris_df_versicolor.columns]
iris_versicolor_corr_matrix = iris_df_versicolor.corr()
with open(f"{iris_dir}\\summary\\iris_versicolor_corr_matrix.md", "w") as file:  
    file.write(iris_versicolor_corr_matrix.to_markdown()) 

# Perform the same steps for virginica.
iris_df_virginica = iris_df.loc[iris_df['species_type'] == 'Iris-virginica'].drop(columns = 'species_type')
iris_df_virginica.columns = [f"{column}_virginica" for column in iris_df_virginica.columns]
iris_virginica_corr_matrix = iris_df_virginica.corr()
with open(f"{iris_dir}\\summary\\iris_virginica_corr_matrix.md", "w") as file:  
    file.write(iris_virginica_corr_matrix.to_markdown()) 