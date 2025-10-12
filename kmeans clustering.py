import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# Select features for clustering
features = dataset[['AnnualIncome', 'SpendingScore']]

# Apply K-Means (3 clusters)
kmeans = KMeans(n_clusters=3, n_init=10)
dataset['Cluster'] = kmeans.fit_predict(features)

# Plot clusters
plt.scatter(dataset['AnnualIncome'], dataset['SpendingScore'], c=dataset['Cluster'], cmap='viridis')
plt.title('Customer Segments by Income and Spending')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.colorbar(label='Cluster')
plt.show()
