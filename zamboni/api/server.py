import json
import requests

from flask import Flask

app = Flask(__name__)


@app.route('/healthcheck')
def healthcheck():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/schedule/<startDate>/<endDate>')
def schedule(startDate, endDate):
    params = {'startDate': startDate, 'endDate': endDate}
    r = requests.get('https://statsapi.web.nhl.com/api/v1/schedule', params=params)
    json_obj = r.json()
    return json.dumps(json_obj), 200, {'ContentType': 'application/json'}


@app.route('/player/<playerId>')
def player(playerId):
    params = {'playerId': playerId}
    reqString = 'http://statsapi.web.nhl.com/api/v1/people/{playerId}'.format(**params)
    r = requests.get(reqString)
    json_obj = r.json()
    return json.dumps(json_obj), 200, {'ContentType': 'application/json'}
