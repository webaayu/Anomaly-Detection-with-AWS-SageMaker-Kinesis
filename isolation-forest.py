from sklearn.ensemble import IsolationForest
import pandas as pd
import pickle

# Load the synthetic training data
data = pd.read_csv("training_data_4.csv")
labels = pd.read_csv("training_labels_4.csv")

# Train Isolation Forest Model
model = IsolationForest(n_estimators=200, contamination=0.0475, random_state=42)
model.fit(data)

# Save the trained model
with open("isolation_forest_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

print("Isolation Forest model trained and saved as isolation_forest_model.pkl")
