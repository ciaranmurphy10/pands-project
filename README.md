# 23-24: 8632 -- PROGRAMMING AND SCRIPTING. 

# Introduction

This repository contains the final project for the Programming and Scripting (23-24: 8632 -- PROGRAMMING AND SCRIPTING) module for the Higher Diploma in Science in Data Analytics at Atlantic Technological University.

# Instructions

This project contains an executable Python file with will produce text and image files summarising and visualising the variables of the Iris dataset. 

To run this file, navigate to the `pands-project` directory and run the following code: 

``` python 
python analysis.py
```

You will need a modern version of Python installed on your machine to run this code.

To install Python, you can download a copy of Python from [Python.org](https://www.python.org/) or download a more full-featured collection of Python-related programs from [Anaconda.com](https://www.anaconda.com/).

# Overview

The Iris data set is a famous collection of data often used to demonstrate statistical and machine learning concepts. It contains the measurements of fifty samples of three species of Iris flower and was popularised by statistician and biologist Ronald Fischer through his work on linear discriminant analysis, although the data was originally collected by botanist Edgar Anderson in the Gaspé Peninsula. 

The three species of flowers examined in the data set are:
* Iris setosa 
* Iris virginica 
* Iris versicolor

The measurements collected are:
* Length of sepal
* Width of sepal
* Length of petal 
* Width of petal

# Summary of Variables

The `summary/iris_summary.txt' contains summary of the variables contained with the data set. From this, we can draw some initial conclusions. 

In general, the lengths of the sepal and petals are greater than their widths, with sepal and petal length means of 5.84cm and 3.76cm and width means of 3.05cm and 1.20cm respectively. Similarly, we can draw from this that sepals and generally longer than petals, although petals have higher standard deviations than sepals despite their shorter mean lengths, with sepal and petal length standard deviations of 0.83cm and 1.76cm and width standard deviations of 0.43cm and 0.76cm respectively.

Looking at the medians and modes, we can see that the sepal and petal lengths have medians of 5.80 and 4.35, the sepal and petal widths have medians of 3.00 and 1.30, the sepal and petal lengths have modes of 5.0 and 1.5 and sepal and petal widths have modes of 3.0 and 0.2. An interesting observation here is that the sepals have medians that are relatively similar to their modes, implying a symmetrical distribution. The petals on the other hand have medians that are quite different from their modes. 

# References

## General

- [https://en.wikipedia.org/wiki/Iris_flower_data_set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
- [https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)
- [https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis](https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis)
- [https://www.statistics.com/historical-spotlight-iris-dataset/](https://www.statistics.com/historical-spotlight-iris-dataset/)
## Code

- [https://realpython.com/python-f-strings/](https://realpython.com/python-f-strings/)
- [https://realpython.com/pandas-python-explore-dataset/](https://realpython.com/pandas-python-explore-dataset/)
- [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
- [https://www.w3schools.com/python/python_file_write.asp](https://www.w3schools.com/python/python_file_write.asp)
- [https://realpython.com/defining-your-own-python-function/](https://realpython.com/defining-your-own-python-function/)
- [https://www.geeksforgeeks.org/python-for-loops/](https://www.geeksforgeeks.org/python-for-loops/)
- [https://seaborn.pydata.org/generated/seaborn.pairplot.html](https://seaborn.pydata.org/generated/seaborn.pairplot.html)
- [https://seaborn.pydata.org/generated/seaborn.histplot.html](https://seaborn.pydata.org/generated/seaborn.histplot.html)
- [https://seaborn.pydata.org/generated/seaborn.scatterplot.html](https://seaborn.pydata.org/generated/seaborn.scatterplot.html)
- [https://www.w3schools.com/python/matplotlib_labels.asp](https://www.w3schools.com/python/matplotlib_labels.asp)
- [https://www.atlassian.com/data/notebook/how-to-save-a-plot-to-a-file-using-matplotlib](https://www.atlassian.com/data/notebook/how-to-save-a-plot-to-a-file-using-matplotlib)
- [https://www.geeksforgeeks.org/python-pair-iteration-in-list/](https://www.geeksforgeeks.org/python-pair-iteration-in-list/)
- [https://seaborn.pydata.org/generated/seaborn.kdeplot.html](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)
- [https://www.geeksforgeeks.org/seaborn-kdeplot-a-comprehensive-guide/](https://www.geeksforgeeks.org/seaborn-kdeplot-a-comprehensive-guide/)
- [https://seaborn.pydata.org/tutorial/color_palettes.html](https://seaborn.pydata.org/tutorial/color_palettes.html)