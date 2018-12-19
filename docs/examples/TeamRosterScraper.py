from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster
import os, time


nba_teams = teams.get_teams()

dirtowrite = 'C://Users//mpollard//Documents//GitHub//nba_api//output//'


for team in nba_teams:
    roster = commonteamroster.CommonTeamRoster(team_id=team['id'])
    roster = roster.get_data_frames()[0]
    filename = team['full_name'] + '-roster.csv'
    roster.to_csv(os.path.join(dirtowrite, filename))
    time.sleep(10)