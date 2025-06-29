"""Configure import path to include the project’s 'src' directory.

This ensures that internal packages and modules in 'src/' can be imported
when executing this script directly or in development environments.
"""

import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)
