library("ggplot2")
library("scales")
library("grid")

# maybe to be removed
setwd("/Users/fq00/Documents/Server/plb/experiments/results")

# import and clean data

data1 = read.csv2("firstExperiment.txt", head = TRUE, sep = " ")
data2 = read.csv2("secondExperiment.txt", head = TRUE, sep = " ")
data3 = read.csv2("sixthExperiment.txt", head = TRUE, sep = " ")
data4 = read.csv2("seventhExperiment.txt", head = TRUE, sep = " ")

# make data

nodes1 = data2$nodes
Greedy_result1 = data2$covering_size
EA_result_mean1 = as.numeric(lapply(split(data1$covering_size, data1$nodes), mean))
EA_result_sd1 = as.numeric(lapply(split(data1$covering_size, data1$nodes), sd))
dataPlot1 = data.frame(x = nodes1, y = Greedy_result1, z = EA_result_mean1, w = EA_result_sd1)
rm(nodes1, Greedy_result1, EA_result_mean1, EA_result_sd1)
dataPlot1<- dataPlot1[-nrow(dataPlot1),]

nodes2 = data4$nodes
Greedy_result2 = data4$covering_size
EA_result_mean2 = as.numeric(lapply(split(data3$covering_size, data3$nodes), mean))
EA_result_sd2 = as.numeric(lapply(split(data3$covering_size, data3$nodes), sd))
dataPlot2 = data.frame(x = nodes2, y = Greedy_result2, z = EA_result_mean2, w = EA_result_sd2)
rm(nodes2, Greedy_result2, EA_result_mean2, EA_result_sd2)

# perform correlation

intercept1 = 0#-38.37268
intercept2 = 0#-75.58022

mod1 = lm(dataPlot1$y ~ dataPlot1$x)
mod2 = lm(I(dataPlot1$z + intercept1) ~ I(dataPlot1$x^(3/4)))
mod3 = lm(dataPlot2$y ~ dataPlot2$x)
mod4 = lm(I(dataPlot2$z + intercept2) ~ I(dataPlot2$x^(3/4)) + I(dataPlot2$x^(1/2)))

# make plot

g <- ggplot()

# plot results for greedy [Chung-Lu]
g <- g + geom_point(aes(x = dataPlot1$x, y = dataPlot1$y, colour = "Greedy [Chung-Lu]", shape = "Greedy [Chung-Lu]"))
g <- g + geom_line(aes(x = dataPlot1$x, y = mod1$fitted.values, colour = "Greedy [Chung-Lu]"), linetype = "dashed")

# plot results for EA [Chung-Lu]
g <- g + geom_point(aes(x = dataPlot1$x, y = dataPlot1$z, colour = "EA [Chung-Lu]", shape = "EA [Chung-Lu]"))
g <- g + geom_line(aes(x = dataPlot1$x, y = mod2$fitted.values, colour = "EA [Chung-Lu]"), linetype = "dashed")
g <- g + geom_ribbon(aes(x = dataPlot1$x, ymin = mod2$fitted.values - dataPlot1$w, ymax = mod2$fitted.values + dataPlot1$w), fill = "#E69F00", alpha = 0.175)

# plot results for greedy [Hyperbolic]
g <- g + geom_point(aes(x = dataPlot2$x, y = dataPlot2$y, colour = "Greedy [Hyperbolic]", shape = "Greedy [Hyperbolic]"))
g <- g + geom_line(aes(x = dataPlot2$x, y = mod3$fitted.values, colour = "Greedy [Hyperbolic]"), linetype = "dashed")

# plot results for EA [Hyperbolic]
g <- g + geom_point(aes(x = dataPlot2$x, y = dataPlot2$z, colour = "EA [Hyperbolic]", shape = "EA [Hyperbolic]"))
g <- g + geom_line(aes(x = dataPlot2$x, y = mod4$fitted.values, colour = "EA [Hyperbolic]"), linetype = "dashed")
g <- g + geom_ribbon(aes(x = dataPlot2$x, ymin = mod4$fitted.values - dataPlot2$w, ymax = mod4$fitted.values + dataPlot2$w), fill = "#009E73", alpha = 0.175)

# legends
cbbPalette <- c("#E69F00", "#56B4E9", "#009E73", "#F0E442")
g <- g + xlab("number of nodes")
g <- g + ylab("covering size [sample mean]")
g <- g + scale_colour_manual(name = "Algorithm", values = cbbPalette, labels=c("EA [Chung-Lu]", "EA [Hyperbolic]", "Greedy [Chung-Lu]", "Greedy [Hyperbolic]"))
g <- g + scale_shape_manual(name = "Algorithm", values=c(0, 2, 3, 4), labels = c("EA [Chung-Lu]", "EA [Hyperbolic]", "Greedy [Chung-Lu]", "Greedy [Hyperbolic]"))

# theme
g <- g + theme_bw()
g <- g + theme(panel.grid.major = element_line(colour = "#999999"))
g <- g + theme(panel.grid.minor = element_line(colour = "#666666", linetype = "dotted"))
g <- g + theme(panel.border = element_rect(colour = "black"))
g <- g + theme(legend.position = c(0.2, 0.84))
g <- g + theme(legend.text = element_text(size = 14))
g <- g + theme(legend.title = element_text(size=14, face = "bold"))
g <- g + theme(legend.background = element_rect(colour = "black"))

# save plot
pdf("total.pdf", width = 6.5, height = 5.5)
g
dev.off()

# clean up
rm(data1, data2, data3, data4, dataPlot1, dataPlot2, cbbPalette, g, mod1, mod2, mod3, mod4, intercep1, intercept2)