#!/usr/bin/env python
"""Contains plotting parameter classes and plotting functions.
"""



#####################################
## Load libraries/packages/modules ##
#####################################

# For general array handling.
import numpy as np

# Matplotlib modules.
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable



# XY data class.
from prettyplots.data import XYData



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
__all__ = ["SinglePlotParams",
           "single_plot",
           "SingleImshowParams",
           "single_imshow",
           "SingleHistParams",
           "single_hist"]



def _to_np_array(c):
    r"""Convert object to a numpy array (if it is not already of that type).

    Parameters
    ----------
    c : `float` | array_like
        The object to be converted (typically a scalar e.g. float).

    Returns
    -------
    c_array : :class:`numpy.ndarray`
        The object as a numpy array.
    """
    c_array = np.array(c)
    if c_array.shape == ():
        c_array = c_array.reshape([1])

    return c_array



class SinglePlotParams():
    r"""Data class to store parameters for function :func:`single_plot`.

    The function :func:`single_plot` displays one or more xy data sets in a
    single plot. If there are multiple xy data sets, one can specify two 
    different y-scales in case some of the xy data sets have their y data
    expressed in one unit, and the remaining xy data sets have their y data
    expressed in another unit.

    Parameters
    -----------
    xy_data_sets : `array_like` (:class:`prettyplots.XYData`, ndim=1) | `array_like` (`array_like` (:class:`prettyplots.XYData`, ndim=1), shape=(2,))
        The xy data sets to be plotted. If ``xy_data_sets`` is of the type
        `array_like` (:class:`prettyplots.XYData`, ndim=1), then each xy data
        set is to be plotted with respect to the left y-scale. If 
        ``xy_data_sets`` is of the type 
        `array_like` (`array_like` (:class:`prettyplots.XYData`, ndim=1), 
        shape=(2,)), then each xy data set in ``xy_data_sets[0]`` is to be
        plotted with respect to the left y-scale, whereas each xy data set in 
        ``xy_data_sets[1]`` is to be plotted with respect to the right y-scale.
    scatterplot : `bool` | `array_like` (`bool`, shape=(2,)), optional
        If ``scatterplot`` is of type `bool`, then ``scatterplot`` specifies
        whether all xy data sets are to be displayed as scatter plots or not. If
        ``scatterplot`` is of type `array_like` (`bool`, shape=(2,)), then
        ``scatterplot[0]`` (``scatterplot[1]``) specifies whether the xy data
        sets to be plotted with respect to the left (right) y-scale are to be
        displayed as scatter plots or not.
    colors : `str` | `array_like` (`str`, ndim=1) | `array_like` (`array_like` (`str`, ndim=1), shape=(2,)), optional
        If ``colors`` is of type `str`, then it specifies the color of each xy
        data set. If ``colors`` is of type `array_like` (`str`, ndim=1), then
        ``colors[i]`` specifies the color of the ``i`` th xy data set to be
        plotted with respect to the left y-scale. If ``colors`` is of type 
        `array_like` (`array_like` (`str`, ndim=1), ndim=1), shape=(2,)), then
        ``colors[0][i]`` (``colors[1][i]``) specifies the color of the ``i`` th
        xy data set to be plotted with respect to the left (right) y-scale.
    markers : `str` | `array_like` (`str`, ndim=1) | `array_like` (`array_like` (`str`, ndim=1), shape=(2,)), optional
        If ``markers`` is of type `str`, then it specifies the marker of each xy
        data set. If ``markers`` is of type `array_like` (`str`, ndim=1), then
        ``markers[i]`` specifies the marker of the ``i`` th xy data set to be
        plotted with respect to the left y-scale. If ``markers`` is of type 
        `array_like` (`array_like` (`str`, ndim=1), ndim=1), shape=(2,)), then
        ``markers[0][i]`` (``markers[1][i]``) specifies the marker of the 
        ``i`` th xy data set to be plotted with respect to the left (right) 
        y-scale.
    markersize : `float`, optional
        The size of the markers (if used).
    vlines : `array_like` (`float`, ndim=1), optional
        Positions of vertical lines along x-axis.
    hlines : `array_like` (`float`, ndim=1), optional
        Positions of vertical lines along y-axis.
    vline_kwargs_set : `array_like` (`dict`, ndim=1), optional
        Keyword arguments specifying line properties of vertical lines.
    hline_kwargs_set : `array_like` (`dict`, ndim=1), optional
        Keyword arguments specifying line properties of horizontal lines.
    linestyles : `str` | `array_like` (`str`, ndim=1) | `array_like` (`array_like` (`str`, ndim=1), shape=(2,)), optional
        If ``linestyles`` is of type `str`, then it specifies the linestyle of 
        each xy data set. If ``linestyles`` is of type 
        `array_like` (`str`, ndim=1), then ``linestyles[i]`` specifies the 
        linestyle of the ``i`` th xy data set to be plotted with respect to the 
        left y-scale. If ``linestyles`` is of type 
        `array_like` (`array_like` (`str`, ndim=1), ndim=1), shape=(2,)), then
        ``linestyles[0][i]`` (``linestyles[1][i]``) specifies the linestyle of 
        the ``i`` th xy data set to be plotted with respect to the left (right)
        y-scale.
    linewidth : `float`, optional
        A characteristic linewidth used to determine the width of data curves, 
        axes, and ticks.
    grid_linewidth : `float`, optional
        The linewidth of the plot grid. If set to ``0``, then the grid will be
        disabled.
    x_lims : `array_like` (`float`, shape=(2,)), optional
        Specifies the plotting range along the x-axis.
    y_lims : `array_like` (`float`, shape(2,)), `array_like` (`float`, shape(2, 2)), optional
        If ``y_lims`` is of type `array_like` (`float`, shape(2,)), then 
        ``y_lims`` specifies the plotting range along the both y-axes. If 
        ``y_lims`` is of type `array_like` (`float`, shape(2, 2)), then 
        ``y_lims[0]`` (``y_lims[1]``) specifies the plotting range along the 
        left (right) y-axis.
    x_log_scale : `bool`, optional
        Specifies whether a logarithmic scale is to be used for the x-axis.
    y_log_scale : `bool` | `array_like` (`bool`, shape=(2,)), optional
        If ``y_log_scale`` is of type `bool`, then ``y_log_scale`` specifies
        whether a logarithmic scale is to be used for both y-axes. If 
        ``y_log_scale`` is of type `array_like` (`bool`, shape=(2,)), then
        ``y_log_scale[0]`` (``y_log_scale[1]``) specifies whether a logarithmic 
        scale is to be used for the left (right) y-axis.
    x_label : `str`, optional
        Specifies the x-axis label.
    y_label : `str` | `array_like` (`str`, shape=(2,)), optional
        If ``y_label`` is of type `str`, then ``y_label`` specifies the label
        for both y-axes. If ``y_label`` is of type 
        `array_like` (`str`, shape=(2,)), then ``y_label[0]`` (``y_label[1]``)
        specifies the label for the left (right) y-axis.
    xy_label_ft_size : `float`, optional
        The font size of the x and y axes labels.
    legend_labels : `array_like` (`str`, ndim=1) | `array_like` (`array_like` (`str`, ndim=1), shape=(2,)), optional
        If ``legend_labels`` is of type `array_like` (`str`, ndim=1), then
        ``legend_labels[i]`` specifies the legendlabel of the ``i`` th xy data 
        set to be plotted with respect to the left y-scale. If ``legend_labels``
        is of type 
        `array_like` (`array_like` (`str`, ndim=1), ndim=1), shape=(2,)), then
        ``legend_labels[0][i]`` (``legend_labels[1][i]``) specifies the legend 
        label of the ``i`` th xy data set to be plotted with respect to the left
        (right) y-scale.
    legend_loc : `str` | `array_like` (`float`, shape=(2,)), optional
        A string or two-element array specifying the location of the legend.
    legend_ft_size : `float`, optional
        The font size of the legend.
    major_xtick_len : `float`, optional
        The length of the major ticks on the x-axis.
    minor_xtick_len : `float`, optional
        The length of the minor ticks on the x-axis.
    major_ytick_len : `float`, optional
        The length of the major ticks on the y-axis.
    minor_ytick_len : `float`, optional
        The length of the minor ticks on the y-axis.
    major_xtick_spacing : `float`, optional
        The spacing between adjacent major ticks on the x-axis.
    minor_xtick_spacing : `float`, optional
        The spacing between adjacent minor ticks on the x-axis.
    major_ytick_spacing : `float` | `array_like` (`float`, shape=(2,)), optional
        If ``major_ytick_spacing`` is of type `float`, then 
        ``major_ytick_spacing`` specifies the spacing between adjacent major
        ticks on both y-axes. Otherwise, ``major_ytick_spacing[0]``
        (``major_ytick_spacing[1]``) specifies the spacing between adjacent 
        major ticks on the left (right) y-axis.
    minor_ytick_spacing : `float` | `array_like` (`float`, shape=(2,)), optional
        If ``minor_ytick_spacing`` is of type `float`, then 
        ``minor_ytick_spacing`` specifies the spacing between adjacent minor
        ticks on both y-axes. Otherwise, ``minor_ytick_spacing[0]``
        (``minor_ytick_spacing[1]``) specifies the spacing between adjacent 
        minor ticks on the left (right) y-axis.
    tick_label_ft_size : `float`, optional
        The font size of the tick labels.
    title : `str`, optional
        Title of plot.
    title_ft_size : `float`, optional
        Title font size.
    fig_label : `str`, optional
        The figure label.
    fig_label_coords : `array_like` ('float', ndim=1, length=2), optional
        The position of the figure label.
    fig_label_ft_size : `float`, optional
        A positive float that specifies the font size of the figure label.
    aspect : `str` | `float`, optional
        A string or positive float that specifies the aspect ratio of the
        figure.
    scale : `float`, optional
        The size of the figure.
    filename : `str` | `None`, optional
        If set to a `str`, the resulting figure will be saved to the path
        ``filename``, otherwise the figure will not be saved.
    img_fmt : `str`, optional
        Image format.
    show : `bool`, optional
        If set to `True`, show the plot, otherwise do not show the plot.

    Attributes
    ----------
    Same as parameters.
    """
    def __init__(self,
                 xy_data_sets,
                 scatterplot=False, colors=None, markers=None, markersize=11,
                 vlines=[], hlines=[],
                 vline_kwargs_set=None, hline_kwargs_set=None,
                 linestyles=None, linewidth=3, grid_linewidth=0,
                 x_lims=[None, None], y_lims=[None, None],
                 x_log_scale=False, y_log_scale=False,
                 x_label='', y_label='', xy_label_ft_size=20,
                 legend_labels=None, legend_loc='best', legend_ft_size=18,
                 major_xtick_len=8, minor_xtick_len=5,
                 major_ytick_len=8, minor_ytick_len=5,
                 major_xtick_spacing=None, minor_xtick_spacing=None,
                 major_ytick_spacing=None, minor_ytick_spacing=None,
                 tick_label_ft_size=18,
                 title='', title_ft_size=20,
                 fig_label='', fig_label_coords=[0.05, 0.93],
                 fig_label_ft_size=20,
                 aspect='auto', scale=1,
                 filename=None, img_fmt='pdf', show=True):
        self.xy_data_sets = xy_data_sets

        self.scatterplot = scatterplot
        self.colors = colors
        self.markers = markers
        self.markersize = markersize

        self.vlines = vlines
        self.hlines = hlines
        self.vline_kwargs_set = vline_kwargs_set
        self.hline_kwargs_set = hline_kwargs_set
        
        self.linestyles = linestyles
        self.linewidth = linewidth
        self.grid_linewidth = grid_linewidth
        
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

        self.title = title
        self.title_ft_size = title_ft_size
        
        self.fig_label = fig_label
        self.fig_label_coords = fig_label_coords
        self.fig_label_ft_size = fig_label_ft_size

        self.aspect = aspect
        self.scale = scale

        self.filename = filename
        self.img_fmt = img_fmt
        self.show = show
        
        return None



def single_plot(params):
    r"""Generate and a single plot based on the parameters ``params``.

    Parameters
    -----------
    params : :class:`SinglePlotParams`
        The plotting parameters.

    Returns
    -------

    """
    mpl.rcParams['text.usetex'] = True

    fig = plt.figure()
    ax_1 = fig.add_subplot(111)
    ax_2 = ax_1.twinx()



    xy_data_sets = params.xy_data_sets
    try:
        num_left_xy_data_sets = len(xy_data_sets[0])
        num_right_xy_data_sets = len(xy_data_sets[1])
        left_xy_data_sets = xy_data_sets[0]
        right_xy_data_sets = xy_data_sets[1]
    except TypeError as e:
        num_left_xy_data_sets = len(xy_data_sets)
        num_right_xy_data_sets = 0
        left_xy_data_sets = xy_data_sets
        right_xy_data_sets = []
    num_xy_data_sets = num_left_xy_data_sets + num_right_xy_data_sets
        
    legend_labels = params.legend_labels
    if legend_labels == None:
        no_legend = True
        left_legend_labels = [None] * num_left_xy_data_sets
        right_legend_labels = [None] * num_right_xy_data_sets
    else:
        no_legend = False
        if isinstance(legend_labels[0], str):
            left_legend_labels = legend_labels
            right_legend_labels = []
        else:
            left_legend_labels = legend_labels[0]
            right_legend_labels = legend_labels[1]

    colors = params.colors
    if colors == None:
        left_colors = [None] * num_left_xy_data_sets
        right_colors = [None] * num_right_xy_data_sets
    else:
        if isinstance(colors, str):
            left_colors = [colors] * num_left_xy_data_sets
            right_colors = [colors] * num_right_xy_data_sets
        elif isinstance(colors[0], str):
            left_colors = colors
            right_colors = []
        else:
            left_colors = colors[0]
            right_colors = colors[1]

    markersize = params.markersize        
    markers = params.markers        
    if markers == None:
        left_markers = [None] * num_left_xy_data_sets
        right_markers = [None] * num_right_xy_data_sets
    else:
        if isinstance(markers, str):
            left_markers = [markers] * num_left_xy_data_sets
            right_markers = [markers] * num_right_xy_data_sets
        elif isinstance(markers[0], str):
            left_markers = markers
            right_markers = []
        else:
            left_markers = markers[0]
            right_markers = markers[1]

    linewidth = params.linewidth
    linestyles = params.linestyles        
    if linestyles == None:
        left_linestyles = [None] * num_left_xy_data_sets
        right_linestyles = [None] * num_right_xy_data_sets
    else:
        if isinstance(linestyles, str):
            left_linestyles = [linestyles] * num_left_xy_data_sets
            right_linestyles = [linestyles] * num_right_xy_data_sets
        elif isinstance(linestyles[0], str):
            left_linestyles = linestyles
            right_linestyles = []
        else:
            left_linestyles = linestyles[0]
            right_linestyles = linestyles[1]

    scatterplot = params.scatterplot
    if isinstance(scatterplot, bool):
        left_scatterplot = scatterplot
        right_scatterplot = scatterplot
    else:
        left_scatterplot = scatterplot[0]
        right_scatterplot = scatterplot[1]

    y_log_scale = params.y_log_scale
    if isinstance(y_log_scale, bool):
        left_y_log_scale = y_log_scale
        right_y_log_scale = y_log_scale
    else:
        left_y_log_scale = y_log_scale[0]
        right_y_log_scale = y_log_scale[1]

    y_label = params.y_label
    if isinstance(y_label, str):
        left_y_label = y_label
        right_y_label = None
    else:
        left_y_label = y_label[0]
        right_y_label = y_label[1]

    y_lims = params.y_lims
    try:
        y_lims[0][0]
        left_y_lims = y_lims[0]
        right_y_lims = y_lims[1]
    except TypeError as e:
        left_y_lims = y_lims
        right_y_lims = y_lims

    major_ytick_spacing = params.major_ytick_spacing
    if major_ytick_spacing == None:
        left_major_ytick_spacing = None
        right_major_ytick_spacing = None
    else:
        try:
            major_ytick_spacing[0][0]
            left_major_ytick_spacing = major_ytick_spacing[0]
            right_major_ytick_spacing = major_ytick_spacing[1]
        except TypeError as e:
            left_major_ytick_spacing = major_ytick_spacing
            right_major_ytick_spacing = major_ytick_spacing

    minor_ytick_spacing = params.minor_ytick_spacing
    if minor_ytick_spacing == None:
        left_minor_ytick_spacing = None
        right_minor_ytick_spacing = None
    else:
        try:
            minor_ytick_spacing[0][0]
            left_minor_ytick_spacing = minor_ytick_spacing[0]
            right_minor_ytick_spacing = minor_ytick_spacing[1]
        except TypeError as e:
            left_minor_ytick_spacing = minor_ytick_spacing
            right_minor_ytick_spacing = minor_ytick_spacing



    plot_handles = []
    for idx in range(num_left_xy_data_sets):
        x = left_xy_data_sets[idx].x
        y = left_xy_data_sets[idx].y

        xerr = left_xy_data_sets[idx].xerr
        yerr = left_xy_data_sets[idx].yerr

        if left_scatterplot:
            plot_handles.append(ax_1.errorbar(x, y, xerr=xerr, yerr=yerr,
                                              marker=left_markers[idx],
                                              c=left_colors[idx],
                                              markersize=markersize,
                                              label=left_legend_labels[idx],
                                              ls='none'))
        else:
            plot_handles.append(ax_1.errorbar(x, y, xerr=xerr, yerr=yerr,
                                              ls=left_linestyles[idx],
                                              c=left_colors[idx], lw=linewidth,
                                              label=left_legend_labels[idx],
                                              marker=left_markers[idx],
                                              markersize=markersize))

    for idx in range(num_right_xy_data_sets):
        x = right_xy_data_sets[idx].x
        y = right_xy_data_sets[idx].y

        xerr = right_xy_data_sets[idx].xerr
        yerr = right_xy_data_sets[idx].yerr

        if right_scatterplot:
            plot_handles.append(ax_2.errorbar(x, y, xerr=xerr, yerr=yerr,
                                              marker=right_markers[idx],
                                              c=right_colors[idx],
                                              markersize=markersize,
                                              label=right_legend_labels[idx],
                                              ls='none'))
        else:
            plot_handles.append(ax_2.errorbar(x, y, xerr=xerr, yerr=yerr,
                                              ls=right_linestyles[idx],
                                              c=right_colors[idx], lw=linewidth,
                                              label=right_legend_labels[idx],
                                              marker=right_markers[idx],
                                              markersize=markersize))



    if params.vline_kwargs_set == None:
        params.vline_kwargs_set = [{}]*len(params.vlines)
    if params.hline_kwargs_set == None:
        params.hline_kwargs_set = [{}]*len(params.hlines)

    for vline, vline_kwargs in zip(params.vlines, params.vline_kwargs_set):
        ax_1.axvline(x=vline, **vline_kwargs)

    for hline, hline_kwargs in zip(params.hlines, params.hline_kwargs_set):
        ax_1.axhline(x=hline, **hline_kwargs)


            
    legend_loc = params.legend_loc
    legend_ft_size = params.legend_ft_size
    if no_legend:
        pass
    else:
        ax_1.legend(handles=plot_handles,
                    labels=[handle.get_label() for handle in plot_handles],
                    loc=legend_loc, frameon=True, fontsize=legend_ft_size)



    grid_linewidth = params.grid_linewidth
    if grid_linewidth != 0:
        ax_1.grid(linewidth=grid_linewidth)


    
    fig_label = params.fig_label
    fig_label_coords = params.fig_label_coords
    fig_label_ft_size = params.fig_label_ft_size
    ax_1.text(fig_label_coords[0], fig_label_coords[1], fig_label,
              fontsize=fig_label_ft_size, horizontalalignment='center',
              verticalalignment='center', transform=ax_1.transAxes)



    x_label = params.x_label
    y_label = params.y_label
    xy_label_ft_size = params.xy_label_ft_size
    ax_1.set_xlabel(x_label, fontsize=xy_label_ft_size)
    ax_1.set_ylabel(left_y_label, fontsize=xy_label_ft_size)
    ax_2.set_ylabel(right_y_label,
                    fontsize=xy_label_ft_size,
                    rotation=270, labelpad=25)



    if params.x_log_scale == True:
        ax_1.set_xscale('log')
    if left_y_log_scale == True:
        ax_1.set_yscale('log')
    if right_y_log_scale == True:
        ax_2.set_yscale('log')
    
    x_lims = params.x_lims
    ax_1.set_xlim(x_lims[0], x_lims[1])
    ax_1.set_ylim(left_y_lims[0], left_y_lims[1])
    ax_2.set_ylim(right_y_lims[0], right_y_lims[1])



    tick_label_ft_size = params.tick_label_ft_size
    
    major_xtick_len = params.major_xtick_len
    minor_xtick_len = params.minor_xtick_len
    major_ytick_len = params.major_ytick_len
    minor_ytick_len = params.minor_ytick_len

    major_xtick_spacing = params.major_xtick_spacing
    minor_xtick_spacing = params.minor_xtick_spacing

    plt.minorticks_on()
    
    if major_xtick_spacing != None:
        x_major_locator = MultipleLocator(major_xtick_spacing)
        ax_1.xaxis.set_major_locator(x_major_locator)
    if minor_xtick_spacing != None:
        x_minor_locator = MultipleLocator(minor_xtick_spacing)
        ax_1.xaxis.set_minor_locator(x_minor_locator)

    if left_major_ytick_spacing != None:
        y_major_locator = MultipleLocator(left_major_ytick_spacing)
        ax_1.yaxis.set_major_locator(y_major_locator)
    if left_minor_ytick_spacing != None:
        y_minor_locator = MultipleLocator(left_minor_ytick_spacing)
        ax_1.yaxis.set_minor_locator(y_minor_locator)

    if right_major_ytick_spacing != None:
        y_major_locator = MultipleLocator(right_major_ytick_spacing)
        ax_2.yaxis.set_major_locator(y_major_locator)
    if right_minor_ytick_spacing != None:
        y_minor_locator = MultipleLocator(right_minor_ytick_spacing)
        ax_2.yaxis.set_minor_locator(y_minor_locator)
    
    ax_1.xaxis.set_ticks_position('both')
    ax_1.yaxis.set_ticks_position('left')
    ax_2.yaxis.set_ticks_position('right')
    
    ax_1.tick_params(axis='x', which='major',
                     labelsize=tick_label_ft_size,
                     width=2.0 * linewidth / 3.0,
                     length=major_xtick_len, direction='in')
    ax_1.tick_params(axis='x', which='minor',
                     width=2.0 * linewidth / 3.0,
                     length=minor_xtick_len, direction='in')

    ax_1.tick_params(axis='y', which='major',
                     labelsize=tick_label_ft_size,
                     width=2.0 * linewidth / 3.0,
                     length=major_ytick_len, direction='in')
    ax_1.tick_params(axis='y', which='minor',
                     width=2.0 * linewidth / 3.0,
                     length=minor_ytick_len, direction='in')

    if num_right_xy_data_sets == 0:
        labelright = False
        y_min, y_max = ax_1.get_ylim()
        y_ticks = ax_1.get_yticks(minor=True)
        ax_2.set_yticks(y_ticks, minor=True)
        ax_2.set_ylim(y_min, y_max)
    else:
        labelright = True
    ax_2.tick_params(axis='y', which='major',
                     labelsize=tick_label_ft_size,
                     width=2.0 * linewidth / 3.0,
                     length=major_ytick_len, direction='in',
                     labelright=labelright)
    ax_2.tick_params(axis='y', which='minor',
                     width=2.0 * linewidth / 3.0,
                     length=minor_ytick_len, direction='in',
                     labelright=labelright)



    for axis in ['top', 'bottom', 'left', 'right']:
        ax_1.spines[axis].set_linewidth(2.0 * linewidth / 3.0)
        ax_2.spines[axis].set_linewidth(2.0 * linewidth / 3.0)



    ax_1.set_title(params.title, fontsize=params.title_ft_size)



    aspect = params.aspect
    ax_1.set_aspect(aspect)
    ax_2.set_aspect(aspect)

    scale = params.scale
    fig_dims = fig.get_size_inches()
    fig.set_figwidth(fig_dims[0] * scale)
    fig.set_figheight(fig_dims[1] * scale)



    fig.tight_layout(pad=1.08)
    if params.show:
        plt.show()
    if isinstance(params.filename, str):
        plt.savefig(params.filename, format=params.img_fmt)

    return None



class SingleImshowParams():
    r"""Data class to store parameters for the function :func:`single_imshow`.

    Parameters
    -----------
    z : array_like(`float`, ndim=2)
        The data to be represented as a 2D image.
    cmap : `str` | :class:`matplotlib.colors.Colormap` | `None`, optional
        Colormap used to map scalar data to color.
    norm : :class:`matplotlib.colors.Normalize` | `None`, optional
        Lower limit to the data range that the colormap covers.
    interpolation : `str` | `None`, optional
        The interpolation method used in generating the image.
    append_axes_kwargs : `dict`, optional
        Keyword arguments specifying the positioning and size of the colorbar
        axis.
    colorbar_kwargs : `dict`, optional
        Keyword arguments specifying properties of colorbar.
    xticks : array_like(`int`, ndim=1) | `None`, optional
        Positions of ticks along x-axis.
    yticks : array_like(`int`, ndim=1) | `None`, optional
        Positions of ticks along y-axis.
    cbticks : array_like(`int`, ndim=1) | `None`, optional
        Positions of colorbar ticks.
    xticklabels : array_like(`str`, ndim=1, length=len(``xticks``)) | `None`, optional
        Tick labels along x-axis.
    yticklabels : array_like(`str`, ndim=1, length=len(``yticks``)) | `None`, optional
        Tick labels along y-axis.
    cbticklabels : array_like(`str`, ndim=1, length=len(``xticks``)) | `None`, optional
        Colorbar tick labels along x-axis.
    xtick_len : `float`, optional
        Length of ticks along x-axis.
    ytick_len : `float`, optional
        Length of ticks along y-axis.
    cbtick_len : `float`, optional
        Length of colobar ticks.
    xtick_width : `float`, optional
        Width of ticks along x-axis.
    ytick_width : `float`, optional
        Width of ticks along y-axis.
    cbtick_width : `float`, optional
        Width of colobar ticks.
    tick_label_ft_size : `float`, optional
        Font size of tick labels.
    vlines : array_like(`float`, ndim=1), optional
        Positions of vertical lines along x-axis.
    hlines : array_like(`float`, ndim=1), optional
        Positions of vertical lines along y-axis.
    vline_kwargs : `dict`, optional
        Keyword arguments specifying line properties of vertical lines.
    hline_kwargs : `dict`, optional
        Keyword arguments specifying line properties of horizontal lines.
    frame_thickness : `float`, optional
        Thickness of image frame.
    x_label : `str`, optional
        Specifies the x-axis label.
    y_label : `str`, optional
        Specifies the y-axis label.
    xy_label_ft_size : `float`, optional
        Font size of the x and y axis labels.
    title : `str`, optional
        Title of plot.
    title_ft_size : `float`, optional
        Title font size.
    fig_label : `str`, optional
        Figure label.
    fig_label_coords : array_like(`float`, ndim=1, length=2), optional
        Position of the figure label with respect to the coordinate system of
        the axes.
    fig_label_ft_size : `float`, optional
        Font size of figure label.
    aspect : `str` | `float`, optional
        Aspect ratio of figure.
    scale : `float`, optional
        Size of figure.
    filename : `str` | `None`, optional
        If set to a `str`, the resulting figure will be saved to the path
        ``filename``, otherwise the figure will not be saved.
    img_fmt : `str`, optional
        Image format.
    show : `bool`, optional
        If set to `True`, show the plot, otherwise do not show the plot.

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
                 aspect='auto', scale=1.,
                 filename=None, img_fmt='pdf', show=True):
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

        self.filename = filename
        self.img_fmt = img_fmt
        self.show = show
        
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
    if params.show:
        plt.show()
    if isinstance(params.filename, str):
        plt.savefig(params.filename, format=params.img_fmt)

    return None



class SingleHistParams():
    r"""Data class to store parameters for the function :func:`single_hist`.

    Parameters
    -----------
    x_data_sets : array_like(:class:`prettyplots.XData`, ndim=1)
        The x data sets to be plotted. Should be an array with elements
        :class:`prettyplots.XData`.
    bins : `int` | array_like(`float`, ndim=1), optional
        If set to an `int`, then a histogram with ``bins+1`` bin edges will be
        constructed, equally spaced across the full data range. If set to an
        array, then a histogram will be constructed with bin edges given by
        ``bins``.
    cumulative : `bool` | `float`, optional
        If set to `True`, then for each data set, a histogram is computed where 
        each in gives the counts in that bin plus all bins for smaller values. 
        If set to a negative number, then the direction of accumulation is 
        reversed. If set `False`, then no accumulation is performed. 
    normalized : `bool`, optional
        If set to `True`, then for each data set, the histogram is normalized.
        If set to `False`, no normalization is performed.
    colors : `str` | array_like(`str`, ndim=1), optional
        A string or an array of strings specifying the colors for each data set.
    alphas : `float` | array_like(`float`, ndim=1), optional
        If set to a `float`, then the same transparency level is applied to each
        data set. If set to an array, then ``alphas[i]`` corresponds to the
        transparency level for the :math:`i^{\text{th}}` data set. Note that
        a transparency value of 1 corresponds to no transparency, whereas a
        value of zero corresponds to a completely transparent histogram.
    axes_linewidth : `float`, optional
        A positive float that specifies a characteristic linewidth used to
        determine the width of the axes, and ticks.
    bar_edge_width : `float`, optional
        A positive float that specifies the width of the histogram bar edges.
    x_lims : array_like(`float`, ndim=1, length=2), optional
        Specifies the plotting range along the x-axis: x_lims[0] = x-min; 
        x_lims[1] = x-max.
    y_lims : array_like(`float`, ndim=1, length=2), optional
        Specifies the plotting range along the y-axis: y_lims[0] = y-min; 
        y_lims[1] = y-max.
    x_log_scale : `bool`, optional
        If true, then a logarithmic scale is used for the x-axis, otherwise it
        is not used.
    y_log_scale : `bool`, optional
        If true, then a logarithmic scale is used for the y-axis, otherwise it
        is not used.
    x_label : `str`, optional
        Specifies the x-axis label.
    y_label : `str`, optional
        Specifies the y-axis label.
    xy_label_ft_size : `float`, optional
        A positive float that specifies the font size of the x and y axes
        labels.
    title : `str`, optional
        Title of plot.
    title_ft_size : `float`, optional
        Title font size.
    legend_labels : array_like(`str`, ndim=1), optional
        An array of strings specifying the curve labels of each data set.
    legend_loc : `str` | array_like(`float`, ndim=1, length=2), optional
        A string or two-element array specifying the location of the legend.
    legend_ft_size : `float`, optional
        A positive float that specifies the font size of the legend.
    major_xtick_len : `float`, optional
        A positive float that specifies the length of the major ticks on the
        x-axis.
    minor_xtick_len : `float`, optional
        A positive float that specifies the length of the minor ticks on the
        x-axis.
    major_ytick_len : `float`, optional
        A positive float that specifies the length of the major ticks on the
        y-axis.
    minor_ytick_len : `float`, optional
        A positive float that specifies the length of the minor ticks on the
        y-axis.
    major_xtick_spacing : `float`, optional
        A positive float that specifies the spacing between adjacent major ticks
        on the x-axis.
    minor_xtick_spacing : `float`, optional
        A positive float that specifies the spacing between adjacent minor ticks
        on the x-axis.
    major_ytick_spacing : `float`, optional
        A positive float that specifies the spacing between adjacent major ticks
        on the y-axis.
    minor_ytick_spacing : `float`, optional
        A positive float that specifies the spacing between adjacent minor ticks
        on the y-axis.
    tick_label_ft_size : `float`, optional
        A positive float that specifies the font size of the tick labels.
    fig_label : `str`, optional
        A string that specifies the figure label.
    fig_label_coords : array_like('float', ndim=1, length=2), optional
        An array that specifies the position of the figure label.
    fig_label_ft_size : `float`, optional
        A positive float that specifies the font size of the figure label.
    aspect : `str` | `float`, optional
        A string or positive float that specifies the aspect ratio of the
        figure.
    scale : `float`, optional
        A positive float that specifies the size of the figure.
    filename : `str` | `None`, optional
        If set to a `str`, the resulting figure will be saved to the path
        ``filename``, otherwise the figure will not be saved.
    img_fmt : `str`, optional
        Image format.
    show : `bool`, optional
        If set to `True`, show the plot, otherwise do not show the plot.

    Attributes
    ----------
    Same as parameters.
    """
    def __init__(self,
                 x_data_sets,
                 bins=10,
                 cumulative=False,
                 normalized=False,
                 colors=None, alphas=0.8, axes_linewidth=3, bar_edge_width=2,
                 x_lims=[None, None], y_lims=[None, None],
                 x_log_scale=False, y_log_scale=False,
                 x_label='', y_label='', xy_label_ft_size=20,
                 title='', title_ft_size=20,
                 legend_labels=None, legend_loc='best', legend_ft_size=18,
                 major_xtick_len=8, minor_xtick_len=5,
                 major_ytick_len=8, minor_ytick_len=5,
                 major_xtick_spacing=None, minor_xtick_spacing=None,
                 major_ytick_spacing=None, minor_ytick_spacing=None,
                 tick_label_ft_size=18,
                 fig_label='', fig_label_coords=[0.05, 0.93],
                 fig_label_ft_size=20,
                 aspect='auto', scale=1,
                 filename=None, img_fmt='pdf', show=True):
        self.x_data_sets = x_data_sets
        self.bins = bins
        self.cumulative = cumulative
        self.normalized = normalized

        self.colors = colors
        self.alphas = alphas
        
        self.axes_linewidth = axes_linewidth
        self.bar_edge_width = bar_edge_width
        
        self.x_lims = x_lims
        self.y_lims = y_lims
        self.x_log_scale = x_log_scale
        self.y_log_scale = y_log_scale

        self.x_label = x_label
        self.y_label = y_label
        self.xy_label_ft_size = xy_label_ft_size

        self.title = title
        self.title_ft_size = title_ft_size

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

        self.filename = filename
        self.img_fmt = img_fmt
        self.show = show
        
        return None



def single_hist(params):
    r"""Generate a histogram plot based on the parameters specified in params.

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



    x_data_sets = params.x_data_sets
    num_x_data_sets = len(x_data_sets)

    cumulative = params.cumulative
    normalized = params.normalized
    if cumulative == False:
        hist_type = "bar"
        bar_edge_width = None
    else:
        hist_type = "step"
        bar_edge_width = params.bar_edge_width
    
    legend_labels = params.legend_labels
    no_legend = False
    if legend_labels == None:
        legend_labels = [None] * num_x_data_sets
        no_legend = True

    colors = params.colors
    if colors == None:
        colors = [None] * num_x_data_sets
    else:
        colors = _to_np_array(colors)
        if colors.size == 1:
            colors = np.resize(colors, num_x_data_sets)

    alphas = _to_np_array(params.alphas)
    if alphas.size == 1:
        alphas = np.resize(alphas, num_x_data_sets)


        
    for idx in range(num_x_data_sets):
        x = x_data_sets[idx].x
        
        bins = params.bins
        if isinstance(bins, int):
            bins = np.linspace(np.amin(x), np.amax(x), num=bins+1)
        bins = np.sort(bins)

        if params.x_log_scale == True:
            log_bins = np.logspace(np.log10(bins[0]),
                                   np.log10(bins[-1]),
                                   len(bins))

            ax.hist(x, bins=log_bins, linewidth=bar_edge_width,
                    alpha=alphas[idx], histtype=hist_type,
                    cumulative=cumulative, density=normalized,
                    facecolor=colors[idx], label=legend_labels[idx])
            
        else:
            ax.hist(x, bins=bins, linewidth=bar_edge_width, 
                    alpha=alphas[idx], histtype=hist_type, 
                    cumulative=cumulative, density=normalized,
                    facecolor=colors[idx], label=legend_labels[idx])

    # Need to plot twice to avoid transparent bar edges.
    if hist_type == "bar":
        bar_edge_width = params.bar_edge_width
            
        for idx in range(num_x_data_sets):
            x = x_data_sets[idx].x
        
            bins = params.bins
            if isinstance(bins, int):
                bins = np.linspace(np.amin(x), np.amax(x), num=bins+1)
                bins = np.sort(bins)

            if params.x_log_scale == True:
                log_bins = np.logspace(np.log10(bins[0]),
                                       np.log10(bins[-1]),
                                       len(bins))

                ax.hist(x, bins=log_bins,
                        facecolor="None", density=normalized,
                        edgecolor='black', linewidth=bar_edge_width)
            
            else:
                ax.hist(x, bins=bins,
                        facecolor="None", density=normalized,
                        edgecolor='black', linewidth=bar_edge_width)



    legend_loc = params.legend_loc
    legend_ft_size = params.legend_ft_size
    if no_legend:
        pass
    else:
        ax.legend(loc=legend_loc, frameon=True, fontsize=legend_ft_size)


    
    ax.set_title(params.title, fontsize=params.title_ft_size)



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

    axes_linewidth = params.axes_linewidth
    
    ax.tick_params(axis='x', which='major',
                   labelsize=tick_label_ft_size,
                   width=2.0 * axes_linewidth / 3.0,
                   length=major_xtick_len, direction='in')
    ax.tick_params(axis='x', which='minor',
                   width=2.0 * axes_linewidth / 3.0,
                   length=minor_xtick_len, direction='in')
    ax.tick_params(axis='y', which='major',
                   labelsize=tick_label_ft_size,
                   width=2.0 * axes_linewidth / 3.0,
                   length=major_ytick_len, direction='in')
    ax.tick_params(axis='y', which='minor',
                   width=2.0 * axes_linewidth / 3.0,
                   length=minor_ytick_len, direction='in')



    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(2.0 * axes_linewidth / 3.0)



    aspect = params.aspect
    ax.set_aspect(aspect)

    scale = params.scale
    fig_dims = fig.get_size_inches()
    fig.set_figwidth(fig_dims[0] * scale)
    fig.set_figheight(fig_dims[1] * scale)


    
    fig.tight_layout(pad=1.08)
    if params.show:
        plt.show()
    if isinstance(params.filename, str):
        plt.savefig(params.filename, format=params.img_fmt)

    return None
