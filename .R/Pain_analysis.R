
rm(list=ls())                                       # Clear workspace
 #install.packages("tidyr", dependencies=TRUE)
library(reshape)
library(ggplot2)
library(gridExtra)
library(ez)
library(lsr)
library(pracma)
library(lme4)
library(tidyr)

#################################################################################################

s_folder = "E:\\Adam_Zuba\\behavioral\\ARSQ2\\"
s_files  = list.files(s_folder)                     # All the files in folder

for (s in c(1:4,6:25,27:37)) {  #                   # Subject counter
  
  # Import data for subject s
  data <- read.table(paste(s_folder, s_files[s], sep = ""), 
                     header=TRUE, sep="\t", fill = TRUE, strip.white=TRUE)
  
  data$S <- as.numeric(substr(s_files[s],2,3))      # Change variable "Sub" becuase it's inconsistent across files
  if (s != 31) {
    data <- data[-which(data$answ == 0),]           # Remove all misclicks 
  }
  data$trl <- c(1:nrow(data))                       # Add counter
  
  
  if (data$Phase[75] == 1 && data$Qnr[75] == 1) {   # sanity check to make sure file is standard
    data$Phase[75:106] <- 3                         # Change phase nr of second RSQ
  }
  else {
    stop('Something wrong in file')                 # Give error message
  }
  
  data$Factor <- 0
  data$Factor[ which(data$Qtype == 'ARSQ2' &  data$Qnr %in% c(1,2,3) ) ] <- 1 # Discontinuity of Mind
  data$Factor[ which(data$Qtype == 'ARSQ2' &  data$Qnr %in% c(4,5,6) ) ] <- 2 # Theory of Mind
  data$Factor[ which(data$Qtype == 'ARSQ2' &  data$Qnr %in% c(7,8,9) ) ] <- 3 # Self
  data$Factor[ which(data$Qtype == 'ARSQ2' &  data$Qnr %in% c(10,11,12) ) ] <- 4 # Planning
  data$Factor[ which(data$Qtype == 'ARSQ2' &  data$Qnr %in% c(13,14,15) ) ] <- 5 # Sleepiness
  data$Factor[ which(data$Qtype == 'ARSQ2' &  data$Qnr %in% c(16,17,18) ) ] <- 6 # Comfort
  data$Factor[ which(data$Qtype == 'ARSQ2' &  data$Qnr %in% c(19,20,21) ) ] <- 7 # Somatic Awareness
  data$Factor[ which(data$Qtype == 'ARSQ2' &  data$Qnr %in% c(22,23,24) ) ] <- 8 # health concern
  data$Factor[ which(data$Qtype == 'ARSQ2' &  data$Qnr %in% c(25,26,27) ) ] <- 9 # Visual Thought
  data$Factor[ which(data$Qtype == 'ARSQ2' &  data$Qnr %in% c(28,29,30) ) ] <- 10 # Verbal Thought
  
  # Add info about the tDCS group
  
  data$tDCS <- 0
  if (s %in% c(1, 6, 7, 9, 10, 14, 15, 17, 20, 22, 32, 34, 37)) {         #Frontal
    data$tDCS <- 1}      
  
  else if (s %in% c(2, 3, 5, 8, 13, 18, 21, 25, 23, 24, 30, 36)) {       #Parietal
    data$tDCS <- 2}
  
  else if (s %in% c(4, 11, 12, 16, 19, 26, 27, 28, 29, 31, 33, 35)) {      #SHAM
    data$tDCS <- 3}
  
  else {data$tDCS <- "error"}
  
  
  if (s == 1) {
    dat <-data
    
  }
  else {
    dat <- rbind(dat, data)  
  }
}

#str(dat)
# Change variable type if necessary
dat$Sub    <- factor(dat$Sub)
dat$S      <- factor(dat$S)
dat$Phase  <- factor(dat$Phase)
dat$Factor <- factor(dat$Factor)
dat$tDCS   <- factor(dat$tDCS)
dat$Qnr    <- factor(dat$Qnr)

###################################################################################################################
# Only keep pain scores

dat <- data.frame(dat[which(dat$Qtype=='Pain'),])
# Add order info for Nth query of pain questions per phase
dat$QinF <- repmat(matrix(c(1,1,1,1,2,2,3,3,4,4,5,5,6,6,1,1),16,1),35,1)


###################################################################################################################
# Look at the average "pain profile"
###################################################################################################################

fuu <- unite(dat, P_QinF, c("Phase","QinF"), sep = "_", remove = TRUE, na.rm = FALSE)

mDat <- melt(fuu, id=c("P_QinF","Qnr","tDCS"), measure="answ", var = "CORRECT")
cDat <- cast(mDat, P_QinF+Qnr+tDCS ~ ..., function(x) c( M=mean(x), SE=sd(x)/sqrt(length(x))))

d1   <- cDat[which(cDat$tDCS==1),] # Frontal
lim1 <- aes(ymax = d1$answ_M + d1$answ_SE, ymin= d1$answ_M - d1$answ_SE, width=0.2)
p1   <- qplot(y=answ_M, x=P_QinF, data=d1, colour=Qnr, xlab="Phase + Repetition", ylab="average pain raiting")
p1   <- p1 + geom_point(size=3) + geom_line(aes(group=Qnr),size=1) + geom_errorbar(lim1)

d2   <- cDat[which(cDat$tDCS==2),] # Parietal
lim2 <- aes(ymax = d2$answ_M + d2$answ_SE, ymin= d2$answ_M - d2$answ_SE, width=0.2)
p2   <- qplot(y=answ_M, x=P_QinF, data=d2, colour=Qnr, xlab="Phase + Repetition", ylab="average pain raiting")
p2   <- p2 + geom_point(size=3) + geom_line(aes(group=Qnr),size=1) + geom_errorbar(lim2)

d3   <- cDat[which(cDat$tDCS==3),] # Sham
lim3 <- aes(ymax = d3$answ_M + d3$answ_SE, ymin= d3$answ_M - d3$answ_SE, width=0.2)
p3   <- qplot(y=answ_M, x=P_QinF, data=d3, colour=Qnr, xlab="Phase + Repetition", ylab="average pain raiting")
p3   <- p3 + geom_point(size=3) + geom_line(aes(group=Qnr),size=1) + geom_errorbar(lim3)


gridPlotz <- grid.arrange(p1, p2, p3, ncol = 3, nrow = 1)

ggsave(paste(s_folder, 'Pain_profile.tiff', sep = ""), plot=gridPlotz, device="tiff", width = 10, height = 7)

