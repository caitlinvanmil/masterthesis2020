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

# Dropping unnecessary columns

# In[28]:


p1c = p1[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[29]:


p2c = p2[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[30]:


p3c = p3[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[31]:


p4c = p4[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[32]:


p5c = p5[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[33]:


p6c = p6[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[34]:


p7c = p7[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[35]:


p8c = p8[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[36]:


p9c = p9[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[37]:


p10c = p10[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[38]:


p11c = p11[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[39]:


p12c = p12[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[40]:


p13c = p13[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[41]:


p14c = p14[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[42]:


p15c = p15[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[43]:


p16c = p16[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[44]:


p17c = p17[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[45]:


p18c = p18[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[46]:


p19c = p19[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[47]:


p20c = p20[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[48]:


p21c = p21[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[49]:


p22c = p22[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[50]:


p23c = p23[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[51]:


p24c = p24[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# In[52]:


p25c = p25[["frame"," confidence"," timestamp"," AU01_r"," AU02_r"," AU04_r"," AU05_r",
                    " AU06_r"," AU07_r"," AU09_r"," AU10_r"," AU12_r"," AU14_r"," AU15_r",
                    " AU17_r"," AU20_r"," AU23_r"," AU25_r"," AU26_r"," AU45_r"]]


# Keeping only the rows with a confidence higher than or equal to .7

# In[53]:


p1c2 = p1c[(p1c[" confidence"] >= 0.7) & (p1c[" timestamp"] > 208.00)]


# In[54]:


p2c2 = p2c[(p2c[" confidence"] >= 0.7) & (p2c[" timestamp"] > 195.00)]


# In[55]:


p3c2 = p3c[(p3c[" confidence"] >= 0.7) & (p3c[" timestamp"] > 335.00)]


# In[56]:


p4c2 = p4c[(p4c[" confidence"] >= 0.7) & (p4c[" timestamp"] > 206.00)]


# In[57]:


p5c2 = p5c[(p5c[" confidence"] >= 0.7) & (p5c[" timestamp"] > 194.00)]


# In[58]:


p6c2 = p6c[(p6c[" confidence"] >= 0.7) & (p6c[" timestamp"] > 204.00)]


# In[59]:


p7c2 = p7c[(p7c[" confidence"] >= 0.7) & (p7c[" timestamp"] > 329.00)]


# In[60]:


p8c2 = p8c[(p8c[" confidence"] >= 0.7) & (p8c[" timestamp"] > 281.00)]


# In[61]:


p9c2 = p9c[(p9c[" confidence"] >= 0.7) & (p9c[" timestamp"] > 178.00)]


# In[62]:


p10c2 = p10c[(p10c[" confidence"] >= 0.7) & (p10c[" timestamp"] > 176.00)]


# In[63]:


p11c2 = p11c[(p11c[" confidence"] >= 0.7) & (p11c[" timestamp"] > 150.00)]


# In[64]:


p12c2 = p12c[(p12c[" confidence"] >= 0.7) & (p12c[" timestamp"] > 191.00)]


# In[65]:


p13c2 = p13c[(p13c[" confidence"] >= 0.7) & (p13c[" timestamp"] > 195.00)]


# In[66]:


p14c2 = p14c[(p14c[" confidence"] >= 0.7) & (p14c[" timestamp"] > 218.00)]


# In[67]:


p15c2 = p15c[(p15c[" confidence"] >= 0.7) & (p15c[" timestamp"] > 186.00)]


# In[68]:


p16c2 = p16c[(p16c[" confidence"] >= 0.7) & (p16c[" timestamp"] > 566.00)]


# In[69]:


p17c2 = p17c[(p17c[" confidence"] >= 0.7) & (p17c[" timestamp"] > 184.00)]


# In[70]:


p18c2 = p18c[(p18c[" confidence"] >= 0.7) & (p18c[" timestamp"] > 257.00)]


# In[71]:


p19c2 = p19c[(p19c[" confidence"] >= 0.7) & (p19c[" timestamp"] > 182.00)]


# In[72]:


p20c2 = p20c[(p20c[" confidence"] >= 0.7) & (p20c[" timestamp"] > 236.00)]


# In[73]:


p21c2 = p21c[(p21c[" confidence"] >= 0.7) & (p21c[" timestamp"] > 202.00)]


# In[74]:


p22c2 = p22c[(p22c[" confidence"] >= 0.7) & (p22c[" timestamp"] > 281.00)]


# In[75]:


p23c2 = p23c[(p23c[" confidence"] >= 0.7) & (p23c[" timestamp"] > 169.00)]


# In[76]:


p24c2 = p24c[(p24c[" confidence"] >= 0.7) & (p24c[" timestamp"] > 203.00)]


# In[77]:


p25c2 = p25c[(p25c[" confidence"] >= 0.7) & (p25c[" timestamp"] > 307.00)]


# # Preprocessing
# Creating arrays of all the variables per pitcher

# In[78]:


import numpy as np


# In[79]:


p1c2frame = np.array(p1c2["frame"])
p1c2conf = np.array(p1c2[" confidence"])
p1c2timestamp = np.array(p1c2[" timestamp"])
p1c2AU01_r = np.array(p1c2[" AU01_r"])
p1c2AU02_r = np.array(p1c2[" AU02_r"])
p1c2AU04_r = np.array(p1c2[" AU04_r"])
p1c2AU05_r = np.array(p1c2[" AU05_r"])
p1c2AU06_r = np.array(p1c2[" AU06_r"])
p1c2AU07_r = np.array(p1c2[" AU07_r"])
p1c2AU09_r = np.array(p1c2[" AU09_r"])
p1c2AU10_r = np.array(p1c2[" AU10_r"])
p1c2AU12_r = np.array(p1c2[" AU12_r"])
p1c2AU14_r = np.array(p1c2[" AU14_r"])
p1c2AU15_r = np.array(p1c2[" AU15_r"])
p1c2AU17_r = np.array(p1c2[" AU17_r"])
p1c2AU20_r = np.array(p1c2[" AU20_r"])
p1c2AU23_r = np.array(p1c2[" AU23_r"])
p1c2AU25_r = np.array(p1c2[" AU25_r"])
p1c2AU26_r = np.array(p1c2[" AU26_r"])
p1c2AU45_r = np.array(p1c2[" AU45_r"])


# In[80]:


p2c2frame = np.array(p2c2["frame"])
p2c2conf = np.array(p2c2[" confidence"])
p2c2timestamp = np.array(p2c2[" timestamp"])
p2c2AU01_r = np.array(p2c2[" AU01_r"])
p2c2AU02_r = np.array(p2c2[" AU02_r"])
p2c2AU04_r = np.array(p2c2[" AU04_r"])
p2c2AU05_r = np.array(p2c2[" AU05_r"])
p2c2AU06_r = np.array(p2c2[" AU06_r"])
p2c2AU07_r = np.array(p2c2[" AU07_r"])
p2c2AU09_r = np.array(p2c2[" AU09_r"])
p2c2AU10_r = np.array(p2c2[" AU10_r"])
p2c2AU12_r = np.array(p2c2[" AU12_r"])
p2c2AU14_r = np.array(p2c2[" AU14_r"])
p2c2AU15_r = np.array(p2c2[" AU15_r"])
p2c2AU17_r = np.array(p2c2[" AU17_r"])
p2c2AU20_r = np.array(p2c2[" AU20_r"])
p2c2AU23_r = np.array(p2c2[" AU23_r"])
p2c2AU25_r = np.array(p2c2[" AU25_r"])
p2c2AU26_r = np.array(p2c2[" AU26_r"])
p2c2AU45_r = np.array(p2c2[" AU45_r"])


# In[81]:


p3c2frame = np.array(p3c2["frame"])
p3c2conf = np.array(p3c2[" confidence"])
p3c2timestamp = np.array(p3c2[" timestamp"])
p3c2AU01_r = np.array(p3c2[" AU01_r"])
p3c2AU02_r = np.array(p3c2[" AU02_r"])
p3c2AU04_r = np.array(p3c2[" AU04_r"])
p3c2AU05_r = np.array(p3c2[" AU05_r"])
p3c2AU06_r = np.array(p3c2[" AU06_r"])
p3c2AU07_r = np.array(p3c2[" AU07_r"])
p3c2AU09_r = np.array(p3c2[" AU09_r"])
p3c2AU10_r = np.array(p3c2[" AU10_r"])
p3c2AU12_r = np.array(p3c2[" AU12_r"])
p3c2AU14_r = np.array(p3c2[" AU14_r"])
p3c2AU15_r = np.array(p3c2[" AU15_r"])
p3c2AU17_r = np.array(p3c2[" AU17_r"])
p3c2AU20_r = np.array(p3c2[" AU20_r"])
p3c2AU23_r = np.array(p3c2[" AU23_r"])
p3c2AU25_r = np.array(p3c2[" AU25_r"])
p3c2AU26_r = np.array(p3c2[" AU26_r"])
p3c2AU45_r = np.array(p3c2[" AU45_r"])


# In[82]:


p4c2frame = np.array(p4c2["frame"])
p4c2conf = np.array(p4c2[" confidence"])
p4c2timestamp = np.array(p4c2[" timestamp"])
p4c2AU01_r = np.array(p4c2[" AU01_r"])
p4c2AU02_r = np.array(p4c2[" AU02_r"])
p4c2AU04_r = np.array(p4c2[" AU04_r"])
p4c2AU05_r = np.array(p4c2[" AU05_r"])
p4c2AU06_r = np.array(p4c2[" AU06_r"])
p4c2AU07_r = np.array(p4c2[" AU07_r"])
p4c2AU09_r = np.array(p4c2[" AU09_r"])
p4c2AU10_r = np.array(p4c2[" AU10_r"])
p4c2AU12_r = np.array(p4c2[" AU12_r"])
p4c2AU14_r = np.array(p4c2[" AU14_r"])
p4c2AU15_r = np.array(p4c2[" AU15_r"])
p4c2AU17_r = np.array(p4c2[" AU17_r"])
p4c2AU20_r = np.array(p4c2[" AU20_r"])
p4c2AU23_r = np.array(p4c2[" AU23_r"])
p4c2AU25_r = np.array(p4c2[" AU25_r"])
p4c2AU26_r = np.array(p4c2[" AU26_r"])
p4c2AU45_r = np.array(p4c2[" AU45_r"])


# In[83]:


p5c2frame = np.array(p5c2["frame"])
p5c2conf = np.array(p5c2[" confidence"])
p5c2timestamp = np.array(p5c2[" timestamp"])
p5c2AU01_r = np.array(p5c2[" AU01_r"])
p5c2AU02_r = np.array(p5c2[" AU02_r"])
p5c2AU04_r = np.array(p5c2[" AU04_r"])
p5c2AU05_r = np.array(p5c2[" AU05_r"])
p5c2AU06_r = np.array(p5c2[" AU06_r"])
p5c2AU07_r = np.array(p5c2[" AU07_r"])
p5c2AU09_r = np.array(p5c2[" AU09_r"])
p5c2AU10_r = np.array(p5c2[" AU10_r"])
p5c2AU12_r = np.array(p5c2[" AU12_r"])
p5c2AU14_r = np.array(p5c2[" AU14_r"])
p5c2AU15_r = np.array(p5c2[" AU15_r"])
p5c2AU17_r = np.array(p5c2[" AU17_r"])
p5c2AU20_r = np.array(p5c2[" AU20_r"])
p5c2AU23_r = np.array(p5c2[" AU23_r"])
p5c2AU25_r = np.array(p5c2[" AU25_r"])
p5c2AU26_r = np.array(p5c2[" AU26_r"])
p5c2AU45_r = np.array(p5c2[" AU45_r"])


# In[84]:


p6c2frame = np.array(p6c2["frame"])
p6c2conf = np.array(p6c2[" confidence"])
p6c2timestamp = np.array(p6c2[" timestamp"])
p6c2AU01_r = np.array(p6c2[" AU01_r"])
p6c2AU02_r = np.array(p6c2[" AU02_r"])
p6c2AU04_r = np.array(p6c2[" AU04_r"])
p6c2AU05_r = np.array(p6c2[" AU05_r"])
p6c2AU06_r = np.array(p6c2[" AU06_r"])
p6c2AU07_r = np.array(p6c2[" AU07_r"])
p6c2AU09_r = np.array(p6c2[" AU09_r"])
p6c2AU10_r = np.array(p6c2[" AU10_r"])
p6c2AU12_r = np.array(p6c2[" AU12_r"])
p6c2AU14_r = np.array(p6c2[" AU14_r"])
p6c2AU15_r = np.array(p6c2[" AU15_r"])
p6c2AU17_r = np.array(p6c2[" AU17_r"])
p6c2AU20_r = np.array(p6c2[" AU20_r"])
p6c2AU23_r = np.array(p6c2[" AU23_r"])
p6c2AU25_r = np.array(p6c2[" AU25_r"])
p6c2AU26_r = np.array(p6c2[" AU26_r"])
p6c2AU45_r = np.array(p6c2[" AU45_r"])


# In[85]:


p7c2frame = np.array(p7c2["frame"])
p7c2conf = np.array(p7c2[" confidence"])
p7c2timestamp = np.array(p7c2[" timestamp"])
p7c2AU01_r = np.array(p7c2[" AU01_r"])
p7c2AU02_r = np.array(p7c2[" AU02_r"])
p7c2AU04_r = np.array(p7c2[" AU04_r"])
p7c2AU05_r = np.array(p7c2[" AU05_r"])
p7c2AU06_r = np.array(p7c2[" AU06_r"])
p7c2AU07_r = np.array(p7c2[" AU07_r"])
p7c2AU09_r = np.array(p7c2[" AU09_r"])
p7c2AU10_r = np.array(p7c2[" AU10_r"])
p7c2AU12_r = np.array(p7c2[" AU12_r"])
p7c2AU14_r = np.array(p7c2[" AU14_r"])
p7c2AU15_r = np.array(p7c2[" AU15_r"])
p7c2AU17_r = np.array(p7c2[" AU17_r"])
p7c2AU20_r = np.array(p7c2[" AU20_r"])
p7c2AU23_r = np.array(p7c2[" AU23_r"])
p7c2AU25_r = np.array(p7c2[" AU25_r"])
p7c2AU26_r = np.array(p7c2[" AU26_r"])
p7c2AU45_r = np.array(p7c2[" AU45_r"])


# In[86]:


p8c2frame = np.array(p8c2["frame"])
p8c2conf = np.array(p8c2[" confidence"])
p8c2timestamp = np.array(p8c2[" timestamp"])
p8c2AU01_r = np.array(p8c2[" AU01_r"])
p8c2AU02_r = np.array(p8c2[" AU02_r"])
p8c2AU04_r = np.array(p8c2[" AU04_r"])
p8c2AU05_r = np.array(p8c2[" AU05_r"])
p8c2AU06_r = np.array(p8c2[" AU06_r"])
p8c2AU07_r = np.array(p8c2[" AU07_r"])
p8c2AU09_r = np.array(p8c2[" AU09_r"])
p8c2AU10_r = np.array(p8c2[" AU10_r"])
p8c2AU12_r = np.array(p8c2[" AU12_r"])
p8c2AU14_r = np.array(p8c2[" AU14_r"])
p8c2AU15_r = np.array(p8c2[" AU15_r"])
p8c2AU17_r = np.array(p8c2[" AU17_r"])
p8c2AU20_r = np.array(p8c2[" AU20_r"])
p8c2AU23_r = np.array(p8c2[" AU23_r"])
p8c2AU25_r = np.array(p8c2[" AU25_r"])
p8c2AU26_r = np.array(p8c2[" AU26_r"])
p8c2AU45_r = np.array(p8c2[" AU45_r"])


# In[87]:


p9c2frame = np.array(p9c2["frame"])
p9c2conf = np.array(p9c2[" confidence"])
p9c2timestamp = np.array(p9c2[" timestamp"])
p9c2AU01_r = np.array(p9c2[" AU01_r"])
p9c2AU02_r = np.array(p9c2[" AU02_r"])
p9c2AU04_r = np.array(p9c2[" AU04_r"])
p9c2AU05_r = np.array(p9c2[" AU05_r"])
p9c2AU06_r = np.array(p9c2[" AU06_r"])
p9c2AU07_r = np.array(p9c2[" AU07_r"])
p9c2AU09_r = np.array(p9c2[" AU09_r"])
p9c2AU10_r = np.array(p9c2[" AU10_r"])
p9c2AU12_r = np.array(p9c2[" AU12_r"])
p9c2AU14_r = np.array(p9c2[" AU14_r"])
p9c2AU15_r = np.array(p9c2[" AU15_r"])
p9c2AU17_r = np.array(p9c2[" AU17_r"])
p9c2AU20_r = np.array(p9c2[" AU20_r"])
p9c2AU23_r = np.array(p9c2[" AU23_r"])
p9c2AU25_r = np.array(p9c2[" AU25_r"])
p9c2AU26_r = np.array(p9c2[" AU26_r"])
p9c2AU45_r = np.array(p9c2[" AU45_r"])


# In[88]:


p10c2frame = np.array(p10c2["frame"])
p10c2conf = np.array(p10c2[" confidence"])
p10c2timestamp = np.array(p10c2[" timestamp"])
p10c2AU01_r = np.array(p10c2[" AU01_r"])
p10c2AU02_r = np.array(p10c2[" AU02_r"])
p10c2AU04_r = np.array(p10c2[" AU04_r"])
p10c2AU05_r = np.array(p10c2[" AU05_r"])
p10c2AU06_r = np.array(p10c2[" AU06_r"])
p10c2AU07_r = np.array(p10c2[" AU07_r"])
p10c2AU09_r = np.array(p10c2[" AU09_r"])
p10c2AU10_r = np.array(p10c2[" AU10_r"])
p10c2AU12_r = np.array(p10c2[" AU12_r"])
p10c2AU14_r = np.array(p10c2[" AU14_r"])
p10c2AU15_r = np.array(p10c2[" AU15_r"])
p10c2AU17_r = np.array(p10c2[" AU17_r"])
p10c2AU20_r = np.array(p10c2[" AU20_r"])
p10c2AU23_r = np.array(p10c2[" AU23_r"])
p10c2AU25_r = np.array(p10c2[" AU25_r"])
p10c2AU26_r = np.array(p10c2[" AU26_r"])
p10c2AU45_r = np.array(p10c2[" AU45_r"])


# In[89]:


p11c2frame = np.array(p11c2["frame"])
p11c2conf = np.array(p11c2[" confidence"])
p11c2timestamp = np.array(p11c2[" timestamp"])
p11c2AU01_r = np.array(p11c2[" AU01_r"])
p11c2AU02_r = np.array(p11c2[" AU02_r"])
p11c2AU04_r = np.array(p11c2[" AU04_r"])
p11c2AU05_r = np.array(p11c2[" AU05_r"])
p11c2AU06_r = np.array(p11c2[" AU06_r"])
p11c2AU07_r = np.array(p11c2[" AU07_r"])
p11c2AU09_r = np.array(p11c2[" AU09_r"])
p11c2AU10_r = np.array(p11c2[" AU10_r"])
p11c2AU12_r = np.array(p11c2[" AU12_r"])
p11c2AU14_r = np.array(p11c2[" AU14_r"])
p11c2AU15_r = np.array(p11c2[" AU15_r"])
p11c2AU17_r = np.array(p11c2[" AU17_r"])
p11c2AU20_r = np.array(p11c2[" AU20_r"])
p11c2AU23_r = np.array(p11c2[" AU23_r"])
p11c2AU25_r = np.array(p11c2[" AU25_r"])
p11c2AU26_r = np.array(p11c2[" AU26_r"])
p11c2AU45_r = np.array(p11c2[" AU45_r"])


# In[90]:


p12c2frame = np.array(p12c2["frame"])
p12c2conf = np.array(p12c2[" confidence"])
p12c2timestamp = np.array(p12c2[" timestamp"])
p12c2AU01_r = np.array(p12c2[" AU01_r"])
p12c2AU02_r = np.array(p12c2[" AU02_r"])
p12c2AU04_r = np.array(p12c2[" AU04_r"])
p12c2AU05_r = np.array(p12c2[" AU05_r"])
p12c2AU06_r = np.array(p12c2[" AU06_r"])
p12c2AU07_r = np.array(p12c2[" AU07_r"])
p12c2AU09_r = np.array(p12c2[" AU09_r"])
p12c2AU10_r = np.array(p12c2[" AU10_r"])
p12c2AU12_r = np.array(p12c2[" AU12_r"])
p12c2AU14_r = np.array(p12c2[" AU14_r"])
p12c2AU15_r = np.array(p12c2[" AU15_r"])
p12c2AU17_r = np.array(p12c2[" AU17_r"])
p12c2AU20_r = np.array(p12c2[" AU20_r"])
p12c2AU23_r = np.array(p12c2[" AU23_r"])
p12c2AU25_r = np.array(p12c2[" AU25_r"])
p12c2AU26_r = np.array(p12c2[" AU26_r"])
p12c2AU45_r = np.array(p12c2[" AU45_r"])


# In[91]:


p13c2frame = np.array(p13c2["frame"])
p13c2conf = np.array(p13c2[" confidence"])
p13c2timestamp = np.array(p13c2[" timestamp"])
p13c2AU01_r = np.array(p13c2[" AU01_r"])
p13c2AU02_r = np.array(p13c2[" AU02_r"])
p13c2AU04_r = np.array(p13c2[" AU04_r"])
p13c2AU05_r = np.array(p13c2[" AU05_r"])
p13c2AU06_r = np.array(p13c2[" AU06_r"])
p13c2AU07_r = np.array(p13c2[" AU07_r"])
p13c2AU09_r = np.array(p13c2[" AU09_r"])
p13c2AU10_r = np.array(p13c2[" AU10_r"])
p13c2AU12_r = np.array(p13c2[" AU12_r"])
p13c2AU14_r = np.array(p13c2[" AU14_r"])
p13c2AU15_r = np.array(p13c2[" AU15_r"])
p13c2AU17_r = np.array(p13c2[" AU17_r"])
p13c2AU20_r = np.array(p13c2[" AU20_r"])
p13c2AU23_r = np.array(p13c2[" AU23_r"])
p13c2AU25_r = np.array(p13c2[" AU25_r"])
p13c2AU26_r = np.array(p13c2[" AU26_r"])
p13c2AU45_r = np.array(p13c2[" AU45_r"])


# In[92]:


p14c2frame = np.array(p14c2["frame"])
p14c2conf = np.array(p14c2[" confidence"])
p14c2timestamp = np.array(p14c2[" timestamp"])
p14c2AU01_r = np.array(p14c2[" AU01_r"])
p14c2AU02_r = np.array(p14c2[" AU02_r"])
p14c2AU04_r = np.array(p14c2[" AU04_r"])
p14c2AU05_r = np.array(p14c2[" AU05_r"])
p14c2AU06_r = np.array(p14c2[" AU06_r"])
p14c2AU07_r = np.array(p14c2[" AU07_r"])
p14c2AU09_r = np.array(p14c2[" AU09_r"])
p14c2AU10_r = np.array(p14c2[" AU10_r"])
p14c2AU12_r = np.array(p14c2[" AU12_r"])
p14c2AU14_r = np.array(p14c2[" AU14_r"])
p14c2AU15_r = np.array(p14c2[" AU15_r"])
p14c2AU17_r = np.array(p14c2[" AU17_r"])
p14c2AU20_r = np.array(p14c2[" AU20_r"])
p14c2AU23_r = np.array(p14c2[" AU23_r"])
p14c2AU25_r = np.array(p14c2[" AU25_r"])
p14c2AU26_r = np.array(p14c2[" AU26_r"])
p14c2AU45_r = np.array(p14c2[" AU45_r"])


# In[93]:


p15c2frame = np.array(p15c2["frame"])
p15c2conf = np.array(p15c2[" confidence"])
p15c2timestamp = np.array(p15c2[" timestamp"])
p15c2AU01_r = np.array(p15c2[" AU01_r"])
p15c2AU02_r = np.array(p15c2[" AU02_r"])
p15c2AU04_r = np.array(p15c2[" AU04_r"])
p15c2AU05_r = np.array(p15c2[" AU05_r"])
p15c2AU06_r = np.array(p15c2[" AU06_r"])
p15c2AU07_r = np.array(p15c2[" AU07_r"])
p15c2AU09_r = np.array(p15c2[" AU09_r"])
p15c2AU10_r = np.array(p15c2[" AU10_r"])
p15c2AU12_r = np.array(p15c2[" AU12_r"])
p15c2AU14_r = np.array(p15c2[" AU14_r"])
p15c2AU15_r = np.array(p15c2[" AU15_r"])
p15c2AU17_r = np.array(p15c2[" AU17_r"])
p15c2AU20_r = np.array(p15c2[" AU20_r"])
p15c2AU23_r = np.array(p15c2[" AU23_r"])
p15c2AU25_r = np.array(p15c2[" AU25_r"])
p15c2AU26_r = np.array(p15c2[" AU26_r"])
p15c2AU45_r = np.array(p15c2[" AU45_r"])


# In[94]:


p16c2frame = np.array(p16c2["frame"])
p16c2conf = np.array(p16c2[" confidence"])
p16c2timestamp = np.array(p16c2[" timestamp"])
p16c2AU01_r = np.array(p16c2[" AU01_r"])
p16c2AU02_r = np.array(p16c2[" AU02_r"])
p16c2AU04_r = np.array(p16c2[" AU04_r"])
p16c2AU05_r = np.array(p16c2[" AU05_r"])
p16c2AU06_r = np.array(p16c2[" AU06_r"])
p16c2AU07_r = np.array(p16c2[" AU07_r"])
p16c2AU09_r = np.array(p16c2[" AU09_r"])
p16c2AU10_r = np.array(p16c2[" AU10_r"])
p16c2AU12_r = np.array(p16c2[" AU12_r"])
p16c2AU14_r = np.array(p16c2[" AU14_r"])
p16c2AU15_r = np.array(p16c2[" AU15_r"])
p16c2AU17_r = np.array(p16c2[" AU17_r"])
p16c2AU20_r = np.array(p16c2[" AU20_r"])
p16c2AU23_r = np.array(p16c2[" AU23_r"])
p16c2AU25_r = np.array(p16c2[" AU25_r"])
p16c2AU26_r = np.array(p16c2[" AU26_r"])
p16c2AU45_r = np.array(p16c2[" AU45_r"])


# In[95]:


p17c2frame = np.array(p17c2["frame"])
p17c2conf = np.array(p17c2[" confidence"])
p17c2timestamp = np.array(p17c2[" timestamp"])
p17c2AU01_r = np.array(p17c2[" AU01_r"])
p17c2AU02_r = np.array(p17c2[" AU02_r"])
p17c2AU04_r = np.array(p17c2[" AU04_r"])
p17c2AU05_r = np.array(p17c2[" AU05_r"])
p17c2AU06_r = np.array(p17c2[" AU06_r"])
p17c2AU07_r = np.array(p17c2[" AU07_r"])
p17c2AU09_r = np.array(p17c2[" AU09_r"])
p17c2AU10_r = np.array(p17c2[" AU10_r"])
p17c2AU12_r = np.array(p17c2[" AU12_r"])
p17c2AU14_r = np.array(p17c2[" AU14_r"])
p17c2AU15_r = np.array(p17c2[" AU15_r"])
p17c2AU17_r = np.array(p17c2[" AU17_r"])
p17c2AU20_r = np.array(p17c2[" AU20_r"])
p17c2AU23_r = np.array(p17c2[" AU23_r"])
p17c2AU25_r = np.array(p17c2[" AU25_r"])
p17c2AU26_r = np.array(p17c2[" AU26_r"])
p17c2AU45_r = np.array(p17c2[" AU45_r"])


# In[96]:


p18c2frame = np.array(p18c2["frame"])
p18c2conf = np.array(p18c2[" confidence"])
p18c2timestamp = np.array(p18c2[" timestamp"])
p18c2AU01_r = np.array(p18c2[" AU01_r"])
p18c2AU02_r = np.array(p18c2[" AU02_r"])
p18c2AU04_r = np.array(p18c2[" AU04_r"])
p18c2AU05_r = np.array(p18c2[" AU05_r"])
p18c2AU06_r = np.array(p18c2[" AU06_r"])
p18c2AU07_r = np.array(p18c2[" AU07_r"])
p18c2AU09_r = np.array(p18c2[" AU09_r"])
p18c2AU10_r = np.array(p18c2[" AU10_r"])
p18c2AU12_r = np.array(p18c2[" AU12_r"])
p18c2AU14_r = np.array(p18c2[" AU14_r"])
p18c2AU15_r = np.array(p18c2[" AU15_r"])
p18c2AU17_r = np.array(p18c2[" AU17_r"])
p18c2AU20_r = np.array(p18c2[" AU20_r"])
p18c2AU23_r = np.array(p18c2[" AU23_r"])
p18c2AU25_r = np.array(p18c2[" AU25_r"])
p18c2AU26_r = np.array(p18c2[" AU26_r"])
p18c2AU45_r = np.array(p18c2[" AU45_r"])


# In[97]:


p19c2frame = np.array(p19c2["frame"])
p19c2conf = np.array(p19c2[" confidence"])
p19c2timestamp = np.array(p19c2[" timestamp"])
p19c2AU01_r = np.array(p19c2[" AU01_r"])
p19c2AU02_r = np.array(p19c2[" AU02_r"])
p19c2AU04_r = np.array(p19c2[" AU04_r"])
p19c2AU05_r = np.array(p19c2[" AU05_r"])
p19c2AU06_r = np.array(p19c2[" AU06_r"])
p19c2AU07_r = np.array(p19c2[" AU07_r"])
p19c2AU09_r = np.array(p19c2[" AU09_r"])
p19c2AU10_r = np.array(p19c2[" AU10_r"])
p19c2AU12_r = np.array(p19c2[" AU12_r"])
p19c2AU14_r = np.array(p19c2[" AU14_r"])
p19c2AU15_r = np.array(p19c2[" AU15_r"])
p19c2AU17_r = np.array(p19c2[" AU17_r"])
p19c2AU20_r = np.array(p19c2[" AU20_r"])
p19c2AU23_r = np.array(p19c2[" AU23_r"])
p19c2AU25_r = np.array(p19c2[" AU25_r"])
p19c2AU26_r = np.array(p19c2[" AU26_r"])
p19c2AU45_r = np.array(p19c2[" AU45_r"])


# In[98]:


p20c2frame = np.array(p20c2["frame"])
p20c2conf = np.array(p20c2[" confidence"])
p20c2timestamp = np.array(p20c2[" timestamp"])
p20c2AU01_r = np.array(p20c2[" AU01_r"])
p20c2AU02_r = np.array(p20c2[" AU02_r"])
p20c2AU04_r = np.array(p20c2[" AU04_r"])
p20c2AU05_r = np.array(p20c2[" AU05_r"])
p20c2AU06_r = np.array(p20c2[" AU06_r"])
p20c2AU07_r = np.array(p20c2[" AU07_r"])
p20c2AU09_r = np.array(p20c2[" AU09_r"])
p20c2AU10_r = np.array(p20c2[" AU10_r"])
p20c2AU12_r = np.array(p20c2[" AU12_r"])
p20c2AU14_r = np.array(p20c2[" AU14_r"])
p20c2AU15_r = np.array(p20c2[" AU15_r"])
p20c2AU17_r = np.array(p20c2[" AU17_r"])
p20c2AU20_r = np.array(p20c2[" AU20_r"])
p20c2AU23_r = np.array(p20c2[" AU23_r"])
p20c2AU25_r = np.array(p20c2[" AU25_r"])
p20c2AU26_r = np.array(p20c2[" AU26_r"])
p20c2AU45_r = np.array(p20c2[" AU45_r"])


# In[99]:


p21c2frame = np.array(p21c2["frame"])
p21c2conf = np.array(p21c2[" confidence"])
p21c2timestamp = np.array(p21c2[" timestamp"])
p21c2AU01_r = np.array(p21c2[" AU01_r"])
p21c2AU02_r = np.array(p21c2[" AU02_r"])
p21c2AU04_r = np.array(p21c2[" AU04_r"])
p21c2AU05_r = np.array(p21c2[" AU05_r"])
p21c2AU06_r = np.array(p21c2[" AU06_r"])
p21c2AU07_r = np.array(p21c2[" AU07_r"])
p21c2AU09_r = np.array(p21c2[" AU09_r"])
p21c2AU10_r = np.array(p21c2[" AU10_r"])
p21c2AU12_r = np.array(p21c2[" AU12_r"])
p21c2AU14_r = np.array(p21c2[" AU14_r"])
p21c2AU15_r = np.array(p21c2[" AU15_r"])
p21c2AU17_r = np.array(p21c2[" AU17_r"])
p21c2AU20_r = np.array(p21c2[" AU20_r"])
p21c2AU23_r = np.array(p21c2[" AU23_r"])
p21c2AU25_r = np.array(p21c2[" AU25_r"])
p21c2AU26_r = np.array(p21c2[" AU26_r"])
p21c2AU45_r = np.array(p21c2[" AU45_r"])


# In[100]:


p22c2frame = np.array(p22c2["frame"])
p22c2conf = np.array(p22c2[" confidence"])
p22c2timestamp = np.array(p22c2[" timestamp"])
p22c2AU01_r = np.array(p22c2[" AU01_r"])
p22c2AU02_r = np.array(p22c2[" AU02_r"])
p22c2AU04_r = np.array(p22c2[" AU04_r"])
p22c2AU05_r = np.array(p22c2[" AU05_r"])
p22c2AU06_r = np.array(p22c2[" AU06_r"])
p22c2AU07_r = np.array(p22c2[" AU07_r"])
p22c2AU09_r = np.array(p22c2[" AU09_r"])
p22c2AU10_r = np.array(p22c2[" AU10_r"])
p22c2AU12_r = np.array(p22c2[" AU12_r"])
p22c2AU14_r = np.array(p22c2[" AU14_r"])
p22c2AU15_r = np.array(p22c2[" AU15_r"])
p22c2AU17_r = np.array(p22c2[" AU17_r"])
p22c2AU20_r = np.array(p22c2[" AU20_r"])
p22c2AU23_r = np.array(p22c2[" AU23_r"])
p22c2AU25_r = np.array(p22c2[" AU25_r"])
p22c2AU26_r = np.array(p22c2[" AU26_r"])
p22c2AU45_r = np.array(p22c2[" AU45_r"])


# In[101]:


p23c2frame = np.array(p23c2["frame"])
p23c2conf = np.array(p23c2[" confidence"])
p23c2timestamp = np.array(p23c2[" timestamp"])
p23c2AU01_r = np.array(p23c2[" AU01_r"])
p23c2AU02_r = np.array(p23c2[" AU02_r"])
p23c2AU04_r = np.array(p23c2[" AU04_r"])
p23c2AU05_r = np.array(p23c2[" AU05_r"])
p23c2AU06_r = np.array(p23c2[" AU06_r"])
p23c2AU07_r = np.array(p23c2[" AU07_r"])
p23c2AU09_r = np.array(p23c2[" AU09_r"])
p23c2AU10_r = np.array(p23c2[" AU10_r"])
p23c2AU12_r = np.array(p23c2[" AU12_r"])
p23c2AU14_r = np.array(p23c2[" AU14_r"])
p23c2AU15_r = np.array(p23c2[" AU15_r"])
p23c2AU17_r = np.array(p23c2[" AU17_r"])
p23c2AU20_r = np.array(p23c2[" AU20_r"])
p23c2AU23_r = np.array(p23c2[" AU23_r"])
p23c2AU25_r = np.array(p23c2[" AU25_r"])
p23c2AU26_r = np.array(p23c2[" AU26_r"])
p23c2AU45_r = np.array(p23c2[" AU45_r"])


# In[102]:


p24c2frame = np.array(p24c2["frame"])
p24c2conf = np.array(p24c2[" confidence"])
p24c2timestamp = np.array(p24c2[" timestamp"])
p24c2AU01_r = np.array(p24c2[" AU01_r"])
p24c2AU02_r = np.array(p24c2[" AU02_r"])
p24c2AU04_r = np.array(p24c2[" AU04_r"])
p24c2AU05_r = np.array(p24c2[" AU05_r"])
p24c2AU06_r = np.array(p24c2[" AU06_r"])
p24c2AU07_r = np.array(p24c2[" AU07_r"])
p24c2AU09_r = np.array(p24c2[" AU09_r"])
p24c2AU10_r = np.array(p24c2[" AU10_r"])
p24c2AU12_r = np.array(p24c2[" AU12_r"])
p24c2AU14_r = np.array(p24c2[" AU14_r"])
p24c2AU15_r = np.array(p24c2[" AU15_r"])
p24c2AU17_r = np.array(p24c2[" AU17_r"])
p24c2AU20_r = np.array(p24c2[" AU20_r"])
p24c2AU23_r = np.array(p24c2[" AU23_r"])
p24c2AU25_r = np.array(p24c2[" AU25_r"])
p24c2AU26_r = np.array(p24c2[" AU26_r"])
p24c2AU45_r = np.array(p24c2[" AU45_r"])


# In[103]:


p25c2frame = np.array(p25c2["frame"])
p25c2conf = np.array(p25c2[" confidence"])
p25c2timestamp = np.array(p25c2[" timestamp"])
p25c2AU01_r = np.array(p25c2[" AU01_r"])
p25c2AU02_r = np.array(p25c2[" AU02_r"])
p25c2AU04_r = np.array(p25c2[" AU04_r"])
p25c2AU05_r = np.array(p25c2[" AU05_r"])
p25c2AU06_r = np.array(p25c2[" AU06_r"])
p25c2AU07_r = np.array(p25c2[" AU07_r"])
p25c2AU09_r = np.array(p25c2[" AU09_r"])
p25c2AU10_r = np.array(p25c2[" AU10_r"])
p25c2AU12_r = np.array(p25c2[" AU12_r"])
p25c2AU14_r = np.array(p25c2[" AU14_r"])
p25c2AU15_r = np.array(p25c2[" AU15_r"])
p25c2AU17_r = np.array(p25c2[" AU17_r"])
p25c2AU20_r = np.array(p25c2[" AU20_r"])
p25c2AU23_r = np.array(p25c2[" AU23_r"])
p25c2AU25_r = np.array(p25c2[" AU25_r"])
p25c2AU26_r = np.array(p25c2[" AU26_r"])
p25c2AU45_r = np.array(p25c2[" AU45_r"])


# Creating a nested array per variable

# In[104]:


frame = np.array((p1c2frame,p2c2frame,p3c2frame,p4c2frame,p5c2frame,p6c2frame,p7c2frame,p8c2frame,
         p9c2frame,p10c2frame,p11c2frame,p12c2frame,p13c2frame,p14c2frame,p15c2frame,
         p16c2frame,p17c2frame,p18c2frame,p19c2frame,p20c2frame,p21c2frame,p22c2frame,
         p23c2frame,p24c2frame,p25c2frame))


# In[105]:


conf = np.array((p1c2conf,p2c2conf,p3c2conf,p4c2conf,p5c2conf,p6c2conf,p7c2conf,p8c2conf,
                p9c2conf,p10c2conf,p11c2conf,p12c2conf,p13c2conf,p14c2conf,p15c2conf,p16c2conf,
                p17c2conf,p18c2conf,p19c2conf,p20c2conf,p21c2conf,p22c2conf,p23c2conf,p24c2conf,
                p25c2conf))


# In[106]:


timestamp = np.array((p1c2timestamp,p2c2timestamp,p3c2timestamp,p4c2timestamp,p5c2timestamp,
                      p6c2timestamp,p7c2timestamp,p8c2timestamp,p9c2timestamp,p10c2timestamp,
                      p11c2timestamp,p12c2timestamp,p13c2timestamp,p14c2timestamp,p15c2timestamp,
                      p16c2timestamp,p17c2timestamp,p18c2timestamp,p19c2timestamp,p20c2timestamp,
                      p21c2timestamp,p22c2timestamp,p23c2timestamp,p24c2timestamp,p25c2timestamp))


# In[107]:


AU01_r = np.array((p1c2AU01_r,p2c2AU01_r,p3c2AU01_r,p4c2AU01_r,p5c2AU01_r,p6c2AU01_r,p7c2AU01_r,
                   p8c2AU01_r,p9c2AU01_r,p10c2AU01_r,p11c2AU01_r,p12c2AU01_r,p13c2AU01_r,
                   p14c2AU01_r,p15c2AU01_r,p16c2AU01_r,p17c2AU01_r,p18c2AU01_r,p19c2AU01_r,
                   p20c2AU01_r,p21c2AU01_r,p22c2AU01_r,p23c2AU01_r,p24c2AU01_r,p25c2AU01_r))


# In[108]:


AU02_r = np.array((p1c2AU02_r,p2c2AU02_r,p3c2AU02_r,p4c2AU02_r,p5c2AU02_r,p6c2AU02_r,p7c2AU02_r,
                   p8c2AU02_r,p9c2AU02_r,p10c2AU02_r,p11c2AU02_r,p12c2AU02_r,p13c2AU02_r,
                   p14c2AU02_r,p15c2AU02_r,p16c2AU02_r,p17c2AU02_r,p18c2AU02_r,p19c2AU02_r,
                   p20c2AU02_r,p21c2AU02_r,p22c2AU02_r,p23c2AU02_r,p24c2AU02_r,p25c2AU02_r))


# In[109]:


AU04_r = np.array((p1c2AU04_r,p2c2AU04_r,p3c2AU04_r,p4c2AU04_r,p5c2AU04_r,p6c2AU04_r,p7c2AU04_r,
                   p8c2AU04_r,p9c2AU04_r,p10c2AU04_r,p11c2AU04_r,p12c2AU04_r,p13c2AU04_r,
                   p14c2AU04_r,p15c2AU04_r,p16c2AU04_r,p17c2AU04_r,p18c2AU04_r,p19c2AU04_r,
                   p20c2AU04_r,p21c2AU04_r,p22c2AU04_r,p23c2AU04_r,p24c2AU04_r,p25c2AU04_r))


# In[110]:


AU05_r = np.array((p1c2AU05_r,p2c2AU05_r,p3c2AU05_r,p4c2AU05_r,p5c2AU05_r,p6c2AU05_r,p7c2AU05_r,
                   p8c2AU05_r,p9c2AU05_r,p10c2AU05_r,p11c2AU05_r,p12c2AU05_r,p13c2AU05_r,
                   p14c2AU05_r,p15c2AU05_r,p16c2AU05_r,p17c2AU05_r,p18c2AU05_r,p19c2AU05_r,
                   p20c2AU05_r,p21c2AU05_r,p22c2AU05_r,p23c2AU05_r,p24c2AU05_r,p25c2AU05_r))


# In[111]:


AU06_r = np.array((p1c2AU06_r,p2c2AU06_r,p3c2AU06_r,p4c2AU06_r,p5c2AU06_r,p6c2AU06_r,p7c2AU06_r,
                   p8c2AU06_r,p9c2AU06_r,p10c2AU06_r,p11c2AU06_r,p12c2AU06_r,p13c2AU06_r,
                   p14c2AU06_r,p15c2AU06_r,p16c2AU06_r,p17c2AU06_r,p18c2AU06_r,p19c2AU06_r,
                   p20c2AU06_r,p21c2AU06_r,p22c2AU06_r,p23c2AU06_r,p24c2AU06_r,p25c2AU06_r))


# In[112]:


AU07_r = np.array((p1c2AU07_r,p2c2AU07_r,p3c2AU07_r,p4c2AU07_r,p5c2AU07_r,p6c2AU07_r,p7c2AU07_r,
                   p8c2AU07_r,p9c2AU07_r,p10c2AU07_r,p11c2AU07_r,p12c2AU07_r,p13c2AU07_r,
                   p14c2AU07_r,p15c2AU07_r,p16c2AU07_r,p17c2AU07_r,p18c2AU07_r,p19c2AU07_r,
                   p20c2AU07_r,p21c2AU07_r,p22c2AU07_r,p23c2AU07_r,p24c2AU07_r,p25c2AU07_r))


# In[113]:


AU09_r = np.array((p1c2AU09_r,p2c2AU09_r,p3c2AU09_r,p4c2AU09_r,p5c2AU09_r,p6c2AU09_r,p7c2AU09_r,
                   p8c2AU09_r,p9c2AU09_r,p10c2AU09_r,p11c2AU09_r,p12c2AU09_r,p13c2AU09_r,
                   p14c2AU09_r,p15c2AU09_r,p16c2AU09_r,p17c2AU09_r,p18c2AU09_r,p19c2AU09_r,
                   p20c2AU09_r,p21c2AU09_r,p22c2AU09_r,p23c2AU09_r,p24c2AU09_r,p25c2AU09_r))


# In[114]:


AU10_r = np.array((p1c2AU10_r,p2c2AU10_r,p3c2AU10_r,p4c2AU10_r,p5c2AU10_r,p6c2AU10_r,p7c2AU10_r,
                   p8c2AU10_r,p9c2AU10_r,p10c2AU10_r,p11c2AU10_r,p12c2AU10_r,p13c2AU10_r,
                   p14c2AU10_r,p15c2AU10_r,p16c2AU10_r,p17c2AU10_r,p18c2AU10_r,p19c2AU10_r,
                   p20c2AU10_r,p21c2AU10_r,p22c2AU10_r,p23c2AU10_r,p24c2AU10_r,p25c2AU10_r))


# In[115]:


AU12_r = np.array((p1c2AU12_r,p2c2AU12_r,p3c2AU12_r,p4c2AU12_r,p5c2AU12_r,p6c2AU12_r,p7c2AU12_r,
                   p8c2AU12_r,p9c2AU12_r,p10c2AU12_r,p11c2AU12_r,p12c2AU12_r,p13c2AU12_r,
                   p14c2AU12_r,p15c2AU12_r,p16c2AU12_r,p17c2AU12_r,p18c2AU12_r,p19c2AU12_r,
                   p20c2AU12_r,p21c2AU12_r,p22c2AU12_r,p23c2AU12_r,p24c2AU12_r,p25c2AU12_r))


# In[116]:


AU14_r = np.array((p1c2AU14_r,p2c2AU14_r,p3c2AU14_r,p4c2AU14_r,p5c2AU14_r,p6c2AU14_r,p7c2AU14_r,
                   p8c2AU14_r,p9c2AU14_r,p10c2AU14_r,p11c2AU14_r,p12c2AU14_r,p13c2AU14_r,
                   p14c2AU14_r,p15c2AU14_r,p16c2AU14_r,p17c2AU14_r,p18c2AU14_r,p19c2AU14_r,
                   p20c2AU14_r,p21c2AU14_r,p22c2AU14_r,p23c2AU14_r,p24c2AU14_r,p25c2AU14_r))


# In[117]:


AU15_r = np.array((p1c2AU15_r,p2c2AU15_r,p3c2AU15_r,p4c2AU15_r,p5c2AU15_r,p6c2AU15_r,p7c2AU15_r,
                   p8c2AU15_r,p9c2AU15_r,p10c2AU15_r,p11c2AU15_r,p12c2AU15_r,p13c2AU15_r,
                   p14c2AU15_r,p15c2AU15_r,p16c2AU15_r,p17c2AU15_r,p18c2AU15_r,p19c2AU15_r,
                   p20c2AU15_r,p21c2AU15_r,p22c2AU15_r,p23c2AU15_r,p24c2AU15_r,p25c2AU15_r))


# In[118]:


AU17_r = np.array((p1c2AU17_r,p2c2AU17_r,p3c2AU17_r,p4c2AU17_r,p5c2AU17_r,p6c2AU17_r,p7c2AU17_r,
                   p8c2AU17_r,p9c2AU17_r,p10c2AU17_r,p11c2AU17_r,p12c2AU17_r,p13c2AU17_r,
                   p14c2AU17_r,p15c2AU17_r,p16c2AU17_r,p17c2AU17_r,p18c2AU17_r,p19c2AU17_r,
                   p20c2AU17_r,p21c2AU17_r,p22c2AU17_r,p23c2AU17_r,p24c2AU17_r,p25c2AU17_r))


# In[119]:


AU20_r = np.array((p1c2AU20_r,p2c2AU20_r,p3c2AU20_r,p4c2AU20_r,p5c2AU20_r,p6c2AU20_r,p7c2AU20_r,
                   p8c2AU20_r,p9c2AU20_r,p10c2AU20_r,p11c2AU20_r,p12c2AU20_r,p13c2AU20_r,
                   p14c2AU20_r,p15c2AU20_r,p16c2AU20_r,p17c2AU20_r,p18c2AU20_r,p19c2AU20_r,
                   p20c2AU20_r,p21c2AU20_r,p22c2AU20_r,p23c2AU20_r,p24c2AU20_r,p25c2AU20_r))


# In[120]:


AU23_r = np.array((p1c2AU23_r,p2c2AU23_r,p3c2AU23_r,p4c2AU23_r,p5c2AU23_r,p6c2AU23_r,p7c2AU23_r,
                   p8c2AU23_r,p9c2AU23_r,p10c2AU23_r,p11c2AU23_r,p12c2AU23_r,p13c2AU23_r,
                   p14c2AU23_r,p15c2AU23_r,p16c2AU23_r,p17c2AU23_r,p18c2AU23_r,p19c2AU23_r,
                   p20c2AU23_r,p21c2AU23_r,p22c2AU23_r,p23c2AU23_r,p24c2AU23_r,p25c2AU23_r))


# In[121]:


AU25_r = np.array((p1c2AU25_r,p2c2AU25_r,p3c2AU25_r,p4c2AU25_r,p5c2AU25_r,p6c2AU25_r,p7c2AU25_r,
                   p8c2AU25_r,p9c2AU25_r,p10c2AU25_r,p11c2AU25_r,p12c2AU25_r,p13c2AU25_r,
                   p14c2AU25_r,p15c2AU25_r,p16c2AU25_r,p17c2AU25_r,p18c2AU25_r,p19c2AU25_r,
                   p20c2AU25_r,p21c2AU25_r,p22c2AU25_r,p23c2AU25_r,p24c2AU25_r,p25c2AU25_r))


# In[122]:


AU26_r = np.array((p1c2AU26_r,p2c2AU26_r,p3c2AU26_r,p4c2AU26_r,p5c2AU26_r,p6c2AU26_r,p7c2AU26_r,
                   p8c2AU26_r,p9c2AU26_r,p10c2AU26_r,p11c2AU26_r,p12c2AU26_r,p13c2AU26_r,
                   p14c2AU26_r,p15c2AU26_r,p16c2AU26_r,p17c2AU26_r,p18c2AU26_r,p19c2AU26_r,
                   p20c2AU26_r,p21c2AU26_r,p22c2AU26_r,p23c2AU26_r,p24c2AU26_r,p25c2AU26_r))


# In[123]:


AU45_r = np.array((p1c2AU45_r,p2c2AU45_r,p3c2AU45_r,p4c2AU45_r,p5c2AU45_r,p6c2AU45_r,p7c2AU45_r,
                   p8c2AU45_r,p9c2AU45_r,p10c2AU45_r,p11c2AU45_r,p12c2AU45_r,p13c2AU45_r,
                   p14c2AU45_r,p15c2AU45_r,p16c2AU45_r,p17c2AU45_r,p18c2AU45_r,p19c2AU45_r,
                   p20c2AU45_r,p21c2AU45_r,p22c2AU45_r,p23c2AU45_r,p24c2AU45_r,p25c2AU45_r))


# Creating a dataframe with the variables

# In[124]:


data = pd.DataFrame()
data['AU01_r'] = AU01_r
data['AU02_r'] = AU02_r
data['AU04_r'] = AU04_r
data['AU05_r'] = AU05_r
data['AU06_r'] = AU06_r
data['AU07_r'] = AU07_r
data['AU09_r'] = AU09_r
data['AU10_r'] = AU10_r
data['AU12_r'] = AU12_r
data['AU14_r'] = AU14_r
data['AU15_r'] = AU15_r
data['AU17_r'] = AU17_r
data['AU20_r'] = AU20_r
data['AU23_r'] = AU23_r
data['AU25_r'] = AU25_r
data['AU26_r'] = AU26_r
data['AU45_r'] = AU45_r
data


# # Loading data

# Loading the rankings dataset

# In[125]:


rankings = pd.read_csv("Data/Created Datasets/Rankings.csv")
rankings


# # Preprocessing

# Converting the ranking classes to numbers

# In[126]:


from sklearn import preprocessing
le = preprocessing.LabelEncoder()
y_encoded = le.fit_transform(rankings['Classified Ranking'])
y_encoded


# 0 = high, 2 = middle, 1 = low

# Adding encoded rankings to dataset

# In[127]:


data["y"] = y_encoded
data


# Creating 3D array by combining the nested arrays of the variables into an array

# In[128]:


X = data.iloc[:, :-1].values
print(X.shape)
X = np.array(X)


# Zero padding

# In[129]:


longest = 0
for p in range(0,25):
    if len(X[p][0]) > longest:
        longest = len(X[p][0])
print(longest)


# In[130]:


X_padded = np.zeros((25,17,24946))
X_padded.shape


# In[131]:


for p, arrays in enumerate(X):
    for variable, array in enumerate(arrays):
        for time, num in enumerate (array):
            X_padded[p][variable][time] = num


# Reducing 3D array into 2D array

# In[132]:


X_padded_2d = X_padded.reshape(25, 17*24946)
X_padded_2d.shape


# Establishing majority baseline

# In[133]:


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


# In[134]:


10/(7+10+8)


# # Feature extraction: PCA

# In[135]:


import matplotlib.pyplot as plt


# In[136]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_padded_2d)


# By trial & error I found that 24 components explain all the variance in the data

# In[137]:


from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

pca = PCA(n_components=24)
X_pca = pca.fit_transform(X_padded_2d)
PCA_df = pd.DataFrame(data = X_pca, columns = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15', 'PC16', 'PC17', 'PC18', 'PC19', 'PC20', 'PC21', 'PC22', 'PC23', 'PC24'])
PCA_df = pd.concat([PCA_df, data['y']], axis = 1)
PCA_df['y'] = LabelEncoder().fit_transform(PCA_df['y'])
PCA_df


# In[138]:


expl_var = pca.explained_variance_ratio_
expl_var


# In[139]:


sum(pca.explained_variance_ratio_)


# There is no broken-stick point, probably due to the many components, so all the components keep adding a bit to the explained variance, but there is no point at which this added explained variance drastically decreases.

# In[140]:


plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance');


# Based on the eigenvalues I should keep all 24 components (all eigenvalues are higher than 1). However, this might result in overfitting.
# The article by Loquasto & Seborg (2003, June) suggests that the components should explain at least 85% percent of the variance. In this case, this would result in 17 components.

# In[141]:


cov_mat = np.cov(X_pca.T)

eig_vals, eig_vecs = np.linalg.eig(cov_mat)

print('\nEigenvalues \n%s' %eig_vals)


# In[142]:


sum(expl_var)-expl_var[23]-expl_var[22]-expl_var[21]-expl_var[20]-expl_var[19]-expl_var[18]-expl_var[17]


# In[143]:


pca = PCA(n_components=17)
X_pca = pca.fit_transform(X_padded_2d)
PCA_df = pd.DataFrame(data = X_pca, columns = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15', 'PC16', 'PC17'])
PCA_df = pd.concat([PCA_df, data['y']], axis = 1)
PCA_df['y'] = LabelEncoder().fit_transform(PCA_df['y'])
PCA_df


# In[144]:


loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15', 'PC16', 'PC17'])
loadings


# In[145]:


loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

loading_matrix = pd.DataFrame(loadings, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15', 'PC16', 'PC17'])
loading_matrix


# In[146]:


loadings = np.zeros((17,17))


# In[147]:


for i in range(0,17):
    for j in range(0,17):
        sum_AU_r = sum(loading_matrix.iloc[i*24946:i*24946+24946:, j:j+1].values)
        loadings[i,j] = sum_AU_r[0]/14151


# In[148]:


loadings_df = pd.DataFrame(loadings)
loadings_df


# In[149]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_padded_2d)

X = scaler.transform(X_padded_2d)


# In[150]:


from sklearn.decomposition import PCA
pca = PCA(n_components = 17)


# In[151]:


X = pca.fit_transform(X)


# ## K-Nearest Neighbors
# With cross-validation via gridsearch

# In[152]:


n_neighbors = list(range(1,20))
weights = ["uniform", "distance"]
param_grid = {"n_neighbors": n_neighbors, "weights": weights}


# In[153]:


from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn_search = GridSearchCV(knn, param_grid, cv = 5, scoring = 'accuracy')
knn_search.fit(X, y_encoded)
print("Best parameters: ", knn_search.best_params_)
print("Best accuracy score:", knn_search.best_score_)
cv_results = knn_search.cv_results_
print(cv_results)


# In[154]:


from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn_search = GridSearchCV(knn, param_grid, cv = 5, scoring = 'f1_macro')
knn_search.fit(X, y_encoded)
print("Best parameters: ", knn_search.best_params_)
print("Best macro f1 score:", knn_search.best_score_)
cv_results = knn_search.cv_results_
print(cv_results)


# ## Multinomial Logistic Regression

# With cross-validation via gridsearch

# In[155]:


from sklearn.linear_model import LogisticRegression


# Only 'newton-cg', 'sag', 'saga' and 'lbfgs' handle multinomial loss, and these only handle l2 or no penalty

# In[156]:


penalty = ['l2', 'none']
C = [0.001,0.01,0.1,1,10,100]
solver = ['newton-cg', 'sag', 'saga', 'lbfgs']
param_grid = {"penalty": penalty, "C": C, "solver": solver}


# In[157]:


lr = LogisticRegression(multi_class='multinomial')
lr_search = GridSearchCV(lr, param_grid, cv = 5, scoring = 'accuracy')
lr_search.fit(X, y_encoded)
print("Best parameters: ", lr_search.best_params_)
print("Best accuracy:", lr_search.best_score_)
cv_results = lr_search.cv_results_
print(cv_results)


# In[158]:


lr = LogisticRegression(multi_class='multinomial')
lr_search = GridSearchCV(lr, param_grid, cv = 5, scoring = 'f1_macro')
lr_search.fit(X, y_encoded)
print("Best parameters: ", lr_search.best_params_)
print("Best macro f1 score:", lr_search.best_score_)
cv_results = lr_search.cv_results_
print(cv_results)


# ## Support Vector Machine

# With cross-validation via gridsearch

# In[159]:


from sklearn import svm


# In[160]:


kernel = ["rbf", "linear", "sigmoid", "poly"]
gamma = ["scale", "auto"]
param_grid = {"kernel": kernel, "gamma" : gamma}


# In[161]:


svm = svm.SVC(decision_function_shape = "ovo")
svm_search = GridSearchCV(svm, param_grid, cv = 5, scoring = 'accuracy')
svm_search.fit(X, y_encoded)
print("Best parameters: ", svm_search.best_params_)
print("Best accuracy:", svm_search.best_score_)
cv_results = svm_search.cv_results_
print(cv_results)


# In[162]:


from sklearn import svm


# In[163]:


svm = svm.SVC(decision_function_shape = "ovo")
svm_search = GridSearchCV(svm, param_grid, cv = 5, scoring = 'f1_macro')
svm_search.fit(X, y_encoded)
print("Best parameters: ", svm_search.best_params_)
print("Best macro f1 score:", svm_search.best_score_)
cv_results = svm_search.cv_results_
print(cv_results)


# # Decision Tree

# With cross-validation via gridsearch

# In[164]:


from sklearn.tree import DecisionTreeClassifier


# In[165]:


criterion = ['gini', 'entropy']
max_depth = [4,6,8,12]
max_leaf_nodes = list(range(3,10))
min_samples_split = [2,3,4]
param_grid = {"criterion": criterion, "max_depth" : max_depth, "max_leaf_nodes": max_leaf_nodes, "min_samples_split": min_samples_split}    


# In[166]:


dt = DecisionTreeClassifier(random_state = 1234)
dt_search = GridSearchCV(dt, param_grid, cv = 5, scoring = 'accuracy')
dt_search.fit(X, y_encoded)
print("Best parameters: ", dt_search.best_params_)
print("Best accuracy:", dt_search.best_score_)
cv_results = dt_search.cv_results_
print(cv_results)


# In[167]:


dt = DecisionTreeClassifier(random_state = 1234)
dt_search = GridSearchCV(dt, param_grid, cv = 5, scoring = 'f1_macro')
dt_search.fit(X, y_encoded)
print("Best parameters: ", dt_search.best_params_)
print("Best accuracy:", dt_search.best_score_)
cv_results = dt_search.cv_results_
print(cv_results)


# ## Random Forest

# With cross-validation via gridsearch

# In[168]:


from sklearn.ensemble import RandomForestClassifier


# In[169]:


criterion = ['gini', 'entropy']
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
max_depth = [4,6,8,12]
max_leaf_nodes = list(range(3,10))
min_samples_split = [2,3,4]
param_grid = {"criterion": criterion, "n_estimators": n_estimators, "max_depth" : max_depth, "max_leaf_nodes": max_leaf_nodes, "min_samples_split": min_samples_split} 


# In[170]:


rf = RandomForestClassifier(random_state = 1234)
rf_search = GridSearchCV(rf, param_grid, cv = 5, scoring = 'accuracy')
rf_search.fit(X, y_encoded)
print("Best parameters: ", rf_search.best_params_)
print("Best accuracy:", rf_search.best_score_)
cv_results = rf_search.cv_results_
print(cv_results)


# In[171]:


rf = RandomForestClassifier(random_state = 1234)
rf_search = GridSearchCV(rf, param_grid, cv = 5, scoring = 'f1_macro')
rf_search.fit(X, y_encoded)
print("Best parameters: ", rf_search.best_params_)
print("Best macro f1 score:", rf_search.best_score_)
cv_results = rf_search.cv_results_
print(cv_results)

