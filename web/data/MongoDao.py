from pymongo import MongoClient
from bson.json_util import dumps

class MongoDao:

    def __init__(self, connectString):
        self._client = self.__connect(connectString);
        self._data_db = self._client.auth;
        self._auth_db = self._client.auth;
        self._accounts = self._data_db.accounts;
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

    def listAccounts(self):
        try:
            return [] if self._accounts.count() == 0 else self._accounts.find();
        except:
            print("Failed to get accounts.");
            raise

    def insertAccount(self, name, employees, valuation):
        try:
            r = self._accounts.insert_one({"name": name, "employees": employees, "valuation": valuation});
        except:
            print("Failed to create account.");
            raise

        if id:
            return r.inserted_id
        else:
            raise Exception("Failure creating account.");

    def authenticate(self, token):
        if not token:
            return False
        try:
            return True if self._tokens.find_one({"token": token}) else False
        except:
            print("Failed to query for token.");
            return False