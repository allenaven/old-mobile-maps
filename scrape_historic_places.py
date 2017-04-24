# ./get_al_historic.py

"""
Scrapes the Wikipedia page for Mobile County National Historic Places and
outputs them to a .geojson format file for import into a Leaflet webmap.

Requires Python 3, external packages Beautiful Soup 4 and requests, and 
internal package json.
"""

import requests
from bs4 import BeautifulSoup
import json

def scrape_url():
    the_url = 'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Mobile,_Alabama'
    html = requests.request('GET', the_url)
    return BeautifulSoup(html.content, 'html.parser')

def place_to_dict(tablerow):
    """
    :param tablerow: Input from bs4 
    :return: A tuple suitable for dict creation
    """
    # First td should have title:
    title = tablerow.find('td').text

    # Grab description from the td titled "note"
    descr = tablerow.find('td', 'note').text

    # Extract lat and lon
    try:
        llstr = tablerow.find('span', 'geo').text.split(';')
        ll = [float(_) for _ in llstr]
    except:
        ll = ('error', 'error')

    data = {'name' : title, 'desc' : descr, 'lon' : ll[1], 'lat' : ll[0]}

    # Return a tuple
    return data

def build_geojson(features):
    """
    Building out the geojson is really just making a giant dict, filling it,
    and exporting with json.dumps
    :return: 
    """
    # Initialize the outgoing structure
    feature_list = []
    for number, feature in enumerate(features):
        out = {'type' : 'Feature', 'id' : number + 1, 'properties' : feature,
                   'geometry' : {'type': 'Point', 'coordinates': [feature['lon'], feature['lat']]}}
        feature_list.append(out)

    al_historic = {'type' : 'FeatureCollection', 'features' : feature_list }
    return json.dumps(al_historic, indent=4)

def main():
    soup = scrape_url()
    places = []
    for row in soup.find_all('tr'):
        try:
            if row.get('class')[0] == 'vcard':
                place = place_to_dict(row)
                places.append(place)
        except:
            pass

    the_json = build_geojson(places)
    the_json = 'var al_historic = ' + the_json

    with open('./al_historic.geojson', 'wt') as outfile:
        outfile.writelines(the_json)

# Run the file. As a module, or otherwise.
if __name__ == main:
    main()
else:
    main()