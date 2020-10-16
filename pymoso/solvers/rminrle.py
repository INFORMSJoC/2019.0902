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
Provide an implementation of R-MinRLE for users needing a
multi-objective simulation optimization solver.
"""
from ..chnbase import RLESolver
import sys


class RMINRLE(RLESolver):
    """
    A solver using R-MinRLE for integer-ordered MOSO.

    See also
    --------
    chnbase.RLESolver
    """

    def accel(self, warm_start):
        """
        Compute a candidate ALES. RLESolvers require that this function
        is implemented.

        Parameters
        ----------
        warm_start : set of tuple of int

        Returns
        -------
        set of tuple of int
        """
        if not warm_start:
            print('--* R-MinRLE Error: No feasible warm start. Is x0 feasible?')
            print('--* Aborting.')
            sys.exit()
        return self.get_min(warm_start)
