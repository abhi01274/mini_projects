from PIL import Image

im1 = Image.open('certi.png')
im2 = Image.open('forsk-logo.png')
im3 = Image.open('i_card.png')
im4 = Image.open('document.png')
im5 = Image.open('blank-page.png')

def changeImageSize(maxWidth, 
                    maxHeight, 
                    image):
    
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage

image3 = changeImageSize(1250, 650, im1)
image4 = changeImageSize(1250, 650, im2)
image5 = changeImageSize(1250, 650, im3)
image6 = changeImageSize(1250, 650, im4)
image7 = changeImageSize(1250, 650, im5)
image7.save("gif_program.gif", save_all=True, append_images=[im1,im2, im3, im4], duration=100, loop=0)