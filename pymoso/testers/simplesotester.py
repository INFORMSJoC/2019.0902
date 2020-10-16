# MIT License

# Copyright (c) 2018 Kyle Cooper and Susan Hunter

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#!/usr/bin/env python
"""
Summary
-------
Provide the tester for Test Simple SO problem
"""
from ..problems import probsimpleso
from ..chnutils import edist


def true_g(x):
    """
    Compute the expected values of a point.

    Parameters
    ----------
    x : tuple of int
        A feasible point

    Returns
    -------
    tuple of float
        The objective values
    """
    obj1 = x[0]**2
    return (obj1,)


def get_ranx0(rng):
    """
    Uniformly sample from the feasible space.

    Parameters
    ----------
    rng : prng.MRG32k3a object

    Returns
    -------
    x0 : tuple of int
        The randomly chosen point
    """
    xr = range(-100, 101)
    x1 = rng.choice(xr)
    x0 = (x1,)
    return x0


soln = (0,)


class SimpleSOTester(object):
    """
    Store useful data for working with Test Simple SO problem.

    Attributes
    ----------
    ranorc : chnbase.Oracle class
    true_g : function
    soln : list of set of tuple of int
        The set of LES's which solve TPC locally
    get_ranx0 : function
    """
    def __init__(self):
        self.ranorc = probsimpleso.ProbSimpleSO
        self.true_g = true_g
        self.soln = soln
        self.get_ranx0 = get_ranx0

    def metric(self, eles):
        """
        Compute a metric from a simulated solution to the true solution.

        Parameters
        ----------
        eles : set of tuple of numbers
            Simulated solution

        Returns
        -------
        float
            The performance metric
        """
        point = eles.pop()
        dist = edist(point, self.soln)
        return dist
