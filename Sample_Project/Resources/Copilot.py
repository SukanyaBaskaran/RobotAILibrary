import pandas as pd

# Load CSV files
before = pd.read_csv('file.csv')
after = pd.read_csv('Test1.csv')

# Print column names to verify
print("Columns in 'before' CSV:", before.columns)
print("Columns in 'after' CSV:", after.columns)

# Identify changed elements
changes = before.merge(after, on='element', suffixes=('_before', '_after'))
changed_elements = changes[changes.filter(like='_before').ne(changes.filter(like='_after')).any(axis=1)]

# Handle non-numeric data
# Convert categorical data to numeric if necessary
for col in changed_elements.columns:
    if changed_elements[col].dtype == 'object': # Check if the column is of type object (string)
        changed_elements[col] = pd.factorize(changed_elements[col])[0]


# Save the changed elements for further use
changed_elements.to_csv('changed_elements.csv', index=False)

# Identify specific differences
differences = {}
for index, row in changed_elements.iterrows():
    diffs = {}
    for col in before.columns:
        if col != 'element' and row[f'{col}_before'] != row[f'{col}_after']:
            diffs[col] = (row[f'{col}_before'], row[f'{col}_after'])
    differences[row['element']] = diffs

# Save differences to CSV
difference_df = pd.DataFrame.from_dict(differences, orient='index')
difference_df.to_csv('differences.csv')

# Print differences for verification
print(differences)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Prepare data for training
X = changed_elements.drop(columns=['element'])
y = (changed_elements['element_before'] != changed_elements['element_after']).astype(int)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

