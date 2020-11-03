===============================
Configuring Sphinx from scratch
===============================

Version |version|

**A software demonstration by Sadie Bartholomew of the Sphinx documentation
generator.**

.. note::

   I am *not associated with the Sphinx project at all*. I have chosen
   to give a demo of Sphinx because it is a tool I have found extremely
   useful in my work in RSE roles.


Context
=======

Demo format
-----------

This is a demonstration so will be largely conducted in the terminal.
However, notes are provided, as incoporated into the example documentation
itself.

.. tip::
   
   The source and built documentation, which includes these notes,
   is (and will permanently remain) hosted on GitHub at:
   https://github.com/sadielbartholomew/sphinx-from-scratch


The Dummy Project
-----------------

``quadrilaterals``: a very simple and trivial object-oriented Python codebase
used as a placeholder for a real-life and very likely more complex project.

The codebase models categories of two-dimensional four-sided shape, which
are collectively called quadrilaterals. For each category, such as a
square or a rhombus, there are methods to calculate the area, perimeter and
number of axes of symmetry.

A diagram [#footnote1]_ showing the main classes in the dummy project, and
their inheritance hierarchy [#footnote2]_ :

.. image:: https://www.geogebra.org/resource/ncsc3adx/UDHJc4GCp82dcnjM/material-ncsc3adx.png


An example of the code in use (Python console notation):

.. code:: python

   >>> import quadrilaterals
   >>> square = quadrilaterals.Square(5)
   >>> square.area()
   25
   >>> square.perimeter()
   20
   >>> help(square)
   Help on Square in module quadrilaterals.parallelograms.rectangles.square object:

   class Square(quadrilaterals.parallelograms.rectangles.rectangle.Rectangle, quadrilaterals.kites.rhombi.rhombus.Rhombus)
    |  Square(side_length)
    |  
    |  Base class common to all squares.
    |  
    |  >>> import quadrilaterals
    |  >>> q = quadrilaterals.Square(0.2)
    |  
    |  Method resolution order:
    |      Square
    |      quadrilaterals.parallelograms.rectangles.rectangle.Rectangle
    |      quadrilaterals.kites.rhombi.rhombus.Rhombus
    |      quadrilaterals.kites.kite.Kite
    |      quadrilaterals.parallelograms.parallelogram.Parallelogram
    |      quadrilaterals.quadrilateral.Quadrilateral
    |      builtins.object
    |
   ...
   ...
   ...
   >>> parallelogram = quadrilaterals.Parallelogram(5, 2, 1.5)
   >>> help(parallelogram)
   Help on Parallelogram in module quadrilaterals.parallelograms.parallelogram object:

   class Parallelogram(quadrilaterals.quadrilateral.Quadrilateral)
    |  Parallelogram(parallel_side_A_length, parallel_side_B_length, any_angle=None)
    |  
    |  Base class common to all parallelograms.
    |  
    |  >>> import math
    |  >>> q1 = quadrilaterals.Parallelogram(2, 5, 1.1)
    |  >>> q2 = quadrilaterals.Parallelogram(2, 5, math.pi - 1.1)
    |  
    |  Method resolution order:
    |      Parallelogram
    |      quadrilaterals.quadrilateral.Quadrilateral
    |      builtins.object
    |
   ...
   ...
   ...
   >>> parallelogram.area()
   9.974949866040545
   >>> parallelogram.perimeter()
   14


Quick links
===========

Examples of Sphinx-generated documentation
------------------------------------------


It is hard to tell what has been made with Sphinx without looking at the
codebase source, but often if you scroll to the bottom of some
documentation you can often see a "Created using Sphinx <sphinx version>"
note in the footer. A small number of examples are referenced below.

* A large but absolutely not comprehensive listing collected by the Sphinx
  team: https://www.sphinx-doc.org/en/master/examples.html
* Sphinx's own documentation (made with Sphinx, of course!):
  https://www.sphinx-doc.org/en/master/
* Python 3 documentation: https://docs.python.org/3/
* Python 2 documentation: https://docs.python.org/3/
* Tornado documentation: https://www.tornadoweb.org/en/stable/
* Official RST documentation (note it is also made in Sphinx):
  https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html
* Dask documentation: https://docs.dask.org/en/latest/
* JupyterHub documentation: https://jupyterhub.readthedocs.io/en/stable/
* NumPy documentation: https://numpy.org/doc/stable/reference/
* A small (slightly old) listing of non-Python projects with Sphinx
  documentation:
  https://ericholscher.com/blog/2014/feb/11/sphinx-isnt-just-for-python/
* An example of a book made with Sphinx: https://www.theoretical-physics.net/


Sphinx
------

Basic
^^^^^


* Sphinx documentation homepage: https://www.sphinx-doc.org/en/master/
* Quick start including `sphinx-quickstart` command:
  https://www.sphinx-doc.org/en/master/usage/quickstart.html
* HTML themes: https://www.sphinx-doc.org/en/master/usage/theming.html
  
Advanced
^^^^^^^^

* Guidance on extensions:
  https://www.sphinx-doc.org/en/master/usage/extensions/index.html
* An "awesome" listing of extra Sphinx resources:
  https://github.com/yoloseem/awesome-sphinxdoc
* Big listing of even more HTML themes: https://sphinx-themes.org/
* Our customisation of the "alabaster" default theme, in practice:
  https://ncas-cms.github.io/cf-python/
* Example Sphinx extension project repositories:

  * ``sphinx-copybutton`` (button to copy code in code examples):
    https://github.com/executablebooks/sphinx-copybutton 
  * ``sphinx-toggleprompt`` (button to hide prompts and outputs in
    console-like code examples):
    https://github.com/jurasofish/sphinx-toggleprompt
  * ``sphinx-pyreverse`` (generates UML diagramms of the code or parts of
    it into the documentation): https://github.com/alendit/sphinx-pyreverse


reStructuredText (`.rst` extension) format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Official reStructuredText documentation (note it is also made in Sphinx):
  https://docutils.readthedocs.io/en/sphinx-docs/user/rst/quickstart.html
* Helpful cheatseets:

  * https://docutils.sourceforge.io/docs/user/rst/quickref.html
  * https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst


Documenting projects with Sphinx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* A nice blog post: https://medium.com/@richdayandnight/a-simple-tutorial-on-how-to-document-your-python-project-using-sphinx-and-rinohtype-177c22a15b5b
* A great post showing how to use Sphinx with other tools to document a C++
  project: https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/


.. [#footnote1] Image sourced from `this webpage
   <https://www.geogebra.org/m/bm4ja4wb>`_.

.. [#footnote2] Strictly this diagram does not capture one other
   relationship between the quadrilaterals which also exists, and which the
   dummy project incorporates into the class hierarchy, namely that a
   *rhombus* is a special form of *kite*.
