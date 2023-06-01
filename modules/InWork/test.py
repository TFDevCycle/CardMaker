from string import ascii_letters
from PIL import Image, ImageFont, ImageDraw
import textwrap

# Open image
img = Image.open(fp='img\cards\Card-normal.png', mode='r')
# Load custom font
font = ImageFont.truetype(font='fonts\Yu-Gi-Oh! Matrix Book.ttf', size=14)
# Create DrawText object
draw = ImageDraw.Draw(im=img)
# Define our text
text = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."""

avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
max_char_count = int(img.size[0] * .8 / avg_char_width)
text = textwrap.fill(text=text, width=max_char_count, break_long_words=True)
print(text)
# Add text to the image
draw.text(xy=(img.size[0]/2, img.size[1] / 2), text=text, font=font, fill='#000000', anchor='mm')
# view the result
img.show()