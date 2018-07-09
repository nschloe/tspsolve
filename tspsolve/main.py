# -*- coding: utf-8 -*-
#
import matplotlib.pyplot as plt
import numpy


def greedy(d):
    """
    """
    # Classical greedy TSP
    n = d.shape[0]
    idx = numpy.arange(n)
    last_idx = 0
    path = numpy.empty(n, dtype=int)
    mask = numpy.ones(n, dtype=bool)
    path[0] = last_idx
    mask[last_idx] = False
    for k in range(1, n):
        # Exclude the diagonal, too
        last_idx = idx[mask][numpy.argmin(d[last_idx, mask])]
        path[k] = last_idx
        mask[last_idx] = False
    return path
