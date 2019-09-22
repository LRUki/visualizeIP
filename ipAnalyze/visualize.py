#data visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import numpy as np
warnings.filterwarnings('ignore')
#%matplotlib inline
def barplot_Overview(index=[1,3],name=None,Df=None):
    try:
        data=Df[Df.countryName.isin(name)]
    except TypeError:
        if len(index)==2: #if two variable are given, return the corresponding data within the range between them
            s,e=index
            data=Df[s-1:e] 
        else:
            data=Df.iloc[[x-1 for x in index]] #if more than two v are given, return each corresponding data
    sns.set(rc={'axes.facecolor':'#698c8e', 'figure.facecolor':'#698c8e'})
       #4a8a8e
       #cbebed
       # Initialize the matplotlib figure
    f, ax = plt.subplots(figsize=(13, len(data)*3))
    f.autofmt_xdate()
       
       # Plot the number of ip addresses
       
    ax1=sns.barplot(x="numberOfIp", y="countryName", data=data,
                   label="number of IPV4", color="#76c2db")
    for p in ax1.patches:
        ax.annotate('{:.3f}%'.format(p.get_width()*100/335230),
                    (p.get_x()+p.get_width()+.5, p.get_y()+.4 ),
                    fontsize=20,va='center',color="white")
       # Plot the number of cities
    sns.barplot(x="numberOfCity", y="countryName", data=data,
                label="number of cities", color="#3dffee")
    sns.barplot(x="numberOfRegion",y="countryName",data=data,
               label="number of regions",color="#a0fff5")
       
       
       # Add a legend and informative axis label
    plt.title("Number of IPV4 by country",
                 fontsize=35,color="#e5fdff",fontname='Console')
       
    a=ax.legend(ncol=1, loc="upper left", frameon=True,fontsize=20,
                fancybox=True,shadow=True,framealpha=1,bbox_to_anchor=(1.6, 1))
    a.get_frame().set_facecolor('#a1a2a3')
       
    plt.xticks(fontsize=20,color="white")
    ax.tick_params(axis="y",labelsize=15,colors="w")
       
    plt.xlabel("Summary",fontsize=15,color="#51d0ff")
    plt.ylabel("Country",size=15,color="#51d0ff")
    sns.despine(right=True,top=True,left=True,bottom=True,trim=True)
    plt.show()
def barplot_Ip(index=[1,5],name=None,Df=None):
    dic={225:"countryName" ,2169:"regionName",18308:"cityName"}
    typ=dic.get(len(Df))
    try:
        if typ=="countryName":
            data=Df[Df.countryName.isin(name)]
        elif typ=="regionName":
            data=Df[Df.regionName.isin(name)]
        else:
            data=Df[Df.cityName.isin(name)]
    except TypeError:
        if len(index)==2:
            s,e=index
            data=Df[s-1:e]
        else:
            data=Df.iloc[sorted([x-1 for x in index])]
    sns.set(rc={'axes.facecolor':'#698c8e', 'figure.facecolor':'#698c8e'})
    #4a8a8e
    #cbebed
    # Initialize the matplotlib figure
    f, ax = plt.subplots(figsize=(20, len(data)*3))
    f.autofmt_xdate()
    
    # Plot the number of ip addresses
    ax1=sns.barplot(x="numberOfIp", y=typ, data=data,
                label="number of IPV4", color="#76c2db",**{"alpha":1})
    for p in ax1.patches:
        ax.annotate('{:.3f}%'.format(p.get_width()*100/335230),
                    (p.get_width()+.05, p.get_y()+.4 ),
                   fontsize=100,va='center',color="white")
    
    # Add a legend and informative axis label
    plt.title("Number of ip addresses by {}".format(typ.replace("Name","")),
              fontsize=133,color="#e5fdff",fontname='Console')
    
    a=ax.legend(ncol=1, loc="upper left", frameon=True,fontsize=70,
             fancybox=True,shadow=True,framealpha=1,bbox_to_anchor=(1.2, 1))
    a.get_frame().set_facecolor('#f6e5f9')
    
    plt.xticks(fontsize=90,color="white")
    ax.tick_params(axis="y",labelsize=80,colors="w")
    
    plt.xlabel("Number of IPV4",fontsize=100,color="#51d0ff")
    plt.ylabel(typ.replace("Name",""),size=100,color="#51d0ff")
    sns.despine(right=True,top=True,left=True,bottom=True,trim=True)
    ax1.patches[0].get_y()
    plt.show()
def hist(start=1,end=20,Df=None):   
    f,ax=plt.subplots(figsize=(18,12))
    sns.set_style(rc={'axes.facecolor':'#995e91', 'figure.facecolor':'#995e91'})    
    h1=sns.distplot(Df[(Df.numberOfIp>=start) & (Df.numberOfIp<=end)]["numberOfIp"],
                    color="#ff44ab",hist_kws={"alpha":1},rug=True, 
                    kde_kws={"color": "white", "lw": 5},
                    rug_kws={"color": "pink", "lw": 2})
    
    name={225:"country", 2169:"region",18308:"city"}

    h1.set(xlim=(start,end))
    plt.title("Distribution of IPV4 by {}".format(name.get(len(Df),"Invalid Data")),color="White",size=80)
    ax.tick_params(axis="both",labelsize=60,colors="w")
    plt.xlabel("number of IPV4 by {}".format(name.get(len(Df),"Invalid Data")),size=80,color="#ffe0eb")
    plt.show()
def pie(index=[1,5],dtype=None,Df=None):
    data=Df[[Df.columns[0],dtype]]
    sorted_data=data.sort_values(by=dtype,ascending=False)
    if len(index)==2:
        start,end=index
        labelText=np.array(sorted_data.iloc[start-1:end][Df.columns[0]])
        fractions=np.array([(sorted_data.iloc[i][1]/sorted_data.sum()[dtype]) for i in [x for x in range(start-1,end)]])
        plt.title("Percentage of {} from {}th to {}th".format(dtype,start,end),loc='left',
              fontsize=30,backgroundcolor='lightblue',x=-0.2,y=-0.8)
    elif len(index)>2:
        index.sort()
        start=index[0]
        end=index[-1]
        labelText=np.array(sorted_data.iloc[[x-1 for x in index]][Df.columns[0]])
        fractions=np.array(np.array([(sorted_data.iloc[i][1]/sorted_data.sum()[dtype]) for i in [x-1 for x in index]]))
        plt.title("Percentage of {}, ranked{}th".format(dtype,str(index)[1:-2]),loc='left',
              fontsize=30,backgroundcolor='lightblue',x=-0.2,y=-0.8)
    labelText=np.append(labelText,["Others"])
    othersVal = 1 - fractions.sum() 
    fractions = np.append(fractions, [othersVal])
    plt.pie(fractions, labels=labelText, autopct='%1.1f%%', startangle=150,
            shadow=True,colors=sns.color_palette('muted'),radius=1.3,
            textprops={'color':'darkblue','backgroundcolor':'lightgreen','fontsize':15},
            wedgeprops={'linewidth':7},explode=[0.05 for _ in range(len(fractions))])
    
    
    plt.show()
    