# -*- coding: utf-8 -*-
#
import matplotlib.pyplot as plt
import numpy

import tspsolve


def test_tspsolve():
    filename = "seagull.svg.png"
    img = plt.imread(filename)

    # Find all pixel positions where the alpha value is greater than a threshold
    threshold = 0.9999
    xy = numpy.array(numpy.where(img[:, :, 3] > threshold))

    # compute distance matrix
    dx = numpy.subtract.outer(xy[0], xy[0])
    dy = numpy.subtract.outer(xy[1], xy[1])
    d = numpy.sqrt(dx ** 2 + dy ** 2)

    path = tspsolve.greedy(d)

    plt.plot(xy[0, path], xy[1, path], '-')
    plt.show()
    return


if __name__ == "__main__":
    test_tspsolve()
