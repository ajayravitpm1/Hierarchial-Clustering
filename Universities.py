import pandas as pd
Univ=pd.read_csv("F:/Universities/Universities.csv")
import matplotlib.pylab as plt
import scipy.cluster.hierarchy as sch
plt.figure(figsize=(15,5))
plt.title("Hierarchial Clustering-Dendrogram")
plt.xlabel("Universities");plt.ylabel("Distance")
df=Univ.iloc[:,1:]
def df_normalise(i):
    x=(i-i.mean())/i.std()
    return x
df_norm=df_normalise(df)
from scipy.cluster.hierarchy import linkage
z=linkage(df_norm,method="complete",metric="euclidean")
sch.dendrogram(z)
plt.show()

from sklearn.cluster import AgglomerativeClustering
hcluster=AgglomerativeClustering(n_clusters=3,affinity="euclidean").fit(df_norm)
hcluster_labels=pd.Series(hcluster.labels_)
Univ["Cluster"]=hcluster_labels

hcluster.fit_predict(df_norm)

Univ.to_csv("Universities_new.csv")


plt.figure(figsize=(10, 7))
plt.scatter(Univ.iloc[:,1],Univ.iloc[:,2],c=hcluster.labels_,cmap='rainbow')


