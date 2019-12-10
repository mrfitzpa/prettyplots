Installation instructions
=========================

To install ``prettyplots``, simply issue the following commands in the root
directory of the repository::

     pip install -r requirements.txt
     pip install .

Uninstall prettyplots
---------------------

To uninstall ``prettyplots``, all you need to type is::

    pip uninstall prettyplots

Generating documention files
----------------------------

To generate documentation in html format from source files you will also need
the sphinx and numpydoc pacakges. These can be installed by typing at the root
directory::

    pip install -r requirements-doc.txt

Then, assuming you are in the root directory of ``prettyplots`` and that
``prettyplots`` is already installed, issue the following commands to generate
html documentation files::

    cd docs
    make html

This will generate a set of html files in ``./_build/html`` containing the
documentation of ``qamps``. You can then open any of the files using your
favorite web browser to start navigating the documentation within said browser::

    firefox ./_build/html/index.html &>/dev/null &

If ``prettyplots`` has been updated, the documentation has most likely changed
as well. To update the documentation, first remove the ``reference`` directory
inside ``docs``::

    rm -r reference

and then issue the following command::

    make clean

Now that we have cleaned everything up, we can simply run::

    make html

to generate the new documentation.
