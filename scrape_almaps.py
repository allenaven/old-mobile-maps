# Example url = http://digital.archives.alabama.gov/utils/ajaxhelper/?CISOROOT=maps&CISOPTR=690&action=2&DMSCALE=200&DMWIDTH=512&DMHEIGHT=512&DMX=0&DMY=512&DMTEXT=&DMROTATE=0

# Example url = http://digital.archives.alabama.gov/utils/ajaxhelper/?CISOROOT=maps&CISOPTR=42&action=2&DMSCALE=100&DMWIDTH=512&DMHEIGHT=512&DMX=4608&DMY=2048&DMTEXT=&DMROTATE=0

mapid = '693'
scale = '100'
# width = 512
# height = '512'
x_ul = '0'
y_ul = '0'

# At the 100% zoom setting, get the dimensions of the map. I'm always going to download at 100%
#   scale.
img_width_px = 12000
img_height_px = 7875

# Plan the 512px square tiles given the image dimensions

url_base = f'http://digital.archives.alabama.gov/utils/ajaxhelper/?CISOROOT=maps&CISOPTR={mapid}&action=2&DMSCALE={scale}&DMWIDTH=512&DMHEIGHT=512&DMX={x_ul}&DMY={y_ul}&DMTEXT=&DMROTATE=0'

# Build out the grid and the urls
pass_x = range(0, img_width_px, 512)
pass_y = range(0, img_height_px, 512)

calls = []
for j in pass_y:
    for i in pass_x:
        the_url = f'http://digital.archives.alabama.gov/utils/ajaxhelper/?CISOROOT=maps&CISOPTR={mapid}&action=2&DMSCALE={scale}&DMWIDTH=512&DMHEIGHT=512&DMX={str(i)}&DMY={str(j)}&DMTEXT=&DMROTATE=0'
        calls.append(the_url)

# See this stackoverflow answer about grabbing images with
#   requests

import requests
img = requests.get(calls[1], stream=True)
if img.status_code == 200:
    with open('./file2.jpg', 'wb') as outfile:
        for chunk in img.iter_content(1024):
            outfile.write(chunk)

from PIL import Image
def merge_img(files, width, height):
    """
    Merges image tiles downloaded from AL map site into one proper image
    """
    # Open up first existing tile, get info from it
    the_old = Image.open('./file1.jpg')
    old_mode = the_old.mode

    # Use pillow to create empty image of proper dimensions
    mynew = Image.new(old_mode, (512,512))

    # Paste in the tiles
    mynew.paste(the_old, (0,0))

    # Save it out
    mynew.show()

merge_img('./file1.jpg', 512,512)
