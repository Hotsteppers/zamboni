from zamboni.helpers import constants as c
from itertools import chain

import requests as req
from datetime import datetime


def test_game_ids():
    assert c.GAME_ID_RANGES['regular_season'] == range(20001, 21230)
    assert list(c.GAME_ID_RANGES['round_one']) == list(chain(range(30111, 30118), range(30121, 30128),
                                                             range(30131, 30138), range(30141, 30148),
                                                             range(30151, 30158), range(30161, 30168),
                                                             range(30171, 30178), range(30181, 30188)))
    assert list(c.GAME_ID_RANGES['round_two']) == list(chain(range(30211, 30218), range(30221, 30228),
                                                             range(30231, 30238), range(30241, 30248)))
    assert list(c.GAME_ID_RANGES['conference_finals']) == list(chain(range(30311, 30318), range(30221, 30228)))
    assert c.GAME_ID_RANGES['stanley_cup_finals'] == range(30411, 30418)


def test_pbp_urls():
    test_vars = {'year': '2017', 'gameId': '20391'}
    url_pbp = c.PBP_URL.format(**test_vars)
    res = req.get(url_pbp)

    assert res.status_code == 200

    json_obj = res.json()

    assert list(json_obj.keys()) == ['copyright', 'gamePk', 'link', 'metaData', 'gameData', 'liveData']
    assert json_obj['gameData']['teams']['away']['id'] == 24
    assert json_obj['gameData']['teams']['away']['name'] == 'Anaheim Ducks'
    assert json_obj['gameData']['teams']['home']['id'] == 29
    assert json_obj['gameData']['teams']['home']['name'] == 'Columbus Blue Jackets'

    test_vars['year'] = datetime.now().year
    test_vars['gameId'] = c.GAME_ID_RANGES['regular_season'][0]

    url_pbp = c.PBP_URL.format(**test_vars)
    res = req.get(url_pbp)

    assert res.status_code == 200


def test_shifts_url():
    test_vars = {'year': '2017', 'gameId': '20391'}
    url_shifts = c.SHIFTS_URL.format(**test_vars)
    res = req.get(url_shifts)

    assert res.status_code == 200

    json_obj = res.json()

    assert list(json_obj.keys()) == ['data', 'total']
    assert list(json_obj['data'][0].keys()) == ['detailCode', 'duration', 'endTime',
                                                'eventDescription', 'eventDetails', 'eventNumber',
                                                'firstName', 'gameId', 'hexValue', 'lastName',
                                                'period', 'playerId', 'shiftNumber', 'startTime',
                                                'teamAbbrev', 'teamId', 'teamName', 'typeCode']
    assert json_obj['total'] == 763

    test_vars['year'] = datetime.now().year
    test_vars['gameId'] = c.GAME_ID_RANGES['regular_season'][0]

    url_shifts = c.SHIFTS_URL.format(**test_vars)
    res = req.get(url_shifts)

    assert res.status_code == 200


def test_players_url():
    test_vars = {'playerId': '8475166'}
    url_players = c.PLAYERS_URL.format(**test_vars)
    res = req.get(url_players)

    assert res.status_code == 200

    json_obj = res.json()

    assert json_obj['people'][0]['fullName'] == 'John Tavares'


def test_teams_url():
    url_team = c.TEAMS_URL.format(**{'teamId': '28'})
    res = req.get(url_team)

    assert res.status_code == 200

    obj = res.json()

    assert obj['teams'][0]['name'] == 'San Jose Sharks'


def test_highlights_url():
    test_vars = {'year': '2017', 'gameId': '20391'}
    url_highlights = c.HIGHLIGHTS_URL.format(**test_vars)
    res = req.get(url_highlights)

    assert res.status_code == 200

    obj = res.json()

    assert list(obj.keys()) == ['copyright', 'link',
                                'editorial', 'media', 'highlights']
    assert obj['highlights']['scoreboard']['items'][0]['title'] == 'Gibson robs Foligno with glove'

    test_vars['year'] = datetime.now().year
    test_vars['gameId'] = c.GAME_ID_RANGES['regular_season'][0]

    url_highlights = c.HIGHLIGHTS_URL.format(**test_vars)
    res = req.get(url_highlights)

    assert res.status_code == 200


def test_schedule_url():
    test_vars = {'startDate': '2017-12-01', 'endDate': '2017-12-02'}
    url_schedule = c.SCHEDULE_URL.format(**test_vars)
    res = req.get(url_schedule)

    assert res.status_code == 200

    obj = res.json()

    assert list(obj.keys()) == ['copyright', 'totalItems',
                                'totalEvents', 'totalGames', 'totalMatches', 'wait', 'dates']
    assert obj['totalGames'] == 20
    assert obj['dates'][0]['games'][0]['gamePk'] == 2017020388
