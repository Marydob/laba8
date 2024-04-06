import ImageFilter, ImageDraw, ImageFont
#1
from PIL import Image
image = Image.open('др.jpg')
image.crop((120, 40, 600, 420)).show()
#2
from PIL import Image
try:
    image = Image.open("Новый год.jpg")
    image1 = Image.open("Пасха.jpg")
    image2 = Image.open("Рождество.jpg")
    b = {"Новый год": image, "Рождество": image2, "Пасха": image1}
    a = input("введите праздник (на русском языке): ")
    c=a.title()
    if c == "Новый год":
        b.get("Новый год")
    elif c == "Рождество":
        b.get("Рождество")
    elif c == "Пасха":
        b.get("Пасха")
    img = b[c]
    img.show()
except KeyError:
    print("для этого праздника нет картинки")
#3
img = Image.open("др.jpg")
imgcrop = img.crop((120, 40, 600, 420))
draw = ImageDraw.Draw(imgcrop)
fontpath1 = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
fontpath2 = "System/Library/Fonts/Supplemental/Times New Roman.ttf"
font1 = ImageFont.truetype(fontpath1, 29)
font2 = ImageFont.truetype(fontpath2, 24)
name = input("Введите имя для поздравления: ")
c=name.title()
text1 = c
text2="   ,поздравляю!"
draw.text((130, 80), text1, font=font1, fill="blue",)
draw.text((200, 90), text2, font=font2, fill="green")
imgcrop.show()
imgcrop.save("res.png")