import geopy.distance
from DB import DB

class Location:

    def __init__(self, user):
        self.current_user = user
        self.guardians = None
        self.users = None
        self.candidates = None

    def get_locations(self):
        locations_table = DB.get_table('location')
        locations = []
        try:
            for doc in locations_table.stream():
                locations.append((doc.id, tuple(doc.to_dict().values())))
        except Exception as e:
            pass
        self.users = locations

    def get_guardians(self):
        user_id = self.current_user
        guardians_table = DB.get_table('guardians')
        guardians = None
        try:
            if user_id:
                guardians = guardians_table.document(str(user_id)).get()
                all_guardians = [doc.to_dict() for doc in guardians_table.stream()]
                self.guardians = all_guardians[0]['guardian_id']
        except Exception as e:
            pass

    def distance(self, origin, dest):
        dest = (float(dest[0]), float(dest[1]))
        return geopy.distance.vincenty(origin, dest).m

    def find_candidates(self):
        candidates = []
        origin = self.current_user[1]
        counter = 0
        while len(candidates) < 5:
            dist = self.distance(origin, self.users[counter][1])
            if not dist >= 50 and dist > 30:
                candidates.append(self.users[counter][0])
            counter += 1
        self.candidates = candidates

    def notify(self):
        pass

