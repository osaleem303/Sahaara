from firebase_admin import credentials, firestore, initialize_app
from kmeans import Cluster
import copy
from DB import DB


class Event:

    def __init__(self):
        self.data = None
        self.centroids = None


    def get_data(self):
        events = []
        events_table = DB.get_table('data')
        try:
            for event in events_table.stream():
                events.append((event.id, event.to_dict()))
        except Exception as e:
            pass
        self.data = events

    def calc_hotzones(self):
        points = {}
        for event in range(len(self.data)):
            points[self.data[event][0]] = self.data[event][1]
        self.centroids = copy.deepcopy(Cluster().cluster(points))

    def update_zone(self):
        centroids = self.centroids
        try:
            table = DB.get_table('zones')
            for center in centroids.keys():
                if table.document(center).get().exists:
                    DB.get_table('zones')\
                        .document(center)\
                        .update({'longitude': self.centroids[center]['longitude'],
                                 'latitude': self.centroids[center]['latitude']})
                else:
                    DB.get_table('zones') \
                        .document(center) \
                        .set({'longitude': self.centroids[center]['longitude'],
                                 'latitude': self.centroids[center]['latitude']})
        except Exception as e:
            return f"An Error occured: {e}"
