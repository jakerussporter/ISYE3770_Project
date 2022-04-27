# ISYE3770_Project
Statistics project for ISYE 3770 at Gatech

For the difference between processed_teams.csv and processed_no_teams.csv, one file is for counting all medals accumulated by all athletes for each country per year and the other is an attempt at counting all medals earned for a country by event per year. For example, in the sport of rowing, the whole team is given a medal per tracking by the official Olympics, however the main dataset we have is a list of all athletes and the medals they earned, so it is borderline impossible to account for the fact the multiple athletes make up a team that earn one singular medal (There is just too many unique event names to investigate where we could see if they are a team sport or not). I have attempted to remediate the situation by counting unique rows without the personal information with processed_no_teams.csv, however the info is a bit off from the official reports by the Olympics for medals earned for each team. It might be best to use processed_teams.csv because of this reason and state why in our report.
