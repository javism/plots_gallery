import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

with plt.xkcd():
    
    num_guides = (2,0,0,0,3,2,4,26,51,51,9)
    n_groups = len(num_guides)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4

    rects1 = ax.bar(index, num_guides, bar_width,
                    alpha=opacity, color='g',
                    label='Guides')

    plt.annotate(
        'Last update \n April 2020',
        xy=(10,10), arrowprops=dict(arrowstyle='->'), xytext=(5, 30))

    ax.set_xlabel('Year')
    ax.set_ylabel('Number guides')
    ax.set_title('AI Ethics Guidelines Global Inventory')
    ax.set_xticks(index + bar_width / 2 - 0.15)
    ax.set_xticklabels(['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'], rotation=50)
    ax.legend()


    fig.tight_layout()

plt.show()