import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Example dataset: online fraud detection (simplified)
data = pd.DataFrame({
    'Amount': [1000, 200, 50, 5000, 1500, 100, 12000, 30],
    'Sender_Balance': [5000, 1000, 800, 15000, 7000, 1200, 30000, 500],
    'Recipient_Balance': [10000, 2000, 900, 20000, 10000, 1500, 35000, 800],
    'Is_Fraud': [0, 0, 0, 1, 0, 0, 1, 0]
})

# Splitting the features and target variable
X = data[['Amount', 'Sender_Balance', 'Recipient_Balance']]
y = data['Is_Fraud']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Training the XGBoost classifier
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
print('Classification Report:')
print(classification_report(y_test, y_pred))
