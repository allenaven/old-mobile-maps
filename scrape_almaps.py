#!/usr/bin/env python

"""
AA 2017

Script to download a proper image from webmap Mrsid portal. You need to know
the map ID and map pixel dimensions before you run this script. That info is
available at the map source page.

Start off here, at the "Alabama Maps Collection":
http://digital.archives.alabama.gov/cdm/landingpage/collection/maps

From there, find the map you're interested in. Get the "map ID" (my term for
it) from the URL of the map you've clicked into, it will be an integer
immediately following the /id/ portion of the URL. Make it more descriptive
if you want to, before passing it to this script. It's just a name.

Next, on the map source page, click into the "fullscreen" view and manipulate
the zoom control slider until it is at 100% (shown by the tooltip popup on the
slider control). This is important--you have to be at 100% to get the correct
dimensions.

Now go into your browser "inspect properties" tool (varies according to which
browser you're running). In the inspector, look for the <div id="imageLayer">.
Within that, you will see tags for with and height. Those are what you want!

Example url = http://digital.archives.alabama.gov/utils/ajaxhelper/?CISOROOT=maps&CISOPTR=690&action=2&DMSCALE=200&DMWIDTH=512&DMHEIGHT=512&DMX=0&DMY=512&DMTEXT=&DMROTATE=0
Example url = http://digital.archives.alabama.gov/utils/ajaxhelper/?CISOROOT=maps&CISOPTR=42&action=2&DMSCALE=100&DMWIDTH=512&DMHEIGHT=512&DMX=4608&DMY=2048&DMTEXT=&DMROTATE=0
"""

import argparse
import requests
import os
from PIL import Image


class sidmap(object):
    """
    The raster map online in mrsid form
    Assumes that you want to download 512x512 px tiles
    """

    def __init__(self, mapid, map_width_px, map_height_px, **kwargs):
        self.mapid = str(mapid)
        self.img_width_px = map_width_px
        self.img_height_px = map_height_px

    def __str__(self):
        return f'Map id: {self.mapid}\nImage width: {str(self.img_width_px)}\nImage height: {str(self.img_height_px)}'

    def build_tile_descrips(self):
        """
        :return: List of urls to query for all tiles in the image 
        """
        xrange = [i for i in range(0, self.img_width_px, 512)]
        yrange = [j for j in range(0, self.img_height_px, 512)]

        xy = [(x,y) for y in yrange for x in xrange]
        descripts = []
        for x, y in xy:
            tile_url = f'http://digital.archives.alabama.gov/utils/ajaxhelper/?CISOROOT=maps&CISOPTR={self.mapid}&action=2&DMSCALE=100&DMWIDTH=512&DMHEIGHT=512&DMX={x}&DMY={y}&DMTEXT=&DMROTATE=0'
            descripts.append((x,y,tile_url))
        return descripts

    def get_tile(self, tile_descrip):
        """
        Download the specified tile
        :param tile_descrip:  The tile object to be downloaded, a tuple
          specifying the url and position (upper left corner x and y
          in absolute pixels).
        :return: A binary object to be saved to image file
        """
        # Unpack the info from argument
        x_ul, y_ul, img_url = tile_descrip

        # Check, create a subdir to store tile files
        try:
            os.mkdir(self.mapid)
        except FileExistsError:
            pass

        # Download with requests.get
        img = requests.get(img_url, stream=True)

        # Save in subdirectory named for the map ID number
        outfilename = f'map_image_{self.mapid}_{x_ul}_{y_ul}.jpg'
        outpath = os.path.join(self.mapid, outfilename)
        if img.status_code == 200:
            with open(outpath, 'wb') as outfile:
                for chunk in img.iter_content(1024):
                    outfile.write(chunk)

        # Returns info useful for the mosaic function
        return (x_ul, y_ul, img_url, outpath)

    def merge_img(self, mergeinfo):
        """
        Reads the scraped files, merges them, saves them out
        :return: The filename of the new mosaiced image
        """
        # Setup the new image
        mosaic = Image.new('RGB', (self.img_width_px, self.img_height_px))

        # Paste in the tiles
        for i in mergeinfo:
            tile = Image.open(i[3])
            mosaic.paste(tile, (i[0], i[1]))

        # Write the mosaiced raster out to file with name {mapid}
        mosaic.save(f'mosaic_{self.mapid}.jpg')

# ## Testing example (don't run this!)
# def testcase():
#     # testmap = sidmap('693', 12000, 7875)
#     testmap = sidmap('693', 2000, 1600)
#     test_descripts = testmap.build_tile_descrips()
#     tiles = []
#     for i in test_descripts:
#         tiles.append(testmap.get_tile(i))
#
#     return testmap.merge_img(tiles)
# testcase()


if __name__ == '__main__':
    prs = argparse.ArgumentParser(description='Easily get a mrsid image')
    prs.add_argument('id', type=str, help="Name to assign the map")
    prs.add_argument('width', type=int, help="Width of map (pixels)")
    prs.add_argument('height', type=int, help="Height of map (pixels)")
    args = prs.parse_args()
    print(f"Working!\nID = {args.id}\nWidth = {args.width}\nHeight = {args.height}")

    # Do the work:
    map = sidmap(args.id, args.width, args.height)
    tile_descriptions = map.build_tile_descrips()
    tiles = []
    for i in tile_descriptions:
        tiles.append(map.get_tile(i))
    map.merge_img(tiles)

    print('\nFinished. Check for mosaiced raster.\n')
else:
    print('Have a nice day!')
