# tspsolve

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/tspsolve/master.svg)](https://circleci.com/gh/nschloe/tspsolve/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/tspsolve.svg)](https://codecov.io/gh/nschloe/tspsolve)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPi Version](https://img.shields.io/pypi/v/tspsolve.svg)](https://pypi.org/project/tspsolve)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/tspsolve.svg?logo=github&label=Stars)](https://github.com/nschloe/tspsolve)

Algorithms for the [traveling salesman problem
(TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem) in Python.

Implemented so far:

  * Nearest neighbor algorithm
    ```python
    import tspsolve

    # Create matrix of distances d
    path = tspsolve.nearest_neighbor(d)
    ```

  * [2-opt](https://en.wikipedia.org/wiki/2-opt) improvement
    ```python
    import tspsolve

    # Create matrix of distances d and an initial path
    new_path = tspsolve.two_opt(d, path, verbose=True)
    ```

For [Euclidiean
TSP](https://en.wikipedia.org/wiki/Travelling_salesman_problem#Euclidean_TSP), the
distance matrix can be computed efficiently with
```python
dx = numpy.subtract.outer(x, x)
dy = numpy.subtract.outer(y, y)
d = numpy.sqrt(dx ** 2 + dy ** 2)
```

### Installation

tspsolve is [available from the Python Package
Index](https://pypi.org/project/tspsolve/), so simply type
```
pip install -U tspsolve
```
to install or upgrade.

### Testing

To run the tspsolve unit tests, check out this repository and type
```
pytest
```

### Distribution

To create a new release

1. bump the `__version__` number,

2. publish to PyPi and GitHub:
    ```
    make publish
    ```

### License

tspsolve is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
