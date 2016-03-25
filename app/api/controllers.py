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

        script = "e = g.addEdge('belongs', g.V(%s), g.V(%s)); " % (user_id, dub_id)
        script += "e.setProperty('emo_id', %s)" % emo_id
        script = '{"gremlin": "%s"}' % script
        try:
            response = requests.post('http://ec2-52-50-189-192.eu-west-1.compute.amazonaws.com:8182', data=script)
        except ConnectionError as e:
            return 500, "db abruption"
        if response.status_code == 500:
            return 400, response.json()['message']
        return "ok"

def 