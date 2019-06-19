from skimage import color, io

origin_file = input('Image file name: ')
img = color.rgb2gray(io.imread(origin_file))
print(img)
w, h = img.shape
io.imsave('greyed_'+origin_file+'.png', img)
# io.show()
