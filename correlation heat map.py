import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Compute correlation matrix on numeric columns
numeric_cols = dataset.select_dtypes(include=['float64', 'int64'])
corr = numeric_cols.corr()

# Plot heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
