data_set <- read.csv("/home/msiddique/WSDL_Work/Breitbart_Retweet_Analysis/Graphs/CarneyTweetLifeTime.csv", header = TRUE)
data_set$Timestamp = as.Date(data_set$Timestamp, "%Y/%m/%d")
plot(x = data_set$Timestamp,y = data_set$Present,
     xlab = "Memento Timestamp",
     ylab = "Tweet Presence in mementos",
     main = "Carney tweet life span",
     pch = 19,
     cex.lab=1.5
)
legend("bottomleft",legend = c("Tweet Id: 977231225814478848"),pch = 19,title="Legend")
