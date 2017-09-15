library("ggplot2")
library("scales")
library("grid")

# import and clean data

data1 = read.csv2("sixthExperiment.txt", head = TRUE, sep = " ")
data2 = read.csv2("seventhExperiment.txt", head = TRUE, sep = " ")

# make data

nodes = data2$nodes
Greedy_result = data2$covering_size
EA_result_mean = as.numeric(lapply(split(data1$covering_size, data1$nodes), mean))
EA_result_sd = as.numeric(lapply(split(data1$covering_size, data1$nodes), sd))

dataPlot = data.frame(x = nodes, y = Greedy_result, z = EA_result_mean, w = EA_result_sd)
rm(nodes, Greedy_result, EA_result_mean, EA_result_sd)

# perform correlation

mod1 = lm(dataPlot$y ~ dataPlot$x)
mod2 = lm(dataPlot$z ~ I(dataPlot$x^(3/4)))

# make plot

g <- ggplot(data = dataPlot)

# plot results for greedy
g <- g + geom_point(aes(x = x, y = y, colour = "Greedy", shape = "Greedy"))
g <- g + geom_line(aes(x = x, y = mod1$fitted.values, colour = "Greedy"), linetype = "dashed")

# plot results for EA
g <- g + geom_point(aes(x = x, y = z, colour = "EA", shape = "EA"))
g <- g + geom_line(aes(x = x, y = mod2$fitted.values, colour = "EA"), linetype = "dashed")
g <- g + geom_ribbon(aes(x = x, ymin = mod2$fitted.values - w, ymax = mod2$fitted.values + w), fill = "#66CC99", alpha = 0.175)

# legends
# cbbPalette <- c("#009E73", "#E69F00")
cbbPalette <- c("#66CC99", "#CC6666")
g <- g + xlab("number of nodes")
g <- g + ylab("covering size [sample mean]")
g <- g + scale_colour_manual(name = "Algorithm", values = cbbPalette, labels=c("EA", "Greedy"))
g <- g + scale_shape_manual(name = "Algorithm", values=c(0, 2), labels = c("EA", "Greedy"))

# theme
g <- g + theme_bw()
g <- g + theme(panel.grid.major = element_line(colour = "#999999"))
g <- g + theme(panel.grid.minor = element_line(colour = "#666666", linetype = "dotted"))
g <- g + theme(panel.border = element_rect(colour = "black"))
g <- g + theme(legend.position = c(0.12, 0.88))
g <- g + theme(legend.text = element_text(size = 14))
g <- g + theme(legend.title = element_text(size=14, face = "bold"))
g <- g + theme(legend.background = element_rect(colour = "black"))

# save plot
pdf("sixtSeventhExperiment.pdf", width = 6.5, height = 5.5)
g
dev.off()

# clean up
rm(data1, data2, dataPlot, cbbPalette, g, mod1, mod2)