def data_collect(url):
    import requests
    from bs4 import BeautifulSoup
    import csv
    import os

    init_request = requests.get(url)
    init_soup = BeautifulSoup(init_request.content, "html.parser")
    table = init_soup.find("table",{"id":"games"})
    table_body = table.find("tbody")
    games = table_body.find_all("tr")
    name_find = init_soup.find("h1",{"itemprop":"name"})
    temp_list = name_find.find_all("span")
    team_name = temp_list[1].get_text()

    for game in games:
        opp_name = game.find("td", {"data-stat":"opp"}).get_text()
        if opp_name != "":
            outcome = game.find("td", {"data-stat":"game_outcome"}).get_text()
            if outcome != "":
                date = game.find("td",{"data-stat":"game_date"})['csk']
                csv_file_name = team_name + " vs " + opp_name + ": " + date
                team_score = game.find("td", {"data-stat":"pts_off"}).get_text()
                first_down = game.find("td", {"data-stat":"first_down_off"}).get_text()
                yards_offensive = game.find("td", {"data-stat":"yards_off"}).get_text()
                yards_passing = game.find("td", {"data-stat":"pass_yds_off"}).get_text()
                yards_rushed = game.find("td", {"data-stat":"rush_yds_off"}).get_text()
                turnovers_lost = game.find("td", {"data-stat":"to_off"}).get_text()
                if turnovers_lost == "":
                    turnovers_lost = "0"

                os.chdir("/Users/sharonqiu/documents/sports scrape/2017 Data All Teams") #change to 2018 if scraping 2018 scores
                new_file = open(csv_file_name+".csv","w")
                with new_file:
                    writer = csv.writer(new_file)
                    writer.writerow(["Game Outcome","Team Score","1stD","Yards Gained Offence","Yards Gained Passing","Yards Gained Rushing","Lost Turnovers"])
                    writer.writerow([outcome,team_score,first_down,yards_offensive,yards_passing,yards_rushed,turnovers_lost])
