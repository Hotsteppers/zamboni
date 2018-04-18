from itertools import chain

# Public NHL API Endpoints
PBP_URL = 'https://statsapi.web.nhl.com/api/v1/game/{year}0{gameId}/feed/live?site=en_nhl'
SHIFTS_URL = 'http://www.nhl.com/stats/rest/shiftcharts?cayenneExp=gameId={gameId}'
PLAYERS_URL = 'http://statsapi.web.nhl.com/api/v1/people/{playerId}'
TEAMS_URL = 'https://statsapi.web.nhl.com/api/v1/teams/{teamId}'
HIGHLIGHTS_URL = 'https://statsapi.web.nhl.com/api/v1/game/{year}0{gameId}/content?site=en_nhl'
SCHEDULE_URL = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate={startDate}&endDate={endDate}'

# Game ID Hash Table
GAME_ID_RANGES = {
  'regular_season': range(20001, 21230),
  'round_one': chain(range(30111, 30118), range(30121, 30128), range(30131, 30138), range(30141, 30148),
                     range(30151, 30158), range(30161, 30168), range(30171, 30178), range(30181, 30188)),
  'round_two': chain(range(30211, 30218), range(30221, 30228), range(30231, 30238), range(30241, 30248)),
  'conference_finals': chain(range(30311, 30318), range(30221, 30228)),
  'stanley_cup_finals': range(30411, 30418)
}
