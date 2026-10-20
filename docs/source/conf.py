# -*- coding: utf-8 -*-
"""Sphinx configuration for the SunFounder Zero 2W Starter Kit documentation.

This repository holds the **English** documentation only, which is the master
copy. Translations live on separate branches (``docs-cn``, ``docs-de``,
``docs-es``, ``docs-fr``, ``docs-it``, ``docs-ja``, ...), each created from this
branch once the English text has been finalised. Do not add a second language to
this branch.
"""

import os
import sys

sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------
project = "SunFounder Zero 2W Starter Kit"
copyright = "2026, SunFounder"
author = "SunFounder"

release = "1.0.0"
version = "1.0"

language = "en"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.todo",
    "sphinx_copybutton",
    # Listed as an extension as well, matching the other SunFounder docs repos.
    "sphinx_rtd_theme",
    # NOTE: sphinxcontrib.youtube is deliberately not enabled — this kit has no
    # video tutorials. If videos are ever produced, add the extension here and to
    # docs/requirements.txt at the same time as the first ``.. youtube::``
    # directive.
]

# The SunFounder navigation bar at the top of every page is a theme override.
templates_path = ["_templates"]
# Holds lang.js, which the layout uses to tell a visitor that a translated
# version of the page exists.
html_static_path = ["_static"]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    # --- Pages from the shared repository (sf-shared) that this kit does not use ---
    # The submodule brings in the whole shared tree; everything this kit needs is
    # listed in a toctree, and anything else would only produce "not included in any
    # toctree" warnings and copy unused images into the build.
    #
    # NOTE: these must be excluded by DIRECTORY where possible. A local sparse
    # checkout can hide files that a real clone has, which is exactly how a build
    # can pass locally and fail on Read the Docs. _shared/component holds 55 pages
    # this kit never references.
    "_shared/component",
    # The shared pages we *do* use are deliberately NOT listed: Sphinx has to know
    # about a file to resolve it from a toctree.
    #
    # set_up_pi.rst is listed because this kit keeps its own version at
    # docs/source/set_up_pi.rst: if the shared copy were still read as a document
    # it would define the same ``_set_up_pi`` label a second time and warn.
    "_shared/pi_start/set_up_pi.rst",
    "_shared/pi_start/need_components.rst",
    "_shared/pi_start/need_components_fusion_hat.rst",
    "_shared/pi_start/power_supply_robot_hat.rst",
    "_shared/pi_start/run_installer_fusion_hat.rst",
    "_shared/appendix/blynk_app.rst",
    "_shared/appendix/filezilla.rst",
    "_shared/appendix/i2c_configuration.rst",
    "_shared/appendix/spi_configuration.rst",
]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"

# SunFounder's site customisation, shared with every other kit's docs:
#   custom.js / custom.css  - served from ezblock.cc, they build the top bar
#   lang.js                 - local file; offers a link to a translated version
#                             of the page when one exists for the visitor's
#                             browser language
html_js_files = [
    "https://ezblock.cc/readDocFile/custom.js",
    "./lang.js",
]
html_css_files = [
    "https://ezblock.cc/readDocFile/custom.css",
]

html_theme_options = {
    # NOTE: other SunFounder docs repos also set ``flyout_display``,
    # ``version_selector`` and ``language_selector`` here. Those are not options
    # of the published sphinx_rtd_theme — they warn as "unsupported theme option"
    # and are silently ignored, which nobody notices there because those builds
    # do not use ``-W``. The flyout position and the hidden selectors are done by
    # custom.css / custom.js from ezblock.cc above, so dropping them changes
    # nothing on the page.
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 3,
    "includehidden": True,
    "titles_only": False,
}

html_context = {
    # The theme's "Edit on GitHub" link assumes a single repository holding every
    # page. Neither half of this project satisfies that: our pages live under
    # docs/source/ (not source/), and the install/setup/appendix pages come from
    # the sf-shared submodule, which is a different repository entirely. A link
    # generated here would be wrong for most pages, so it is switched off rather
    # than published broken.
    "display_github": False,
    "github_user": "sunfounder",
    "github_repo": "zero2w-kit",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

html_last_updated_fmt = "%Y-%m-%d"

# -- Options for LaTeX / PDF output ------------------------------------------
latex_documents = [
    ("index", "Zero2WStarterKit.tex", project, author, "manual"),
]

# -- Options for todo --------------------------------------------------------
todo_include_todos = True

# -- Copybutton --------------------------------------------------------------
copybutton_prompt_text = r"\$ |>>> |pi@raspberrypi:~\$ "
copybutton_prompt_is_regexp = True

# -- Shared substitutions ----------------------------------------------------
# Only the ones this kit actually references are kept here. The shared pages
# define their own `|shared_link_*|` substitutions locally, so they do not need
# entries in this file.
rst_epilog = """
.. |link_sf_facebook| raw:: html

    <a href="https://www.facebook.com/groups/sunfounder" target="_blank">SunFounder Facebook Community</a>
"""
