#install.packages("pracma", dependencies=TRUE)
#install.packages("lme4", dpendencies=TRUE)
#install.packages("reshape", dependencies=TRUE)
#install.packages("ggplot2", dependencies=TRUE)
#install.packages("gridExtra", dependencies=TRUE)
#install.packages("ez", dependencies=TRUE)
#install.packages("lsr", dependencies=TRUE)
library(reshape)
library(ggplot2)
library(gridExtra)
library(ez)
library(lsr)
library(pracma)
library(lme4)

rm(list=ls())                                       # Clear workspace

#################################################################################################

s_folder = "E:\\Adam_Zuba\\behavioral\\ARSQ2\\"
s_files  = list.files(s_folder)                    # All the files in folder

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
dat$Sub <- factor(dat$Sub)
dat$S <- factor(dat$S)
dat$Phase <- factor(dat$Phase)
dat$Factor <- factor(dat$Factor)
dat$tDCS <- factor(dat$tDCS)

###################################################################################################################
# Remove analysis of pain scores; will be done separately

dat <- data.frame(dat[-which(dat$Qtype=='Pain'),])



# ###################################################################################################################
# # Check correlations between items within Factors
# ###################################################################################################################
# 
# dat$QinF <- repmat(matrix(c(1,2,3),3,1),1050,1)   # adds item count to each Factor
# 
# cDat <- dat[which(dat$Phase==3),]
# 
# cor.test(cDat$answ[which(cDat$Factor==1  & cDat$QinF==1)] , cDat$answ[which(cDat$Factor==1  & cDat$QinF==2)])
# cor.test(cDat$answ[which(cDat$Factor==1  & cDat$QinF==1)] , cDat$answ[which(cDat$Factor==1  & cDat$QinF==3)])
# cor.test(cDat$answ[which(cDat$Factor==1  & cDat$QinF==2)] , cDat$answ[which(cDat$Factor==1  & cDat$QinF==3)])
# 
# cor.test(cDat$answ[which(cDat$Factor==2  & cDat$QinF==1)] , cDat$answ[which(cDat$Factor==2  & cDat$QinF==2)])
# cor.test(cDat$answ[which(cDat$Factor==2  & cDat$QinF==1)] , cDat$answ[which(cDat$Factor==2  & cDat$QinF==3)])
# cor.test(cDat$answ[which(cDat$Factor==2  & cDat$QinF==2)] , cDat$answ[which(cDat$Factor==2  & cDat$QinF==3)])


###################################################################################################################
# Check retest correlations and sources of variance as in Alexander Diaz et al. (2013) frontinhumneurosci
###################################################################################################################

mDat <- melt(dat, id=c("S","Phase","Factor"), measure="answ", var = "CORRECT")
cDat <- cast(mDat, S+Phase+Factor ~ ..., mean)

### Retest correlations ###
###########################
correlationz <- matrix(0,10,3); tz <- matrix(0,10,3); pvalz <- matrix(0,10,3)
corrPairs <- matrix(c(1,1,2,2,3,3),3,2)
for (p in c(1:3)) {
  for (f in c(1:10)) {
    fuu <- cor.test(cDat$answ[which(cDat$Factor==f & cDat$Phase==corrPairs[p,1])], 
                    cDat$answ[which(cDat$Factor==f & cDat$Phase==corrPairs[p,2])])
    #summary(fuu)
    correlationz[f,p] <-  as.numeric(fuu$estimate)
    tz[f,p]           <-  as.numeric(fuu$statistic)
    pvalz[f,p]        <-  round(as.numeric(fuu$p.value), digits = 3)
  }
}
# SUMMARY OF ABOVE: All are significant, except Phase 1 vs (Phase 2 & 3) for Factor 1
# For looking individually
cor.test(cDat$answ[which(cDat$Factor==1  & cDat$Phase==1)] , cDat$answ[which(cDat$Factor==1  & cDat$Phase==3)])
plot(cDat$answ[which(cDat$Factor==1  & cDat$Phase==3)] , cDat$answ[which(cDat$Factor==1  & cDat$Phase==1)], type='p',pch = 16, cex = 0.75)
abline(lm(cDat$answ[which(cDat$Factor==1  & cDat$Phase==1)] ~ cDat$answ[which(cDat$Factor==1  & cDat$Phase==3)]), col="red")

# Differences between correlations
t.test(correlationz[,1], correlationz[,2], paired = TRUE); cohensD(correlationz[,1], correlationz[,2], method = "paired")
t.test(correlationz[,1], correlationz[,3], paired = TRUE); cohensD(correlationz[,1], correlationz[,3], method = "paired")
t.test(correlationz[,2], correlationz[,3], paired = TRUE); cohensD(correlationz[,2], correlationz[,3], method = "paired")


###1111

Phases <- c("1 x 2","1 x 3","2 x 3")
Mean_corr <- c(mean(correlationz[,1]), mean(correlationz[,2]), mean(correlationz[,3]))
SD_corr <- c(sd(correlationz[,1]), sd(correlationz[,2]), sd(correlationz[,3]))
Mean_corr_fac <-data.frame (Phases, Mean_corr, SD_corr)

# reprezentacja SD na plocie
sd_corr <- aes(ymax = Mean_corr + SD_corr, ymin= Mean_corr - SD_corr)

# Plot
p_t <- ggplot(Mean_corr_fac) +
  geom_bar( aes(Phases, Mean_corr), stat="identity", fill="skyblue", alpha=0.8) +
  geom_errorbar( aes(x=Phases, ymax=Mean_corr+SD_corr, ymin=Mean_corr-SD_corr), width=0.2, colour="orange") +
  labs(y="Mean correlations")
p_t


# SUMMARY OF ABOVE: on average, correlations are much stronger between Phases 2 & 3 (<- close in time?)




### Sources of variance (within, between, block) ###
####################################################
lmX <-  lm(answ ~ S+Phase,data=cDat[which(cDat$Factor==1),]); anova(lmX)
lmX <-  lm(answ ~ S+Phase,data=cDat[which(cDat$Factor==2),]); anova(lmX)
lmX <-  lm(answ ~ S+Phase,data=cDat[which(cDat$Factor==3),]); anova(lmX)
lmX <-  lm(answ ~ S+Phase,data=cDat[which(cDat$Factor==4),]); anova(lmX)
lmX <-  lm(answ ~ S+Phase,data=cDat[which(cDat$Factor==5),]); anova(lmX)
lmX <-  lm(answ ~ S+Phase,data=cDat[which(cDat$Factor==6),]); anova(lmX)
lmX <-  lm(answ ~ S+Phase,data=cDat[which(cDat$Factor==7),]); anova(lmX)
lmX <-  lm(answ ~ S+Phase,data=cDat[which(cDat$Factor==8),]); anova(lmX)
lmX <-  lm(answ ~ S+Phase,data=cDat[which(cDat$Factor==9),]); anova(lmX)
lmX <-  lm(answ ~ S+Phase,data=cDat[which(cDat$Factor==10),]); anova(lmX)

# SUMMARY OF ABOVE: Factor 1 has high intraindiv. variance; Phase has practically no effect; rest tends to replicate

# From now on we will exclude Phase 2

###################################################################################################################
# Overall full ANOVA
###################################################################################################################

mDat <- melt(dat[-which(dat$Phase==2),], id=c("S","Phase","Factor","tDCS"), measure="answ", var = "CORRECT")
cDat <- cast(mDat, S+Phase+Factor+tDCS ~ ..., mean)
#str(cDat)

stat <- ezANOVA(data=cDat, dv=.(answ), wid=.(S), within=.(Factor,Phase), between=.(tDCS), type=3)
print(stat)



###################################################################################################################
# LMER example
###################################################################################################################


mDat <- melt(dat[-which(dat$Phase==2),], id=c("S","Factor","Phase","tDCS"), measure="answ", var = "CORRECT")
cDat <- cast(mDat, S+Factor+Phase+tDCS ~ ..., mean)

stat <- ezANOVA(data=cDat[which(cDat$Factor==1),], dv=.(answ), wid=.(S), within=.(Phase), between=.(tDCS), type=3)
print(stat)

fullModel = lmer(answ ~ Phase*tDCS + (1|S), data=cDat[which(cDat$Factor==6),])
anova(fullModel)
#summary(lmeModel)
drop1(fullModel, test="Chisq")

reducedModel <- lmer(answ ~ Phase + tDCS + (1|S), data=cDat[which(cDat$Factor==6),])
anova(fullModel,reducedModel,test="Chisq")

drop1(reducedModel, test="Chisq")


###################################################################################################################
# Linear Mixed-Models for EEG GFP in 4 frequency bands
###################################################################################################################

mDat <- melt(dat[-which(dat$Phase==2),], id=c("S","Factor","Phase","tDCS"), measure="answ", var = "CORRECT")
cDat <- cast(mDat, S+Factor+Phase+tDCS ~ ..., mean)


# Import the EEG predictors created in matlab
EEGstuff <- read.table("E:\\Adam_Zuba\\scripts\\EEG\\bandABS.dat", 
                       header=FALSE, sep="\t", fill = TRUE, strip.white=TRUE)


fullModel = lmer(answ ~ Phase*tDCS*... + (1|S), data=cDat[which(cDat$Factor==6),])
anova(fullModel)
#summary(lmeModel)
drop1(fullModel, test="Chisq")

reducedModel <- lmer(answ ~ Phase + tDCS + (1|S), data=cDat[which(cDat$Factor==6),])
anova(fullModel,reducedModel,test="Chisq")

drop1(reducedModel, test="Chisq")
