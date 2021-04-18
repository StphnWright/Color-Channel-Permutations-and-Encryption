"""
Using matplotlib and numpy to process and modify source image data.

The function imageshow enhances the source images for use on a MacBook
Pro, while rgb_ints_example produces red, purple, and green diagnol
squares over a black background. Onechannel produces a new pattern that
contains only red, green, or blue channels of the source image while
permutecolorchannels swaps the color channels and restores the correct
color components for the campus image with its colors permuted. Decrypt
returns a noisy image to its original state by XORing the image key. 
"""

import numpy as np
import matplotlib.pyplot as plt


def imageshow(img, dpi = 200):
    if dpi > 0:
        F = plt.gcf()
        F.set_dpi(dpi)
    plt.imshow(img)


def rgb_ints_example():
    red, green, blue = range(3)
    img = np.zeros((150, 150, 3), dtype=np.uint8)
    
    for x in range(50):
        for y in range(50):
            img[x, y, red] = 255  # red pixels
            img[x + 50, y + 50,:] = (128, 0, 128)  # purple pixels
            img[x + 100, y + 100, green] = 255  # green pixels
    
    return img


plt.imshow(rgb_ints_example())


def onechannel(pattern, rgb):
    filtered = np.copy(pattern)
    
    for y in range(pattern.shape[0]):
        for x in range(pattern.shape[1]):
            if rgb == 0:
                filtered[y, x, 0] = pattern[y, x, 0]
                filtered[y, x, 1] = 0
                filtered[y, x, 2] = 0
            elif rgb == 1:
                filtered[y, x, 0] = 0
                filtered[y, x, 1] = pattern[y, x, 1]
                filtered[y, x, 2] = 0
            else:
                filtered[y, x, 0] = 0
                filtered[y, x, 1] = 0
                filtered[y, x, 2] = pattern[y, x, 2]

    return filtered


def permutecolorchannels(img, perm):
    filtered = np.copy(img)
    
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            filtered[y, x, perm[0]] = img[y, x, 0]
            filtered[y, x, perm[1]] = img[y, x, 1]
            filtered[y, x, perm[2]] = img[y, x, 2]
    
    return filtered


def decrypt(image, key):
    filtered = np.copy(image)
    
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            red = image[y, x, 0] ^ key[x]
            green = image[y, x, 1] ^ key[x]
            blue = image[y, x, 2] ^ key[x]
            filtered[y, x,:] = (red, green, blue)
    
    return filtered


def main():
    
    pattern = plt.imread('pattern.png')
    permcolors = plt.imread('permcolors.jpg')
    secret = plt.imread('secret.bmp')
    key = np.load('key.npy')
    
    plt.imshow(onechannel(pattern, 0))
    plt.show()
    plt.imshow(onechannel(pattern, 1))
    plt.show()
    plt.imshow(onechannel(pattern, 2))
    plt.show()
    plt.imshow(permutecolorchannels(pattern, [1, 0, 2]))
    plt.show()
    plt.imshow(permutecolorchannels(pattern, [2, 0, 1]))
    plt.show()
    plt.imshow(permutecolorchannels(permcolors, [1, 2, 0]))
    plt.show()
    plt.imshow(decrypt(secret, key))


if __name__ == '__main__':
    main()
