# -*- coding: utf-8 -*-
#
import numpy

import tspsolve


def test_tspsolve():
    # Find all pixel positions where the alpha value is greater than a threshold
    # filename = "seagull.svg.png"
    # img = plt.imread(filename)
    # threshold = 0.9
    # yx = numpy.array(numpy.where(img[:, :, 3] > threshold))
    # xy = yx[[1, 0]]

    numpy.random.seed(0)
    xy = numpy.random.rand(2, 10)

    # compute distance matrix
    dx = numpy.subtract.outer(xy[0], xy[0])
    dy = numpy.subtract.outer(xy[1], xy[1])
    d = numpy.sqrt(dx ** 2 + dy ** 2)

    path = tspsolve.nearest_neighbor(d).tolist()
    assert path == [0, 3, 9, 2, 1, 7, 8, 5, 6, 4]
    # import matplotlib.pyplot as plt
    # plt.plot(xy[0, path + [path[0]]], xy[1, path + [path[0]]], "-")
    # plt.axis("square")
    # plt.gca().invert_yaxis()
    # plt.show()

    path = tspsolve.two_opt(d, path, verbose=True).tolist()
    assert path == [9, 3, 0, 7, 8, 1, 2, 5, 6, 4]
    # plt.plot(xy[0, path + [path[0]]], xy[1, path + [path[0]]], "-")
    # plt.axis("square")
    # plt.gca().invert_yaxis()
    # plt.show()
    return


if __name__ == "__main__":
    test_tspsolve()
