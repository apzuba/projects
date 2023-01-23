
###################################################################################################################
# NB! This is a completely new script for including EEG biomarkers into the analysis
###################################################################################################################

# install.packages("lmerTest", dependencies=TRUE) # AZ! install missing packages
#install.packages("psych", dependencies=TRUE)
#install.packages("effects", dependencies=TRUE)
#install.packages("sjPlot", dependencies=TRUE)
library(reshape)
library(ggplot2)
library(gridExtra)
library(ez)
library(lsr)
library(pracma)
library(sjPlot)
library(effects)
library(psych)
library(lme4)
library(lmerTest)

rm(list=ls())                                       # Clear workspace

###################################################################################################################
# First import behavioral data
###################################################################################################################

s_folder = "E:\\Adam_Zuba\\behavioral\\ARSQ2\\"
s_files  = list.files(s_folder)                     # All the files in folder

for (s in c(1:4,6:25,27:33,35:37)) {  #                   # Subject counter
  
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
    data$tDCS <- 2}      
  
  else if (s %in% c(2, 3, 5, 8, 13, 18, 21, 25, 23, 24, 30, 36)) {       #Parietal
    data$tDCS <- 3}
  
  else if (s %in% c(4, 11, 12, 16, 19, 26, 27, 28, 29, 31, 33, 35)) {      #SHAM
    data$tDCS <- 1}
  
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
# Remove analysis of pain scores; not relevant right now

dat <- data.frame(dat[-which(dat$Qtype=='Pain'),])


###################################################################################################################
# Import the EEG predictors created in matlab
###################################################################################################################


EEGstuff <- read.table("E:\\Adam_Zuba\\scripts\\EEG\\bandABS.dat", 
                       header=FALSE, sep="\t", fill = TRUE, strip.white=TRUE)

# Names Fase1/Fase2 + Delta/Theta/Alpha/Beta + frontal(fo)/parietal(pa)
colnames(EEGstuff) <- c("F1_D_fo","F1_T_fo","F1_A_fo","F1_B_fo","F1_D_pa","F1_T_pa","F1_A_pa","F1_B_pa", 
                        "F2_D_fo","F2_T_fo","F2_A_fo","F2_B_fo","F2_D_pa","F2_T_pa","F2_A_pa","F2_B_pa")

# Remove some subjects and order columns according to electrode cluster
EEGstuff <- EEGstuff[-c(5,26,34),c(1:4,9:12,5:8,13:16)]


# Prepare behavioral results
mDat <- melt(dat[-which(dat$Phase==2),], id=c("S","Factor","Phase","tDCS"), measure="answ", var = "CORRECT")
cDat <- cast(mDat, S+Factor+Phase+tDCS ~ ..., mean) # c(mean,sd)
#cDat$answ <- cDat$answ_mean/(cDat$answ_sd + 1)

###################################################################################################################
# Linear Mixed-Models for EEG absolute power in 4 frequency bands (frontal / parietal)
###################################################################################################################

# This is an example of use: http://rinterested.github.io/statistics/mixed_effects_comparison.html

### 1. SPECIFY WHETHER TO LOOK AT FRONTAL/PARIETAL DATA
bar <- EEGstuff[,c(1:8)] #<- frontal; 9:16 is parietal

### 2. SPECIFY WHICH FACTOR TO LOOK AT
data = cDat[which(cDat$Factor==2),] # can be 1 to 10

# Prepare data accordingly 
idx <- order(c(seq_along(bar[,1]), seq_along(bar[,1]))) # for interleaving Phase1&2
data$deltaPow <- c(bar[,1],bar[,5])[idx]
data$thetaPow <- c(bar[,2],bar[,6])[idx]
data$alphaPow <- c(bar[,3],bar[,7])[idx]
data$betaPow  <- c(bar[,4],bar[,8])[idx]
#data$answ <- data$answ / 5
data[,c(5:9)] <- scale(data[,c(5:9)], scale = TRUE) # NB! Rescales the data; better for model calculations

# plot(sort(data$deltaPow))
# plot(log(sort(data$deltaPow)))

### 3. LOOK AT THE FULL MODEL

fullModel = lmer(answ ~ tDCS*Phase*deltaPow + tDCS*Phase*thetaPow + tDCS*Phase*alphaPow + tDCS*Phase*betaPow + 
                        (1|S), REML = F, data=data)
#summary(fullModel)
#coef(fullModel)
anova(fullModel)
drop1(fullModel)


### 4. AUTOMATIC MODEL SELECTION

stepsBack <- step(fullModel,reduce.random=FALSE)
reducedModel <- get_model(stepsBack)
anova(reducedModel) # <- this gives you the final model
#ranef(reducedModel)
#mDat <- get_model_data(model=reducedModel, type = "pred", pred.type = "fe")

# Here you can change the "...Pow" term according to what you want to look at
plot_model(reducedModel, type = "pred", terms = c("alphaPow","Phase", "tDCS"))


### Do this 20 times for each Factor separately for frontal/parietal region :) lol




