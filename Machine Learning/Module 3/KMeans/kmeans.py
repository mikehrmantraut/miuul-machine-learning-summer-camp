####################################
# K-Means
####################################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from yellowbrick.cluster import KElbowVisualizer


df = pd.read_csv("datasets/USArrests.csv", index_col=0)

df.head()
df.isnull().sum()
df.info()
df.describe().T

sc = MinMaxScaler((0, 1))
df = sc.fit_transform(df)

df[0:5]

kmeans = KMeans(n_clusters=4, random_state=17).fit(df)
kmeans.get_params()

kmeans.n_clusters
kmeans.cluster_centers_
kmeans.labels_
kmeans.inertia_

# Determine Optimal Cluster Numbers
kmeans = KMeans()
ssd = []
K = range(1, 30)

for k in K:
    kmeans = KMeans(n_clusters=k).fit(df)
    ssd.append(kmeans.inertia_)

plt.plot(K, ssd, "o")
plt.xlabel("SSE/SSR/SSD Corresponding to Different K Values")
plt.title("Elbow Method for Optimal Cluster Number")
plt.show()

kmeans = KMeans()
elbow = KElbowVisualizer(kmeans, k=(2, 20))
elbow.fit(df)
elbow.show()

# Final Clusters
kmeans = KMeans(n_clusters=elbow.elbow_value_).fit(df)

kmeans.n_clusters
kmeans.cluster_centers_
kmeans.labels_
df[0:5]

clusters = kmeans.labels_

df = pd.read_csv("datasets/USArrests.csv", index_col=0)

df["cluster"] = clusters

df.head()

df["cluster"] = df["cluster"] + 1

df[df["cluster"]==1]

df.groupby("cluster").agg( ["count", "mean", "median"])

df.to_csv("cluster.csv")
