data_set <- read.csv("/home/msiddique/WSDL_Work/Breitbart_Retweet_Analysis/Graphs/NolteTweetLifeTime.csv", header = TRUE)
data_set$Timestamp
data_set$Timestamp = as.Date(data_set$Timestamp, "%Y/%m/%d")
data_set$Timestamp
data_set$Value
plot(x = data_set$Timestamp,y = data_set$Value,
     xlab = "Memento Timestamp",
     ylab = "Tweet Presence in mementos",
     main = "NolteNC tweet life span",
     pch = 19,
     cex.lab= 1.5,
     type = "o"
)
legend("bottomleft", legend=c("Tweet Id: 973230239005409282"), pch = 19, title = "Legend")

