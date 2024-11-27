# This code will add all subdirectories to __all__ variable so the entire module can be imported with just one line -
# from solutions import *
from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]