import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import *

def Hist(station1_PM25_Array,ylabel = "频数",xlabel = "",title = ""):
    plt.rcParams['font.sans-serif']=['Simhei']
    plt.rcParams['axes.unicode_minus']=False#显示负号\n",
    plt.figure(figsize=(6,4))## 设置画布\n",
    plt.hist(station1_PM25_Array,bins=50)
    plt.ylabel(ylabel)
    if(xlabel != ""):
        plt.xlabel(xlabel)
    if(title != ""):
        plt.title(title)
    plt.show()
def Norm(station1_PM25_Array,ylabel = "",xlabel = "",title = ""):
    plt.rcParams['font.sans-serif']=['Simhei']
    fig,axes=plt.subplots(figsize=(6,4))
    sns.distplot(station1_PM25_Array,kde = True, bins = 20,rug = True,fit=norm,ax=axes)

    mu =np.mean(station1_PM25_Array) #计算均值 
    sigma = np.std(station1_PM25_Array)
    sigma2 = np.std(station1_PM25_Array)*np.std(station1_PM25_Array) #计算方差
    print("均值："+str(round(mu,2))+"\n方差："+str(round(sigma,2))+"^2")

def HistLog(station1_PM25_Array,ylabel = "频数",xlabel = "",title = ""):
    station1_PM25_Array_log = np.log(station1_PM25_Array)
    Hist(station1_PM25_Array_log,ylabel,xlabel,title)
def NormLog(station1_PM25_Array,ylabel = "",xlabel = "",title = ""):
    plt.rcParams['font.sans-serif']=['Simhei']
    station1_PM25_Array_log = np.log(station1_PM25_Array)
    Norm(station1_PM25_Array_log,ylabel,xlabel,title)
