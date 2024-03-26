import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc_forum_pageviews.csv')
df.date = pd.to_datetime(df.date)

# set the date column as index in the file
df.set_index('date', inplace=True)
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    """
        df_copy = df.copy()
        y = df_copy.value
  
        y.plot(kind='line', color='red', figsize=(16, 6))
        plt.xlabel("Date")
        plt.ylabel("Page Views")
        plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
   
        # Save image and return fig (don't change this part)
        fig = plt.gcf()
        fig.savefig('line_plot.png')
    
        return fig
    """
    df_copy = df.copy()
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df_copy.index, df_copy['value'], 'r', linewidth=1.2)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig

#draw_line_plot()
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.reset_index()
    df_bar['year'] = df_bar.date.dt.year
    df_bar['month'] = df_bar.date.dt.month
    df_bar = df_bar.groupby(['year', 'month'], sort=False)['value'].mean().round().unstack()
    
    # Draw bar plot
    df_bar.plot(kind='bar')
    plt.xlabel("Years")
    plt.ylabel('Average Page Views')
    plt.title('Average Daily Page Views by Month and Year')
    plt.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    #plt.show()
    # Save image and return fig (don't change this part)
    fig = plt.gcf()
    fig.savefig('bar_plot.png')
    return fig
#draw_bar_plot()
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # create figure and axe
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    # Draw box plots (using Seaborn)
    #colors = ['blue', 'orange', 'green', 'red']
    color = ["blue", "yellow", "red", "green"]
    sns.boxplot(data=df_box, x='Year', y='value', ax=axes[0], palette=color)
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')


    #color = ['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b','#e377c2','#7f7f7f','#bcbd50','#bcbd22',#'#ff9896','#aec7e8']
    colors = ["blue", "yellow", "red", "green", "orange", "purple", "pink", "teal", "brown", "black", "white", "gray"]
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], order=month_order, palette=colors)
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    # Save image and return fig (don't change this part)
    plt.tight_layout()
    fig = plt.gcf()
    fig.savefig('box_plot.png')
    return fig
#draw_box_plot()