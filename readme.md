# Historic Mobile Webmap

All good maps have a story to tell. This site shares one. See it at https://www.mobilemap.us/.

Mobile, Alabama is a coastal city with a rich New World history spanning French, British, Spanish, American, Confederate, and ultimately (again) American governance.

<!-- TOC depthFrom:2 -->

- [Historic map notes](#historic-map-notes)
    - [Mobile 1838](#mobile-1838)
    - [Mobile 1900](#mobile-1900)
- [Technical notes](#technical-notes)
- [Open-source software used in this project](#open-source-software-used-in-this-project)
- [Map hosting providers](#map-hosting-providers)
- [Changelog](#changelog)
- [License](#license)

<!-- /TOC -->

## Historic map notes

_I have more maps in the pipeline. Contact me if you can help source or georeference interesting, high quality historic maps of the area._

### Mobile 1838

- [Source](http://digital.archives.alabama.gov/cdm/ref/collection/maps/id/683)

### Mobile 1900

- [Source](http://digital.archives.alabama.gov/cdm/ref/collection/maps/id/692)

----------

## Technical notes

- Webmap is built on the excellent open-source [Leaflet](http://leafletjs.com) framework
- I used the stellar open-source [QGIS](http://qgis.org/en/site/) to georeference the scanned images. My georeferencing isn't perfect but it's close. [Read more about georeferencing these maps](https://www.allenaven.com/note/working_with_historic_maps/).
- Within the repo is a script (`scrape_historic_places.py`) to scrape and parse the [Mobile, AL National Registry of Historic Places data from Wikipedia](https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Mobile,_Alabama). The script exports the data to `.geojson` usable in Leaflet. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) made this process _really_ easy to code.
- The webmap loads quite a bit of Javascript... I'm serving it all locally rather than calling it through a CDN. Since the site is hosted on AWS EC2 it should load as quickly as anything else, I think. Lemme know if there's a better way to do that.
    - Update: moved hosting to Netlify. Seems to load quicker than it did from AWS.
- In addition to all the Javascript, the raster historic maps are _really_ heavy

## Open-source software used in this project

This project would not exist without the talented developers in the FOSS geospatial community. Thank you.

- [QGIS](http://qgis.org/en/site/)
- [Leaflet.js](http://leafletjs.com), Copyright (c) 2010-2016, Vladimir Agafonkin Copyright (c) 2010-2011, CloudMade, [BSD 2-clause Simplified License](https://github.com/Leaflet/Leaflet/blob/master/LICENSE)
- [Leaflet.MagnifyingGlass](https://github.com/bbecquet/Leaflet.MagnifyingGlass), Copyright (c) 2013 Benjamin Becquet, [MIT License](https://github.com/bbecquet/Leaflet.MagnifyingGlass/blob/master/LICENSE)
- [EasyButton.js](http://danielmontague.com/projects/easyButton.js/), Copyright (C) 2014 Daniel Montague, [MIT License](https://github.com/CliffCloud/Leaflet.EasyButton/blob/master/LICENSE)
- [Leaflet.fullscreen](http://brunob.github.io/leaflet.fullscreen/), Copyright (c) 2013, Bruno Bergot, [MIT License](https://github.com/brunob/leaflet.fullscreen/blob/master/LICENSE)
- [Leaflet.StyledLayerControl](https://github.com/davicustodio/Leaflet.StyledLayerControl) ([CC Attribution 3.0 Unported License](https://creativecommons.org/licenses/by/3.0/deed.en_US))
- [Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster), Copyright 2012 David Leaver, [MIT License](https://github.com/Leaflet/Leaflet.markercluster/blob/master/MIT-LICENCE.txt)

## Map hosting providers

Thanks for supporting free-tier users!

- [Mapbox](https://www.mapbox.com)
- [Carto](https://carto.com)
- [OpenStreetMap](http://www.openstreetmap.org/)

## Changelog

- 2017-05-20 Initial version of map online at my professional website
- 2017-05-27 Moved map to [Netlify](https://www.netlify.com/) to take advantage of their CDN, Git integration, and pricing for open-source projects
- 2017-06-06 Revamped to add sidebar and default fullscreen. Added MIT license.

## License

This is free software under the [MIT License](./LICENSE).