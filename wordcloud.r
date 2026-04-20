library(wordcloud)
library(RColorBrewer)

data <- read.csv("text.csv")

wordcloud(
  data$text,
  min.freq = 1,
  max.words = 100,
  random.order = FALSE,
  rot.per = 0.3,
  colors = brewer.pal(8, "Dark2")
)