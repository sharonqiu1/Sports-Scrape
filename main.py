import os
os.chdir("/Users/sharonqiu/documents/sports scrape") #change directory to wherever your files are stored
import dataCollect as collect
import teamUrlsList as teams
teamUrls = teams.listTeams()

for i in range(len(teamUrls)):
    collect.data_collect("https://www.pro-football-reference.com" + teamUrls[i])
