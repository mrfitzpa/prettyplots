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
    xerr : float | array_like(`float`, ndim=1, length=x.size) | array_like(`float`, ndim=2, shape=(2, x.size)), optional
        The x error. If ``xerr`` is a `float`, then ``xerr`` is the size of the
        '+' and '-' error bars for each data point. If ``xerr`` is a 
        one-dimensional array, then ``xerr[i]`` is the size of the '+' and '-'
        error bars for the :math:`i^{\mathrm{th}}` data point.
    yerr : float | array_like(`float`, ndim=1, length=y.size) | array_like(`float`, ndim=2, shape=(2, y.size)), optional
        The y error. If ``yerr`` is a `float`, then ``yerr`` is the size of the
        '+' and '-' error bars for each data point. If ``yerr`` is a 
        one-dimensional array, then ``yerr[i]`` is the size of the '+' and '-'
        error bars for the :math:`i^{\mathrm{th}}` data point.
    Attributes
    ----------
    Same as parameters.
    """
    def __init__(self, x, y, xerr=None, yerr=None):
        self.x = x
        self.y = y
        self.xerr = xerr
        self.yerr = yerr

        return None
