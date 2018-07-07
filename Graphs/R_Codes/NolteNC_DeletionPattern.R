data_set <- read.csv("/home/msiddique/WSDL_Work/Breitbart_Retweet_Analysis/Graphs/NolteNC_pattern_50.csv", header = TRUE)
data_set$Start = as.POSIXct(data_set$Start,  format="%Y/%m/%d")
data_set$End =  as.POSIXct(data_set$End, format="%Y/%m/%d")  
par(mar=c(4,4,2,0)+ 0.2)
plot(0, type='n', xlim=range(c(data_set$Start, data_set$End)), ylim=c(1, nrow(data_set)),
     xlab='Tweet Life Span', ylab='Number of Tweets', xaxt='n', yaxt='n', main = "NolteNC Tweet Deletion Pattern", cex.lab = 1.5)
years <- c(min(data_set$Start),max(data_set$Start), min(data_set$End),max(data_set$End))
abline(v=years, lty=3, col='gray')
axis(1, at=years, labels=format(years, '%m-%d'))
axis(2, at=c(0,10,20,30,40,50), labels=c(0,10,20,30,40,50), las=2, tick = 5)
lines(x=as.POSIXct(c(apply(data_set[c('Start','End')],1,c, NA))),
      y=rep(nrow(data_set):1, each=3),lwd=5,
      col = "blue")
