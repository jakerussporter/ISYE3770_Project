import pandas as pd
import numpy as np

#Convert csv file into pandas dataframe.
df = pd.read_csv ('athlete_events.csv')

#Drop unneeded columns for main arguement and for filtering out teams.
#Medals is for just the medals each team had
#Totals is for the attempts each team had at a medal for the Olympics
medals = df.drop(['ID','Name', 'Sex', 'Age', 'Height', 'Weight'], axis=1)
totals = df.drop(['ID','Name', 'Sex', 'Age', 'Height', 'Weight'], axis=1)

#Drop athletes who didn't earn a medal.
medals = medals[medals['Medal'].notna()]

#uncomment line below to disable the counting of team medals for each individual x_i on that team.
#df = df.drop_duplicates()

#filter out remaining columns, leaving only country and year left.
medals = medals.drop(['Team', 'City', 'Games', 'Season', 'Sport', 'Event', 'Medal'], axis = 1)
totals = totals.drop(['Team', 'City', 'Games', 'Season', 'Sport', 'Event', 'Medal'], axis = 1)


#group the dataframe by unique country AND year.
medals_data = medals.groupby(['NOC', 'Year']).size()
totals_data = totals.groupby(['NOC', 'Year']).size()


#Create pandas array where year is the rows and country or NOC label is the columns.
#medals
m_countries = medals.NOC.unique()
m_countries.sort()
m_years = medals.Year.unique()
m_years.sort()
a = np.zeros(shape=(len(m_years), len(m_countries)))

m_processed = pd.DataFrame(a,columns=m_countries)
m_processed.index = m_years
for i, v in medals_data.items():
    m_processed.at[i[1], i[0]] = v

#totals
t_countries = totals.NOC.unique()
t_countries.sort()
t_years = totals.Year.unique()
t_years.sort()
b = np.zeros(shape=(len(t_years), len(t_countries)))

t_processed = pd.DataFrame(b,columns=t_countries)
t_processed.index = t_years
for i, v in totals_data.items():
    t_processed.at[i[1], i[0]] = v

#Drop countries from totals that never earned a single medal
diff = np.setdiff1d(t_countries, m_countries)
diff = diff.tolist()
t_processed = t_processed.drop(diff, axis=1)

#Create rate table of each countries medals / attemps for each Olympics
medal_rate = m_processed.div(t_processed)
medal_rate = medal_rate.fillna(0)

#Turn the data into a csv file of the (medals earned) / (attempts at medals). If line df = df.drop_duplicates() on line
#14 is uncommented, rename the file name below to 'medal_rate_no_teams.csv'.

m_processed.to_csv('processed_teams.csv', index=True)
t_processed.to_csv('attempts_teams.csv', index=True)
medal_rate.to_csv('medal_rate.csv', index=True)
