**[CircleCI](https://circleci.com/gh/Hotsteppers)**: [![CircleCI](https://circleci.com/gh/Hotsteppers/zamboni/tree/master.svg?style=svg)](https://circleci.com/gh/Hotsteppers/zamboni/tree/master)

# zamboni
Public NHL API Scraper and Task Scheduler

## Contributing

### Clone and Set up a Virtualenv

We recommend setting up a virutalenv when working on this locally. From within the project run

```
python3 -m venv env/
source env/bin/activate
```

To read more about Python3 Virtual Environments look [here](https://docs.python.org/3/library/venv.html)

### Testing
Run `make test` 

We are enforcing syntax with Flake8. You can read more about Flake8 [here](http://flake8.pycqa.org/en/latest/)

## NHL Public API
- **Schedule**: `https://statsapi.web.nhl.com/api/v1/schedule?startDate={startDate}&endDate={endDate}`
  - Gets all scheduled games between `{startDate}` and `{endDate}` (inclusive)
  - `{startDate}` & `{endDate}` in the form `YYYY-MM-DD`
  - `{endDate}` does not need to be specified if retrieving only a single day
- **Play-By-Play**: `https://statsapi.web.nhl.com/api/v1/game/{year}0{gameId}/feed/live?site=en_nhl`
  - Gets a single games PBP Data. This includes but is not limited too: Starting rosters, Game Events like goals or shots, final game scores, officials, and the games three stars. 
  - `{year}` is the year the game fell within 
  - `{gameId}` is a 5-digit game identifier used to connect these records with schedule, highlight, and shift records.
- **Shifts**: `http://www.nhl.com/stats/rest/shiftcharts?cayenneExp=gameId={year}0{gameId}`
  - Gets player shift data. This includes: shift start, stop, duration as well as which events occured while this player was on the ice.
  - `{year}` is the year the game fell within 
  - `{gameId}` is a 5-digit game identifier used to connect these records with schedule, highlight, and play-by-play records.
- **Players**: `http://statsapi.web.nhl.com/api/v1/people/{playerId}`
  - Gets a players personal data. This includes: first name, last name, number, height, weight, position, etc...
  - `{playerId}` - 7-digit player identifier used to identify player across data sets
- **Teams**: `https://statsapi.web.nhl.com/api/v1/teams/{teamId}`
  - Gets team details. This includes: Team name, timezone, conference, etc...
  - `{teamId}` - 1-31 used to identify team across data sets
- **Highlights**: `https://statsapi.web.nhl.com/api/v1/game/{year}0{gameId}/content?site=en_nhl`
  - Gets the chosen games highlight plays. 
  - `{year}` is the year the game fell within 
  - `{gameId}` is a 5-digit game identifier used to connect these records with schedule, play-by-play, and shift records.
