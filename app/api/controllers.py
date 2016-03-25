from flask.ext.restful import Resource
from flask import request
import requests
from requests.exceptions import ConnectionError


class Add(Resource):
    def post(self):
        r = request
        user_id = r.form['user_id']
        dub_id = r.form['dub_id']
        emo_id = r.form['emo_id']

        db_proxy = DbProxy()
        db_proxy.add("e = g.addEdge('belongs', g.V(%s), g.V(%s)); " % (user_id, dub_id))
        db_proxy.add("e.setProperty('emo_id', %s)" % emo_id)
        try:
            response = db_proxy.send()
        except ConnectionError as e:
            return 500, "db abruption"
        if response.status_code == 500:
            return 400, response.json()['message']
        return response.status_code, "ok"


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class DbProxy(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.script = ""

    def add(self, line):
        self.script += line

    def send(self):
        self.script = '{"gremlin": "%s"}' % self.script
        try:
            response = requests.post('http://ec2-52-50-189-192.eu-west-1.compute.amazonaws.com:8182', data=self.script)
        except ConnectionError as e:
            raise e
        self.script = ''
        return response
