# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx Documentation Sample'
copyright = '2022, Stef P'
author = 'Stef P'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Stef: Remove alabaster theme, use the ReadTheDocs theme instead
# To access the theme: 
#     pip install sphinx-rtd-theme (inside C:/User/[username])
#     make html (to rebuild documentation)
# html_theme = 'alabaster'
# html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "logo_only": True,
    "display_version": True,
}
