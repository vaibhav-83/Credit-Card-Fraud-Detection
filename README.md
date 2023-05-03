# Credit Card Fraud Detection

*This is a Neural Network which can classify whether the given credit card transaction was fraudulent.*

The Neural Network implemented uses a Supervised Training algorithm: The Single Layer Perceptron Training Rule. The network has been trained on a large set of values.

## Description of dataset:

-> Dataset: creditcard 1000 entries.csv file

We have fetched the database from Kaggle. This dataset presents transactions that occurred in two days, where there are 492 frauds out of 1136 transactions.

28 features were used in the classification. The description of the features was not provided by Kaggle, as it was deemed to be private. All of the features were real numbers and PCA normalized. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise. The range of values of all features was between -114 to 121, although most values lie in between -2 & 2.

The original database contained 284,807 rows. Out of them, we took in all 1136 rows

## Usage:

You can modify the no. of iterations in the file `train.py`. Then run test.py to check accuracy.

By default, 45 iterations have been performed on the training dataset (first 600 values) and final weights are available under `final_weights.txt`.
Testing values are next 536 values after training values. The accuracy is about 97% in testing dataset.
You can also modify the balance of no. of tuples for training and testing using variables `train` & `test` in `train.py` and `test.py`.

## Statistics:

No. of iterations   No. of correct outputs  No. of incorrect outputs  Accuracy
----------------------------------------------------------------------------------    
    40	                    520	                    16	              97.0149
    41	                    518	                    18	              96.6418
    42	                    517	                    19	              96.4552
    43	                    517	                    19	              96.4552
    44	                    520	                    16	              97.0149
    45	                    522	                    14	              97.3881
    46	                    517	                    19	              96.4552
    47	                    521                     15	              97.2015
    48	                    472	                    64	              88.0597
    49	                    493	                    43	              91.9776
    50	                    517                     19	              96.4552
    51	                    511	                    25	              95.3358
    52	                    519	                    17	              96.8284
    53	                    516	                    20	              96.2687
    54	                    517                     19	              96.4552
    55	                    517	                    19	              96.4552
-----------------------------------------------------------------------------------