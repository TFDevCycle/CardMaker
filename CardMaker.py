from PIL import Image, ImageDraw, ImageFont
import os
import re

souce_path = "img/"
source_card = "Card.png"
source_image = souce_path + source_card 

level_image = "Level.png"
level_file = Image.open(souce_path + level_image)
level_file.resize((8,8),Image.ANTIALIAS)

# Size must be 225x225
image_card = "Placeholder.png"

card_image = Image.open(souce_path + image_card)

print("Source Image: " + source_card)
print("Card Image: " + image_card + "\n")

Title       = "Template"
Level       = 12
Type        = "[Type1 / Type2]"
Description = "This is a Template, for this State"
Attack      = 0
Defense     = 0

txt_color = "black"

fontsize = 36
fontsize1 = 16
fontsize2 = 12

fontfile1 = "fonts/Matrix-Bold.otf"
fontfile2 = "fonts/Yu-Gi-Oh! Matrix Book.ttf"

i = 0
area_x = 255
area_y = 67

border = True
border_color = "black" 
border_size = 5

output_dir = "output"
text_alignment = "left"

img_fraction = 1

line_height = 0
line_width = 0

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

title_x = 20
title_y = 28 

type_x = 25
type_y = 340

desc_x = 25
desc_y = 360

fontsize -= 1

font = ImageFont.truetype(fontfile1, fontsize)
font1 = ImageFont.truetype(fontfile1, fontsize1)
font2 = ImageFont.truetype(fontfile2, fontsize2)

print("Final font size: ",fontsize)

draw.text((title_x, title_y), Title, font=font, fill=txt_color, align=text_alignment)
draw.text((type_x, type_y), Type, font=font1, fill=txt_color, align=text_alignment)
draw.text((desc_x, desc_y), Description, font=font2, fill=txt_color, align=text_alignment)

for i in range(Level):
    area_x = area_x - 16
    area = area_x, area_y
    image_with_text.paste(level_file, area) 

area = 24, 90 
image_with_text.paste(card_image, area)

out = Image.alpha_composite(image, image_with_text)

out.show()

file_name = re.sub(r"[^a-zA-Z0-9 | ]*","", Title).replace(" ", "_")+'.png'
out.save(os.path.join(output_dir, file_name))

