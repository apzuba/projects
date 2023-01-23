#install.packages(dep=TRUE, c("reshape", "ggplot2", "ez", "lsr", "reshape2", "MASS", "labeling", "lme4"))
library(reshape)                                    # Import necessary packages
library(ggplot2)
library(ez)
library(lsr)
library(reshape2)
library(labeling) 
library(lme4)
library(lubridate)

theme_set(theme_bw())

#install.packages(dep=TRUE, c("lubridate"))


rm(list=ls())                                       # Clear workspace

#################################################################################################

s_folder = "E:\\Adam_Zuba\\behavioral\\ARSQ2\\"
s_files  = list.files(s_folder)                     # All the files in folder

#for (s in c(21:21)) {                                # Subject counter

for (s in c(1:4,6:25,27:37)) {    
  
  # Import data for subject s
  data <- read.table(paste(s_folder, s_files[s], sep = ""), 
                     header=TRUE, sep="\t", fill = TRUE, strip.white=TRUE)
  
  
  data$Sub <- s                                     # Change variable "Sub" becuase it's inconsistent across files
  data <- data[-which(data$answ == 0),]             # Remove all misclicks 
  data$trl <- c(1:nrow(data))                       # Add counter
  
  
  if (data$Phase[75] == 1 && data$Qnr[75] == 1) {   # sanity check to make sure file is standard
    data$Phase[75:106] <- 3                         # Change phase nr of second RSQ
  }
  else {
    stop('Something wrong in file')                 # Give error message
  }
  
  # Add info about the factor
  
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
 
  
  # Add data about the absolute change in rating
  
  data$Diff <- 0
  for (i in data$Qnr){
    data$Diff[data$Qtype == 'ARSQ2' & data$Phase == 1] <- abs(data$answ - data$answ[data$Phase == 3 & data$Qnr])
  }
  

 
  # Add info about the tDCS group
  
  data$tDCS <- 0
  if (s %in% c(1, 6, 7, 9, 10, 14, 15, 17, 20, 22, 32, 34, 37)) {         #Frontal
    data$tDCS <- 1}      
  
  else if (s %in% c(2, 3, 5, 8, 13, 18, 21, 25, 23, 24, 30, 36)) {       #Parietal
    data$tDCS <- 2}
  
  else if (s %in% c(4, 11, 12, 16, 19, 26, 27, 28, 29, 31, 33, 35)) {      #SHAM
    data$tDCS <- 3}
  
  else {data$tDCS <- "error"}
  
  
  # Binding dat
  
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
# TODO: Sensible descriptive stats and plots :)


#single participant data - questions
#melt_data <- melt(data[-which(data$Factor==0 | data$Phase==2 ),], id=c("Phase", "Qnr"), measure="answ", var = "ANSWER")
#cast_data <- cast(melt_data, Phase+Qnr ~ ..., function(x) c( M=mean(x), SE=sd(x)/sqrt(length(x))))

#p2i <- qplot(y=answ_M, x=Qnr, data=cast_data, colour=Phase, xlab="Questions", ylab="Average rating")
#p2i <- p2i + geom_point(size=3) + geom_line(aes(group=Phase),size=1) # + geom_errorbar(limits)
#p2i

###################################################################################################

melt_dat_t <- melt(dat[-which(dat$Phase==2 | dat$Qtype=='Pain'),], id=c("Phase", "tDCS"), measure="answ", var = "ANSWER")
cast_dat_t <- cast(melt_dat_t, Phase+tDCS ~ ..., function(x) c( M=mean(x), SE=sd(x)/sqrt(length(x))))

melt_dat <- melt(dat[-which(dat$Phase==2 | dat$Qtype=='Pain'),], id=c("Phase","Factor"), measure="answ", var = "ANSWER")
cast_dat <- cast(melt_dat, Phase+Factor ~ ..., function(x) c( M=mean(x), SE=sd(x)/sqrt(length(x))))

melt_dat_Q <- melt(dat[-which(dat$Phase==2 | dat$Qtype=='Pain'),], id=c("Phase","Qnr"), measure="answ", var = "ANSWER")
cast_dat_Q <- cast(melt_dat_Q, Phase+Qnr ~ ..., function(x) c( M=mean(x), SE=sd(x)/sqrt(length(x))))

melt_dat_D <- melt(dat[which(dat$Qtype == 'ARSQ2' & dat$Phase == 1),], id=c("tDCS","Qnr"), measure="Diff", var = "ANSWER")
cast_dat_D <- cast(melt_dat_D, tDCS+Qnr ~ ..., function(x) c( M=mean(x), SE=sd(x)/sqrt(length(x))))


#####
limits <- aes(ymax = cast_dat$Correct_M + cast_dat$Correct_SE, ymin= cast_dat$Correct_M - cast_dat$Correct_SE, width=0.2)


ggplot(data=cast_dat_t, aes(x=tDCS, y=answ_M, fill=Phase)) + geom_bar(stat="identity", position=position_dodge()) + 
  coord_cartesian(ylim=c(0, 4)) # + geom_errorbar(limits,position=position_dodge(width=0.9))

ggplot(data=cast_dat, aes(x=Factor, y=answ_M, fill=Phase)) + geom_bar(stat="identity", position=position_dodge()) + 
  coord_cartesian(ylim=c(0, 4)) # + geom_errorbar(limits,position=position_dodge(width=0.9))

ggplot(data=cast_dat_Q, aes(x=Qnr, y=answ_M, fill=Phase)) + geom_bar(stat="identity", position=position_dodge()) + 
  coord_cartesian(ylim=c(0, 4)) # + geom_errorbar(limits,position=position_dodge(width=0.9))

# plot - line by Questions
ggplot(cast_dat_Q, aes(x=Qnr)) +
  geom_line(aes(y=answ_M, col=Phase)) 


d <- qplot(y=Diff_M, x=Qnr, data=cast_dat_D, colour=tDCS, xlab="Questions", ylab="Difference in rating")
d <- d + geom_point(size=3) + geom_line(aes(group=tDCS),size=1) # + geom_errorbar(limits)
d

limits <- aes(ymax = cast_dat$answ_M + sd(cast_dat$answ_M), ymin= cast_dat$answ_M - sd(cast_dat$answ_M), width=0.2)


p <- qplot(y=answ_M, x=Factor, data=cast_dat, colour=Phase, xlab="Factors", ylab="Average rating", font.lab=8, cex.lab=20)
p <- p + geom_point(size=3) + geom_line(aes(group=Phase),size=1)  + geom_errorbar(limits)
p

stat <- ezANOVA(data=cast_dat, dv=.(answ_M), wid=.(Phase), within=.(Phase,Factor), type=3)
print(stat)

stat2 <- t.test(, dv=.(answ_M), wid=.(Phase), within=.(), type=3)
print(stat2)

t.test(x, y = NULL,
       alternative = c("two.sided", "less", "greater"),
       mu = 0, paired = FALSE, var.equal = FALSE,
       conf.level = 0.95, …)

t.test(answ_M ~ Phase,Factor, data=cast_dat, alternative = c("two.sided"))




###################################################################################################################

#melt_dat <- melt(dat, id=c("Sub","Phase","Factor","tDCS"), measure="answ", var = "CORRECT")
#cast_dat <- cast(melt_dat, KI+TMS+TS ~ tDCS, mean)

stat <- ezANOVA(data=cast_dat, dv=.(answ_M), wid=.(Sub), within=.(Phase,Factor), , between=.(tDCS), type=3)
print(stat)

lm(Diff ~ Qnr * tDCS, data=dat)


lmer(Diff ~ Qnr * tDCS + (1 | Sub), data=dat[which(dat$Qtype == 'ARSQ2' & dat$Phase == 1),])

