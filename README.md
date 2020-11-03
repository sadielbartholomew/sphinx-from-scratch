# sphinx-from-scratch

Source and notes for a SORSE software demo 10.5281/zenodo.3977886

See: https://zenodo.org/record/3977886#.X6nx43X7TeR


## About


### Background and guide to building from scratch

The directory `converting-txt-or-md-to-rst/` provides files each covering the:

* context i.e. background information for the demonstration
  (``context.<extension>``); and the
* list of steps for how to generate the documentation for the dummy project
  from scratch, as roughly followed in the demonstration itself
  (``steps-to-recreate.<extension>``),

in both the markdown (`.md`, which is very similar to plain text, often `.txt`)
and reStructuredText (`.rst`, RST for short) file formats, to serve as
examples of RST which is used as the markup language for the documentation
source files by Sphinx.


### Pre-made directory of the built documentation

A pre-built example of the generated documentation, including the source,
is provided under the `docs` directory. You can view the outputs as follows:

* the **built HTML** can be viewed after opening up the HTML index page in a
  browser, for example:

  ```console
  $ firefox docs/build/html/index.html
  ```

* and the **built LaTeX** form can be viewed either:

  * as the raw LaTeX source via opening `docs/build/latex/quadrilaterals.tex`
    in a text or TeX editor, for example (with
    [`texmaker`](https://www.xm1math.net/texmaker/) installed):

    ```console
    $ texmaker docs/build/latex/quadrilaterals.tex
    ```
  * or as a PDF by opening up the built PDF,
  `docs/build/latex/quadrilaterals.pdf`, for example via
  (with [`evince`](https://wiki.gnome.org/Apps/Evince) installed):

    ```console
    $ evince docs/build/latex/quadrilaterals.pdf
    ```

Note that the pre-built documentation can be amended and re-built using some
of the commands provided and explained in the
``converting-txt-or-md-to-rst/steps-to-recreate.<extension>`` file.


## Questions

Please feel free to email *sadie.bartholomew@ncas.ac.uk* if you have any
questions about the topics of the software demonstration or this repository.
