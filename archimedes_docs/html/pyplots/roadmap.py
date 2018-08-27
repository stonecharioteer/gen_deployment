# -*- coding: utf-8 -*-
"""
This file is adapted from https://matplotlib.org/devdocs/gallery/lines_bars_and_markers/timeline.html

"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
import csv
names = []
dates = []

with open("roadmap.csv", "r") as f:
    reader = csv.reader(f)
    next(reader, None) # skip the header.
    for row in reader:
        dates.append(row[0])
        names.append(row[1])
dates = [datetime.strptime(ii, "%Y-%m-%d") for ii in dates]
levels = np.array([-5, 5, -3, 3, -1, 1])
fig, ax = plt.subplots(figsize=(12, 10))

# Create the base line
start = min(dates)
stop = max(dates)
ax.plot((start, stop), (0, 0), 'k', alpha=.5)

# Iterate through releases annotating each one
for ii, (iname, idate) in enumerate(zip(names, dates)):
    level = levels[ii % 6]
    vert = 'top' if level < 0 else 'bottom'
    # Place a point on the horizontal axis.
    ax.scatter(idate, 0, s=20, facecolor='w', edgecolor='k', zorder=9999)
    # Plot a line up to the text
    ax.plot((idate, idate), (0, level), c='r', alpha=.7)
    # Give the text a faint background and align it properly
    ax.text(idate, level, iname,
            horizontalalignment='center', verticalalignment=vert, fontsize=8,
            backgroundcolor=(1., 1., 1., .3))
ax.set(title="Archimedes Development Roadmap")

# Set the xticks formatting
# format xaxis with 3 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=1))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
fig.autofmt_xdate()

# Remove components for a cleaner look
plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
        list(ax.spines.values())), visible=False)
plt.show()
