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
Provides implementation of the Test Problem A Oracle for use in PyMOSO.
"""
from ..chnbase import Oracle


class ProbTPA(Oracle):
    """
    An Oracle that simulates Test Problem A.

    Attributes
    ----------
    num_obj : int, 2
    dim : int, 2

    Parameters
    ----------
    rng : prng.MRG32k3a object

    See also
    --------
    chnbase.Oracle
    """
    def __init__(self, rng):
        self.num_obj = 2
        self.dim = 2
        super().__init__(rng)

    def g(self, x, rng):
        """
        Simulates one replication. PyMOSO requires that all valid
        Oracles implement an Oracle.g.

        Parameters
        ----------
        x : tuple of int
        rng : prng.MRG32k3a object

        Returns
        -------
        isfeas : bool
        tuple of float
            simulated objective values
        """
        xr = range(0, 51)
        isfeas = True
        for xi in x:
            if not xi in xr:
                isfeas = False
        obj1 = None
        obj2 = None
        if isfeas:
            z1 = rng.normalvariate(0, 1)
            z2 = rng.normalvariate(0, 1)
            z3 = rng.normalvariate(0, 1)
            xi = [z1**2, z2**2, z3**2]
            obj1 = (x[0]/10.0 - 2.0*xi[0])**2 + (x[1]/10.0 - xi[1])**2
            obj2 = (x[0]**2)/100.0 + (x[1]/10.0 - 2.0*xi[2])**2
        return isfeas, (obj1, obj2)
