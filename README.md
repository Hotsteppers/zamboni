# zamboni
Public NHL API Scraper and Task Scheduler


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
