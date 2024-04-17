# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

# choose countries of interest
my_countries = ['Egypt', 'South Africa','Kenya', 'Ghana', 'South Sudan', 'Rwanda']
# 'United States', 'Mexico','Cuba', 'Brazil', 'Puerto Rico', 'Canada'
# 'Germany', 'Kazakhstan','Serbia', 'Poland', 'Spain', 'France'
# 'Mongolia', 'Philippines','South Korea', 'North Korea', 'Vietnam', 'India'
# 'Egypt', 'South Africa','Kenya', 'Ghana', 'South Sudan', 'Rwanda'

# Load in the data with read_csv()
df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()

# Plot the data on a line graph
for c in unique_countries:
  if c in my_countries:
    
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == c]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == c]['Access']

    plt.plot(years, sum_elec, label=c, marker='o', linestyle="-")

  
plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity In Africa')
# 'Percent of Population with Access to Electricity In North and South America'
# 'Percent of Population with Access to Electricity In Europe'
# 'Percent of Population with Access to Electricity In Asia'
# 'Percent of Population with Access to Electricity In Africa'
plt.legend()
plt.show()
