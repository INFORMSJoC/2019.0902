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
Provide an implementation of R-SPLINE for users needing a 
single-objective simulation optimization solver. 
"""
from ..chnbase import RASolver
import sys


class RSPLINE(RASolver):
    """
    R-SPLINE solver for single-objective simulation optimization.
    
    Parameters
    ----------
    orc : chnbase.Oracle object
	kwargs : dict
	
	See also
	--------
	chnbase.RASolver
    """

    def __init__(self, orc, **kwargs):
        if orc.num_obj > 1:
            print('--* Warning: R-SPLINE operates on single objective problems!')
            print('--* Continuing: R-SPLINE will optimize only the first objective.')
        super().__init__(orc, **kwargs)

    def spsolve(self, warm_start):
        """
        Use SPLINE to solve the sample path problem. 
        
        Parameters
        ----------
        warm_start : set of tuple of int
			For RSPLINE, this is a singleton set
		
		Returns
		-------
		set of tuple of int
			For RSPLINE, this is a singleton set containing the sample
			path minimizer
        """
        # warm_start is a singleton set, so extract the item
        warm_start = self.upsample(warm_start)
        if not warm_start:
            print('--* R-SPLINE Error: Empty warm start. Is x0 feasible?')
            print('--* Aborting. ')
            sys.exit()
        ws = warm_start.pop()
        _, xmin, _, _ = self.spline(ws)
        # return a singleton set
        return {xmin}
