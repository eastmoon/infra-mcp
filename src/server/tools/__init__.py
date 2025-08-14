# in my_package/__init__.py
import os
import glob

# Dynamically populate __all__ with Python files in the directory
__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.join(os.path.dirname(__file__), "*.py")) if f != os.path.basename(__file__)]
