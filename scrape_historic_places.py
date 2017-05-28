#!/usr/bin/env python
# A.Aven 2017
# ./get_al_historic.py

"""
Scrapes Wikipedia page for Mobile County National Historic Places. Parses
historic place data table. Outputs to .geojson format for a Leaflet webmap.

Requires Python 3 and packages Beautiful Soup 4, requests, json
"""

import requests
from bs4 import BeautifulSoup
import json

def scrape_url():
    """Grabs the specified page and returns parsed BeautifulSoup object"""
    the_url = 'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Mobile,_Alabama'
    html = requests.request('GET', the_url)
    sp = BeautifulSoup(html.content, 'html.parser')

    # Get rid of some really annoying element in the Wiki page:
    remove_sortkeys = sp.find_all("span", "sortkey")
    for _ in remove_sortkeys:
        _.decompose()

    return sp

def place_to_dict(tablerow):
    """
    :param tablerow: One table row <tr> from bs4 which will be
      broken down by this function
    :return: A dict with which to build geojson
    """
    # First td contains title:
    title = tablerow.find('td').text

    # Grab description from the td titled "note"
    descr = tablerow.find('td', 'note').text

    # Extract lat and lon. Haven't had any errors but I put the try/except
    #   in just incase it chokes on something funky.
    try:
        llstr = tablerow.find('span', 'geo').text.split(';')
        ll = [float(_) for _ in llstr]
    except:
        ll = ('error', 'error')

    # Build dict to return
    data = {'name' : title, 'desc' : descr, 'lon' : ll[1], 'lat' : ll[0]}

    # Return dict
    return data

def build_geojson(features):
    """
    Building out the geojson is really just making a giant dict, filling it,
    and returning it using json.dumps
    :return:
    """
    # Initialize the outgoing structure
    feature_list = []
    for number, feature in enumerate(features):
        out = {'type' : 'Feature', 'id' : number + 1, 'properties' : feature,
               'geometry' : {'type': 'Point', 'coordinates': [feature['lon'], feature['lat']]}}
        feature_list.append(out)

    al_historic = {'type' : 'FeatureCollection', 'features' : feature_list}
    return json.dumps(al_historic, indent=4)

def main():
    """
    Run the script
    """
    soup = scrape_url()
    places = []
    for row in soup.find_all("tr", "vcard"):
        place = place_to_dict(row)
        places.append(place)

    the_json = build_geojson(places)
    the_json = 'var al_historic = ' + the_json

    # Export to file. If the data get too big I'll have to implement
    #   some io here. Not even close to that right now.
    with open('./al_historic.geojson', 'wt') as outfile:
        outfile.writelines(the_json)

# Run on command line
if __name__ == '__main__':
    main()
