
from PIL import ImageDraw
from PIL import Image, ImageEnhance
from PIL import ImageFont

img= Image.open("forsk-logo.png")

str1= input("Enter the Name for certifiacte")
def ReduceOpacity(im, opacity):
    """
    Returns an image with reduced opacity.
    Taken from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/362879
    """
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

im1 = ReduceOpacity(img, 0.1)
img_w, img_h = im1.size

draw = ImageDraw.Draw(im1)

select_font= ImageFont.truetype("Xerox Serif Wide Italic.ttf", size=70 )
draw.text((300,30), "Certificate of Participation",(202,1,127), font=select_font)

select_font2= ImageFont.truetype("Xoxoxa.ttf", size=40 )
draw.text((450,140), "This is the certification for the projectX ",(20,190,27), font=select_font2)

draw.text((600,210), "Is Given To",(20,192,27), font=select_font2)

select_font3= ImageFont.truetype("Xerox Serif Wide Italic.ttf", size=50 )
draw.text((500,300), str1 ,(201,19,27), font=select_font3)

draw.text((250,430), "Warm Regards" ,(20,190,27), font=select_font2)


select_font3= ImageFont.truetype("Xerox Serif Wide Italic.ttf", size=30 )
draw.text((250,500), "Forsk Technologies Pvt. ltd." ,(20,190,27), font=select_font3)

img2= Image.open("images.png")

im1.paste(img2 ,(1009,400))

img3= Image.open("sign.png")

im1.paste(img3 ,(250,550))



im1.save("certi.png", "PNG", resolution=100.0)

