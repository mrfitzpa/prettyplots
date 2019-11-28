#!/usr/bin/env python
"""prettyplots module

This module contains classes and functions that can be used to make pretty
in accordance with the tastes of the author. :)
"""



__author__     = "Matthew Fitzpatrick"
__copyright__  = "Copyright 2019"
__credits__    = ["Matthew Fitzpatrick"]
__version__    = "1.0.1"
__maintainer__ = "Matthew Fitzpatrick"
__email__      = "mfitzpatrick@dwavesys.com"
__status__     = "Non-production"



####################
## Load libraries ##
####################

# For general array handling:
import numpy as np

# Matplotlib modules:
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable



##################################
## Define classes and functions ##
##################################

def to_np_array(c):
    r"""Convert object to a numpy array (if it is not already of that type).

    Parameters
    ----------
    c : scalar | array
        The object to be converted (typically a scalar e.g. float).

    Returns
    -------
    c_array : array
        The object as an array.
    """
    c_array = np.array(c)
    if c_array.shape == ():
        c_array = c_array.reshape([1])

    return c_array



class XYData():
    r"""Simple data class to store x and y data for plotting.

    Parameters
    ----------
    x : array
        The x-data.
    y : array
        The corresponding y-data.
    Attributes
    ----------
    Same as parameters.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

        return None



class SinglePlotParams():
    r"""Data class to store parameters for the function :func:`single_plot`.

    Parameters
    -----------
    xy_data_sets : array
        The xy data sets to be plotted. Should be an array with elements
        :class:`XYData`.
    scatterplot : bool
        If True, plot data as scatterplot.
    colors : str | array
        A string or an array of strings specifying the colors of each data set.
    markers : str | array
        A string or an array of strings specifying the markers to use (assuming
        the parameter scatterplot is set to True).
    markersize : float
        A positive float that specifies the size of the markers (if used).
    linestyles : str | array
        A string or an array of strings specifying the linestyles of each data
        set.
    linewidth : float
        A positive float that specifies a characteristic linewidth used to
        determine the width of data curves, axes, and ticks.
    x_lims : two-element array
        Specifies the plotting range along the x-axis: x_lims[0] = x-min; 
        x_lims[1] = x-max.
    y_lims : two-element array
        Specifies the plotting range along the y-axis: y_lims[0] = y-min; 
        y_lims[1] = y-max.
    x_log_scale : bool
        If true, then a logarithmic scale is used for the x-axis, otherwise it
        is not used.
    y_log_scale : bool
        If true, then a logarithmic scale is used for the y-axis, otherwise it
        is not used.
    x_label : str
        Specifies the x-axis label.
    y_label : str
        Specifies the y-axis label.
    xy_label_ft_size : float
        A positive float that specifies the font size of the x and y axes
        labels.
    legend_labels : array
        An array of strings specifying the curve labels of each data set.
    legend_loc : str | two-element array
        A string or two-element array specifying the location of the legend.
    legend_ft_size : float
        A positive float that specifies the font size of the legend.
    major_xtick_len : float
        A positive float that specifies the length of the major ticks on the
        x-axis.
    minor_xtick_len : float
        A positive float that specifies the length of the minor ticks on the
        x-axis.
    major_ytick_len : float
        A positive float that specifies the length of the major ticks on the
        y-axis.
    minor_ytick_len : float
        A positive float that specifies the length of the minor ticks on the
        y-axis.
    major_xtick_spacing : float
        A positive float that specifies the spacing between adjacent major ticks
        on the x-axis.
    minor_xtick_spacing : float
        A positive float that specifies the spacing between adjacent minor ticks
        on the x-axis.
    major_ytick_spacing : float
        A positive float that specifies the spacing between adjacent major ticks
        on the y-axis.
    minor_ytick_spacing : float
        A positive float that specifies the spacing between adjacent minor ticks
        on the y-axis.
    tick_label_ft_size : float
        A positive float that specifies the font size of the tick labels.
    fig_label : str
        A string that specifies the figure label.
    fig_label_coords : two-element array
        An array that specifies the position of the figure label.
    fig_label_ft_size : float
        A positive float that specifies the font size of the figure label.
    aspect : str | float
        A string or positive float that specifies the aspect ratio of the
        figure.
    scale : float
        A positive float that specifies the size of the figure.

    Attributes
    ----------
    Same as parameters.
    """
    def __init__(self,
                 xy_data_sets,
                 scatterplot=False, colors=None, markers=None, markersize=11,
                 linestyles=None, linewidth=3,
                 x_lims=[None, None], y_lims=[None, None],
                 x_log_scale=False, y_log_scale=False,
                 x_label='', y_label='', xy_label_ft_size=20,
                 legend_labels=None, legend_loc='best', legend_ft_size=18,
                 major_xtick_len=8, minor_xtick_len=5,
                 major_ytick_len=8, minor_ytick_len=5,
                 major_xtick_spacing=None, minor_xtick_spacing=None,
                 major_ytick_spacing=None, minor_ytick_spacing=None,
                 tick_label_ft_size=18,
                 fig_label='', fig_label_coords=[0.05, 0.93],
                 fig_label_ft_size=20,
                 aspect='auto', scale=1):
        self.xy_data_sets = xy_data_sets

        self.scatterplot = scatterplot
        self.colors = colors
        self.markers = markers
        self.markersize = markersize
        self.linestyles = linestyles
        self.linewidth = linewidth
        
        self.x_lims = x_lims
        self.y_lims = y_lims
        self.x_log_scale = x_log_scale
        self.y_log_scale = y_log_scale

        self.x_label = x_label
        self.y_label = y_label
        self.xy_label_ft_size = xy_label_ft_size

        self.legend_labels = legend_labels
        self.legend_loc = legend_loc
        self.legend_ft_size = legend_ft_size

        self.major_xtick_len = major_xtick_len
        self.minor_xtick_len = minor_xtick_len
        self.major_ytick_len = major_ytick_len
        self.minor_ytick_len = minor_ytick_len
        self.major_xtick_spacing = major_xtick_spacing
        self.minor_xtick_spacing = minor_xtick_spacing
        self.major_ytick_spacing = major_ytick_spacing
        self.minor_ytick_spacing = minor_ytick_spacing
        self.tick_label_ft_size = tick_label_ft_size

        self.fig_label = fig_label
        self.fig_label_coords = fig_label_coords
        self.fig_label_ft_size = fig_label_ft_size

        self.aspect = aspect
        self.scale = scale
        
        return None



def single_plot(params):
    r"""Generate a single plot based on the parameters specified in params.

    Parameters
    -----------
    params : :class:`SinglePlotParams`
        The plotting parameters.

    Returns
    -------

    """
    mpl.rcParams['text.usetex'] = True

    fig = plt.figure()
    ax = fig.add_subplot(111)



    xy_data_sets = params.xy_data_sets
    num_xy_data_sets = len(xy_data_sets)
    
    legend_labels = params.legend_labels
    no_legend = False
    if legend_labels == None:
        legend_labels = [None] * num_xy_data_sets
        no_legend = True

    colors = params.colors
    if colors == None:
        colors = [None] * num_xy_data_sets
    else:
        colors = to_np_array(colors)
        if colors.size == 1:
            colors = np.resize(colors, num_xy_data_sets)

    markersize = params.markersize        
    markers = params.markers        
    if markers == None:
        markers = [None] * num_xy_data_sets
    else:
        markers = to_np_array(markers)
        if markers.size == 1:
            markers = np.resize(markers, num_xy_data_sets)

    linewidth = params.linewidth
    linestyles = params.linestyles        
    if linestyles == None:
        linestyles = [None] * num_xy_data_sets
    else:
        linestyles = to_np_array(linestyles)
        if linestyles.size == 1:
            linestyles = np.resize(linestyles, num_xy_data_sets)


        
    for idx in range(num_xy_data_sets):
        x = xy_data_sets[idx].x
        y = xy_data_sets[idx].y

        if params.scatterplot:
            ax.scatter(x, y, marker=markers[idx], c=colors[idx],
                       s=markersize, label=legend_labels[idx])
        else:
            ax.plot(x, y, ls=linestyles[idx], c=colors[idx],
                    lw=linewidth, label=legend_labels[idx],
                    marker=markers[idx], markersize=markersize)


            
    legend_loc = params.legend_loc
    legend_ft_size = params.legend_ft_size
    if no_legend:
        pass
    else:
        ax.legend(loc=legend_loc, frameon=True, fontsize=legend_ft_size)


    
    fig_label = params.fig_label
    fig_label_coords = params.fig_label_coords
    fig_label_ft_size = params.fig_label_ft_size
    ax.text(fig_label_coords[0], fig_label_coords[1], fig_label,
            fontsize=fig_label_ft_size, horizontalalignment='center',
            verticalalignment='center', transform=ax.transAxes)



    x_label = params.x_label
    y_label = params.y_label
    xy_label_ft_size = params.xy_label_ft_size
    ax.set_xlabel(x_label, fontsize=xy_label_ft_size)
    ax.set_ylabel(y_label, fontsize=xy_label_ft_size)



    if params.x_log_scale == True:
        ax.set_xscale('log')
    if params.y_log_scale == True:
        ax.set_yscale('log')
    
    x_min, x_max = params.x_lims
    y_min, y_max = params.y_lims
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)



    tick_label_ft_size = params.tick_label_ft_size
    
    major_xtick_len = params.major_xtick_len
    minor_xtick_len = params.minor_xtick_len
    major_ytick_len = params.major_ytick_len
    minor_ytick_len = params.minor_ytick_len

    major_xtick_spacing = params.major_xtick_spacing
    minor_xtick_spacing = params.minor_xtick_spacing
    major_ytick_spacing = params.major_ytick_spacing
    minor_ytick_spacing = params.minor_ytick_spacing

    plt.minorticks_on()
    
    if major_xtick_spacing != None:
        x_major_locator = MultipleLocator(major_xtick_spacing)
        ax.xaxis.set_major_locator(x_major_locator)
    if minor_xtick_spacing != None:
        x_minor_locator = MultipleLocator(minor_xtick_spacing)
        ax.xaxis.set_minor_locator(x_minor_locator)

    if major_ytick_spacing != None:
        y_major_locator = MultipleLocator(major_ytick_spacing)
        ax.yaxis.set_major_locator(y_major_locator)
    if minor_ytick_spacing != None:
        y_minor_locator = MultipleLocator(minor_ytick_spacing)
        ax.yaxis.set_minor_locator(y_minor_locator)
    
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')
    
    ax.tick_params(axis='x', which='major',
                   labelsize=tick_label_ft_size,
                   width=2.0 * linewidth / 3.0,
                   length=major_xtick_len, direction='in')
    ax.tick_params(axis='x', which='minor',
                   width=2.0 * linewidth / 3.0,
                   length=minor_xtick_len, direction='in')
    ax.tick_params(axis='y', which='major',
                   labelsize=tick_label_ft_size,
                   width=2.0 * linewidth / 3.0,
                   length=major_ytick_len, direction='in')
    ax.tick_params(axis='y', which='minor',
                   width=2.0 * linewidth / 3.0,
                   length=minor_ytick_len, direction='in')



    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(2.0 * linewidth / 3.0)



    aspect = params.aspect
    ax.set_aspect(aspect)

    scale = params.scale
    fig_dims = fig.get_size_inches()
    fig.set_figwidth(fig_dims[0] * scale)
    fig.set_figheight(fig_dims[1] * scale)


    
    fig.tight_layout(pad=1.08)
    plt.show()

    return None



def print_single_plot_template():
    r"""Prints a single-plot template (for quick use in notebooks).

    Parameters
    -----------

    Returns
    -------

    """
    print("xy_data_sets = []")
    print()
    print("scatterplot = False")
    print("colors = None")
    print("markers = None")
    print("markersize = 10")
    print("linestyles = None")
    print("linewidth = 3")
    print()
    print("x_lims = [None, None]")
    print("y_lims = [None, None]")
    print("x_log_scale = False")
    print("y_log_scale = False")
    print()
    print("x_label = r''")
    print("y_label = r''")
    print("xy_label_ft_size = 20")
    print()
    print("legend_labels = None")
    print("legend_loc = 'best'")
    print("legend_ft_size = 18")
    print()
    print("major_xtick_len = 8")
    print("minor_xtick_len = 5")
    print("major_ytick_len = 8")
    print("minor_ytick_len = 5")
    print("major_xtick_spacing = None")
    print("minor_xtick_spacing = None")
    print("major_ytick_spacing = None")
    print("minor_ytick_spacing = None")
    print("tick_label_ft_size = 18")
    print()
    print("fig_label = r''")
    print("fig_label_coords = [0.07, 0.91]")
    print("fig_label_ft_size = 20")
    print()
    print("aspect = 'auto'")
    print("scale = 1")
    print()
    print("plot_params = prettyplots.SinglePlotParams(")
    print("                  xy_data_sets=xy_data_sets,")
    print("                  scatterplot=scatterplot, colors=colors, markers=markers,")
    print("                  markersize=markersize, linestyles=linestyles,")
    print("                  linewidth=linewidth,")
    print("                  x_lims=x_lims, y_lims=y_lims,")
    print("                  x_log_scale=x_log_scale, y_log_scale=y_log_scale,")
    print("                  x_label=x_label, y_label=y_label,")
    print("                  xy_label_ft_size=xy_label_ft_size,")
    print("                  legend_labels=legend_labels, legend_loc=legend_loc,")
    print("                  legend_ft_size=legend_ft_size,")
    print("                  major_xtick_len=major_xtick_len,")
    print("                  minor_xtick_len=minor_xtick_len,")
    print("                  major_ytick_len=major_ytick_len,")
    print("                  minor_ytick_len=minor_ytick_len,")
    print("                  major_xtick_spacing=major_xtick_spacing,")
    print("                  minor_xtick_spacing=minor_xtick_spacing,")
    print("                  major_ytick_spacing=major_ytick_spacing,")
    print("                  minor_ytick_spacing=minor_ytick_spacing,")
    print("                  tick_label_ft_size=tick_label_ft_size,")
    print("                  fig_label=fig_label, fig_label_coords=fig_label_coords,")
    print("                  fig_label_ft_size=fig_label_ft_size,")
    print("                  aspect=aspect, scale=scale)")

    return None



class SingleImshowParams():
    r"""Data class to store parameters for the function :func:`single_imshow`.

    Parameters
    -----------
    z : array_like(float, ndim=2)
        The data to be represented as a 2D image.
    cmap : str | :class:`matplotlib.colors.Colormap` | None
        Colormap used to map scalar data to color.
    norm : :class:`matplotlib.colors.Normalize` | None
        Lower limit to the data range that the colormap covers.
    interpolation : str | None
        The interpolation method used in generating the image.
    append_axes_kwargs : dict
        Keyword arguments specifying the positioning and size of the colorbar
        axis.
    colorbar_kwargs : dict
        Keyword arguments specifying properties of colorbar.
    xticks : array_like(int, ndim=1) | None
        Positions of ticks along x-axis.
    yticks : array_like(int, ndim=1) | None
        Positions of ticks along y-axis.
    cbticks : array_like(int, ndim=1) | None
        Positions of colorbar ticks.
    xticklabels : array_like(str, ndim=1, length=len(xticks)) | None
        Tick labels along x-axis.
    yticklabels : array_like(str, ndim=1, length=len(yticks)) | None
        Tick labels along y-axis.
    cbticklabels : array_like(str, ndim=1, length=len(xticks)) | None
        Colorbar tick labels along x-axis.
    xtick_len : float
        Length of ticks along x-axis.
    ytick_len : float
        Length of ticks along y-axis.
    cbtick_len : float
        Length of colobar ticks.
    xtick_width : float
        Width of ticks along x-axis.
    ytick_width : float
        Width of ticks along y-axis.
    cbtick_width : float
        Width of colobar ticks.
    tick_label_ft_size : float
        Font size of tick labels.
    vlines : array_like(float, ndim=1)
        Positions of vertical lines along x-axis.
    hlines : array_like(float, ndim=1)
        Positions of vertical lines along y-axis.
    vline_kwargs : dict
        Keyword arguments specifying line properties of vertical lines.
    hline_kwargs : dict
        Keyword arguments specifying line properties of horizontal lines.
    frame_thickness : float
        Thickness of image frame.
    x_label : str
        Specifies the x-axis label.
    y_label : str
        Specifies the y-axis label.
    xy_label_ft_size : float
        Font size of the x and y axis labels.
    title : str
        Title of plot.
    title_ft_size : float
        Title font size.
    fig_label : str
        Figure label.
    fig_label_coords : array_like(float, ndim=1, length=2)
        Position of the figure label with respect to the coordinate system of
        the axes.
    fig_label_ft_size : float
        Font size of figure label.
    aspect : str | float
        Aspect ratio of figure.
    scale : float
        Size of figure.

    Attributes
    ----------
    Same as parameters.
    """
    def __init__(self,
                 z,
                 cmap=None, norm=None, interpolation=None,
                 append_axes_kwargs={"position": "right",
                                     "size": "5%",
                                     "pad": 0.05},
                 colorbar_kwargs={},
                 xticks=None, yticks=None, cbticks=None,
                 xticklabels=None, yticklabels=None, cbticklabels=[],
                 xtick_len=8, ytick_len=8, cbtick_len=8,
                 xtick_width=2, ytick_width=2, cbtick_width=2,
                 tick_label_ft_size=18,
                 vlines=[], hlines=[], vline_kwargs={}, hline_kwargs={},
                 frame_thickness=2,
                 x_label='', y_label='', xy_label_ft_size=20,
                 title='', title_ft_size=20,
                 fig_label='', fig_label_coords=[0.07, 0.91],
                 fig_label_ft_size=20,
                 aspect='auto', scale=1.):
        self.z = z

        self.cmap = cmap
        self.norm = norm
        self.interpolation = interpolation
        self.append_axes_kwargs = append_axes_kwargs
        self.colorbar_kwargs = colorbar_kwargs



        self.xticks = range(z.shape[1]) if xticks == None else xticks
        self.yticks = range(z.shape[0]) if yticks == None else yticks
        self.cbticks = cbticks
        
        self.xticklabels = ([''] * z.shape[1] if xticklabels == None
                            else xticklabels)
        self.yticklabels = ([''] * z.shape[0] if yticklabels == None
                            else yticklabels)
        self.cbticklabels = cbticklabels
        
        self.xtick_len = xtick_len
        self.ytick_len = ytick_len
        self.cbtick_len = cbtick_len
        
        self.xtick_width = xtick_width
        self.ytick_width = ytick_width
        self.cbtick_width = cbtick_width
        
        self.tick_label_ft_size = tick_label_ft_size


        
        self.vlines = vlines
        self.hlines = hlines
        self.vline_kwargs = vline_kwargs
        self.hline_kwargs = hline_kwargs


        
        self.frame_thickness = frame_thickness


        
        self.x_label = x_label
        self.y_label = y_label
        self.xy_label_ft_size = xy_label_ft_size


        
        self.title = title
        self.title_ft_size = title_ft_size



        self.fig_label = fig_label
        self.fig_label_coords = fig_label_coords
        self.fig_label_ft_size = fig_label_ft_size


        
        self.aspect = aspect
        self.scale = scale


        
        return None



def single_imshow(params):
    r"""Generate a figure containing a single imshow plot.

    Parameters
    -----------
    params : :class:`SingleImshowParams`
        The plotting parameters.

    Returns
    -------

    """
    mpl.rcParams['text.usetex'] = True

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(**params.append_axes_kwargs)


    
    im = ax.imshow(params.z,
                   cmap=params.cmap,
                   norm=params.norm,
                   interpolation=params.interpolation)

    cb = fig.colorbar(im, cax=cax, **params.colorbar_kwargs)



    ax.set_xticks(params.xticks)
    ax.set_yticks(params.yticks)
    if params.cbticks != None:
        cb.set_ticks(params.cbticks)

    ax.set_xticklabels(params.xticklabels)
    ax.set_yticklabels(params.yticklabels)
    if params.cbticklabels != None:
        cb.set_ticklabels(params.cbticklabels)

    ax.tick_params(axis='x', which='major',
                   labelsize=params.tick_label_ft_size,
                   length=params.xtick_len, width=params.xtick_width,
                   direction='out')
    ax.tick_params(axis='y', which='major',
                   labelsize=params.tick_label_ft_size,
                   length=params.ytick_len, width=params.ytick_width,
                   direction='out')
    cb.ax.tick_params(labelsize=params.tick_label_ft_size,
                      length=params.cbtick_len, width=params.cbtick_width)


    
    # Fix bug in imshow, need to manually adjust y-limits for full display.
    ax.set_ylim(-0.5+len(params.yticks), -0.5)



    for vline in params.vlines:
        ax.axvline(x=vline, **params.vline_kwargs)

    for hline in params.hlines:
        ax.axhline(y=hline, **params.hline_kwargs)



    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(params.frame_thickness)

    cb.outline.set_linewidth(params.frame_thickness)
    

    ax.set_xlabel(params.x_label, fontsize=params.xy_label_ft_size)
    ax.set_ylabel(params.y_label, fontsize=params.xy_label_ft_size)



    ax.set_title(params.title, fontsize=params.title_ft_size)
    

    
    fig_label = params.fig_label
    fig_label_coords = params.fig_label_coords
    fig_label_ft_size = params.fig_label_ft_size
    ax.text(params.fig_label_coords[0], params.fig_label_coords[1],
            params.fig_label, fontsize=params.fig_label_ft_size,
            horizontalalignment='center', verticalalignment='center',
            transform=fig.transFigure)


    
    aspect = params.aspect
    ax.set_aspect(aspect)

    scale = params.scale
    fig_dims = fig.get_size_inches()
    fig.set_figwidth(fig_dims[0] * scale)
    fig.set_figheight(fig_dims[1] * scale)


    
    fig.tight_layout(pad=1.08)
    plt.show()

    return None



def print_single_imshow_template():
    r"""Prints a single-imshow template (for quick use in notebooks).

    Parameters
    -----------

    Returns
    -------
    """
    print("z = <array_like(float, ndim)>")
    print()
    print("cmap = None")
    print("norm = None")
    print("interpolation = None")
    print("append_axes_kwargs = {'position': 'right',")
    print("                      'size': '5%',")
    print("                      'pad': 0.05}")
    print("colorbar_kwargs = {}")
    print()
    print("xticks = None")
    print("yticks = None")
    print("cbticks = None")
    print("xticklabels = None")
    print("yticklabels = None")
    print("cbticklabels = None")
    print("xtick_len = 8")
    print("ytick_len = 8")
    print("cbtick_len = 8")
    print("xtick_width = 2")
    print("ytick_width = 2")
    print("cbtick_width = 2")
    print("tick_label_ft_size = 18")
    print()
    print("vlines = []")
    print("hlines = []")
    print("vline_kwargs = {}")
    print("hline_kwargs = {}")
    print()
    print("frame_thickness = 2")
    print()
    print("x_label = r''")
    print("y_label = r''")
    print("xy_label_ft_size = 20")
    print()
    print("title = r''")
    print("title_ft_size = 20")
    print()
    print("fig_label = r''")
    print("fig_label_coords = [0.07, 0.91]")
    print("fig_label_ft_size = 20")
    print()
    print("aspect = 'auto'")
    print("scale = 1")
    print()
    print()
    print()
    print("plot_params = prettyplots.SingleImshowParams(")
    print("                  z=z,")
    print("                  cmap=cmap, norm=norm, interpolation=interpolation,")
    print("                  append_axes_kwargs=append_axes_kwargs,")
    print("                  colorbar_kwargs=colorbar_kwargs,")
    print("                  xticks=xticks, yticks=yticks, cbticks=cbticks,")
    print("                  xticklabels=xticklabels,")
    print("                  yticklabels=yticklabels,")
    print("                  cbticklabels=cbticklabels,")
    print("                  xtick_len=xtick_len,")
    print("                  ytick_len=ytick_len,")
    print("                  cbtick_len=cbtick_len,")
    print("                  xtick_width=xtick_width,")
    print("                  ytick_width=ytick_width,")
    print("                  cbtick_width=cbtick_width,")
    print("                  tick_label_ft_size=tick_label_ft_size,")
    print("                  vlines=vlines, hlines=hlines,")
    print("                  vline_kwargs=vline_kwargs, hline_kwargs=hline_kwargs,")
    print("                  frame_thickness=frame_thickness,")
    print("                  x_label=x_label, y_label=y_label,")
    print("                  xy_label_ft_size=xy_label_ft_size,")
    print("                  title=title, title_ft_size=title_ft_size,")
    print("                  fig_label=fig_label, fig_label_coords=fig_label_coords,")
    print("                  fig_label_ft_size=fig_label_ft_size,")
    print("                  aspect=aspect, scale=scale)")
    print()
    print()
    print()
    print("prettyplots.single_imshow(plot_params)")
    

    return None
