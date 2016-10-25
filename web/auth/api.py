#!/usr/bin/python3
from flask import Flask, request, json, Response
from MongoDao import MongoDao
from bson import json_util
import os

auth = Flask(__name__)
logger = auth.logger
dao = MongoDao(
    os.environ['DB_PORT_27017_TCP_ADDR'])

@auth.route('/create', methods=['POST'])
def create_user():

    item_doc = {
        'name': request.form['key'],
        'description': request.form['secret']
    }
    inserted = dao.new(item_doc)

    if inserted:
        return Response(json_util.dumps({"new_user":inserted}), status=201);
    else:
        return Response(status=401);

@auth.route("/token")
def getToken():
    logger.debug("Get Token");
    key = request.args.get('key');
    secret = request.args.get('secret');
    result = dao.authenticateClient(key, secret);
    if result:
        return Response(json_util.dumps({"token":result}), status=201);
    else:
        return Response(status=401);

@auth.route("/health")
def health():
    logger.debug("Get Health");
    return json.jsonify(healthy='true');

if __name__ == "__main__":
    auth.run()
