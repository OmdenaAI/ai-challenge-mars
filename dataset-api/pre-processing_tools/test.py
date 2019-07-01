# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:29:41 2019

@author: SEBASTIAN LAVERDE
"""

import cv2
from PIL import Image
import matplotlib.pyplot as plt
import tools
import numpy as np
from scipy import ndimage
#from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
#%%
#images
#PSP_001414_1780_RED_img_row_33792_col_12288_w_1024_h_1024_x_0_y_0
#PSP_001414_1780_RED_img_row_32768_col_15360_w_1024_h_1024_x_0_y_0
#PSP_001414_1780_RED_img_row_32768_col_14336_w_1024_h_1024_x_0_y_0
#PSP_001414_1780_RED_img_row_32768_col_13312_w_1024_h_1024_x_0_y_0
#PSP_001414_1780_RED_img_row_9216_col_11264_w_1024_h_1024_x_0_y_0
#chameleon
#parachute

path = "C:/Users/SEBASTIAN LAVERDE/Documents/Unterlagen/SoSe2019/mars/python/1024x1024/"
img = cv2.imread(path + 'chameleon.jpg')
im = Image.open(path + 'chameleon.jpg')
np_im = np.array(im)

sharpened = tools.sharp(np_im, 3)
stretched = tools.stretch_8bit(np_im)
enhanced = tools.stretch_8bit(sharpened)

#im.save('output/original.jpg')
#cv2.imwrite('output/enhanced.jpg', enhanced)
#cv2.imwrite('output/stretched.jpg', stretched)
#cv2.imwrite('output/sharpened.jpg', sharpened)

#_________________ create function with this _________________________
list_im = ['output/original.jpg','output/sharpened.jpg','output/stretched.jpg','output/enhanced.jpg']
imgs    = [ Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# save that beautiful picture
imgs_comb = Image.fromarray( imgs_comb)
#imgs_comb.save( 'test_hor.jpg' )    

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = Image.fromarray( imgs_comb)
#imgs_comb.save( 'test_ver.jpg' )
#_______________________________________________________________________

#%%
def concatenate(imgflnames): #file name, Image.fromarray for cv2 or numpy. Error: ValueError: cannot resize an array that references or is referenced
                                #by another array in this way.
                                #Use the np.resize function or refcheck=False

    images = [cv2.imread(i) for i in imgflnames] #for loop one line for lists
    print("\n", type(images), "\n")
    print("lenght: ", len(images))
    print("dimension 0: ", images[0].ndim)
    print("dimension 1: ", images[1].ndim)
    min_shape = sorted( [(np.sum(i.shape), i.shape ) for i in images])[0][1]
    print(min_shape)
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in images ) )
    imgs_comb = Image.fromarray( imgs_comb)
    return imgs_comb

def concatenate2(imgflnames): #file name, dimensionality problem: all the input arrays must have same number of dimensions
    images = [Image.open(i) for i in imgflnames] #for loop one line for lists
    print("\n", type(images), "\n")
    print("lenght: ", len(images))
    print("dimension 0: ", images[0].size)
    print("dimension 1: ", images[1].size)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in images])[0][1]
    print(min_shape)
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in images ) )
    imgs_comb = Image.fromarray( imgs_comb)
    return imgs_comb
#%%
list_im = ['output/enhancement/original.jpg','output/enhancement/enhanced.jpg']
imgs    = [ Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack((np.asarray(i.resize(min_shape) ) for i in imgs))

# save that beautiful picture
imgs_comb = Image.fromarray( imgs_comb)
plt.imshow(imgs_comb)
plt.show()

two = concatenate(list_im)
plt.imshow(two)
plt.show()
#imgs_comb.save( 'orginal_final.jpg' )

#tools.augment_random(img, 20)

#augmented = tools.augment_simple(img)
#cv2.imwrite("output/chameleon.jpg", img)
#cv2.imwrite("output/flipped.jpg", augmented[0])
#cv2.imwrite("output/rolled.jpg", augmented[1])
#cv2.imwrite("output/rotated90.jpg", augmented[2])
#cv2.imwrite("output/rotated180.jpg", augmented[3])
#%% register_image(img)
#try with chameleon and rotate 27.5
#try resize again
img = cv2.imread('resized.jpg')
plt.imshow(img)
plt.show()
#img = cv2.imread('resized.jpg')

ref = tools.generate_template(img)
plt.imshow(ref)
plt.show()

ref = tools.generate_template(img, [255,0,0])
plt.imshow(ref)
plt.show()
#%%
img_list = ['output/enhancement/original.jpg','output/enhancement/enhanced.jpg', 'bilinear_template.jpg'] #dimensionality problem
images = [Image.open(i) for i in img_list]
for i in images:
    print (i.size)
    print (type(i))

concatenated = concatenate(img_list)
plt.imshow(concatenated)
plt.show()

#%%
list_im = 'output/enhancement/original.jpg'
imgs    = Image.open(list_im)
imgs2 = cv2.imread(list_im)
print(imgs.size)
print("PIL Image type: ", type(imgs))
print(imgs2.shape)
print("CV2read imgs2 type: ", type(imgs2))

list_im = 'output/enhancement/enhanced.jpg'
imgs    = Image.open(list_im)
imgs2 = cv2.imread(list_im)
print("\n",imgs.size)
print("PIL Image type: ", type(imgs))
print(imgs2.shape)
print("CV2read imgs2 type: ", type(imgs2))

list_im = 'bilinear_template.jpg'
imgs    = Image.open(list_im)
imgs2 = cv2.imread(list_im)
print("\n",imgs.size)
print("PIL Image type: ", type(imgs))
print(imgs2.shape)
print("CV2read imgs2 type: ", type(imgs2))
#%%
#img_rotated = ndimage.rotate(img, 27)
#cv2.imwrite('output/rotated_chameleon27.jpg', img_rotated)

#transformations = tools.register_image(img, ref = 'bilinear_template.jpg') #best result so far
transformations = tools.register_image(img)
transformations = tools.register_image(img ,'solid')
transformations = tools.register_image(img, ref = 'bilinear_template.jpg') #homography function could have the same
#%%
cv2.imwrite('output/translation_resized_bilinear.jpg', transformations[0])
cv2.imwrite('output/rotation_resized_bilinear.jpg', transformations[1])
cv2.imwrite('output/scaled_rotation_resized_bilinear.jpg', transformations[2])
cv2.imwrite('output/affine_resized_bilinear.jpg', transformations[3])
cv2.imwrite('output/bilinear_resized_bilinear.jpg', transformations[4])

#%%
def random_color(low=5, high=250):
    color = [np.random.randint(5,250),np.random.randint(5,250),np.random.randint(5,250)]
    return color
#%%
def generate_template():
    ref = np.zeros((img.shape[0],img.shape[1],3), dtype = 'uint8')
    margin = int(min(img.shape[0], img.shape[1])/10)
    #for 200,200 to shape[1]-200 shape[0]-200 generate random
    for i in range(0,img.shape[1]-2*margin):
        i+=1
        for j in range(0,img.shape[0]-2*margin):
            ref[margin+i,margin+j,:] = random_color()
            j+=1
    return ref
        

#%%
plt.imshow(ref)
plt.show()
cv2.imwrite('test_template.jpg', ref)