
Dane <- read.table("/Users/apzuba/Documents/Kogni/Semestr 2/Statystyka/Projekt/complete.csv", header=TRUE, sep=",", na.strings="NA",
   dec=".", strip.white=TRUE)
dane_correct <- subset(Dane, subset=correct == "1")
with(dane_correct, plotMeans(rt, kategoria, zgodnosc, error.bars="se", connect=TRUE, legend.pos="farright"))
lmTKz <- lm(rt ~ typ *kategoria +zgodnosc, data=dane_correct)
summary(lmTKz)
Stroop <- read.table("/Users/apzuba/Desktop/stroop.txt", header=TRUE, sep="", na.strings="NA", dec=".", 
  strip.white=TRUE)
with(dane_correct, plotMeans(rt, typ, zgodnosc, error.bars="se", connect=TRUE, legend.pos="farright"))
dev.print(png, filename="/Users/apzuba/Desktop/TypZgodnosc.png", width=10, height=10, pointsize=12, units="in", 
  res=72)
lmTZ <- lm(rt ~ typ *  zgodnosc, data=dane_correct)
summary(lmTZ)
with(dane_correct, plotMeans(rt, typ, zgodnosc, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
with(dane_correct, Barplot(zgodnosc, by=kategoria, style="divided", legend.pos="above", xlab="zgodnosc", 
  ylab="Frequency"))
library(rgl, pos=20)
library(nlme, pos=21)
library(mgcv, pos=21)
Boxplot(rt~kategoria, data=dane_correct, id=list(method="y"))
scatter3d(rt~condition+key|kategoria, data=dane_correct, surface=FALSE, residuals=TRUE, parallel=FALSE, bg="white", 
  axis.scales=TRUE, grid=TRUE, ellipsoid=FALSE)
with(dane_correct, Hist(rt, groups=kategoria, scale="frequency", breaks="Sturges", col="darkgray"))
with(Dane, plotMeans(correct, kategoria, error.bars="se", connect=TRUE))
summary(Dane)
with(Dane, plotMeans(correct, kategoria, typ, error.bars="se", connect=TRUE, legend.pos="farright"))
with(Dane, plotMeans(correct, kategoria, typ, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
dev.print(png, filename="/Users/apzuba/Desktop/Correctness.png", width=6.999999999999999, height=6.999999999999999, 
  pointsize=12, units="in", res=72)
with(Dane, (t.test(correct, alternative='two.sided', mu=0.0, conf.level=.95)))
library(abind, pos=23)
library(e1071, pos=24)
numSummary(Dane[,"correct", drop=FALSE], groups=Dane$kategoria, statistics=c("mean", "sd", "IQR", "quantiles"), 
  quantiles=c(0,.25,.5,.75,1))
Dane_log <- read.table("/Users/apzuba/Documents/Kogni/Semestr 2/Statystyka/Projekt/complete.csv", header=TRUE, 
  sep="", na.strings="NA", dec=",", strip.white=TRUE)
Dane_log <- read.table("/Users/apzuba/Documents/Kogni/Semestr 2/Statystyka/Projekt/complete.csv", header=TRUE, 
  sep=";", na.strings="NA", dec=",", strip.white=TRUE)
normalityTest(~logRT, test="shapiro.test", data=Dane_log)
with(Dane_log, Hist(logRT, scale="frequency", breaks="Sturges", col="darkgray"))
with(Dane_log, Dotplot(logRT, bin=TRUE, breaks="Sturges"))
indexplot(Dane_log[,'logRT', drop=FALSE], type='p', id.method='y', id.n=2)
densityPlot( ~ logRT, data=Dane_log, bw=bw.SJ, adjust=1, kernel=dnorm, method="adaptive")
normalityTest(~rt, test="shapiro.test", data=dane_correct)
with(Dane_log, qqPlot(logRT, dist="norm", id=list(method="y", n=2, labels=rownames(Dane_log))))
indexplot(Dane_log[,'logRT', drop=FALSE], type='h', id.method='y', id.n=2)
with(Dane_log, Hist(logRT, scale="frequency", breaks="Sturges", col="darkgray"))
with(Dane_log, Dotplot(logRT, bin=TRUE, breaks="Sturges"))
with(Dane_log, discretePlot(logRT, scale="frequency"))
Dane_log100 <- read.table("/Users/apzuba/Documents/Kogni/Semestr 2/Statystyka/Projekt/complete.csv", header=TRUE, 
  sep=";", na.strings="NA", dec=",", strip.white=TRUE)
with(Dane_log100, Hist(logRT, scale="frequency", breaks="Sturges", col="darkgray"))
normalityTest(~logRT, test="shapiro.test", data=Dane_log100)
normalityTest(~logRT, test="shapiro.test", data=Dane_log100)
normalityTest(~logRT, test="shapiro.test", data=Dane_log)
with(Dane_log, Hist(logRT, scale="frequency", breaks="Sturges", col="darkgray"))
with(Dane_log, Hist(logRT, scale="frequency", breaks="Sturges", col="darkgray"))
with(Dane_log, Hist(rt, scale="frequency", breaks="Sturges", col="darkgray"))
Dane_PrymaTarget <- read.table("/Users/apzuba/Documents/Kogni/Semestr 2/Statystyka/Projekt/complete-1.csv", 
  header=TRUE, sep=";", na.strings="NA", dec=".", strip.white=TRUE)
with(Dane_PrymaTarget, plotMeans(rt, target, pryma, error.bars="se", connect=TRUE, legend.pos="farright"))
with(Dane_PrymaTarget, plotMeans(rt, target, pryma, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
lmTargetP <- lm(rt ~ target *pryma, data=Dane_PrymaTarget)
summary(lmTargetP)
dane_TP_corr <- subset(Dane_PrymaTarget, subset=correct == "1")
with(dane_TP_corr, plotMeans(rt, target, typ, error.bars="se", connect=TRUE, legend.pos="farright"))
with(dane_TP_corr, plotMeans(rt, target, typ, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
with(dane_TP_corr, plotMeans(rt, target, typ, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
with(dane_TP_corr, plotMeans(rt, target, pryma, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
with(dane_TP_corr, plotMeans(rt, target, pryma, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
with(dane_TP_corr, plotMeans(rt, typ, error.bars="conf.int", level=0.95, connect=TRUE))
lmTyp <- lm(rt ~ typ, data=dane_TP_corr)
summary(lmTyp)
lmWszystko <- lm(rt ~ pryma *target *typ, data=dane_TP_corr)
summary(lmWszystko)
with(dane_TP_corr, plotMeans(rt, target, typ, error.bars="se", connect=TRUE, legend.pos="farright"))
with(dane_TP_corr, plotMeans(rt, target, typ, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
dev.print(png, filename="/Users/apzuba/Desktop/TypTarget.png", width=10, height=10, pointsize=12, units="in", 
  res=72)
with(dane_TP_corr, plotMeans(rt, target, pryma, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
dev.print(png, filename="/Users/apzuba/Desktop/PrymaTarget.png", width=10, height=10, pointsize=12, units="in", 
  res=72)
with(dane_TP_corr, plotMeans(rt, pryma, typ, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
dev.print(png, filename="/Users/apzuba/Desktop/PrymaTyp.png", width=10, height=10, pointsize=12, units="in", res=72)
Boxplot(rt~zgodnosc, data=dane_correct, id=list(method="y"))
with(dane_TP_corr, plotMeans(rt, target, error.bars="conf.int", level=0.95, connect=TRUE))
with(dane_TP_corr, plotMeans(rt, target, pryma, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
with(dane_correct, plotMeans(rt, kategoria, zgodnosc, error.bars="se", connect=TRUE, legend.pos="farright"))
dev.print(png, filename="/Users/apzuba/Desktop/KategoriaZgodnosc.png", width=10, height=10, pointsize=12, 
  units="in", res=72)
dane_correct_bezFlower <- subset(dane_correct, subset=kategoria  =/ "flower")
dane_correct <- within(dane_correct, {
  pos <- NULL 
})
dane_correct <- within(dane_correct, {
  condition <- NULL 
})
dane_corr_noFlow <- subset(dane_correct, subset=kategoria =="mushroom" or "spider")
dane_corr_noMush <- subset(dane_correct, subset=kategoria =="mushroom, spider")
dane_corr_noFlow <- subset(dane_correct, subset=kategoria - "flower")
with(dane_corr_noFlow, Hist(rt, scale="frequency", breaks="Sturges", col="darkgray"))
dane_corr_Mush <- subset(dane_correct, subset=kategoria == "mushroom")
dane_corr_Spi <- subset(dane_correct, subset=kategoria == "spider")
dane_corr_MushSpi <- mergeRows(dane_corr_Spi, dane_corr_Mush, common.only=FALSE)
with(dane_corr_MushSpi, plotMeans(rt, kategoria, zgodnosc, error.bars="se", connect=TRUE, legend.pos="farright"))
lmMushSpi_ZgKat <- lm(rt ~ zgodnosc *kategoria, data=dane_corr_MushSpi)
summary(lmMushSpi_ZgKat)
with(dane_corr_MushSpi, plotMeans(rt, kategoria, zgodnosc, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
with(dane_corr_MushSpi, plotMeans(rt, kategoria, zgodnosc, error.bars="conf.int", level=0.95, connect=TRUE, 
  legend.pos="farright"))
dane_TP_corr$dane_TP_corrMush <- with(dane_TP_corr, factor(target, levels=c('mushroom','spider','flower')))
with(dane_TP_corr, plotMeans(rt, dane_TP_corrMush, error.bars="se", connect=TRUE))
with(dane_TP_corr, plotMeans(rt, dane_TP_corrMush, error.bars="conf.int", level=0.95, connect=TRUE))
dane_TP_corr$kat <- with(dane_TP_corr, factor(dane_TP_corrMush, levels=c('mushroom','spider','flower')))
with(dane_TP_corr, plotMeans(rt, kat, error.bars="conf.int", level=0.95, connect=TRUE))

