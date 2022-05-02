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


host_countries = ['GRE', 'FRA', 'USA', 'GBR', 'SWE', 'BEL', 'SUI', 'NED', 'GER', 'NOR', 'FIN', 'ITA', 'AUS', 'AUT', 'JPN', 'MEX', 'FRG', 'CAN', 'URS', 'YUG', 'KOR', 'ESP', 'CHN', 'RUS', 'BRA']
host_countries_years = [('GRE', 1896), ('FRA', 1900), ('USA', 1904), ('GBR', 1908), ('SWE', 1912), ('BEL', 1920), ('FRA', 1924), ('SUI', 1928), ('NED', 1928), ('USA', 1932), ('GER', 1936), ('SUI', 1948), ('GBR', 1948), ('NOR', 1952), ('FIN', 1952), ('ITA', 1956), ('AUS', 1956), ('USA', 1960), ('ITA', 1960), ('AUT', 1964), ('JPN', 1964), ('FRA', 1968), ('MEX', 1968), ('JPN', 1972), ('FRG', 1972), ('AUT', 1976), ('CAN', 1976), ('USA', 1980), ('URS', 1980), ('YUG', 1984), ('USA', 1984), ('CAN', 1988), ('KOR', 1988), ('FRA', 1992), ('ESP', 1992), ('NOR', 1994), ('USA', 1996), ('JPN', 1998), ('AUS', 2000), ('USA', 2002), ('GRE', 2004), ('ITA', 2006), ('CHN', 2008), ('CAN', 2010), ('GBR', 2012), ('RUS', 2014), ('BRA', 2016)]

#Create rate table of each countries medals / attemps for each Olympics
medal_rate = m_processed.div(t_processed)
#medal_rate = medal_rate.fillna(0)
medal_rate = medal_rate[host_countries]

hosted_values = medal_rate.copy()
hosted_values[:] = np.nan

non_hosted_values = medal_rate.copy()

for item in host_countries_years:
    hosted_values.at[item[1], item[0]] = non_hosted_values.at[item[1], item[0]]
    non_hosted_values.at[item[1], item[0]] = np.nan


print(medal_rate)
#print(non_hosted_values)

#Turn the data into a csv file of the (medals earned) / (attempts at medals). If line df = df.drop_duplicates() on line
#14 is uncommented, rename the file name below to 'medal_rate_no_teams.csv'.

m_processed.to_csv('processed_teams.csv', index=True)
t_processed.to_csv('attempts_teams.csv', index=True)
medal_rate.to_csv('medal_rate.csv', index=True)
hosted_values.to_csv('hosted_values.csv', index=True)
non_hosted_values.to_csv('non_hosted_values.csv', index=True)
