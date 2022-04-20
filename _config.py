from PIL import ImageFont

souce_path   = "img/"
path_cards   = "cards/"
path_type    = "type/"
path_lvl     = "lvl/"
path_cardimg = "cardimages/"
path_rarity  = "rarity/"
path_extras  = "extras/"
path_linkarrow  = "linkarrow/"
path_symbol  = "symbols/"

i = 0
area_x = 380
area_y = 76

fontsize = 48
fontsize1 = 15
fontsize2 = 15
fontsize3 = 20
fontsize4 = 17

fontfile1 = "fonts/Yu-Gi-Oh! Matrix Regular Small Caps 2.ttf"
fontfile2 = "fonts/Matrix-Bold.otf"
fontfile3 = "fonts\Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf"
fontfile4 = "fonts\Yu-Gi-Oh! Matrix Book.ttf"

title_x = 30
title_y = 28 
type_x = 35
type_y = 463
auflage_x = 45
auflage_y = 440
card_id_x = 300
card_id_y = 440
desc_x = 35
desc_y = 483
atk_x = 265
atk_y = 559
def_x = 350
def_y = 559
serial_x = 20
serial_y = 583
fontsize -= 1

font = ImageFont.truetype(fontfile1, fontsize)
font1 = ImageFont.truetype(fontfile3, fontsize1)
font2 = ImageFont.truetype(fontfile1, fontsize2)
font3 = ImageFont.truetype(fontfile1, fontsize3)
font4 = ImageFont.truetype(fontfile1, fontsize4)

title_color = "black"
desc_color  = "black"

title_color_xyz = "white"
desc_color_xyz  = "black"

border = True
border_color = "black" 
border_size = 5

output_dir = "output"
text_alignment = "left"

img_fraction = 1

line_height = 0
line_width = 0