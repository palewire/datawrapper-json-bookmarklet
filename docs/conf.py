"""Settings for Sphinx."""

from datetime import datetime
from typing import Any

project = "Datawrapper JSON bookmarklet"
year = datetime.now().year
copyright = f"{year} palewire"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "palewire"
pygments_style = "sphinx"

html_sidebars: dict[Any, Any] = {}
html_theme_options: dict[Any, Any] = {
    "canonical_url": "https://palewi.re/docs/first-llm-classifier/",
    "nosidebar": True,
}

extensions = [
    "myst_parser",
]

myst_enable_extensions = [
    "attrs_block",
    "colon_fence",
]

html_static_path = ["_static"]
