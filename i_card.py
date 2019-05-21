from PIL import ImageDraw
from PIL import Image, ImageEnhance
from PIL import ImageFont



img= Image.open("forsk-logo.png")

str_name = input("enter the name")
str_coll = input("enter the college name")
str_branch = input("enter the branch")
str_batch = input("enter the batch")


def ReduceOpacity(im, opacity):
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

img1 = ReduceOpacity(img, 0.1)
draw = ImageDraw.Draw(img1)

select_font3= ImageFont.truetype("Xerox Serif Wide Italic.ttf", size=60 )
draw.text((350,100), "Forsk Technologies pvt. ltd." ,(169,90,90), font=select_font3)

img2= Image.open("images.png")
img1.paste(img2 ,(80,10))


select_font= ImageFont.truetype("Xerox Serif Wide Italic.ttf", size=40 )
draw.text((150,250), "Name :" ,(202,190,27), font=select_font)
draw.text((400,250), str_name ,(111,49,49), font=select_font)


draw.text((150,330), "College :" ,(202,190,27), font=select_font)
draw.text((400,330), str_coll ,(111,49,49), font=select_font)


draw.text((150,410), "Branch :" ,(202,190,27), font=select_font)
draw.text((400,410), str_branch ,(111,49,49), font=select_font)


draw.text((150,490), "Batch :" ,(202,190,27), font=select_font)
draw.text((400,490), str_batch ,(111,49,49), font=select_font)



select_font2= ImageFont.truetype("Xerox Serif Wide Italic.ttf", size=30 )
draw.text((1009,450), "Signature" ,(0,10,2), font=select_font2)

img2= Image.open("sign.png")
img1.paste(img2 ,(990,500))

img2= Image.open("passphoto.png")
img1.paste(img2 ,(1009,220))


img1.save("i_card.png", "PNG", resolution=100.0)
