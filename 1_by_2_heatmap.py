

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def one_by_two_columns_heatmap(frame, 
                               subplot1_values = "ED_MAIN_PE_LEAKS_2017" , 
                               subplot2_values = "ED_SER_PE_LEAKS_2017",
                               y_axis = "DECADE", 
                               x_axis = "MATERIAL", 
                               aggfunc = "count"):

    ''' This function create 2 plots  (1 row x 2 cols) and I make them 
    share same width and height as well as y axis values. The caviet 
    here is that y axes do not necessarily align when you plot 2 graps 
    with different patterns, hence the matplotlib argument yshare or xshare
    does not work here, because it only pick one of the y axis to share.
    I was required to customize yaxes in a way that 
    they are sorted and all y values are shared among plots'''
    

    # make two plots same width and create an independent plot for the heat bar legend:
    fig, (ax1, ax2, axcb) = plt.subplots(1, 3, gridspec_kw = {'width_ratios': [1,1,0.08]})
    # Keep it same height:
    ax1.get_shared_y_axes().join(ax2)  

    # condition 1:
    # Condition applied to the pivot table values to be displayed:
    cond1 = (frame[subplot1_values] > 0) 
    # Apply condition to dataframe
    frame_cond1 = frame[cond1]
    # Create pivot table from condition 1 dataframe:
    frame_cond1_pivot = frame_cond1.pivot_table(values   = subplot1_values,
                                                index    = y_axis,
                                                columns  = x_axis,
                                                aggfunc  = aggfunc).fillna(0).sort_values(by = y_axis)
    # Apply pivot table to generate heatmap for condition 1 pivot table:

    

    # condition 2:
    # # Condition applied to the pivot table values to be displayed:
    cond2 = (frame[subplot2_values] > 0) 
    # # Apply condition 2 to dataframe
    frame_cond2 = frame[cond2]
    # Create pivot table from condition 2 dataframe:
    frame_cond2_pivot = frame_cond2.pivot_table(values   = subplot2_values,
                                                index    = y_axis,
                                                columns  = x_axis,
                                                aggfunc  = aggfunc).fillna(0).sort_values(by = y_axis)
    
    # Reindex pivot table like subplot1 (ax1) so y axis values aligns exactly between ax1 = ax2:

    if len(frame_cond1_pivot.index) > len(frame_cond2_pivot.index):
        frame_cond2_pivot = frame_cond2_pivot.reindex_like(frame_cond1_pivot).fillna(0)
    else:
        frame_cond1_pivot = frame_cond1_pivot.reindex_like(frame_cond2_pivot).fillna(0)

    vmin_cond1 = frame_cond1_pivot.values.min()
    vmax_cond1 = frame_cond1_pivot.values.max()
    vmin_cond2 = frame_cond2_pivot.values.min()
    vmax_cond2 = frame_cond2_pivot.values.max()

    vmin = min([vmin_cond1, vmin_cond2])
    vmax = max([vmax_cond1, vmax_cond2])

    cond1_heatmap = sns.heatmap(data   = frame_cond1_pivot,
                                annot  = True,                               # Display number inside heatmap
                                fmt    = ".1f",                              # Rounding numbers to 1 decimal
                                cmap   = "Reds",                             # Seaborn Pallete with red gradients
                                ax     = ax1,                                # make this the subplot object ax1
                                vmin   = vmin,                               # Max value between the two heatmaps (automate this)
                                vmax   = vmax,                               # Min value
                                cbar   = False)                              # Removing this bar because I want one common bar
                                                                             # for all heatmaps
                                                                             # the other graph to vmax = 37 so I will keep that bar
    # Set ax1 subplot title:
    cond1_heatmap.set_title(subplot1_values)
    # Remove x label from ax1 plot - keep only ticks label:
    cond1_heatmap.set_xlabel('')
    # Remove xaxis ticks from ax1 plot:
    cond1_heatmap.xaxis.set_ticks_position('none')
    # Remove yaxis ticks from ax1 plot:
    cond1_heatmap.yaxis.set_ticks_position('none')
    # Set xaxis rotation tp zero of tick labels for ax1 plot:
    cond1_heatmap.set_xticklabels(cond1_heatmap.get_xticklabels(), rotation = 0)
    # Set yaxis rotation of tick labels for ax1 plot:
    cond1_heatmap.set_yticklabels(cond1_heatmap.get_yticklabels(), rotation = 0)

    

    # Apply pivot table to generate heatmap for condition 2 pivot table:
    cond2_heatmap = sns.heatmap(data  = frame_cond2_pivot,
                                annot = True,              # Display number inside heatmap
                                fmt   = ".1f",             # Rounding numbers to 1 decimal
                                cmap  = "Reds",            # Seaborn Pallete with red gradients
                                ax    = ax2,               # make this the subplot object ax2
                                vmax  = vmax,              # Max value between the two heatmaps (automate this)
                                vmin  = vmin,              # Min value
                                cbar_ax = axcb)            # adding the max value based on the highste value of the heatmap objects. 
    # Set ax2 subplot title:
    cond2_heatmap.set_title(subplot2_values)
    # Remove y label from ax2 plot - we only need ax1 y label since both plot are aligned:
    cond2_heatmap.set_ylabel('')                            
    # Remove x label and keep tick x ticl labels:
    cond2_heatmap.set_xlabel('')                            
    # Remove ax2 x ticks:
    cond2_heatmap.xaxis.set_ticks_position('none')          
    # Remove ax2 y ticks
    cond2_heatmap.yaxis.set_ticks_position('none')          
    # Keep ax2 xtick labels with certain rotation:
    cond2_heatmap.set_xticklabels(cond2_heatmap.get_xticklabels(), rotation = 0)  # impose 0 rotation
    # Keep ax2 ytick labels with certain rotation:
    cond2_heatmap.set_yticklabels(cond2_heatmap.get_yticklabels(), rotation = 0)  # impose 0 rotation
    # If I want to remove the tick labels when y axis is perfect aligend between the two graphs. 
    cond2_heatmap.set_yticklabels('') 

    #return frame_cond1_pivot

    plt.show()

    

one_by_two_columns_heatmap(data_for_gas_asset_ed_plots, 
                               subplot1_values = "ED_MAIN_PE_LEAKS_2017" , 
                               subplot2_values = "ED_SER_PE_LEAKS_2017",
                               y_axis = "DECADE", 
                               x_axis = "MATERIAL", 
                               aggfunc = "count")

one_by_two_columns_heatmap(data_for_gas_asset_ed_plots, 
                               subplot1_values = "ED_MAIN_ST_LEAKS_2017" , 
                               subplot2_values = "ED_SER_ST_LEAKS_2017",
                               y_axis = "DECADE", 
                               x_axis = "MATERIAL", 
                               aggfunc = "count")