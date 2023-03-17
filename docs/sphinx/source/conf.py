# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'hsa-runtime64'
copyright = '2023, AMD'
author = 'AMD'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['breathe', 'myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
primary_domain = 'cpp'
highlight_language = 'cpp'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Breathe Configuration
breathe_projects = { 'hsa-runtime64': '../../../build/docs/doxygen/xml'}
breathe_default_project = 'hsa-runtime64'
breathe_default_members = ('members')
breathe_show_define_initializer = True
breathe_show_include = True

