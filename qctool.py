import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import *

# 直方图
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



# 柏拉图
def Pareto_analysis(data):
    plt.rcParams['font.sans-serif']=['Simhei']
    data.sort_values(ascending=False,inplace = True)
    p = data.cumsum()/data.sum()
    key = p[p>0.8].index[0]
    key_num = data.index.tolist().index(key)
    print('More than 80% of the node values are indexed as：',key)
    print('More than 80% of the node values index position is：',key_num)

    key_product = data.loc[:key]
    print('The key factors are：')
    print(key_product)

    # 柏拉图分析
    print('The factors are：')
    print(data)
    print('The cumulative factors are：')
    print(data.cumsum())
    print('The percentage of factors are：')
    print(data/data.sum())
    print('The cumulative percentage of factors are：')
    print(data.cumsum()/data.sum())

    plt.figure(figsize=(6,4),dpi=500)
    data.plot(kind = 'bar', color = 'g',edgecolor = 'black', alpha = 0.8, width = 0.6,rot=0)
    plt.ylabel('Frequency')
    plt.xlabel('Characteristic factor')
    p.plot(style = '--ko',secondary_y = True)

    plt.axvline(key_num,color='r',linestyle="--",alpha=0.8)  
    plt.text(key_num+0.2,p[key],'The cumulative proportion is: %.3f%%' % (p[key]*100), color = 'r')  
    plt.ylabel('Cumulative percentages')

    plt.xlim(-0.5,len(data)-0.5)

# 散点图
def scatter(x,y,xlabel = '',ylabel = '',title = ''):
    fig,ax1=plt.subplots(figsize=(6,4))
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

    #数据准备
    X= x #定义样本点X
    Y= y#定义样本点Y，形成sin函数
    new_x=np.arange(X.min(),X.max(),0.1) #定义差值点
    new_x1=np.arange(X.min()-50,X.max()+50,0.1) #定义延伸线x范围

    x = X
    y = Y
    z1 = np.polyfit(x,y,1) #用1次多项式拟合  可以改为5 次多项式。。。。 返回三次多项式系数
    p1= np.poly1d(z1)
    print(p1) #在屏幕上打印拟合多项式

    yvals = p1(new_x1)#也可以使用yvals=np.polyval(z1,x)

    ##作图

    ax1.plot(X,Y,'o',label='散点')
    from sklearn.metrics import r2_score
    r2 = r2_score(Y,p1(X))
    if (abs(r2)>0.3):
        if (abs(r2)<0.8):
            print('弱相关')
        else:
            print('强相关')
    else:
        print('基本不相关')
    print('相关系数R：',r2)

    # print(X,Y)
    # ax1.plot(new_x,iy1,label='插值点')
    ax1.plot(new_x1,yvals,'r',label='拟合曲线')
    ax1.set_ylim(Y.min()-50,Y.max()+50)
    ax1.set_ylabel(ylabel)
    ax1.set_xlabel(xlabel)
    ax1.set_title(title)
    ax1.legend()

# 控制图
def ControlFig(id = 1,pollutant='PM2.5',x = np.array([]),x_start = np.array([]),minTime = 0,maxTime = 0,minTime_start=0,maxTime_start=0):
    nsigma = 3
    matplotlib.rcParams['figure.figsize'] = (10.0, 4.0)

    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

    # data
    plt.plot(x, marker='o', mec='k', mfc='red', ms=5, lw=2, alpha=0.5)
    plt.hlines(y=np.mean(x_start), xmin=minTime, xmax=maxTime, colors='r', linestyles='-', linewidth=3, alpha=0.5)

    # Shewhart univariate control limits for x:
    UCL = np.mean(x_start) + nsigma*np.std(x_start)
    LCL = np.mean(x_start) - nsigma*np.std(x_start)
    plt.hlines(y=UCL, xmin=minTime, xmax=maxTime, colors='r', linestyles='--', linewidth=1, alpha=0.5)
    plt.hlines(y=LCL, xmin=minTime, xmax=maxTime, colors='r', linestyles='--', linewidth=1, alpha=0.5)

    plt.xlabel('时间(h)')
    plt.ylabel(pollutant+'含量')
    plt.title('监测站'+str(id)+' '+pollutant+'控制图')

    print('UCL:%.2f,CL:%.2f,LCL:%.2f (t:%d~%d)' %(UCL,np.mean(x),LCL,minTime_start,maxTime_start))

    plt.show()
