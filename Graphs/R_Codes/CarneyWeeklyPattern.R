data_set <- read.csv("//home/msiddique/WSDL_Work/Breitbart_Retweet_Analysis/Outputs/Carney_Weekly.csv", header = TRUE)
data_set$NewTweets
count <- table(data_set$NewTweets, data_set$OldTweets, data_set$MissingTweets)
bp <- barplot(t(data_set[ , -1]),
              ylab = "Tweets",
              main = "Deletion Pattern For John Carney",
              col = c("yellow", "darkblue", "red"),
              ylim = c(0,150)
)

axis(side = 1, at = bp , labels = data_set$Day)

legend("topleft", legend =  c("New Tweets in memento", "Same Tweets as previous memento", "Missing Tweets"), cex=0.8, fill = c("yellow", "darkblue", "red"))
