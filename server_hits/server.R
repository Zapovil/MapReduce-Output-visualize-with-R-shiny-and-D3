library(ggplot2)

data <- read.table("MyData.csv",sep = ",")
colnames(data)<-c("Ip","count")
popular <- as.data.frame(data[order(data$count,decreasing = TRUE),c(1,2)])
popular<-popular[1:20,]

function(input, output, session) {


  output$bar1<-renderPlot({

   # plot1<-head(data.frame(Freq=terms()),n=20)

    ggplot(data =popular ,aes(x=Ip,y=count))+geom_bar(stat="identity",fill="steelblue")+theme_minimal()+coord_flip()+geom_text(aes(label=Ip),vjust=0.5,color="black",size=4.0)+ylab("Number of request")+xlab("Top User")+ggtitle("Top Request ")
  })


}
