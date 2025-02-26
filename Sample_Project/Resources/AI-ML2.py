import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier


# Reading the required files into Python using pandas
df = pd.read_csv('file.csv')
test = pd.read_csv('Test1.csv')

# Fill the NaN values with 'None' (ensure consistency across both datasets)
df = df.fillna('None')
test = test.fillna('None')

# Encoding categorical features using pd.get_dummies() - ensure both datasets are consistent
X_train = pd.get_dummies(df.drop('element', axis=1))
X_test = pd.get_dummies(test.drop('element', axis=1))

# Make sure the test set has the same columns as the training set
# Add missing columns to the test set, filling them with zeros
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

# Create a dictionary of elements to encode the target variable
element_dict = dict(zip(df['element'].unique(), range(df['element'].nunique())))

# Replace element values with corresponding numerical values
y_train = df['element'].replace(element_dict)

# Initialize and train the RandomForest model
rf = RandomForestClassifier(n_estimators=50, random_state=0)
rf.fit(X_train, y_train)
result=rf.predict(X_train)
print(result)


def predict_elements():
    # Get the number of records in the test dataset
    num_of_records = len(test)

    # Concatenate the test data and train data (this is unnecessary for model training but might be used for some comparison purposes)
    concatenated = pd.concat([df, test], axis=0).drop('element', axis=1)

    if num_of_records == 1:
        # Process the test record and make predictions
        processed_test = pd.DataFrame(pd.get_dummies(concatenated).iloc[-num_of_records]).T
        probabilities = list(rf.predict_proba(processed_test)[0])
        element_name = list(element_dict.keys())[np.argmax(probabilities)]
        element_name = f'Hence, the name of our predicted element is {element_name}'
        score = list(zip(df['element'].unique(), probabilities))
    elif num_of_records > 1:
        # Process multiple records and make predictions
        processed_test = pd.get_dummies(concatenated).iloc[-num_of_records:]
        probabilities = list(rf.predict_proba(processed_test))

        score = []
        for i in range(len(probabilities)):
            score.append(list(zip(df['element'].unique(), list(probabilities[i]))))

        element_index = np.argmax(probabilities, axis=1)
        element_name = []
        for ind_, i in enumerate(element_index):
            element_name.append(
                (ind_, f'Hence, the name of our predicted element is {list(element_dict.keys())[i]}')
            )

    return score, element_name, test


# Calling the predict_elements method to return predictions and scores
scores, element_name, test_df = predict_elements()

# Print the scores and predicted element names
print(scores)
print(element_name)
