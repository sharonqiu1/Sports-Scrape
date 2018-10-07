def listTeams():
    import requests
    from bs4 import BeautifulSoup

    init_request = requests.get("https://www.pro-football-reference.com/years/2017/") #change to 2018 if needed
    soup = BeautifulSoup(init_request.content,"html.parser")
    table_container = soup.find("div",{"id":"content"})

    afc_outer = table_container.find("div",{"id":"all_AFC"})
    afc_table = afc_outer.find("table",{"id":"AFC"})
    afc_table_body = afc_table.tbody
    values = afc_table_body.find_all("tr")

    nfc_outer = table_container.find("div",{"id":"all_NFC"})
    nfc_table = nfc_outer.find("table",{"id":"NFC"})
    nfc_table_body = nfc_table.tbody
    nfcvalues = nfc_table_body.find_all("tr")

    values.extend(nfcvalues)
    link = []
    for i in range(len(values)):
        if (values[i].find('th')):
            link.append(values[i].th.a['href'])

    return link
