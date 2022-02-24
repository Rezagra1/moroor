#image proccesing
py -m pip install pillow

from PIL import Image

img = Image.open(file_directory) # open an image
we can print(img) for show image information
also img.size or img.format or img.mode


adding filter

prom PIL import Imagefilter
filterd_img = img.filter(ImageFilter.BLUR)
filterd_img.save("blure.png", 'png')#save a file with png format and blure name
#png format support imagefilter

also we have ImageFilter.SHARPEN # to get sharp an image

img.convert("L"):  make picture black&white

img.rotate(90): rotate picture 90 degree

img.resize((200,200)): resize the picture
img.thumbnail((200,200)) : resize the picture with ceeping tha aspect ratio #تناسب تصوير


img.crop((100,100,400,400)) # crop picture from that corners

