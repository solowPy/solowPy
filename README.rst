=======
solowPy
=======

|Build Status| |Coverage Status| |Development Status| |Latest Version| |Downloads| |DOI|

.. |Build Status| image:: https://travis-ci.org/solowPy/solowPy.svg?branch=master
   :target: https://travis-ci.org/solowPy/solowPy
.. |Coverage Status| image:: https://coveralls.io/repos/solowPy/solowPy/badge.svg
   :target: https://coveralls.io/r/solowPy/solowPy
.. |Development Status| image:: https://pypip.in/status/solowPy/badge.svg 
   :target: https://pypi.python.org/pypi/solowPy/
.. |Latest Version| image:: https://pypip.in/version/solowpy/badge.svg
   :target: https://pypi.python.org/pypi/solowPy/
.. |Downloads| image:: https://pypip.in/download/solowPy/badge.svg
   :target: https://pypi.python.org/pypi/solowPy/
.. |DOI| image:: https://zenodo.org/badge/doi/10.5281/zenodo.16759.svg
   :target: http://dx.doi.org/10.5281/zenodo.16759

Library for solving, simulating, and estimating the `Solow (1956)`_ model of economic growth.

.. _`Solow (1956)`:  http://piketty.pse.ens.fr/files/Solow1956.pdf

Quick summary of Solow (1956)
=============================

The following summary of the Solow model of economic growth largely follows `Romer (2011)`_.

.. _`Romer (2011)`: http://highered.mheducation.com/sites/0073511374/index.html

The production function
~~~~~~~~~~~~~~~~~~~~~~~

The Solow model of economic growth focuses on the behavior of four
variables: output, `Y`, capital, `K`, labor, `L`, and knowledge (or technology
or the "effectiveness of labor"), `A`. At each point in time the economy has
some amounts of capital, labor, and knowledge that can be combined to produce
output according to some production function, `F`.

.. math::

    Y(t) = F(K(t), A(t)L(t))

where `t` denotes time.

The evolution of the inputs to production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The initial levels of capital, :math:`K_0`, labor, :math:`L_0`, and technology,
:math:`A_0`, are taken as given. Labor and technology are assumed to grow at
constant rates:

.. math::

    \dot{A}(t) = gA(t)
    \dot{L}(t) = nL(t)

where the rate of technological progrss, `g`, and the population growth rate,
`n`, are exogenous parameters.

Output is divided between consumption and investment. The fraction of output
devoted to investment, :math:`0 < s < 1`, is exogenous and constant. One unit
of output devoted to investment yields one unit of new capital. Capital is
assumed to decpreciate at a rate :math:`0\le \delta`. Thus aggregate capital
stock evolves according to

.. math::

    \dot{K}(t) = sY(t) - \delta K(t).

Although no restrictions are placed on the rates of technological progress and
population growth, the sum of `g`, `n`, and :math:`delta` is assumed to be
positive.

The dynamics of the model
~~~~~~~~~~~~~~~~~~~~~~~~~

Because the economy is growing over time (due to exogenous technological
progress and population growth) it is useful to focus on the behavior of
capital stock per unit of effective labor

.. math::
    
    k \equiv K/AL.

Applying the chain rule to the equation of motion for capital stock yields (after a
bit of algebra!) an equation of motion for capital stock per unit of effective
labor.

.. math::

    \dot{k}(t) = s f(k) - (g + n + \delta)k(t)

That's it! The Solow model of economic growth reduced to a single non-linear ordinary differential equation.

Installation
============

Assuming you have `pip`_ on your computer (as will be the case if you've `installed Anaconda`_) you can install the latest stable release of ``solowPy`` by typing
    
.. code:: bash

    pip install solowPy

at a terminal prompt.

.. _pip: https://pypi.python.org/pypi/pip
.. _`installed Anaconda`: http://quant-econ.net/getting_started.html#installing-anaconda

Example notebooks
=================

There are a number of example notebooks that demonstrate how to use the ``solowPy`` library to solve, simulate, and estimate generic Solow models of economic growth.

- `Motivation`_
- `Getting started`_
- `Finding the steady state`_
- `Graphical analysis`_
- `Solving the model`_
- `Impulse response functions`_
- `Calibration and estimation`_

.. _`Motivation`: http://nbviewer.ipython.org/github/solowPy/solowPy/blob/master/examples/0%20Motivation.ipynb
.. _`Getting started`: http://nbviewer.ipython.org/github/solowPy/solowPy/blob/master/examples/1%20Getting%20started.ipynb
.. _`Finding the steady state`: http://nbviewer.ipython.org/github/solowPy/solowPy/blob/master/examples/2%20Finding%20the%20steady%20state.ipynb
.. _`Graphical analysis`: http://nbviewer.ipython.org/github/solowPy/solowPy/blob/master/examples/3%20Graphical%20analysis.ipynb
.. _`Solving the model`: http://nbviewer.ipython.org/github/solowPy/solowPy/blob/master/examples/4%20Solving%20the%20model.ipynb
.. _`Impulse response functions`: http://nbviewer.ipython.org/github/solowPy/solowPy/blob/master/examples/5%20Impulse%20response%20functions.ipynb
.. _`Calibration and estimation`: http://nbviewer.ipython.org/github/solowPy/solowPy/blob/master/examples/6%20Calibration%20and%20estimation.ipynb
