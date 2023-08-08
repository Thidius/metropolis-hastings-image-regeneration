# libraries
import matplotlib.pyplot as plt
import numpy as np
import cv2

# reading image
inputimage = cv2.imread(r"C:\Users\username\Desktop\image.png")
dimensions = list(inputimage.shape)
# fetching image dimensions
imwidth = dimensions[0]
imheight = dimensions[1]

num = 10000000  # no_of_samples


def image_to_matrix(image, width, height):
    'converting color image to BnW image, then creating matrix T from position of each pixel'
    'T is then returned as a normalized probability distribution over width x height'
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    T = cv2.bitwise_not(gray_image)
    return np.array(T) / (255 * width * height)


prop_distribution = image_to_matrix(inputimage, imwidth, imheight)  # proposed distribution


def im_posterior_func(x):
    return prop_distribution.item((int(np.floor(x[0])), int(np.floor(x[1]))))


def sampler(posterior_func, Np, width, height, no_of_samples=4, start_position=None):
    'Metropolis-hastings-algorithm'
    # starting parameter position
    if start_position == None:
        current_position = [0, 0]
    else:
        assert len(start_position) == Np, "start_position is not correct length"
        current_position = [0, 0]

    samples = [list(current_position)]
    print(current_position)
    # fixed covariance matrix

    # Sampling loop
    for i in range(no_of_samples):
        # suggest new position
        x = np.random.uniform(low=0, high=height)
        y = np.random.uniform(low=0, high=width)
        X_n = [x, y]

        # Compute log posteriors of current and proposed position
        cur_posterior = posterior_func(current_position)
        prop_posterior = posterior_func(X_n)

        # Acceptance probability
        A = 1
        if cur_posterior == 0:
            current_position = X_n
            samples.append(list(current_position))
            continue
        if prop_posterior / cur_posterior < 1:
            A = prop_posterior / cur_posterior

        # Possibly update position
        if A >= 1:
            current_position = X_n
        else:
            u = np.random.uniform(0, 1)
            if A >= u:
                current_position = X_n

        # Extend the samples array vertically for each iteration
        samples.append(list(current_position))
    return np.array(samples)


samples = sampler(im_posterior_func, 2, imwidth, imheight, no_of_samples=num, start_position=None)  # position samples
xs, ys = samples.T

plt.hist2d(ys, -xs, bins=[np.arange(0, imheight, 1), np.arange(-imwidth, 0, 1)], cmap=plt.cm.binary)
plt.show()
