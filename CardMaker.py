from PIL import Image, ImageDraw, ImageFont
import os
import re

# Your Card Infos
Title       = "Fire Dragon"
Attribute   = "Void"
Level       = 6
Type        = "[Dragon / Effect]"
Description = "The Ultimate Power"
Attack      = "2400"
Defense     = "2000"

souce_path = "img/"
source_card = "Card-effect.png"
source_image = souce_path + source_card 

level_image = "Level-Red.png"
level_file = Image.open(souce_path + level_image)
level_file.resize((8,8),Image.ANTIALIAS)

# Size must be 320x320
image_card = "firedragon.jpg"

print("Source Image: " + source_card)
print("Card Image: " + image_card + "\n")

txt_color = "black"

fontsize = 48
fontsize1 = 15
fontsize2 = 15
fontsize3 = 20

fontfile1 = "fonts/Yu-Gi-Oh! Matrix Regular Small Caps 2.ttf"
fontfile2 = "fonts/Matrix-Bold.otf"
fontfile3 = "fonts\Yu-Gi-Oh! ITC Stone Serif Small Caps Bold.ttf"
fontfile4 = "fonts\Yu-Gi-Oh! Matrix Book.ttf"

i = 0
area_x = 380
area_y = 76

border = True
border_color = "black" 
border_size = 5

output_dir = "output"
text_alignment = "left"

img_fraction = 1

line_height = 0
line_width = 0

card_image = Image.open(souce_path + image_card)
card = card_image.resize((320,320),Image.ANTIALIAS)
image = Image.open(source_image).convert('RGBA')
image_with_text = Image.new('RGBA', image.size, (255,255,255,0))
draw = ImageDraw.Draw(image_with_text)

title_x = 0
title_y = 0

type_x = 0
type_y = 0

desc_x = 0
desc_y = 0

font = ImageFont.truetype("arial.ttf", fontsize)

image_width = image.size[0]
image_height = image.size[1]

print("Image height: "+str(image_height))
print("Image width: "+str(image_width) + "\n")

if Title.find(os.linesep) >= 0:
    print("New line found. Checking longest line width")
    lines = Title.split(os.linesep)
    for line in lines:
        if(font.getsize(line)[0] > line_width):
            line_width = font.getsize(line)[0]
        line_height += font.getsize(line)[1]
else:    
    line_width = font.getsize(Title)[0]
    line_height = font.getsize(Title)[1]

title_x = 30
title_y = 28 

type_x = 35
type_y = 463

desc_x = 35
desc_y = 483

atk_x = 265
atk_y = 559

def_x = 350
def_y = 559


fontsize -= 1

font = ImageFont.truetype(fontfile1, fontsize)
font1 = ImageFont.truetype(fontfile3, fontsize1)
font2 = ImageFont.truetype(fontfile1, fontsize2)
font3 = ImageFont.truetype(fontfile1, fontsize3)

print("Final font size: ",fontsize)

draw.text((title_x, title_y), Title, font=font, fill=txt_color, align=text_alignment)
draw.text((type_x, type_y), Type, font=font1, fill=txt_color, align=text_alignment)
draw.text((desc_x, desc_y), Description, font=font2, fill=txt_color, align=text_alignment)
draw.text((atk_x, atk_y), Attack, font=font3, fill=txt_color, align=text_alignment)
draw.text((def_x, def_y), Defense, font=font3, fill=txt_color, align=text_alignment)


for i in range(Level):
    area_x = area_x - 27
    area = area_x, area_y
    image_with_text.paste(level_file, area) 

if Attribute == "Void":
    attribute_image = "Void.png"
    attribute_path = Image.open(souce_path + attribute_image)
    area_x = 355
    area_y = 29
    area = area_x, area_y
    image_with_text.paste(attribute_path, area)
elif Attribute == "Time":
    attribute_image = "Time.png"
    attribute_path = Image.open(souce_path + attribute_image)
    area_x = 355
    area_y = 29
    area = area_x, area_y
    image_with_text.paste(attribute_path, area)  

area = 51, 113 

image_with_text.paste(card, area)

out = Image.alpha_composite(image, image_with_text)

out.show()

file_name = re.sub(r"[^a-zA-Z0-9 | ]*","", Title).replace(" ", "_")+'.png'
out.save(os.path.join(output_dir, file_name))

