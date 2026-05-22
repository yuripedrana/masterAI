import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.cluster import DBSCAN, KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


df = pd.DataFrame(load_iris().data, columns=load_iris().feature_names)
print(df.describe())


X_std = StandardScaler().fit_transform(df)

min_samples = 5
for eps in [0.35, 0.45, 0.55]:
    noise = -1
    dbscan = DBSCAN(eps=eps, min_samples=min_samples).fit(X_std)
    n_clusters = len(set(dbscan.labels_)) - (1 if noise in dbscan.labels_ else 0)
    print(f'eps: {eps}, Estimated number of clusters: {n_clusters}, Noise points: {(dbscan.labels_ == noise).sum()}')

iris = load_iris()
X,y = iris.data, iris.target
feature_names = iris.feature_names

scaler = StandardScaler()
X_std = scaler.fit_transform(X)
wcss = []
k_values = range(1, 11)
elbow_point = 3

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_std)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_values, wcss, marker='o')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
plt.title('Elbow Method for Optimal k')
plt.xticks(k_values)
plt.grid()
plt.axvline(x=elbow_point, color='red', linestyle='--', label='Elbow Point')
plt.legend()
plt.show()

kmeans = KMeans(n_clusters=elbow_point, random_state=42)
kmeans.fit(X_std)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
print(f'Cluster labels: {labels}')
plt.figure(figsize=(8, 6))
plt.scatter(X_std[:, 0], X_std[:, 1], c=labels, cmap='viridis', s=50)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.title('K-Means Clustering of Iris Dataset')
plt.legend()
plt.grid()
plt.show()

silhouette_avg = silhouette_score(X_std, labels)
print(f'Silhouette Score for k={elbow_point}: {silhouette_avg:.2f}')







