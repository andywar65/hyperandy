"""Sphinx configuration."""
project = "Hyperandy"
author = "Andy War"
copyright = "2023, Andy War"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
