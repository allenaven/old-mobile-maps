# Old Mobile: Historic Maps via the Web

One of the US Library of Congress' best-kept secrets is their digital archive of thousands of high-quality scans of historic maps. Many of those were created by Union Army surveyors during the 1860s, during and after the US Civil War and Reconstruction, making Civil War sites especially well-represented in the map archives.

Mobile, Alabama is a coastal city with a long New World history including French, British, Spanish, American, Confederate States, and ultimately (again) American governance.

## Historic map notes

### Mobile 1838

- [View source](http://digital.archives.alabama.gov/cdm/ref/collection/maps/id/683)

_More historic maps to come. Contact me if you can help source or georeference interesting, high-quality historic maps of the city._

## Tech notes

1. Webmap built on the excellent open-source [Leaflet](http://leafletjs.com) framework
1. I georeferenced the historic map images using the stellar open-source [QGIS](http://qgis.org/en/site/). My georeferencing isn't perfect but it's pretty close. [Read more about georeferencing these maps]().
1. Within the repo is a Python script I wrote and used to scrape and parse [Mobile, AL National Registry of Historic Places data from Wikipedia](https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Mobile,_Alabama). The script exports the data to `.geojson` usable in Leaflet. Beautiful-soup 4 makes the whole process _really_ easy.
1. The webmap loads quite a bit of Javascript... I'm hosting it all locally rather than calling it through a CDN because since this site is hosted on S3 it should load just as quickly as anything else. I think. Lemme know if there's a better way to do that.

## Open-source software used in this project

1. [Leaflet.js](http://leafletjs.com)
1. [Leaflet.MagnifyingGlass](https://github.com/bbecquet/Leaflet.MagnifyingGlass)
1. [EasyButton.js](http://danielmontague.com/projects/easyButton.js/)
1. [leaflet.fullscreen](http://brunob.github.io/leaflet.fullscreen/)
1. [Leaflet.StyledLayerControl](https://github.com/davicustodio/Leaflet.StyledLayerControl)
1. [leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster)

## Map hosting providers

Thanks for giving generously of your bandwidth and resource for free-tier users!

1. [Mapbox](https://www.mapbox.com)
1. [Carto](https://carto.com)
1. [OpenStreetMap](http://www.openstreetmap.org/)
