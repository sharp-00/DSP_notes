# Plot the data of all India rainfall along with summary stats

import pandas as pd 
import matplotlib.pyplot as plt


if __name__ == "__main__":
        
    #load data
    df = pd.read_csv("./all-india-monthly-rainfall.csv", index_col=0)

    #extract the data for the color map plot
    years = df.index
    months = df.columns
    aimr = df
   
    # print(df.shape, years.shape, months.shape)
    
    

    #initialize figure
    fig = plt.figure(figsize=[8,8])

    #create axes instances for plotting  #left margin, bottom margin, width, height
    ax_cmp = fig.add_axes([0.3, 0.35, 0.5, 0.5]) 
    ax_cb = fig.add_axes([0.85, 0.35, 0.03, 0.5])
    #ax_yrl = ax_cmp.twiny()
    #ax_yrl.set_position([0.1, 0.35, 0.2, 0.5])
    ax_yrl = fig.add_axes([0.1, 0.35, 0.2, 0.5])
    ax_mth = fig.add_axes([0.3, 0.1, 0.5, 0.25])
    

    #plot the colormap
    cm = ax_cmp.pcolormesh(months, years, aimr, cmap="viridis")
    cb = plt.colorbar(cm, cax=ax_cb)

    #plot the aimr monthly time series over years
    ax_yrl.plot(aimr, years, color="gray", lw=0.75, alpha=0.65)
    ax_yrl.plot(aimr.mean(axis=1), years, color="r",lw=1, alpha=1 )
    #try to plot the error bars with the mean(to show uncertainity), remove the other lines)

    #plot the monthly averages as a bar chart
    ax_mth.bar(x=months, height=aimr.mean(axis=0), color="sandybrown")
    
    #plot customisations
    ylims = ax_mth.get_ylim()
    ax_mth.set_ylim(ylims[::-1])

    #axis not aligned

    #show results
    plt.show()
