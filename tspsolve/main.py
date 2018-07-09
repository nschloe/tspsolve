# -*- coding: utf-8 -*-
#
import numpy


def nearest_neighbor(d):
    """Classical greedy algorithm. (Start somewhere and always take the nearest item.)
    """
    n = d.shape[0]
    idx = numpy.arange(n)
    path = numpy.empty(n, dtype=int)
    mask = numpy.ones(n, dtype=bool)

    last_idx = 0
    path[0] = last_idx
    mask[last_idx] = False
    for k in range(1, n):
        last_idx = idx[mask][numpy.argmin(d[last_idx, mask])]
        path[k] = last_idx
        mask[last_idx] = False
    return path


def two_opt(d, path, verbose=False):
    """https://en.wikipedia.org/wiki/2-opt
    """
    path = numpy.array(path)

    edges = numpy.stack([path[:-1], path[1:]])
    min_path_cost = numpy.sum(d[tuple(edges)])
    n = d.shape[0]
    while True:
        found_new = False
        for i in range(n - 1):
            for k in range(i + 2, n + 1):
                new_path = numpy.concatenate([path[:i], path[i:k][::-1], path[k:]])
                edges = numpy.stack([new_path[:-1], new_path[1:]])
                path_cost = numpy.sum(d[tuple(edges)])
                if path_cost < min_path_cost:
                    if verbose:
                        print(
                            "Found better path ({} > {})".format(
                                min_path_cost, path_cost
                            )
                        )
                    path = new_path
                    min_path_cost = path_cost
                    # Go back to outmost loop
                    found_new = True
                    break
            if found_new:
                break
        if not found_new:
            break
    return path
