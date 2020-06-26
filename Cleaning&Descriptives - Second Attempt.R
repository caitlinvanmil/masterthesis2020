#Loading required packages
library(dplyr)
library(readr)
library(ggplot2)
library(reshape2)
library(ggcorrplot)

#Combining the csv files from 2018-2019, 2019-2020 and DEiA 2019-2020 SM1; selecting the right columns; and deleting the low confidence rows
df1 <- list.files(path= "C:/Users/caitl.DESKTOP-RHI6DMF/OneDrive - tilburguniversity.edu/Data Science/Master/Blok 3 & 4/Master's Thesis/Data/2018-2019/OpenFace", full.names = TRUE) %>% 
  lapply(read_csv) %>% 
  bind_rows 

df1 <- select(df1,frame, timestamp, confidence, AU01_r:AU45_r)
df1c <- subset(df1, confidence>=0.7)

df2 <- list.files(path="C:/Users/caitl.DESKTOP-RHI6DMF/OneDrive - tilburguniversity.edu/Data Science/Master/Blok 3 & 4/Master's Thesis/Data/2019-2020/Pitchers", full.names = TRUE) %>% 
  lapply(read_csv) %>% 
  bind_rows 

df2 <- select(df2,frame, timestamp, confidence, AU01_r:AU45_r)
df2c <- subset(df2, confidence>=0.7)

df3 <- list.files(path="C:/Users/caitl.DESKTOP-RHI6DMF/OneDrive - tilburguniversity.edu/Data Science/Master/Blok 3 & 4/Master's Thesis/Data/DEiA III 2019-2020 SM1", full.names = TRUE) %>% 
  lapply(read_csv) %>% 
  bind_rows 

df3 <- select(df3,frame, timestamp, confidence, AU01_r:AU45_r)
df3c <- subset(df3, confidence>=0.7)

#Combining those three data frames into one data frame
df12 = rbind(df1c,df2c)
pitcherdata = rbind(df12,df3c)

#Descriptive statistics
summary(pitcherdata$AU01_r)
sd(pitcherdata$AU01_r)

summary(pitcherdata$AU02_r)
sd(pitcherdata$AU02_r)

summary(pitcherdata$AU04_r)
sd(pitcherdata$AU04_r)

summary(pitcherdata$AU05_r)
sd(pitcherdata$AU05_r)

summary(pitcherdata$AU06_r)
sd(pitcherdata$AU06_r)

summary(pitcherdata$AU07_r)
sd(pitcherdata$AU07_r)

summary(pitcherdata$AU09_r)
sd(pitcherdata$AU09_r)

summary(pitcherdata$AU10_r)
sd(pitcherdata$AU10_r)

summary(pitcherdata$AU12_r)
sd(pitcherdata$AU12_r)

summary(pitcherdata$AU14_r)
sd(pitcherdata$AU14_r)

summary(pitcherdata$AU15_r)
sd(pitcherdata$AU15_r)

summary(pitcherdata$AU17_r)
sd(pitcherdata$AU17_r)

summary(pitcherdata$AU20_r)
sd(pitcherdata$AU20_r)

summary(pitcherdata$AU23_r)
sd(pitcherdata$AU23_r)

summary(pitcherdata$AU25_r)
sd(pitcherdata$AU25_r)

summary(pitcherdata$AU26_r)
sd(pitcherdata$AU26_r)

summary(pitcherdata$AU45_r)
sd(pitcherdata$AU45_r)

#Missing values
colSums(is.na(pitcherdata))

#Reading rankings csv file
rankings <- read.csv(paste0("Data/Created Datasets/Rankings.csv"), row.names = 1)

#Stacked bar graph for rankings
ggplot(rankings, aes("classified rankings"))+
  geom_bar(aes(fill = Classified.Ranking))+
  scale_fill_manual("classes", values = c("midnightblue", "grey", "darkgoldenrod3"))

#Pearson correlations between AUs & timestamp
cor.test(pitcherdata$AU01_r, pitcherdata$AU02_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU04_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU05_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU06_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU07_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU09_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU10_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU12_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU14_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU15_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU02_r, pitcherdata$AU04_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU05_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU06_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU07_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU09_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU10_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU12_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU14_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU15_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU02_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU04_r, pitcherdata$AU05_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU06_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU07_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU09_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU10_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU12_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU14_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU15_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU04_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU05_r, pitcherdata$AU06_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU07_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU09_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU10_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU12_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU14_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU15_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU05_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU06_r, pitcherdata$AU07_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU09_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU10_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU12_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU14_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU15_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU06_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU07_r, pitcherdata$AU09_r)
cor.test(pitcherdata$AU07_r, pitcherdata$AU10_r)
cor.test(pitcherdata$AU07_r, pitcherdata$AU12_r)
cor.test(pitcherdata$AU07_r, pitcherdata$AU14_r)
cor.test(pitcherdata$AU07_r, pitcherdata$AU15_r)
cor.test(pitcherdata$AU07_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU07_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU07_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU07_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU07_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU07_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU09_r, pitcherdata$AU10_r)
cor.test(pitcherdata$AU09_r, pitcherdata$AU12_r)
cor.test(pitcherdata$AU09_r, pitcherdata$AU14_r)
cor.test(pitcherdata$AU09_r, pitcherdata$AU15_r)
cor.test(pitcherdata$AU09_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU09_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU09_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU09_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU09_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU09_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU10_r, pitcherdata$AU12_r)
cor.test(pitcherdata$AU10_r, pitcherdata$AU14_r)
cor.test(pitcherdata$AU10_r, pitcherdata$AU15_r)
cor.test(pitcherdata$AU10_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU10_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU10_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU10_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU10_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU10_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU12_r, pitcherdata$AU14_r)
cor.test(pitcherdata$AU12_r, pitcherdata$AU15_r)
cor.test(pitcherdata$AU01_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU12_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU12_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU12_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU12_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU12_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU14_r, pitcherdata$AU15_r)
cor.test(pitcherdata$AU14_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU14_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU14_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU14_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU14_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU14_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU15_r, pitcherdata$AU17_r)
cor.test(pitcherdata$AU15_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU15_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU15_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU15_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU15_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU17_r, pitcherdata$AU20_r)
cor.test(pitcherdata$AU17_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU17_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU17_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU17_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU20_r, pitcherdata$AU23_r)
cor.test(pitcherdata$AU20_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU20_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU20_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU23_r, pitcherdata$AU25_r)
cor.test(pitcherdata$AU23_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU23_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU25_r, pitcherdata$AU26_r)
cor.test(pitcherdata$AU25_r, pitcherdata$AU45_r)

cor.test(pitcherdata$AU26_r, pitcherdata$AU45_r)

cor.test(pitcherdata$timestamp,pitcherdata$AU01_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU02_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU04_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU05_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU06_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU07_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU09_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU10_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU12_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU14_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU15_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU17_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU20_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU23_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU25_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU26_r)
cor.test(pitcherdata$timestamp,pitcherdata$AU45_r)

#Correlation matrix heatmap
cormat <- round(cor(pitcherdata[,4:20]),2)
rownames(cormat) <- c("Inner brow raiser", "Outer brow raiser", "Brow lowerer",
  "Upper lid raiser", "Cheeck raiser", "Lid tightener", "Nose wrinkler",
  "Upper lip raiser", "Lip corner puller", "Dimpler", "Lip corner depressor", 
  "Chin raiser", "Lip stretcher", "Lip tightener", "Lips part","Jaw drop",
  "Blink")
colnames(cormat) <- c("Inner brow raiser", "Outer brow raiser", "Brow lowerer",
  "Upper lid raiser", "Cheeck raiser", "Lid tightener", "Nose wrinkler",
  "Upper lip raiser", "Lip corner puller", "Dimpler", "Lip corner depressor",
  "Chin raiser", "Lip stretcher", "Lip tightener", "Lips part","Jaw drop",
  "Blink")
head(cormat)

corrplot <- ggcorrplot(cormat, hc.order = FALSE, type = "lower",
  lab = TRUE, colors = c("darkgoldenrod3", "grey", "midnightblue"))
corrplot
