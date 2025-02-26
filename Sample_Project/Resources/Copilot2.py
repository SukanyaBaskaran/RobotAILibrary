import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Read and preprocess the data
df = pd.read_csv('file.csv')
test = pd.read_csv('Test.csv')

# Fill NaN values with 'None'
df = df.fillna('None')
test = test.fillna('None')

# Convert categorical variables to dummy/indicator variables
X_train = pd.get_dummies(df.drop('element', axis=1))
X_test = pd.get_dummies(test)

# Ensure the same dummy variables are used in training and testing datasets
X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

# Create a dictionary of elements
element_dict = dict(zip(df['element'].unique(), range(df['element'].nunique())))

# Replace element values with numerical values
y_train = df['element'].replace(element_dict)

# Step 2: Train the Random Forest model
rf = RandomForestClassifier(n_estimators=50, random_state=0)
rf.fit(X_train, y_train)


def predict_elements():
    num_of_records = len(X_test)

    if num_of_records == 1:
        processed_test = pd.DataFrame(X_test).iloc[-num_of_records].to_frame().T
        probabilities = list(rf.predict_proba(processed_test)[0])
        element_name = list(element_dict.keys())[np.argmax(probabilities)]
        element_name = 'Hence, the name of our predicted element is {}'.format(element_name)
        score = list(zip(df['element'].unique(), probabilities))

    elif num_of_records > 1:
        processed_test = pd.DataFrame(X_test).iloc[-num_of_records:]
        probabilities = list(rf.predict_proba(processed_test))

        score = []
        element_name = []
        for i in range(len(probabilities)):
            score.append(list(zip(df['element'].unique(), list(probabilities[i]))))
            element_index = np.argmax(probabilities[i])
            element_name.append(
                (i, 'Hence, the name of our predicted element is {}'.format(list(element_dict.keys())[element_index])))

    return score, element_name, test

# Calling the predict_elements method to return
scores, element_name, test_df = predict_elements()
print(scores)
print(element_name)
