import json
import pytest

from zamboni.api import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    client = server.app.test_client()

    yield client


def test_healthcheck(client):
    """Test healthcheck."""

    rv = client.get('/healthcheck')
    assert rv.status_code == 200
    assert rv.content_type == 'application/json'


def test_get_schedule(client):
    """Test Retrieving Schedules"""
    rv = client.get('/schedule/2017-12-01/2017-12-02')
    assert rv.status_code == 200
    assert rv.content_type == 'application/json'
    data = json.loads(rv.data)
    assert data['totalGames'] == 20


def test_get_player_by_id(client):
    """Test Retrieving Player Details By Player ID"""
    rv = client.get('/player/8475166')
    assert rv.status_code == 200
    assert rv.content_type == 'application/json'
    data = json.loads(rv.data)
    assert data['people'][0]['fullName'] == 'John Tavares'


def test_get_team_by_id(client):
    """Test Retrieving Teams By Team ID"""
    rv = client.get('/team/28')
    assert rv.status_code == 200
    assert rv.content_type == 'application/json'
    data = json.loads(rv.data)
    assert data['teams'][0]['name'] == 'San Jose Sharks'


def test_get_pbp(client):
    """Test Retrieving Play-by-Play Data"""
    rv = client.get('/pbp/2017/20391')
    assert rv.status_code == 200
    assert rv.content_type == 'application/json'
    data = json.loads(rv.data)
    assert data['gameData']['teams']['away']['id'] == 24
    assert data['gameData']['teams']['away']['name'] == 'Anaheim Ducks'
    assert data['gameData']['teams']['home']['id'] == 29
    assert data['gameData']['teams']['home']['name'] == 'Columbus Blue Jackets'


def test_get_shifts(client):
    """Test Retrieving Shift Data"""
    rv = client.get('/shifts/2017/20391')
    assert rv.status_code == 200
    assert rv.content_type == 'application/json'
    data = json.loads(rv.data)
    assert list(data.keys()) == ['data', 'total']
    assert list(data['data'][0].keys()) == ['detailCode', 'duration', 'endTime',
                                            'eventDescription', 'eventDetails', 'eventNumber',
                                            'firstName', 'gameId', 'hexValue', 'lastName',
                                            'period', 'playerId', 'shiftNumber', 'startTime',
                                            'teamAbbrev', 'teamId', 'teamName', 'typeCode']
    assert data['total'] == 763


def test_get_highlights(client):
    """Test Retrieving Game Highlights"""
    rv = client.get('/highlights/2017/20391')
    assert rv.status_code == 200
    assert rv.content_type == 'application/json'
    data = json.loads(rv.data)
    assert list(data.keys()) == ['copyright', 'link',
                                 'editorial', 'media', 'highlights']
    assert data['highlights']['scoreboard']['items'][0]['title'] == 'Gibson robs Foligno with glove'
