import socket
import requests
import time
import json

all_days = []
all_venues = {}


def get_stores(ad):
    # Find the user's current location using their api
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    # print(f"Hostname: {hostname}")
    # print(f"IP Address: {ip_address}")

    my_url = "https://geolocation-db.com/json/" + "142.157.215.88" + ".79&position=true"

    # print("my ip address: ", ip_address)

    response = requests.get(my_url).json()

    # print(response)
    latitude = response.get("latitude")
    longitude = response.get("longitude")

    # JSON file is a dictionary
    TRUE_ip = response.get("IPv4")

    # print("TRUE ip: ", TRUE_ip)

    def ipInfo(addr=''):
        from urllib.request import urlopen
        from json import load
        if addr == '':
            url = 'https://iplocation.com/json'
        else:
            url = 'https://ipinfo.io/' + addr + '/json'
        res = urlopen(url)
        # response from url(if res==None then check connection)
        data = load(res)
        # print("data:", data)
        # will load the json response into data
        return data.get("city")

        # for attr in data.keys():
        # will print the data line by line
        # print(attr,' '*13+'\t->\t',data[attr])

    # ------------- USER CITY CONFIRMATION --------------#

    user_city = "Your City"
    url = "https://besttime.app/api/v1/venues/search"
    if ad != "":
        our_search = "busy " + ad
        print(our_search)
    else:
        user_city = ipInfo(TRUE_ip)
        # Now that we have the long and lat, we put that in the search
        our_search = "busiest grocery store and malls in " + user_city.lower()
        # print(our_search)

    params = {
        'api_key_private': 'pri_71a7b209702843c2a5bcedc699b13db8',
        'q': our_search,
        'num': 20,
        'fast': False
    }

    response = requests.request("POST", url, params=params)

    # print(response)
    # gives us a link to json file with all the venues and their foot traffic data
    # print(response.json())

    # uncomment this for API connection

    dic_url_for_data = response.json()
    print(dic_url_for_data)

    url_for_data = (dic_url_for_data.get("_links")).get("venue_search_progress")
    # print(url_for_data)

    '''
    f = open("venues_json.json")
    venues_json = json.load(f)
    json_for_data = venues_json.get("venues")

    # dictionary for all addresses
    all_venues = {}
    i = 0
    st = 0
    ed = 7
    lst = []
    for ven in json_for_data:
        if ven.get("venue_foot_traffic_forecast") != None:
            ven_name = ven.get("venue_name")
            ven_address = ven.get("venue_address")
            ven_id = ven.get("venue_id")
            ven_h = ven.get("venue_foot_traffic_forecast")
            ven_hours = {}
            # all_venues.update({ven_name: [ven_address, ven_hours, i]})
            for day in range(len(ven) - 1):
                ven_day_info = ven_h[day].get("day_info")
                ven_open = ven_day_info.get("venue_open")
                ven_closed = ven_day_info.get("venue_closed")
                if ven_open != "Closed":
                    ven_hours.update({ven_day_info.get("day_text"): (str(ven_open) + "h" + "-" + str(ven_closed) + "h")})
                # all_venues.update({ven_name: [ven_address, ven_hours, i]})
                else:
                    ven_hours.update({ven_day_info.get("day_text"): str(ven_closed) })

                # in a new html file, where we get access when we click
                # on "see heatmap"
                day = ven_day_info.get("day_text")
                day_data = ven_h[0].get("day_raw")

            all_venues.update({ven_name: [ven_address, ven_hours, i]})
            i += 1
            st += 7
            ed += 7
            all_days.append(day_data)
    '''

    # this code is for when we have access to the url again

    time.sleep(10)
    venue_info = requests.get(url_for_data).json()
    lst_dic = venue_info.get("venues")

    day_data = []
    i = 0
    for ven in lst_dic:
        if ven.get("venue_foot_traffic_forecast") is not None:
            ven_name = ven.get("venue_name")
            ven_address = ven.get("venue_address")
            ven_id = ven.get("venue_id")
            ven_h = ven.get("venue_foot_traffic_forecast")
            ven_hours = {}
            # all_venues.update({ven_name: [ven_address, ven_hours, i]})
            for day in range(len(ven) - 1):
                ven_day_info = ven_h[day].get("day_info")
                ven_open = ven_day_info.get("venue_open")
                ven_closed = ven_day_info.get("venue_closed")
                if ven_open != "Closed":
                    ven_hours.update(
                        {ven_day_info.get("day_text"): (str(ven_open) + "h" + "-" + str(ven_closed) + "h")})
                # all_venues.update({ven_name: [ven_address, ven_hours, i]})
                elif ven_open == "Closed":
                    ven_hours.update({ven_day_info.get("day_text"): str(ven_closed)})
                else:
                    ven_hours.update({ven_day_info.get("day_text"): str("Open 24h")})

                # in a new html file, where we get access when we click
                # on "see heatmap"
                day = ven_day_info.get("day_text")
                day_data = ven_h[0].get("day_raw")

            all_venues.update({ven_name: [ven_address, ven_hours, i]})
            i += 1
            all_days.append(day_data)

    # return all_venues, all_days
    return all_venues, all_days, user_city
    # return url_for_data

# print(get_stores()[0])
# print(get_stores()[1])
# print(get_stores()[1][15:21])