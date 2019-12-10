#!/usr/bin/env python
"""``prettyplots`` is a small Python library for creating plots in accordance
with the tastes of the author.
"""


#####################################
## Load libraries/packages/modules ##
#####################################

# For general array handling:
import numpy as np

# Matplotlib modules:
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable



# Load submodules.
from . import data
from . import plot
from . import template

from . import version



############################
## Authorship information ##
############################

__author__       = "Matthew Fitzpatrick"
__copyright__    = "Copyright 2019"
__credits__      = ["Matthew Fitzpatrick"]
__version__      = version.version
__full_version__ = version.full_version
__maintainer__   = "Matthew Fitzpatrick"
__email__        = "mrfitzpa@sfu.ca"
__status__       = "Development"



##################################
## Define classes and functions ##
##################################

# List of public objects in package.
__all__ = ["show_config"]



def show_config():
    """Print information about the version of qamps and libraries it uses.

    Parameters
    ----------

    Returns
    -------
    """
    print(version.version_summary)

    return None
