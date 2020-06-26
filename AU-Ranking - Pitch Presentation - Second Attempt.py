#!/usr/bin/env python
# coding: utf-8

# # Loading data
# Loading data from all pitchers, filling the missing values with the last value

# In[1]:


import pandas as pd


# In[2]:


import warnings
warnings.filterwarnings("ignore")


# In[3]:


p1 = pd.read_csv("Data/2018-2019/OpenFace/2018-2019_1_LittleSister.csv")
p1.fillna(method = 'pad')


# In[4]:


p2 = pd.read_csv("Data/2018-2019/OpenFace/2018-2019_2_FLIPR.csv")
p1.fillna(method = 'pad')


# In[5]:


p3 = pd.read_csv("Data/2018-2019/OpenFace/2018-2019_3_BubblePop.csv")
p1.fillna(method = 'pad')


# In[6]:


p4 = pd.read_csv("Data/2018-2019/OpenFace/2018-2019_4_RecognEyes.csv")
p1.fillna(method = 'pad')


# In[7]:


p5 = pd.read_csv("Data/2018-2019/OpenFace/2018-2019_5_HOTIDY.csv")
p1.fillna(method = 'pad')


# In[8]:


p6 = pd.read_csv("Data/2018-2019/OpenFace/2018-2019_6_FitPoint.csv")
p1.fillna(method = 'pad')


# In[9]:


p7 = pd.read_csv("Data/2018-2019/OpenFace/2018-2019_7_SOLON.csv")
p1.fillna(method = 'pad')


# In[10]:


p8 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_1-1_tAIste.csv")
p1.fillna(method = 'pad')


# In[11]:


p9 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_1-2_Choos3Wisely.csv")
p1.fillna(method = 'pad')


# In[12]:


p10 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_1-3_SmArt.csv")
p1.fillna(method = 'pad')


# In[13]:


p11 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_1-4_StudentFood.csv")
p1.fillna(method = 'pad')


# In[14]:


p12 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_1-5_wAIste.csv")
p1.fillna(method = 'pad')


# In[15]:


p13 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_1-7_Chattern.csv")
p1.fillna(method = 'pad')


# In[16]:


p14 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_1-8_FindIT.csv")
p1.fillna(method = 'pad')


# In[17]:


p15 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_2-1_Ar-T-ficial.csv")
p1.fillna(method = 'pad')


# In[18]:


p16 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_2-2_Recipe-Me.csv")
p1.fillna(method = 'pad')


# In[19]:


p17 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_2-3_Salix.csv")
p1.fillna(method = 'pad')


# In[20]:


p18 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_2-4_Peech.csv")
p1.fillna(method = 'pad')


# In[21]:


p19 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_2-6_HoodFood.csv")
p1.fillna(method = 'pad')


# In[22]:


p20 = pd.read_csv("Data/2019-2020/Pitchers/2019-2020_2-7_LockUp.csv")
p1.fillna(method = 'pad')


# In[23]:


p21 = pd.read_csv("Data/DEiA III 2019-2020 SM1/DEiA_1_Ziggurat.csv")
p1.fillna(method = 'pad')


# In[24]:


p22 = pd.read_csv("Data/DEiA III 2019-2020 SM1/DEiA_2_PREA.csv")
p1.fillna(method = 'pad')


# In[25]:


p23 = pd.read_csv("Data/DEiA III 2019-2020 SM1/DEiA_3_YoungBoosters.csv")
p1.fillna(method = 'pad')


# In[26]:


p24 = pd.read_csv("Data/DEiA III 2019-2020 SM1/DEiA_4_Whitebox.csv")
p1.fillna(method = 'pad')


# In[27]:


p25 = pd.read_csv("Data/DEiA III 2019-2020 SM1/DEiA_5_SoccerAcademy.csv")
p1.fillna(method = 'pad')


# # Data cleaning

# Keeping only the rows that correspond with the pitch presentation and with a confidence higher than or equal to .7

# In[28]:


p1c = p1[(p1[" confidence"] >= 0.7) & (p1[" timestamp"] >= 51.00) & (p1[" timestamp"] <= 208.00)]


# In[29]:


p2c = p2[(p2[" confidence"] >= 0.7) & (p2[" timestamp"] >= 5.00) & (p2[" timestamp"] <= 195.00)]


# In[30]:


p3c = p3[(p3[" confidence"] >= 0.7) & (p3[" timestamp"] >= 19.00) & (p3[" timestamp"] <= 335.00)]


# In[31]:


p4c = p4[(p4[" confidence"] >= 0.7) & (p4[" timestamp"] >= 1.00) & (p4[" timestamp"] <= 206.00)]


# In[32]:


p5c = p5[(p5[" confidence"] >= 0.7) & (p5[" timestamp"] >= 3.00) & (p5[" timestamp"] <= 194.00)]


# In[33]:


p6c = p6[(p6[" confidence"] >= 0.7) & (p6[" timestamp"] >= 5.00) & (p6[" timestamp"] <= 204.00)]


# In[34]:


p7c = p7[(p7[" confidence"] >= 0.7) & (p7[" timestamp"] >= 23.00) & (p7[" timestamp"] <= 329.00)]


# In[35]:


p8c = p8[(p8[" confidence"] >= 0.7) & (p8[" timestamp"] <= 281.00)]


# In[36]:


p9c = p9[(p9[" confidence"] >= 0.7) & (p9[" timestamp"] <= 178.00)]


# In[37]:


p10c = p10[(p10[" confidence"] >= 0.7) & (p10[" timestamp"] <= 176.00)]


# In[38]:


p11c = p11[(p11[" confidence"] >= 0.7) & (p11[" timestamp"] <= 150.00)]


# In[39]:


p12c = p12[(p12[" confidence"] >= 0.7) & (p12[" timestamp"] <= 191.00)]


# In[40]:


p13c = p13[(p13[" confidence"] >= 0.7) & (p13[" timestamp"] <= 195.00)]


# In[41]:


p14c = p14[(p14[" confidence"] >= 0.7) & (p14[" timestamp"] <= 218.00)]


# In[42]:


p15c = p15[(p15[" confidence"] >= 0.7) & (p15[" timestamp"] <= 186.00)]


# In[43]:


p16c = p16[(p16[" confidence"] >= 0.7) & (p16[" timestamp"] <= 566.00)]


# In[44]:


p17c = p17[(p17[" confidence"] >= 0.7) & (p17[" timestamp"] <= 184.00)]


# In[45]:


p18c = p18[(p18[" confidence"] >= 0.7) & (p18[" timestamp"] <= 257.00)]


# In[46]:


p19c = p19[(p19[" confidence"] >= 0.7) & (p19[" timestamp"] <= 182.00)]


# In[47]:


p20c = p20[(p20[" confidence"] >= 0.7) & (p20[" timestamp"] <= 236.00)]


# In[48]:


p21c = p21[(p21[" confidence"] >= 0.7) & (p21[" timestamp"] <= 202.00)]


# In[49]:


p22c = p22[(p22[" confidence"] >= 0.7) & (p22[" timestamp"] <= 281.00)]


# In[50]:


p23c = p23[(p23[" confidence"] >= 0.7) & (p23[" timestamp"] <= 169.00)]


# In[51]:


p24c = p24[(p24[" confidence"] >= 0.7) & (p24[" timestamp"] >= 1.00) & (p24[" timestamp"] <= 203.00)]


# In[52]:


p25c = p25[(p25[" confidence"] >= 0.7) & (p25[" timestamp"] <= 307.00)]


# Keeping only the AU_r columns

# In[53]:


p1c = p1c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[54]:


p2c = p2c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[55]:


p3c = p3c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[56]:


p4c = p4c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[57]:


p5c = p5c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[58]:


p6c = p6c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[59]:


p7c = p7c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[60]:


p8c = p8c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[61]:


p9c = p9c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[62]:


p10c = p10c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[63]:


p11c = p11c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[64]:


p12c = p12c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[65]:


p13c = p13c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[66]:


p14c = p14c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[67]:


p15c = p15c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[68]:


p16c = p16c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[69]:


p17c = p17c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[70]:


p18c = p18c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[71]:


p19c = p19c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[72]:


p20c = p20c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[73]:


p21c = p21c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[74]:


p22c = p22c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[75]:


p23c = p23c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[76]:


p24c = p24c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[77]:


p25c = p25c[[" AU01_r"," AU02_r"," AU04_r"," AU05_r"," AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# # Pre-processing

# Creating a dataframe with the statical features mean, maximum, standard deviation, skewness and kurtosis per action unit

# Minimum was not included as this was 0.00 for everyone

# In[78]:


import numpy as np


# In[79]:


from scipy.stats import skew, kurtosis


# In[80]:


pitchers = [p1c, p2c, p3c, p4c, p5c, p6c, p7c, p8c, p9c, p10c, p11c, p12c, p13c, p14c, p15c, p16c, p17c, p18c, p19c, p20c,
           p21c, p22c, p23c, p24c, p25c]

matrix = np.zeros((25,85))

for i in range(len(pitchers)):
    for j in range (0,17):
        matrix[i,j*5:j*5+5] = [np.mean(pitchers[i].iloc[:, j:j+1].values), np.amax(pitchers[i].iloc[:, j:j+1].values),
                               np.std(pitchers[i].iloc[:, j:j+1].values), skew(pitchers[i].iloc[:, j:j+1].values),
                               kurtosis(pitchers[i].iloc[:, j:j+1].values)]
        
data = pd.DataFrame(matrix)
data = data.rename(columns={0: 'meanAU1', 1: 'maxAU1', 2: 'stdAU1', 3: 'skewAU1', 4: 'kurtAU1'})
data = data.rename(columns={5: 'meanAU2', 6: 'maxAU2', 7: 'stdAU2', 8: 'skewAU2', 9: 'kurtAU2'})
data = data.rename(columns={10: 'meanAU4', 11: 'maxAU4', 12: 'stdAU4', 13: 'skewAU4', 14: 'kurtAU4'})
data = data.rename(columns={15: 'meanAU5', 16: 'maxAU5', 17: 'stdAU5', 18: 'skewAU5', 19: 'kurtAU5'})
data = data.rename(columns={20: 'meanAU6', 21: 'maxAU6', 22: 'stdAU6', 23: 'skewAU6', 24: 'kurtAU6'})
data = data.rename(columns={25: 'meanAU7', 26: 'maxAU7', 27: 'stdAU7', 28: 'skewAU7', 29: 'kurtAU7'})
data = data.rename(columns={30: 'meanAU9', 31: 'maxAU9', 32: 'stdAU9', 33: 'skewAU9', 34: 'kurtAU9'})
data = data.rename(columns={35: 'meanAU10', 36: 'maxAU10', 37: 'stdAU10', 38: 'skewAU10', 39: 'kurtAU10'})
data = data.rename(columns={40: 'meanAU12', 41: 'maxAU12', 42: 'stdAU12', 43: 'skewAU12', 44: 'kurtAU12'})
data = data.rename(columns={45: 'meanAU14', 46: 'maxAU14', 47: 'stdAU14', 48: 'skewAU14', 49: 'kurtAU14'})
data = data.rename(columns={50: 'meanAU15', 51: 'maxAU15', 52: 'stdAU15', 53: 'skewAU15', 54: 'kurtAU15'})
data = data.rename(columns={55: 'meanAU17', 56: 'maxAU17', 57: 'stdAU17', 58: 'skewAU17', 59: 'kurtAU17'})
data = data.rename(columns={60: 'meanAU20', 61: 'maxAU20', 62: 'stdAU20', 63: 'skewAU20', 64: 'kurtAU20'})
data = data.rename(columns={65: 'meanAU23', 66: 'maxAU23', 67: 'stdAU23', 68: 'skewAU23', 69: 'kurtAU23'})
data = data.rename(columns={70: 'meanAU25', 71: 'maxAU25', 72: 'stdAU25', 73: 'skewAU25', 74: 'kurtAU25'})
data = data.rename(columns={75: 'meanAU26', 76: 'maxAU26', 77: 'stdAU26', 78: 'skewAU26', 79: 'kurtAU26'})
data = data.rename(columns={80: 'meanAU45', 81: 'maxAU45', 82: 'stdAU45', 83: 'skewAU45', 84: 'kurtAU45'})
data


# # Loading data

# Loading the rankings dataset

# In[81]:


rankings = pd.read_csv("Data/Created Datasets/Rankings.csv")
rankings


# # Pre-processing

# Converting the ranking classes to numbers

# In[82]:


from sklearn import preprocessing
le = preprocessing.LabelEncoder()
y_encoded = le.fit_transform(rankings['Classified Ranking'])
y_encoded


# 0 = high, 2 = middle, 1 = low

# Adding encoded rankings to dataset

# In[83]:


data["y"] = y_encoded


# Storing the data set as backup

# In[84]:


data.to_csv("statistical_features_full.csv", index=False)


# Making sure only the features from the train data that correlate abs(0.2) or higher with the target are included for each of the five manually created folds

# In[85]:


selected_features1 = []
corr_df = data[0:15].corr(method = 'pearson')
for column in corr_df:
    if corr_df["y"][column] >= abs(0.2):
        selected_features1.append(column)
selected_features1 = selected_features1[:-1]
X_train1 = data[0:15][selected_features1]
X_val1 = data[15:20][selected_features1]
X_test1 = data[20:25][selected_features1]
 
print(X_train1.shape)
print(X_val1.shape)
print(X_test1.shape)

print(selected_features1)


# In[86]:


selected_features2 = []
corr_df = data.iloc[[0,1,2,3,4,5,6,7,8,9,20,21,22,23,24]].corr(method = 'pearson')
for column in corr_df:
    if corr_df["y"][column] >= abs(0.2):
        selected_features2.append(column)
selected_features2 = selected_features2[:-1]
X_train2 = data.iloc[[0,1,2,3,4,5,6,7,8,9,20,21,22,23,24]][selected_features2]
X_val2 = data[10:15][selected_features2]
X_test2 = data[15:20][selected_features2]
 
print(X_train2.shape)    
print(X_val2.shape)
print(X_test2.shape)

print(selected_features2)


# In[87]:


selected_features3 = []
corr_df = data.iloc[[0,1,2,3,4,15,16,17,18,19,20,21,22,23,24]].corr(method = 'pearson')
for column in corr_df:
    if corr_df["y"][column] >= abs(0.2):
        selected_features3.append(column)
selected_features3 = selected_features3[:-1]
X_train3 = data.iloc[[0,1,2,3,4,15,16,17,18,19,20,21,22,23,24]][selected_features3]
X_val3 = data[5:10][selected_features3]
X_test3 = data[10:15][selected_features3]
        
print(X_train3.shape)
print(X_val3.shape)
print(X_test3.shape)

print(selected_features3)


# In[88]:


selected_features4 = []
corr_df = data.iloc[[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]].corr(method = 'pearson')
for column in corr_df:
    if corr_df["y"][column] >= abs(0.2):
        selected_features4.append(column)
selected_features4 = selected_features4[:-1]
X_train4 = data.iloc[[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]][selected_features4]
X_val4 = data[0:5][selected_features4]
X_test4 = data[5:10][selected_features4]
 
print(X_train4.shape)
print(X_val4.shape)
print(X_test4.shape)

print(selected_features4)


# In[89]:


selected_features5 = []
corr_df = data.iloc[[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]].corr(method = 'pearson')
for column in corr_df:
    if corr_df["y"][column] >= abs(0.2):
        selected_features5.append(column)
selected_features5 = selected_features5[:-1]
X_train5 = data.iloc[[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]][selected_features5]
X_val5 = data[20:25][selected_features5]
X_test5 = data[0:5][selected_features5]

print(X_train5.shape)
print(X_val5.shape)
print(X_test5.shape)

print(selected_features5)


# In[90]:


selected_features = [selected_features1, selected_features2, selected_features3, selected_features4, selected_features5]


# Establishing majority baseline

# In[91]:


c0 = 0
c1 = 0
c2 = 0
for c in y_encoded:
    if c == 0:
        c0 += 1
    if c == 1:
        c1 += 1
    if c == 2:
        c2 += 1
print(c0)
print(c1)
print(c2)


# In[92]:


10/(7+10+8)


# Scaling the features

# In[93]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaler.fit(X_train1)
X_train1 = scaler.transform(X_train1)
X_val1 = scaler.transform(X_val1)
X_test1 = scaler.transform(X_test1)

scaler.fit(X_train2)
X_train2 = scaler.transform(X_train2)
X_val2 = scaler.transform(X_val2)
X_test2 = scaler.transform(X_test2)

scaler.fit(X_train3)
X_train3 = scaler.transform(X_train3)
X_val3 = scaler.transform(X_val3)
X_test3 = scaler.transform(X_test3)

scaler.fit(X_train4)
X_train4 = scaler.transform(X_train4)
X_val4 = scaler.transform(X_val4)
X_test4 = scaler.transform(X_test4)

scaler.fit(X_train5)
X_train5 = scaler.transform(X_train5)
X_val5 = scaler.transform(X_val5)
X_test5 = scaler.transform(X_test5)


# Creating the five folds for the target

# In[94]:


y = data["y"]


# In[95]:


y_train1 = y[0:15]
y_train2 = np.concatenate((y[0:10], y[20:25]))
y_train3 = np.concatenate((y[0:5], y[15:25]))
y_train4 = y[10:25]
y_train5 = y[5:20]


# In[96]:


y_val1 = y[15:20]
y_val2 = y[10:15]
y_val3 = y[5:10]
y_val4 = y[0:5]
y_val5 = y[20:25]


# In[97]:


y_test1 = y[20:25]
y_test2 = y[15:20]
y_test3 = y[10:15]
y_test4 = y[5:10]
y_test5 = y[0:5]


# Creating variables for the code below to loop over so that the algorithm is run on each of the five folds

# In[98]:


X_train = X_train1, X_train2, X_train3, X_train4, X_train5
X_val = X_val1, X_val2, X_val3, X_val4, X_val5
X_test = X_test1, X_test2, X_test3, X_test4, X_test5
y_train = y_train1, y_train2, y_train3, y_train4, y_train5
y_val = y_val1, y_val2, y_val3, y_val4, y_val5
y_test = y_test1, y_test2, y_test3, y_test4, y_test5


# In[99]:


from sklearn.metrics import accuracy_score, f1_score


# ## K-Nearest Neighbors

# In[100]:


from sklearn.neighbors import KNeighborsClassifier


# In[101]:


n_neighbors = list(range(1,4))
weights = ["uniform", "distance"]


# In[102]:


average_accuracies = []
for i in range(0,5):
    highest_accuracy = 0
    for j in n_neighbors:
        for k in weights:
            knn = KNeighborsClassifier(n_neighbors = j, weights = k)
            knn.fit(X_train[i],y_train[i])
            y_val_pred = knn.predict(X_val[i])
            current_accuracy = accuracy_score(y_val[i],y_val_pred)
            if current_accuracy > highest_accuracy:
                highest_accuracy = current_accuracy
                best_n_neighbors = j
                best_weights = k
    print(best_n_neighbors)
    print(best_weights)
    knn = KNeighborsClassifier(n_neighbors = best_n_neighbors, weights = best_weights)
    knn.fit(X_train[i], y_train[i])
    y_test_pred = knn.predict(X_test[i])
    best_accuracy = accuracy_score(y_test[i],y_test_pred)
    print(best_accuracy)
    average_accuracies.append(best_accuracy)
print(average_accuracies)
print(np.mean(average_accuracies))


# In[103]:


average_macrof1s = []
for i in range(0,5):
    highest_macrof1 = 0
    for j in n_neighbors:
        for k in weights:
            knn = KNeighborsClassifier(n_neighbors = j, weights = k)
            knn.fit(X_train[i],y_train[i])
            y_val_pred = knn.predict(X_val[i])
            current_macrof1 = f1_score(y_val[i],y_val_pred, average = 'macro')
            if current_macrof1 > highest_macrof1:
                highest_macrof1 = current_macrof1
                best_n_neighbors = j
                best_weights = k
    print(best_n_neighbors)
    print(best_weights)
    knn = KNeighborsClassifier(n_neighbors = best_n_neighbors, weights = best_weights)
    knn.fit(X_train[i], y_train[i])
    y_test_pred = knn.predict(X_test[i])
    best_macrof1 = f1_score(y_test[i],y_test_pred, average = 'macro')
    print(best_macrof1)
    average_macrof1s.append(best_macrof1)
print(average_macrof1s)
print(np.mean(average_macrof1s))


# ## Multinomial Logistic Regression

# In[104]:


from sklearn.linear_model import LogisticRegression


# Only 'newton-cg', 'sag', 'saga' and 'lbfgs' handle multinomial loss, and these only handle l2 or no penalty

# In[105]:


penalty = ['l2', 'none']
C = [0.001,0.01,0.1,1,10,100]
solver = ['newton-cg', 'sag', 'saga', 'lbfgs']


# In[106]:


average_accuracies = []
for i in range(0,5):
    highest_accuracy = 0
    for j in penalty:
        for k in C:
            for l in solver:
                lr = LogisticRegression(penalty = j, C = k, solver = l, multi_class = 'multinomial')
                lr.fit(X_train[i],y_train[i])
                y_val_pred = lr.predict(X_val[i])
                current_accuracy = accuracy_score(y_val[i],y_val_pred)
                if current_accuracy > highest_accuracy:
                    highest_accuracy = current_accuracy
                    best_penalty = j
                    best_C = k
                    best_solver = l
    print(best_penalty)
    print(best_C)
    print(best_solver)
    lr = LogisticRegression(penalty = best_penalty, C = best_C, solver = best_solver, multi_class = 'multinomial')
    lr.fit(X_train[i], y_train[i])
    y_test_pred = lr.predict(X_test[i])
    best_accuracy = accuracy_score(y_test[i],y_test_pred)
    print(best_accuracy)
    average_accuracies.append(best_accuracy)
print(average_accuracies)
print(np.mean(average_accuracies))


# In[107]:


average_macrof1s = []
for i in range(0,5):
    highest_macrof1 = 0
    for j in penalty:
        for k in C:
            for l in solver:
                lr = LogisticRegression(penalty = j, C = k, solver = l, multi_class = 'multinomial')
                lr.fit(X_train[i],y_train[i])
                y_val_pred = lr.predict(X_val[i])
                current_macrof1 = f1_score(y_val[i],y_val_pred, average = 'macro')
                if current_macrof1 > highest_macrof1:
                    highest_macrof1 = current_macrof1
                    best_penalty = j
                    best_C = k
                    best_solver = l
    print(best_penalty)
    print(best_C)
    print(best_solver)
    lr = LogisticRegression(penalty = best_penalty, C = best_C, solver = best_solver, multi_class = 'multinomial')
    lr.fit(X_train[i], y_train[i])
    y_test_pred = lr.predict(X_test[i])
    best_macrof1 = f1_score(y_test[i],y_test_pred, average = 'macro')
    print(best_macrof1)
    average_macrof1s.append(best_macrof1)
print(average_macrof1s)
print(np.mean(average_macrof1s))


# ## Support Vector Machine

# In[108]:


from sklearn.svm import SVC


# In[109]:


kernel = ["rbf", "linear", "sigmoid", "poly"]
gamma = ["scale", "auto"]


# In[110]:


average_accuracies = []
for i in range(0,5):
    highest_accuracy = 0
    for j in kernel:
        for k in gamma:
            svm = SVC(kernel = j, gamma = k)
            svm.fit(X_train[i],y_train[i])
            y_val_pred = svm.predict(X_val[i])
            current_accuracy = accuracy_score(y_val[i],y_val_pred)
            if current_accuracy > highest_accuracy:
                highest_accuracy = current_accuracy
                best_kernel = j
                best_gamma = k
    print(best_kernel)
    print(best_gamma)
    svm = SVC(kernel = best_kernel, gamma = best_gamma)
    svm.fit(X_train[i], y_train[i])
    y_test_pred = svm.predict(X_test[i])
    best_accuracy = accuracy_score(y_test[i],y_test_pred)
    print(best_accuracy)
    average_accuracies.append(best_accuracy)
print(average_accuracies)
print(np.mean(average_accuracies))


# In[111]:


average_macrof1s = []
for i in range(0,5):
    highest_macrof1 = 0
    for j in kernel:
        for k in gamma:
            svm = SVC(kernel = j, gamma = k)
            svm.fit(X_train[i],y_train[i])
            y_val_pred = svm.predict(X_val[i])
            current_macrof1 = f1_score(y_val[i],y_val_pred, average = 'macro')
            if current_macrof1 > highest_macrof1:
                highest_macrof1 = current_macrof1
                best_kernel = j
                best_gamma = k
    print(best_kernel)
    print(best_gamma)
    svm = SVC(kernel = best_kernel, gamma = best_gamma)
    svm.fit(X_train[i], y_train[i])
    y_test_pred = svm.predict(X_test[i])
    best_macrof1 = f1_score(y_test[i],y_test_pred, average = 'macro')
    print(best_macrof1)
    average_macrof1s.append(best_macrof1)
print(average_macrof1s)
print(np.mean(average_macrof1s))


# # Decision Tree

# In[112]:


from sklearn.tree import DecisionTreeClassifier


# In[113]:


criterion = ['gini', 'entropy']
max_depth = [4,6,8,12]
max_leaf_nodes = list(range(3,10))
min_samples_split = [2,3,4]


# In[114]:


np.random.seed(1234)

average_accuracies = []
for i in range(0,5):
    highest_accuracy = 0
    for j in criterion:
        for k in max_depth:
            for l in max_leaf_nodes:
                for m in min_samples_split:
                    dt = DecisionTreeClassifier(criterion = j, max_depth = k, max_leaf_nodes = l, min_samples_split = m)
                    dt.fit(X_train[i],y_train[i])
                    y_val_pred = dt.predict(X_val[i])
                    current_accuracy = accuracy_score(y_val[i],y_val_pred)
                    if current_accuracy > highest_accuracy:
                        highest_accuracy = current_accuracy
                        best_criterion = j
                        best_max_depth = k
                        best_max_leaf_nodes = l
                        best_min_samples_split = m
    print(best_criterion)
    print(best_max_depth)
    print(best_max_leaf_nodes)
    print(best_min_samples_split)
    dt = DecisionTreeClassifier(criterion = best_criterion, max_depth = best_max_depth,
                                max_leaf_nodes = best_max_leaf_nodes, min_samples_split = best_min_samples_split)
    dt.fit(X_train[i], y_train[i])
    y_test_pred = dt.predict(X_test[i])
    best_accuracy = accuracy_score(y_test[i],y_test_pred)
    print(best_accuracy)
    average_accuracies.append(best_accuracy)
    names = selected_features[i]
    print(sorted(zip(map(lambda x: round(x, 4), dt.feature_importances_), names), reverse=True))
print(average_accuracies)
print(np.mean(average_accuracies))


# In[115]:


np.random.seed(1234)

average_macrof1s = []
for i in range(0,5):
    highest_macrof1 = 0
    for j in criterion:
        for k in max_depth:
            for l in max_leaf_nodes:
                for m in min_samples_split:
                    dt = DecisionTreeClassifier(criterion = j, max_depth = k, max_leaf_nodes = l, min_samples_split = m)
                    dt.fit(X_train[i],y_train[i])
                    y_val_pred = dt.predict(X_val[i])
                    current_macrof1 = f1_score(y_val[i],y_val_pred, average = 'macro')
                    if current_macrof1 > highest_macrof1:
                        highest_macrof1 = current_macrof1
                        best_criterion = j
                        best_max_depth = k
                        best_max_leaf_nodes = l
                        best_min_samples_split = m
    print(best_criterion)
    print(best_max_depth)
    print(best_max_leaf_nodes)
    print(best_min_samples_split)
    dt = DecisionTreeClassifier(criterion = best_criterion, max_depth = best_max_depth, 
                                max_leaf_nodes = best_max_leaf_nodes, min_samples_split = best_min_samples_split)
    dt.fit(X_train[i], y_train[i])
    y_test_pred = dt.predict(X_test[i])
    best_macrof1 = f1_score(y_test[i],y_test_pred, average = 'macro')
    print(best_macrof1)
    average_macrof1s.append(best_macrof1)
print(average_macrof1s)
print(np.mean(average_macrof1s))


# ## Random Forest

# In[116]:


from sklearn.ensemble import RandomForestClassifier


# In[117]:


criterion = ['gini', 'entropy']
n_estimators = [2, 4, 6, 8, 10,30,50,70,100]
max_depth = [4,6,8,12]
max_leaf_nodes = list(range(3,10))
min_samples_split = [2,3,4]


# In[118]:


np.random.seed(1234)

average_accuracies = []
for i in range(0,5):
    highest_accuracy = 0
    for j in criterion:
        for k in n_estimators:
            for l in max_depth:
                for m in max_leaf_nodes:
                    for n in min_samples_split:
                        rf = RandomForestClassifier(criterion = j, n_estimators = k, max_depth = l, max_leaf_nodes = m,
                                                    min_samples_split = n)
                        rf.fit(X_train[i],y_train[i])
                        y_val_pred = rf.predict(X_val[i])
                        current_accuracy = accuracy_score(y_val[i],y_val_pred)
                        if current_accuracy > highest_accuracy:
                            highest_accuracy = current_accuracy
                            best_criterion = j
                            best_n_estimators = k
                            best_max_depth = l
                            best_max_leaf_nodes = m
                            best_min_samples_split = n
    print(best_criterion)
    print(best_n_estimators)
    print(best_max_depth)
    print(best_max_leaf_nodes)
    print(best_min_samples_split)
    rf = RandomForestClassifier(criterion = best_criterion, n_estimators = best_n_estimators, max_depth = best_max_depth,
                                max_leaf_nodes = best_max_leaf_nodes, min_samples_split = best_min_samples_split)
    rf.fit(X_train[i], y_train[i])
    y_test_pred = rf.predict(X_test[i])
    best_accuracy = accuracy_score(y_test[i],y_test_pred)
    print(best_accuracy)
    average_accuracies.append(best_accuracy)
print(average_accuracies)
print(np.mean(average_accuracies))


# In[119]:


np.random.seed(1234)

average_macrof1s = []
for i in range(0,5):
    highest_macrof1 = 0
    for j in criterion:
        for k in n_estimators:
            for l in max_depth:
                for m in max_leaf_nodes:
                    for n in min_samples_split:
                        rf = RandomForestClassifier(criterion = j, n_estimators = k, max_depth = l, max_leaf_nodes = m,
                                                    min_samples_split = n)
                        rf.fit(X_train[i],y_train[i])
                        y_val_pred = rf.predict(X_val[i])
                        current_macrof1 = f1_score(y_val[i],y_val_pred, average = 'macro')
                        if current_macrof1 > highest_macrof1:
                            highest_macrof1 = current_macrof1
                            best_criterion = j
                            best_n_estimators = k
                            best_max_depth = l
                            best_max_leaf_nodes = m
                            best_min_samples_split = n
    print(best_criterion)
    print(best_n_estimators)
    print(best_max_depth)
    print(best_max_leaf_nodes)
    print(best_min_samples_split)
    rf = RandomForestClassifier(criterion = best_criterion, n_estimators = best_n_estimators, max_depth = best_max_depth,
                                max_leaf_nodes = best_max_leaf_nodes, min_samples_split = best_min_samples_split)
    rf.fit(X_train[i], y_train[i])
    y_test_pred = rf.predict(X_test[i])
    best_macrof1 = f1_score(y_test[i],y_test_pred, average = 'macro')
    print(best_macrof1)
    average_macrof1s.append(best_macrof1)
print(average_macrof1s)
print(np.mean(average_macrof1s))

