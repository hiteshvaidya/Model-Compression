
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

#weights
x = [2.09,-0.98,1.48,0.09,0.05,-0.14,-1.08,2.12,-0.91,1.92,0,-1.03,1.87,0,1.53,1.49]
y = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]

plt.scatter(x,y)
plt.show()

X = np.array([2.09,-0.98,1.48,0.09,0.05,-0.14,-1.08,2.12,-0.91,1.92,0,-1.03,1.87,0,1.53,1.49])
X = np.reshape(X,(-1,1))

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print('centroids = ',centroids)
print('\nlabels = ',labels)

colors = ["g.","r.","c.","y."]
print('\nmapping of datapoints to clusters = ')
for i in range(len(X)):
    print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i],5, colors[labels[i]], markersize = 10)


plt.scatter(centroids[:],y[:4], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()

#grafients
a = [-0.03,-0.01,0.03,0.02,-0.01,0.01,-0.02,0.12,-0.01,0.02,0.04,0.01,-0.07,-0.02,0.01,-0.02]
b = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]

plt.scatter(a,b)
plt.show()

Y = np.array([-0.03,-0.01,0.03,0.02,-0.01,0.01,-0.02,0.12,-0.01,0.02,0.04,0.01,-0.07,-0.02,0.01,-0.02])
Y = np.reshape(Y,(-1,1))

colors = ["g.","r.","c.","y."]
print('\ngrouping of gradients = ')
grad0 = np.array([])
grad1 = np.array([])
grad2 = np.array([])
grad3 = np.array([])
for i in range(len(labels)):
    #print("coordinate:",X[i], "label:", labels[i])
    
    if labels[i] == 0:
    	grad0 = np.append(grad0,Y[i])    	
    elif labels[i] == 1:
    	grad1 = np.append(grad1,Y[i])    	
    elif labels[i] == 2:
    	grad2 = np.append(grad2,Y[i])    	
    elif labels[i] == 3:
    	grad3 = np.append(grad3,Y[i])  	

print(grad0)
print(grad1)
print(grad2)
print(grad3)
lr = 1

centroids[0] -= lr*np.sum(grad0)
centroids[1] -= lr*np.sum(grad1)
centroids[2] -= lr*np.sum(grad2)
centroids[3] -= lr*np.sum(grad3)
print("\nFine-tuned centroids = ",centroids)
