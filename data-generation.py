import random
import pandas as pd
import numpy as np

# Generate synthetic anomaly data
def generate_anomalous_data(num_rows=2000, num_features=4, anomaly_percentage=0.05):
    data = []
    labels = []
    
    for _ in range(num_rows):
        row = [random.uniform(0, 1) for _ in range(num_features)]
        is_anomalous = random.random() < anomaly_percentage
        if is_anomalous:
            row = [random.uniform(4, 10) if random.random() < 0.5 else val for val in row]
            labels.append(1)
        else:
            labels.append(0)
        data.append(row)
    
    # Convert to DataFrame
    df_data = pd.DataFrame(data, columns=[f'feature_{i}' for i in range(num_features)])
    df_labels = pd.DataFrame(labels, columns=["anomaly"])

    # Save as CSV files
    df_data.to_csv("training_data_4.csv", index=False)
    df_labels.to_csv("training_labels_4.csv", index=False)

if __name__ == "__main__":
    generate_anomalous_data()
    print("Synthetic dataset with anomalies generated and saved to CSV files.")
