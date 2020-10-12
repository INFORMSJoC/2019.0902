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

"""Display all solvers, problems, and test problems"""

from .basecomm import *
from inspect import getmembers, isclass, ismodule


class ListItems(BaseComm):
    """
    Implements the CLI command listitems.

    See also
    --------
    BaseComm
    """
    def run(self):
        """
        Print the list of solvers, problems, and testers that are
        included in PyMOSO.
        """
        ## list of problem classes
        probclasses = getmembers(problems, isclass)
        ## list of solver classes
        solvclasses = getmembers(solvers, isclass)
        ## list of classes with test problems
        testclasses = getmembers(testers, isclass)
        ## print the solvers and their docstrings
        sstr = 'Solver'
        sstrund = '************************'
        descstr = 'Description'
        print(f'\n{sstr:30} {descstr:30}')
        print(f'{sstrund:30} {sstrund:30}')
        for s0, s1 in solvclasses:
            docstr = s1.__doc__.split('\n')[1].strip()
            print(f'{s0:30} {docstr:30}')
        ## print the problems, their docstrings, and determine if they have a
        ##      tester
        pstr = 'Problems'
        tstr = 'Test Name (if available)'
        print(f'\n{pstr:30} {descstr:60} {tstr:30}')
        print(f'{sstrund:30} {sstrund:60} {sstrund:30}')
        for p0, p1 in probclasses:
            ctlist = [t[0] for t in testclasses if issubclass(t[1]().ranorc, p1)]
            p2 = ctlist[0] if ctlist else ''
            docstr = p1.__doc__.split('\n')[1].strip()
            print(f'{p0:30} {docstr:60} {p2:30}')
