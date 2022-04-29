# ISYE3770_Project
Statistics project for ISYE 3770 at Gatech

For the difference between processed_teams.csv and processed_no_teams.csv, one file is for counting all medals accumulated by all athletes for each country per year and the other is an attempt at counting all medals earned for a country by event per year. For example, in the sport of rowing, the whole team is given a medal per tracking by the official Olympics, however the main dataset we have is a list of all athletes and the medals they earned, so it is borderline impossible to account for the fact the multiple athletes make up a team that earn one singular medal (There is just too many unique event names to investigate where we could see if they are a team sport or not). I have attempted to remediate the situation by counting unique rows without the personal information with processed_no_teams.csv, however the info is a bit off from the official reports by the Olympics for medals earned for each team. It might be best to use processed_teams.csv because of this reason and state why in our report.

If you would like to run the files, make sure you have pandas and numpy installed, however if you would like to just open the csv's I created, just download those from here and open them. I would not suggest trying to mess with the python file unless you have all the packages installed on your machine and if you actually understand or think you understand what you're doing. To run in terminal, go to the file location and run it as: python statsProjectPreprocess.py

# *UPDATE*

Changed the python file to process the data into (medals earned) / (total olympic events participated in for that year). The reason for this change is that countries send varying ammounts of participants per year, so its not smart to only compare the total medals they earned, when its obvious that if you send more participants, the more you're going to win. I have now changed the data to be a rate, so that we can then compare different years of a country based on how well they did, ignore the number of participants. Also uploaded the csv data that corresponds with this change. I also wrote a little r script to plot the data for an individual country. Now we just need to perform actual calculations on the data.


