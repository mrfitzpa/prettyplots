#!/usr/bin/env python
"""Contains class definitions for data sets to plot.
"""



#####################################
## Load libraries/packages/modules ##
#####################################



############################
## Authorship information ##
############################

__author__     = "Matthew Fitzpatrick"
__copyright__  = "Copyright 2020"
__credits__    = ["Matthew Fitzpatrick"]
__maintainer__ = "Matthew Fitzpatrick"
__email__      = "mfitzpatrick@dwavesys.com"
__status__     = "Development"



##################################
## Define classes and functions ##
##################################

# List of public objects in objects.
__all__ = ["XData", "XYData"]



class XData():
    r"""Simple data class to store x data for plotting.

    Parameters
    ----------
    x : array_like(`float`, ndim=1)
        The x-data.
    Attributes
    ----------
    Same as parameters.
    """
    def __init__(self, x):
        self.x = x

        return None



class XYData():
    r"""Simple data class to store x and y data for plotting.

    Parameters
    ----------
    x : array_like(`float`, ndim=1)
        The x-data.
    y : array_like(`float`, ndim=1)
        The corresponding y-data.
    Attributes
    ----------
    Same as parameters.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

        return None
