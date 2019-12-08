import random as rand
import geopy.distance
from statistics import mean



class Cluster:

    def __init__(self):
        pass

    def distance(self, origin, dest):
        dest = (float(dest[0]), float(dest[1]))
        try:
            return geopy.distance.vincenty(origin, dest).m
        except Exception as e:
            print(0)

    def shouldStop(self, oldCentroids, centroids, iterations):
        if iterations > 100: return True
        return oldCentroids == centroids

    def getLabels(self,dataSet, centroids):
        labels = {}
        for key in dataSet.keys():
            point = dataSet[key]
            cd1 = None
            cd2 = None
            origin = (float(point['longitude']), float(point['latitude']))
            dest = centroids[list(centroids.keys())[0]]
            dest = (dest['longitude'], dest['latitude'])
            cd1 = self.distance(origin, dest)
            dest = centroids[list(centroids.keys())[1]]
            dest = (dest['longitude'], dest['latitude'])
            cd2 = self.distance(origin, dest)
            if cd1 < cd2:
                labels[key] = list(centroids.keys())[0]
            else:
                labels[key] = list(centroids.keys())[1]
        return labels

    def getCentroids(self, dataSet, labels, k, centroids):
        new = {}
        cx1 = []
        cx2 = []
        cy1 = []
        cy2 = []
        for label in labels.keys():
            if label == list(centroids.keys())[0]:
                cx1.append(float(dataSet[label]["longitude"]))
                cy1.append(float(dataSet[label]["latitude"]))
            else:
                cx2.append(float(dataSet[label]["longitude"]))
                cy2.append(float(dataSet[label]["latitude"]))
        centroids[list(centroids.keys())[0]]['longitude'] = mean(cx1)
        centroids[list(centroids.keys())[0]]['latitude'] = mean(cy1)
        centroids[list(centroids.keys())[1]]['longitude'] = mean(cx2)
        centroids[list(centroids.keys())[1]]['latitude'] = mean(cy2)
        return centroids

    def cluster(self, points):
        k = 2
        oldCentroids = None
        centroids = {}
        vals = points.keys()
        c1 = rand.randint(0, len(vals))
        c2 = c1
        while c1 == c2:
            c2 = rand.randint(0, len(vals))

        centroids[list(vals)[c1]] = points[list(vals)[c1]]
        centroids[list(vals)[c2]] = points[list(vals)[c2]]

        iterations = 0
        oldCentroids = None

        while not self.shouldStop(oldCentroids, centroids, iterations):
            # Save old centroids for convergence test. Book keeping.
            oldCentroids = centroids
            iterations += 1

            # Assign labels to each datapoint based on centroids
            labels = self.getLabels(points, centroids)

            # Assign centroids based on datapoint labels
            centroids = self.getCentroids(points, labels, k, centroids)

            # We can get the labels too by calling getLabels(dataSet, centroids)
        # clusters = {centroids.keys()[0]: [], centroids.keys()[1]: []}
        # for label in labels.keys():
        #     if labels[label] == centroids.keys()[0]:
        #         clusters[centroids.keys()[0]].append(label)
        #     else:
        #         clusters[centroids.keys()[1]].append(label)
        return centroids




