from pymongo import MongoClient
import hashlib, random

class MongoDao:

    def __init__(self, connectString):
        self._client = self.__connect(connectString);
        self._auth_db = self._client.auth;
        self._users = self._auth_db.users;
        self._tokens = self._auth_db.tokens;

    def __connect(self, connectString):
        try:
            print("connecting...");
            conn = MongoClient(connectString, connectTimeoutMS=5000);
            print("connected...");
            return conn;
        except:
            print("Could not connect to database.");
            raise

    def authenticateClient(self, key, secret):
        try:
            user = self._users.find_one({'key': key, 'secret': secret});
            return self.__createToken(user) if user else False;
        except:
            print("Failed to get accounts.");
            raise

    def __createToken(self, user):
        token = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest();
        print(token)
        id = self._tokens.insert_one({"userid": user['_id'], "token": token});
        if id:
            return token;
        else:
            raise Exception("Gah. Couldnt create the record!");


    def new(self, **kwargs):
        record = self._users.insert_one(kwargs)
        if record:
            return record;
        else:
            raise Exception("Gah. Couldnt create the record!");
