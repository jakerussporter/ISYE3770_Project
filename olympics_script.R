#Put file path name below
mydata <- read.csv("/Users/jakeporter/Documents/ISYE3770/StatsProject/medal_rate.csv")
df <- data.frame(mydata)
#Change second parameter to reflect countries noc.
#Can also change range of years to better view the data.
plot(df$X, df$USA, type = "o", col = 1, ylim = c(0.0, 1.0), xlim = c(1960, 2016))
