#tharani, #22btrad018, #ai&de

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

f = pd.read_csv('Iris.csv')

d_center=[f['SepalLengthCm'].mean(),f['SepalWidthCm'].mean()]
c_line=[[d_center[0]-1,d_center[0]+1],[d_center[1]+1,d_center[1]-1]]

sns.scatterplot(data=f,x='SepalLengthCm',y='SepalWidthCm',hue='Species')
sns.scatterplot(x=[d_center[0]],y=[d_center[1]],color='black')
sns.lineplot(x=c_line[0],y=c_line[1],color='black')
