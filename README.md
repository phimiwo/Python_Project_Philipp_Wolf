Topic:
My project for the advanced python course will be the Kaggle competition "Titanic: Machine Learning from Disaster"

Step 1:
The first step was to load the training data provided by the project into a pandas dataframe.

Step 2:
Getting familiar with the data by plotting the amount of people who survived against different features.

Step 3:
Preparing the data for machine learning by changing all strings in the data into numbers. I decided to focus on following features:
- Pclass
- Sex (1 is male, 0 is female)
- Age
- SibSp (Number of siblings and spouses a person travelled with)
- Parch (Number of Parents and Children a person travelled with)
- Fare
- Embarked (encoded in numbers 0, 1, 2) 
Some data was missing for Age, Fare, and Embarked. For Age and Fare I filled the missing values with the mean values and for Embarked I assumed that all persons with a missing embarked value embarked in the most 'popular' location S.

This data processing was done in the externally saved function process_data().

Step 4:
Next I wanted to test the two machine learning techniques k-nearest-neighbours and logistic regression on my training data set. To do so I split the training data set in two parts so that I could calculate the accuracy score. The maximum accuracy for knn was about 0.72 while the accuracy for log reg was 0.78.

Step 5:
Loading the test data.

Step 6:
Run the knn and the log reg method on the test data, while training them with the train data set.

Step 7: 
Prepare response data so that it can be uploaded on the kaggle website. I did this in the externally saved function prepare submission. 

Step 8:
Save the submission data in csv files.

Results:
With the knn method, using k=9, I reached a score of 0.646 and with the log reg method I reached a score of 0.768.

Additional Remarks:
Most of the project is performed in the jupyter notebook Version_2, with the two extra functions saved in the process_data.py file. The functions in the process_data.py file are imported into the jupyter notebook.
