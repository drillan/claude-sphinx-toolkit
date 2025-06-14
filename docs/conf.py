# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'claude-sphinx-toolkit'
copyright = '2025, driller'
author = 'driller'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- MyST Parser configuration ----------------------------------------------
myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'tasklist',
    'attrs_inline',
    'attrs_block',
]

# -- Autodoc configuration --------------------------------------------------
autosummary_generate = True

# -- Napoleon configuration -------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# -- Intersphinx configuration ----------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master', None),
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_options = {
    'sidebar_hide_name': True,
    'navigation_with_keys': True,
    'top_of_page_button': 'edit',
    'source_repository': 'https://github.com/user/repo',
    'source_branch': 'main',
    'source_directory': 'docs/',
    'light_css_variables': {
        'color-brand-primary': '#2980b9',
        'color-brand-content': '#2980b9',
    },
    'dark_css_variables': {
        'color-brand-primary': '#3498db',
        'color-brand-content': '#3498db',
    },
}
html_static_path = ['_static']
