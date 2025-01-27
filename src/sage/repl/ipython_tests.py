# sage_setup: distribution = sagemath-repl
'''
Tests for the IPython integration

First, test the pinfo magic for Python code. This is what IPython
calls when you ask for the single-questionmark help, like `foo?` ::

    sage: from sage.repl.interpreter import get_test_shell
    sage: shell = get_test_shell()
    sage: shell.run_cell(u'from sage.repl.ipython_tests import dummy')
    sage: shell.run_cell(u'%pinfo dummy')
    Signature:      dummy(argument, optional=None)
    Docstring:
       Dummy Docstring Title
    <BLANKLINE>
       Dummy docstring explanation.
    <BLANKLINE>
       INPUT:
    <BLANKLINE>
       ... "argument" -- anything. Dummy argument.
    <BLANKLINE>
       ... "optional" -- anything (optional). Dummy optional.
    <BLANKLINE>
       EXAMPLES...
    <BLANKLINE>
    ...
    Init docstring: ...ee help(type(...)) for...signature...
    File:           .../sage/repl/ipython_tests.py
    Type:           function

Next, test the pinfo magic for Cython code::

    sage: from sage.repl.interpreter import get_test_shell
    sage: shell = get_test_shell()
    sage: shell.run_cell(u'from sage.tests.stl_vector import stl_int_vector')
    sage: shell.run_cell(u'%pinfo stl_int_vector')
    ...
       Example class wrapping an STL vector
    <BLANKLINE>
       EXAMPLES...
    <BLANKLINE>
    ...
    Init docstring: ...ee help(type(...)) for...signature...
    File:           .../sage/tests/stl_vector.pyx
    Type:           type
    ...

Next, test the ``pinfo`` magic for ``R`` interface code, see :issue:`26906`::

    sage: from sage.repl.interpreter import get_test_shell   # optional - rpy2
    sage: shell = get_test_shell()                           # optional - rpy2
    sage: shell.run_cell(u'%pinfo r.lm')                     # optional - rpy2
    Signature:       r.lm(...*args, **kwds)
    ...
    String form:     lm
    File:            .../sage/interfaces/r.py
    Docstring:
    title
    *****
    <BLANKLINE>
    Fitting Linear Models
    ...

Next, test the pinfo2 magic for Python code. This is what IPython
calls when you ask for the double-questionmark help, like `foo??` ::

    sage: from sage.repl.interpreter import get_test_shell
    sage: shell = get_test_shell()
    sage: shell.run_cell(u'from sage.repl.ipython_tests import dummy')
    sage: shell.run_cell(u'%pinfo2 dummy')
    Signature: dummy(argument, optional=None)
    ...
    Source:
    def dummy(argument, optional=None):
        """
        Dummy Docstring Title
    <BLANKLINE>
        Dummy docstring explanation.
    <BLANKLINE>
        INPUT:
    <BLANKLINE>
        - ``argument`` -- anything. Dummy argument.
    <BLANKLINE>
        - ``optional`` -- anything (optional). Dummy optional.
    <BLANKLINE>
        EXAMPLES::
    <BLANKLINE>
        ...
        """
        return 'Source code would be here'
    File:      .../sage/repl/ipython_tests.py
    Type:      function

Next, test the pinfo2 magic for Cython code::

    sage: from sage.repl.interpreter import get_test_shell
    sage: shell = get_test_shell()
    sage: shell.run_cell(u'from sage.tests.stl_vector import stl_int_vector')
    sage: shell.run_cell(u'%pinfo2 stl_int_vector')
    ...
    cdef class stl_int_vector(SageObject):
        """
        Example class wrapping an STL vector
    <BLANKLINE>
        EXAMPLES::
    <BLANKLINE>
    ...
        """
    <BLANKLINE>
        cdef vector[int] *data
        cdef string *name
    <BLANKLINE>
        def __cinit__(self):
            """
            The Cython constructor.
    <BLANKLINE>
            EXAMPLES::
    <BLANKLINE>
    ...
    File:   .../sage/tests/stl_vector.pyx
    Type:   type
    ...

Next, test the ``pinfo2`` magic for ``R`` interface code, see :issue:`26906`::

    sage: from sage.repl.interpreter import get_test_shell   # optional - rpy2
    sage: shell = get_test_shell()                           # optional - rpy2
    sage: shell.run_cell(u'%pinfo2 r.lm')                    # optional - rpy2
    Signature:       r.lm(...*args, **kwds)
    ...
    String form:     lm
    File:            .../sage/interfaces/r.py
    Source:
    function (formula, data, subset, weights, na.action, method = "qr",
    ...

Test that there are no warnings being ignored internally::

    sage: import warnings
    sage: warnings.simplefilter('error');  get_test_shell()
    <sage.repl.interpreter.SageTestShell object at 0x...>
'''


def dummy(argument, optional=None):
    """
    Dummy Docstring Title

    Dummy docstring explanation.

    INPUT:

    - ``argument`` -- anything. Dummy argument.

    - ``optional`` -- anything (optional). Dummy optional.

    EXAMPLES::

        sage: from sage.repl.ipython_tests import dummy
        sage: dummy(1)
        'Source code would be here'
    """
    return 'Source code would be here'
