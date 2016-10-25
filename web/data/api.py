#!/usr/bin/python3
from flask import Flask, request, json, Response
from MongoDao import MongoDao
from bson import json_util
import os

data = Flask(__name__)
logger = data.logger
dao = MongoDao(
    os.environ['DB_PORT_27017_TCP_ADDR'])
@data.route("/accounts", methods=['GET', 'POST'])
def accounts():
    logger.debug("Get Accounts");
    token = request.headers.get('token');
    if not dao.authenticate(token):
        return Response(status=401)

    if request.method == "GET":
        return Response(json_util.dumps(dao.listAccounts()), mimetype='application/json')
    elif request.method == "POST":
        name = request.args.get("name");
        employees = int(request.args.get("employees")) or 0
        valuation = int(request.args.get("valuation")) or 0
        if not name or len(name) == 0:
            r = json.jsonify(reason="Name is required.");
            r.status_code=400;
            return r;
        else:
            try:
                id = dao.insertAccount(name, employees, valuation);
                return Response(json_util.dumps({"id": id}), mimetype='application/json', status=201);
            except:
                r = json.jsonify(reason="Failed to create account.");
                r.status_code=500;
                return r;


@data.route("/health")
def health():
    logger.debug("Get Health");
    return json.jsonify(data_healthy='true');

if __name__ == "__main__":
    data.run()
