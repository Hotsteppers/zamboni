import json
import requests

from flask import Flask, Response

app = Flask(__name__)


@app.route('/healthcheck')
def healthcheck():
    r = Response(response='Success', status=200, content_type='application/json')
    return r


# NHL API Routes
@app.route('/schedule/<startDate>/<endDate>')
def get_schedule(startDate, endDate):
    params = {'startDate': startDate, 'endDate': endDate}
    r = requests.get('https://statsapi.web.nhl.com/api/v1/schedule', params=params)
    json_obj = json.dumps(r.json())
    res = Response(response=json_obj, status=200, content_type='application/json')
    return res


@app.route('/player/<playerId>')
def get_player(playerId):
    params = {'playerId': playerId}
    reqString = 'http://statsapi.web.nhl.com/api/v1/people/{playerId}'.format(**params)
    r = requests.get(reqString)
    json_obj = json.dumps(r.json())
    res = Response(response=json_obj, status=200, content_type='application/json')
    return res


@app.route('/team/<teamId>')
def get_team(teamId):
    params = {'teamId': teamId}
    reqString = 'https://statsapi.web.nhl.com/api/v1/teams/{teamId}'.format(**params)
    r = requests.get(reqString)
    json_obj = json.dumps(r.json())
    res = Response(response=json_obj, status=200, content_type='application/json')
    return res


@app.route('/pbp/<year>/<gameId>')
def get_pbp(year, gameId):
    params = {'year': year, 'gameId': gameId}
    reqString = 'https://statsapi.web.nhl.com/api/v1/game/{year}0{gameId}/feed/live?site=en_nhl'.format(**params)
    r = requests.get(reqString)
    json_obj = json.dumps(r.json())
    res = Response(response=json_obj, status=200, content_type='application/json')
    return res


@app.route('/shifts/<year>/<gameId>')
def get_shifts(year, gameId):
    params = {'year': year, 'gameId': gameId}
    arg_part = 'gameId={year}0{gameId}'.format(**params)
    reqString = 'http://www.nhl.com/stats/rest/shiftcharts?cayenneExp={0}'.format(arg_part)
    r = requests.get(reqString)
    json_obj = json.dumps(r.json())
    res = Response(response=json_obj, status=200, content_type='application/json')
    return res


@app.route('/highlights/<year>/<gameId>')
def get_highlights(year, gameId):
    params = {'year': year, 'gameId': gameId}
    reqString = 'https://statsapi.web.nhl.com/api/v1/game/{year}0{gameId}/content?site=en_nhl'.format(**params)
    r = requests.get(reqString)
    json_obj = json.dumps(r.json())
    res = Response(response=json_obj, status=200, content_type='application/json')
    return res
