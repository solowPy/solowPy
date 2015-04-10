"""
models directory imports

objects imported here will live in the `solowpy` namespace

"""
__all__ = ['Model', 'CobbDouglasModel', 'CESModel']

from . model import Model
from . import model
from . cobb_douglas import CobbDouglasModel
from . import cobb_douglas
from . ces import CESModel
from . import ces

# Add Version Attribute
from pkg_resources import get_distribution

__version__ = get_distribution('solowPy').version
