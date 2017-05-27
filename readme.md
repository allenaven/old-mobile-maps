# Old Mobile: Historic Maps via the Web

All good maps have a story to tell. This site shares one. See it at https://mobilemap.us/.

Mobile, Alabama is a coastal city with a rich New World history spanning French, British, Spanish, American, Confederate, and ultimately (again) American governance.

<!-- TOC depthFrom:2 -->

- [Historic map notes](#historic-map-notes)
    - [Mobile 1838](#mobile-1838)
    - [Mobile 1900](#mobile-1900)
- [Technical notes](#technical-notes)
- [Open-source software used in this project](#open-source-software-used-in-this-project)
- [Map hosting providers](#map-hosting-providers)

<!-- /TOC -->

## Historic map notes

_I have more maps in the pipeline. Contact me if you can help source or georeference interesting, high quality historic maps of the area._

### Mobile 1838

- [Source](http://digital.archives.alabama.gov/cdm/ref/collection/maps/id/683)

### Mobile 1900

- [Source](http://digital.archives.alabama.gov/cdm/ref/collection/maps/id/692)

----------

## Technical notes

1. Webmap is built on the excellent open-source [Leaflet](http://leafletjs.com) framework
1. Georeferencing the historic map images was done with stellar open-source [QGIS](http://qgis.org/en/site/). My georeferencing isn't perfect but it's pretty close. [Read more about georeferencing these maps]().
1. Within the repo is a Python script I wrote and used to scrape and parse [Mobile, AL National Registry of Historic Places data from Wikipedia](https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Mobile,_Alabama). The script exports the data to `.geojson` usable in Leaflet. Beautiful-soup 4 makes this process _really_ easy.
1. The webmap loads quite a bit of Javascript... I'm hosting it all locally rather than calling it through a CDN. Since the site is hosted on EC2 it should load as quickly as anything else, I think. Lemme know if there's a better way to do that.

## Open-source software used in this project

1. [Leaflet.js](http://leafletjs.com)
1. [Leaflet.MagnifyingGlass](https://github.com/bbecquet/Leaflet.MagnifyingGlass)
1. [EasyButton.js](http://danielmontague.com/projects/easyButton.js/)
1. [leaflet.fullscreen](http://brunob.github.io/leaflet.fullscreen/)
1. [Leaflet.StyledLayerControl](https://github.com/davicustodio/Leaflet.StyledLayerControl)
1. [leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster)

## Map hosting providers

Thanks for supporting free-tier users!

1. [Mapbox](https://www.mapbox.com)
1. [Carto](https://carto.com)
1. [OpenStreetMap](http://www.openstreetmap.org/)
