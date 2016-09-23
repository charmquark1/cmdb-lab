#!/usr/bin/env Rscript

#I am not sure why my lastz outputs only map ONE contig!
spades1 = read.table("03-spades_lowcov_R",header=T)
velv1 = read.table("03-velvet_lowcov_R" ,header=T)

plot(spades1, type="l", main=expression("Mapping from Low Covg Reads"), xlab ="chr (bp)", ylab="Coverage", col="red")
lines(velv1, type="l", col="blue")
legend("topright", inset=0.05, cex = 1, c("spades1","velv1"), horiz=TRUE, lty=c(1,1), lwd=c(2,2), col=c("red", "blue"), bg="grey96")
#spades2 = read.table("03-spades_hi_Rinput",header=T)
#plot(spades2,type="l")

#velv2 = read.table("03-vel_high_Rinput",header=T)
#plot(velv2,type="l")



