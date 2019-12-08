from firebase_admin import credentials, firestore, initialize_app


cred = credentials.Certificate('sahaarax-firebase-adminsdk-ui047-719a2b3110.json')
default_app = initialize_app(cred)
db = firestore.client()


class DB:
    @classmethod
    def get_table(cls, table):
        return db.collection(table)