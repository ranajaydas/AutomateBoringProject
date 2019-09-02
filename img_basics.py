from PIL import ImageColor
from PIL import Image

# Get the RGBA values for the colour CornFlowerBLue
print('RGBA values:', ImageColor.getcolor('CornFlowerBlue', 'RGBA'))

# Open an image file
filename = 'img_zophie.png'
cat_image = Image.open(filename)
print('Image size of {} = {}'.format(cat_image.filename, cat_image.size))

# Save file as .jpg
cat_image.save('img_zophie.jpg')
