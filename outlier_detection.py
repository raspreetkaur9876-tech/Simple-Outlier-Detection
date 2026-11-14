
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Calculate quartiles
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate limits
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Identify outliers
df["Status"] = df["Marks"].apply(
    lambda x: "Outlier" if x < lower or x > upper else "Normal"
)

# Display results
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower)
print("Upper Limit:", upper)

print("\nOutlier Detection Table:")
print(df.to_string(index=False))

# Display outliers
print("\nDetected Outliers:")
print(df[df["Status"] == "Outlier"])

# Boxplot
plt.boxplot(df["Marks"])
plt.title("Simple Outlier Detection")
plt.ylabel("Marks")
plt.show()
