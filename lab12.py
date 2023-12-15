import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
f = pd.read_csv('Iris.csv')
print(f)
print(f.loc[:,:'PetalWidthCm'])
print(f.loc[:,:'PetalWidthCm'].T.corr().loc[:10,:10])
dcorr=f.loc[:,:'PetalWidthCm'].T.corr()
sns.heatmap(dcorr.corr().loc[:10,:10], annot = True, cmap = "coolwarm")
