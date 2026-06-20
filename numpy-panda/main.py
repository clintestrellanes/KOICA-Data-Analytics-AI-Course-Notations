import numpy as np
import pandas as pd

# 1. NumPy: Create a vectorized array representing weights (kg)
# np.nan represents missing data
weights_kg = np.array([70.5, 82.1, np.nan, 65.2, 90.0])

# Calculate the mean weight, explicitly ignoring the NaN value
mean_weight = np.nanmean(weights_kg)
print(f"Calculated Mean Weight: {mean_weight:.1f} kg\n")

# 2. Pandas: Construct a DataFrame from a dictionary
data = {
    'Patient_ID': [101, 102, 103, 104, 105],
    'Age': [25, 34, 29, 42, 29],
    'Weight_kg': weights_kg,
    'Treatment_Group': ['A', 'B', 'A', 'A', 'B']
}
df = pd.DataFrame(data)

print(f"Original DataFrame (Shape: {df.shape}):")
print(df, "\n")

# 3. Data Cleaning: Handle NaN (Not a Number)
# Replace the missing weight value with the calculated mean
df['Weight_kg'] = df['Weight_kg'].fillna(mean_weight)

# 4. Filtering Data
# Isolate records where the patient age is strictly greater than 30
older_patients = df[df['Age'] > 30]

# 5. Aggregation: Groupby
# Calculate the average weight for Treatment Group A vs. B
group_stats = df.groupby('Treatment_Group')['Weight_kg'].mean().reset_index()

print("Cleaned and Aggregated Data (Average Weight per Group):")
print(group_stats)