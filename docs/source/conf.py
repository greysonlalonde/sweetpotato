# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information -----------------------------------------------------

project = "Sweetpotato"
copyright = "2022, Greyson R. LaLonde"
author = "Greyson R. LaLonde"

# The full version, including alpha/beta/rc tags
release = "v0.6.0-alpha"
version = "v0.6.0-alpha"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_design",
]

# napoleon
napoleon_google_docstring = True

# autodocs
autosummary_generate = True

# todos
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "sphinx_rtd_theme"
# html_theme = "sphinx_book_theme"
html_theme = "furo"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

autodoc_typehints = "description"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# default_light_mode = True
html_theme_options = {
    "use_repository_button": True,
    "logo_only": True,
    "sidebar_hide_name": True,
    # "light_css_variables": {
    #     "color-brand-primary": "#7C4DFF",
    #     "color-brand-content": "#7C4DFF",
    # },
    "source_repository": "https://github.com/greysonlalonde/sweetpotato",
    "source_branch": "main",
    "source_directory": "docs/source/",
    "dark_css_variables": {
        "color-brand-primary": "#7C4DFF",
        "color-brand-content": "#7C4DFF",
        "color-background-item": "var(--color-background-secondary)",
    },
}
html_title = "Sweetpotato"
html_logo = "_static/sweetpotato.png"

pygments_style = "sphinx"
pygments_dark_style = "monokai"
