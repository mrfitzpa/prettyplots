#!/usr/bin/env python
"""Contains printing functions to generate plotting templates for easy use.
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
__all__ = ["print_single_plot_template",
           "print_single_imshow_template",
           "print_single_hist_template"]



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
    print("grid_linewidth = 2")
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
    print("filename = None")
    print("img_fmt = 'pdf'")
    print("show = True")
    print()
    print()
    print()
    print("plot_params = prettyplots.SinglePlotParams(")
    print("                  xy_data_sets=xy_data_sets,")
    print("                  scatterplot=scatterplot, colors=colors, markers=markers,")
    print("                  markersize=markersize, linestyles=linestyles,")
    print("                  linewidth=linewidth, grid_linewidth=grid_linewidth",)
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
    print("                  aspect=aspect, scale=scale,")
    print("                  filename=filename, img_fmt=img_fmt, show=show)")
    print()
    print()
    print()
    print("prettyplots.single_plot(plot_params)")

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
    print("filename = None")
    print("img_fmt = 'pdf'")
    print("show = True")
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
    print("                  aspect=aspect, scale=scale,")
    print("                  filename=filename, img_fmt=img_fmt, show=show)")
    print()
    print()
    print()
    print("prettyplots.single_imshow(plot_params)")
    

    return None



def print_single_hist_template():
    r"""Prints a single histogram template (for quick use in notebooks).

    Parameters
    -----------

    Returns
    -------

    """
    print("x_data_sets = []")
    print("bins = 10")
    print("cumulative = False")
    print("normalized = False")
    print()
    print("colors = None")
    print("alphas = 0.7")
    print()
    print("axes_linewidth = 3")
    print("bar_edge_width = 2")
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
    print("filename = None")
    print("img_fmt = 'pdf'")
    print("show = True")
    print()
    print()
    print()
    print("plot_params = prettyplots.SingleHistParams(")
    print("                  x_data_sets=x_data_sets, bins=bins,")
    print("                  cumulative=cumulative, normalized=normalized,")
    print("                  colors=colors, alphas=alphas,")
    print("                  axes_linewidth=axes_linewidth,")
    print("                  bar_edge_width=bar_edge_width,")
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
    print("                  aspect=aspect, scale=scale,")
    print("                  filename=filename, img_fmt=img_fmt, show=show)")
    print()
    print()
    print()
    print("prettyplots.single_hist(plot_params)")

    return None
