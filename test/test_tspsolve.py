# -*- coding: utf-8 -*-
#
import matplotlib.pyplot as plt
import numpy

import tspsolve


def test_tspsolve():
    # Find all pixel positions where the alpha value is greater than a threshold
    # filename = "seagull.svg.png"
    # img = plt.imread(filename)
    # threshold = 0.9999
    # xy = numpy.array(numpy.where(img[:, :, 3] > threshold))

    xy = numpy.random.rand(2, 20)

    # compute distance matrix
    dx = numpy.subtract.outer(xy[0], xy[0])
    dy = numpy.subtract.outer(xy[1], xy[1])
    d = numpy.sqrt(dx ** 2 + dy ** 2)

    path = tspsolve.nearest_neighbor(d)
    plt.plot(xy[0, path], xy[1, path], '-')
    plt.show()

    path = tspsolve.two_opt(d, path)

    plt.plot(xy[0, path], xy[1, path], '-')
    plt.show()
    return


if __name__ == "__main__":
    test_tspsolve()
