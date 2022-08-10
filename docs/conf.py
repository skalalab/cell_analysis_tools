# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import mock
import os
import sys

# https://blog.rtwilson.com/how-to-make-your-sphinx-documentation-compile-with-readthedocs-when-youre-using-numpy-and-scipy/ 
# MOCK_MODULES = ['numpy', 'scipy']
# for mod_name in MOCK_MODULES:
#     sys.modules[mod_name] = mock.Mock()

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# sys.path.insert(0, os.path.abspath("."))
# path_cell_analysis_tools = os.path.abspath("../cell_analysis_tools")
# sys.path.insert(0, path_cell_analysis_tools)
# print(f"added path:{path_cell_analysis_tools}")

## added module path did this fix things?!
sys.path.insert(0, os.path.abspath('../'))



# -- Project information -----------------------------------------------------

project = "cell_analysis_tools"
copyright = "2022, Skala Lab"
author = "Skala Lab"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "autodocsumm",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
# html_theme = 'pydata_sphinx_theme'

# html_theme = 'sphinx_adc_theme'
# html_theme_path = [sphinx_adc_theme.get_html_theme_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "css/custom.css",
]
