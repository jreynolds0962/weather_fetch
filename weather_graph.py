# get weather data for past week
# make sure data is in FH (fareinheit)
# plot each degree in FH
# X axis should be days of the week
# Y axis should be degrees
# Graph should be line plot


# import libraries matplotlib and requsts (for api)
from urllib.request import HTTPDigestAuthHandler
import cped
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import datetime
import retreive_weather


# Required: key, url 
# Optional: city="null", days=7, units="imperial", lat="33.44", lon="-94.04"



#Updating weather list
weather = retreive_weather.weather
# date formated to readable text
for i in range(0,8):
    weather[i][0] = datetime.datetime.fromtimestamp(weather[i][0]).strftime('%Y-%m-%d')
date = []
lows = []
highs = []
for i in range(0,8):
    date.append(weather[i][0])
    lows.append(weather[i][1])
    highs.append(weather[i][2])
highest = max(highs)
lowest = min(lows)


#Color pallete of graph
color_palette = sns.color_palette("OrRd", n_colors=len(highs))
colors = np.linspace(0, 1, len(highs))
color_palette = sns.color_palette("coolwarm", n_colors=len(highs)).as_hex()



# ----------------- Creating bar graph --------------------

# Set the figure size
plt.figure(figsize=(10, 6))

# Plot the bars
plt.bar(range(len(highs)), highs, color=color_palette, alpha=0.7)
plt.bar(range(len(lows)), lows, color=color_palette, alpha=0.7)

# Set the x-axis ticks and labels
plt.xticks(range(len(highs)), date)

# Set the y-axis label
plt.ylabel('Temperature (°F)')

# Add a legend
plt.legend(['Max Temperature', 'Min Temperature'])

# Show the plot
plt.show()


# plt.bar(x=date, height=highs)
# plt.ylim(lowest-30, highest+30)
# plt.title("temperature ranges for the past 7 in city")
# plt.show()
#print(weather)



# x axis is date
# Y axis is temperature