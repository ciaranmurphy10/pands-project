from sklearn import datasets
import pandas as pd

# Import the Iris dataset from the sklearn library.  
iris = datasets.load_iris()

# The dataset will initially be of type sklearn.utils._bunch.Bunch, so we'll need to convert it to a pandas dataframe before we continue.
# A sklearn.utils._bunch.Bunch object can be accessed like a dictionary.
# We can get our column names from the feature_names attribute and our data from the data attribute. 
# We can use the DataFrame function from the pandas library to create our pandas DataFrame. 
iris_df = pd.DataFrame(data = iris['data'], columns = iris['feature_names'])

