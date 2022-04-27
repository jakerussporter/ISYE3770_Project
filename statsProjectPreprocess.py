import pandas as pd
import numpy as np

#Convert csv file into pandas dataframe.
df = pd.read_csv ('athlete_events.csv')

#Drop unneeded columns for main arguement and for filtering out teams.
df = df.drop(['ID','Name', 'Sex', 'Age', 'Height', 'Weight'], axis=1)

#Drop athletes who didn't earn a medal.
df = df[df['Medal'].notna()]

#uncomment line below to disable the counting of team medals for each individual x_i on that team.
#df = df.drop_duplicates()

#filter out remaining columns, leaving only country and year left.
df = df.drop(['Team', 'City', 'Games', 'Season', 'Sport', 'Event', 'Medal'], axis = 1)

#group the dataframe by unique country AND year.
data = df.groupby(['NOC', 'Year']).size()

#Create pandas array where year is the rows and country or NOC label is the columns.
countries = df.NOC.unique()
countries.sort()
years = df.Year.unique()
years.sort()
a = np.zeros(shape=(len(years), len(countries)))
processed = pd.DataFrame(a,columns=countries)
processed.index = years
for i, v in data.items():
    processed.at[i[1], i[0]] = v

#Turn the data into a csv file. If line df = df.drop_duplicates() on line
#14 is uncommented, rename the file name below to 'processed_no_teams.csv'.
processed.to_csv('processed_teams.csv', index=True)
