
from PIL import Image

# Function to change the image size
def changeImageSize(maxWidth, 
                    maxHeight, 
                    image):
    
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage
#str1= input("enter the image path >> ")
# Take two images for blending them together   
image1 = Image.open("document.png")
image2 = Image.open("forsk-logo.png")

# Make the images of uniform size
image3 = changeImageSize(1200, 600, image1)
image4 = changeImageSize(1200, 600, image2)

# Make sure images got an alpha channel
image5 = image3.convert("RGBA")
image6 = image4.convert("RGBA")


# alpha-blend the images with varying values of alpha
alphaBlended1 = Image.blend(image5, image6, alpha=.4)

# Display the alpha-blended images
alphaBlended1.show()
