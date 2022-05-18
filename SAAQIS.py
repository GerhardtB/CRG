#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Import-libraries" data-toc-modified-id="Import-libraries-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Import libraries</a></span></li><li><span><a href="#Connect-goolge-sheets" data-toc-modified-id="Connect-goolge-sheets-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Connect goolge sheets</a></span></li><li><span><a href="#Functions" data-toc-modified-id="Functions-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Functions</a></span></li><li><span><a href="#Visualisation-functions" data-toc-modified-id="Visualisation-functions-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Visualisation functions</a></span></li><li><span><a href="#Directories" data-toc-modified-id="Directories-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Directories</a></span></li><li><span><a href="#Read-all-stations-using-regular-expressions" data-toc-modified-id="Read-all-stations-using-regular-expressions-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Read all stations using regular expressions</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Read-all-the-data" data-toc-modified-id="Read-all-the-data-6.0.1"><span class="toc-item-num">6.0.1&nbsp;&nbsp;</span>Read all the data</a></span></li><li><span><a href="#Rename-with-Google-Sheets" data-toc-modified-id="Rename-with-Google-Sheets-6.0.2"><span class="toc-item-num">6.0.2&nbsp;&nbsp;</span>Rename with Google Sheets</a></span></li><li><span><a href="#Rename-variables" data-toc-modified-id="Rename-variables-6.0.3"><span class="toc-item-num">6.0.3&nbsp;&nbsp;</span>Rename variables</a></span></li><li><span><a href="#Station-information-from-Google-Sheets" data-toc-modified-id="Station-information-from-Google-Sheets-6.0.4"><span class="toc-item-num">6.0.4&nbsp;&nbsp;</span>Station information from Google Sheets</a></span></li></ul></li></ul></li><li><span><a href="#Write-backup" data-toc-modified-id="Write-backup-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Write backup</a></span></li><li><span><a href="#Load-backup" data-toc-modified-id="Load-backup-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Load backup</a></span></li><li><span><a href="#Data-quality-control" data-toc-modified-id="Data-quality-control-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>Data quality control</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Set-investigation-period" data-toc-modified-id="Set-investigation-period-9.0.1"><span class="toc-item-num">9.0.1&nbsp;&nbsp;</span>Set investigation period</a></span></li><li><span><a href="#Apply-all-limits-to-all-variables" data-toc-modified-id="Apply-all-limits-to-all-variables-9.0.2"><span class="toc-item-num">9.0.2&nbsp;&nbsp;</span>Apply all limits to all variables</a></span></li><li><span><a href="#Stuck-values" data-toc-modified-id="Stuck-values-9.0.3"><span class="toc-item-num">9.0.3&nbsp;&nbsp;</span>Stuck values</a></span></li><li><span><a href="#Write-Level_0-Data" data-toc-modified-id="Write-Level_0-Data-9.0.4"><span class="toc-item-num">9.0.4&nbsp;&nbsp;</span>Write Level_0 Data</a></span></li><li><span><a href="#Import-Level_0" data-toc-modified-id="Import-Level_0-9.0.5"><span class="toc-item-num">9.0.5&nbsp;&nbsp;</span>Import Level_0</a></span></li></ul></li><li><span><a href="#Select-stations-with-more-than-70%-annual-data-recovery" data-toc-modified-id="Select-stations-with-more-than-70%-annual-data-recovery-9.1"><span class="toc-item-num">9.1&nbsp;&nbsp;</span>Select stations with more than 70% annual data recovery</a></span><ul class="toc-item"><li><span><a href="#Data-Recovery" data-toc-modified-id="Data-Recovery-9.1.1"><span class="toc-item-num">9.1.1&nbsp;&nbsp;</span>Data Recovery</a></span></li><li><span><a href="#Stations-with-sufficient-data" data-toc-modified-id="Stations-with-sufficient-data-9.1.2"><span class="toc-item-num">9.1.2&nbsp;&nbsp;</span>Stations with sufficient data</a></span></li><li><span><a href="#Years-of-data-per-stations" data-toc-modified-id="Years-of-data-per-stations-9.1.3"><span class="toc-item-num">9.1.3&nbsp;&nbsp;</span>Years of data per stations</a></span></li><li><span><a href="#New-dataframe-with-selected-stations" data-toc-modified-id="New-dataframe-with-selected-stations-9.1.4"><span class="toc-item-num">9.1.4&nbsp;&nbsp;</span>New dataframe with selected stations</a></span></li><li><span><a href="#Update-site-information-from-sheets" data-toc-modified-id="Update-site-information-from-sheets-9.1.5"><span class="toc-item-num">9.1.5&nbsp;&nbsp;</span>Update site information from sheets</a></span></li></ul></li><li><span><a href="#Data-statistics" data-toc-modified-id="Data-statistics-9.2"><span class="toc-item-num">9.2&nbsp;&nbsp;</span>Data statistics</a></span></li></ul></li><li><span><a href="#Visualization" data-toc-modified-id="Visualization-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>Visualization</a></span><ul class="toc-item"><li><span><a href="#Period-plots" data-toc-modified-id="Period-plots-10.1"><span class="toc-item-num">10.1&nbsp;&nbsp;</span>Period plots</a></span></li></ul></li><li><span><a href="#Gauteng" data-toc-modified-id="Gauteng-11"><span class="toc-item-num">11&nbsp;&nbsp;</span>Gauteng</a></span><ul class="toc-item"><li><span><a href="#TimeSeries" data-toc-modified-id="TimeSeries-11.1"><span class="toc-item-num">11.1&nbsp;&nbsp;</span>TimeSeries</a></span><ul class="toc-item"><li><span><a href="#Annual-averages-for-sites-with-complete-data" data-toc-modified-id="Annual-averages-for-sites-with-complete-data-11.1.1"><span class="toc-item-num">11.1.1&nbsp;&nbsp;</span>Annual averages for sites with complete data</a></span></li></ul></li><li><span><a href="#Box-Plots" data-toc-modified-id="Box-Plots-11.2"><span class="toc-item-num">11.2&nbsp;&nbsp;</span>Box Plots</a></span><ul class="toc-item"><li><span><a href="#Daily" data-toc-modified-id="Daily-11.2.1"><span class="toc-item-num">11.2.1&nbsp;&nbsp;</span>Daily</a></span></li><li><span><a href="#Hourly" data-toc-modified-id="Hourly-11.2.2"><span class="toc-item-num">11.2.2&nbsp;&nbsp;</span>Hourly</a></span></li></ul></li></ul></li><li><span><a href="#Mpumalanga" data-toc-modified-id="Mpumalanga-12"><span class="toc-item-num">12&nbsp;&nbsp;</span>Mpumalanga</a></span><ul class="toc-item"><li><span><a href="#TimeSeries" data-toc-modified-id="TimeSeries-12.1"><span class="toc-item-num">12.1&nbsp;&nbsp;</span>TimeSeries</a></span><ul class="toc-item"><li><span><a href="#Annual-Averages" data-toc-modified-id="Annual-Averages-12.1.1"><span class="toc-item-num">12.1.1&nbsp;&nbsp;</span>Annual Averages</a></span></li></ul></li><li><span><a href="#Box-Plots" data-toc-modified-id="Box-Plots-12.2"><span class="toc-item-num">12.2&nbsp;&nbsp;</span>Box Plots</a></span><ul class="toc-item"><li><span><a href="#Daily" data-toc-modified-id="Daily-12.2.1"><span class="toc-item-num">12.2.1&nbsp;&nbsp;</span>Daily</a></span></li><li><span><a href="#Hourly" data-toc-modified-id="Hourly-12.2.2"><span class="toc-item-num">12.2.2&nbsp;&nbsp;</span>Hourly</a></span></li></ul></li></ul></li><li><span><a href="#Limpopo" data-toc-modified-id="Limpopo-13"><span class="toc-item-num">13&nbsp;&nbsp;</span>Limpopo</a></span><ul class="toc-item"><li><span><a href="#TimeSeries" data-toc-modified-id="TimeSeries-13.1"><span class="toc-item-num">13.1&nbsp;&nbsp;</span>TimeSeries</a></span><ul class="toc-item"><li><span><a href="#Annual-Averages" data-toc-modified-id="Annual-Averages-13.1.1"><span class="toc-item-num">13.1.1&nbsp;&nbsp;</span>Annual Averages</a></span></li></ul></li><li><span><a href="#Box-Plots" data-toc-modified-id="Box-Plots-13.2"><span class="toc-item-num">13.2&nbsp;&nbsp;</span>Box Plots</a></span><ul class="toc-item"><li><span><a href="#Daily" data-toc-modified-id="Daily-13.2.1"><span class="toc-item-num">13.2.1&nbsp;&nbsp;</span>Daily</a></span></li><li><span><a href="#Hourly" data-toc-modified-id="Hourly-13.2.2"><span class="toc-item-num">13.2.2&nbsp;&nbsp;</span>Hourly</a></span></li></ul></li></ul></li><li><span><a href="#North-West" data-toc-modified-id="North-West-14"><span class="toc-item-num">14&nbsp;&nbsp;</span>North-West</a></span><ul class="toc-item"><li><span><a href="#TimeSeries" data-toc-modified-id="TimeSeries-14.1"><span class="toc-item-num">14.1&nbsp;&nbsp;</span>TimeSeries</a></span><ul class="toc-item"><li><span><a href="#Annual-Averages" data-toc-modified-id="Annual-Averages-14.1.1"><span class="toc-item-num">14.1.1&nbsp;&nbsp;</span>Annual Averages</a></span></li></ul></li><li><span><a href="#Box-Plots" data-toc-modified-id="Box-Plots-14.2"><span class="toc-item-num">14.2&nbsp;&nbsp;</span>Box Plots</a></span><ul class="toc-item"><li><span><a href="#Daily" data-toc-modified-id="Daily-14.2.1"><span class="toc-item-num">14.2.1&nbsp;&nbsp;</span>Daily</a></span></li><li><span><a href="#Hourly" data-toc-modified-id="Hourly-14.2.2"><span class="toc-item-num">14.2.2&nbsp;&nbsp;</span>Hourly</a></span></li></ul></li><li><span><a href="#Bivariate-polar-plots" data-toc-modified-id="Bivariate-polar-plots-14.3"><span class="toc-item-num">14.3&nbsp;&nbsp;</span>Bivariate polar plots</a></span></li></ul></li><li><span><a href="#GJA-analysis" data-toc-modified-id="GJA-analysis-15"><span class="toc-item-num">15&nbsp;&nbsp;</span>GJA analysis</a></span></li><li><span><a href="#Check-compliance" data-toc-modified-id="Check-compliance-16"><span class="toc-item-num">16&nbsp;&nbsp;</span>Check compliance</a></span><ul class="toc-item"><li><span><a href="#Jabavu" data-toc-modified-id="Jabavu-16.1"><span class="toc-item-num">16.1&nbsp;&nbsp;</span>Jabavu</a></span></li><li><span><a href="#Diepkloof" data-toc-modified-id="Diepkloof-16.2"><span class="toc-item-num">16.2&nbsp;&nbsp;</span>Diepkloof</a></span></li><li><span><a href="#Springs" data-toc-modified-id="Springs-16.3"><span class="toc-item-num">16.3&nbsp;&nbsp;</span>Springs</a></span></li><li><span><a href="#Olifantsfontein" data-toc-modified-id="Olifantsfontein-16.4"><span class="toc-item-num">16.4&nbsp;&nbsp;</span>Olifantsfontein</a></span></li></ul></li></ul></div>

# # Import libraries

# In[148]:


# The pandas data science library that gives the 'spreadsheet'-like capabilities to python
import pandas as pd
# The matplotlip library is used to visualize data
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import matplotlib.cm as cm
from matplotlib.dates import DateFormatter

# The pathlib library is used to manage access to disk. It helps us to keep things the same between Windows and Linux
from pathlib import Path
# The os library is used to list and access files and directories on the hard drive
import os, sys
# Numpy is the numerical library. It is used by many of the ones before, but we import it for in case
import numpy as np
# From Numpy we also import the nan 'missing-value' object that we use alot
from numpy import nan
# For fancy matching of strings, we use re
import re
# String libary for temporary file import
from io import StringIO
# Create tooltips for interactive plots
import mpld3
# For connecting to google sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Reading excel data format
import xlrd
# Library for manipulating date and time
import datetime 
# Scientif python library for statistics
from scipy import interpolate
# Windrose library
from windrose import WindroseAxes
#Interactive widget
import ipywidgets as widgets
from ipywidgets import interact, interact_manual
#Figure style library
import seaborn as sns
sns.set_theme(style="whitegrid")
#Register pandas formatters and converters with matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import re


# # Connect goolge sheets

# https://docs.google.com/spreadsheets/d/1_SjistxWekMyf_w59pu5vHDrhOfmeHLurB47mfq_ahM/edit?usp=sharing

# In[149]:


# Configure the connection 
scope = ['https://spreadsheets.google.com/feeds']

# Give the path to the Service Account Credential json file 
# 1. Go to Google Development Console (https://console.developers.google.com/project)
# 2. Create new project
# 3. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
# 4. Fill out the form
# 5. Click “Create key”
# 6. Select “JSON” and click “Create”

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/roelof/jupyter/key/crgprojects-b66f872bd816.json',
                                                               scope)
# Authorise your Notebook
gc = gspread.authorize(credentials)

# The sprad sheet ID, which can be taken from the link to the sheet
spreadsheet_key = '1_SjistxWekMyf_w59pu5vHDrhOfmeHLurB47mfq_ahM'


#Opening the worksheet by using Worksheet ID
def readSheet():
    workbook = gc.open_by_key(spreadsheet_key)#Selecting which sheet to pulling the data
    stations = workbook.worksheet('QC_Stations')#Pulling the data and transform it to the data frame
    values = stations.get_all_values()
    Stations = pd.DataFrame(values[1:], columns=values[0])
    return(stations,Stations)
stations, Stations = readSheet()


# # Functions

# In[150]:


def head(filename,N=10):
    n=0
    with open(Path(filename)) as fp:
        for l in fp.readlines():
            if n<N:
                print(l,end="")
                n=n+1
                
def tail(filename,N=10):
    n=0
    with open(Path(filename)) as fp:
        lines=[i for i in fp.readlines()]
        Nlines=len(lines)
        for l in lines[Nlines-N:]:
            if n<N:
                print(l,end="")
                n=n+1
                
def ConvertNumeric(df,var):
    df[var]= pd.to_numeric(df[var],errors='coerce')
    
def testLogger(filename):
    Sep=","
    Data=[]
    with open(filename) as fp:
        for line in fp.readlines():
            row=line.split(Sep)
            Data.append(len(row))
    print(pd.DataFrame({"Columns":Data}).describe())
    
def ncolumnsLogger(filename):
    Sep=","
    Data=[]
    with open(filename) as fp:
        for line in fp.readlines():
            row=line.split(Sep)
            Data.append(len(row))
    return(np.median(np.array(Data)))

def readLogger(filename, nLines=18):
    DataString=""
    Sep=","
    with open(filename) as fp:
        for line in fp.readlines():
            row=line.split(Sep)
            if isinstance(nLines, list):
                if len(row) in nLines and re.match('\W*(\d{4})[/.-](\d{2})[/.-](\d{2})\s{1}(\d{2}):(\d{2}):(\d{2})\W*',row[0]):
                    DataString=DataString+line                
            else:
                if len(row) == nLines and re.match('\W*(\d{4})[/.-](\d{2})[/.-](\d{2})\s{1}(\d{2}):(\d{2}):(\d{2})\W*',row[0]):
                    DataString=DataString+line
    return(DataString)

def readRM(filename, nLines=18):
    DataString=""
    Sep=","
    with open(filename) as fp:
        for line in fp.readlines():
            row=line.split(Sep)
            if len(row) == nLines and re.match('\W*(\d{4})[/.-](\d{2})[/.-](\d{2})\s{1}(\d{2}):(\d{2}):(\d{2})\W*',row[0]):
                DataString=DataString+line
    return(DataString)

def lsR(dir,pattern=".csv",prefix="",postfix=""):
    list=[]
    for path,dirs,files in os.walk(Path(dir)):
        for f in files:
            if f.count(pattern) > 0 and f.startswith(prefix) and f.endswith(postfix):
                list.append(os.path.join(path,f))
    return(list)

def clearplots():
    plt.clf()
    
def readStation(file, authority, var):
    # Read the data file
    df=pd.read_excel(file,
                     skiprows=[0,1,3,4], 
                     parse_dates=[0], 
                     date_parser=custom_date_parser, 
                     index_col=0, 
                     na_values=['', '#N/A', '#N/A N/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN', '-nan','1.#IND','1.#QNAN', '<NA>', 'N/A', 'NA', 'NULL', 'NaN', 'n/a','nan', 'null','-999.0']
                    )
    df.index.name='Date'
    # Remove lines with a bad date index
    df=df.loc[~df.index.isnull()]
    # Remove lines where all data is missing
    df=df.dropna(axis=0, how='all')
    # Make sure that the variables are numeric
    df=df.apply(pd.to_numeric, errors='ignore')
    # Create short version
    df=df.stack()
    df=df.reset_index(level=[1])
    df.columns=['Site','Value']
    df['Variable']=var
    df['Unit']='ppm'
    df['Status']=0
    df['Authority']=authority
    df['Type']=""
    df=df.reset_index()
    df=df.set_index((df.Site + df.Variable + df.Unit + df.Date.astype(str) + df.Value.astype(str)).apply(hash))
    return(df)

def extractStation(df,Var,Site="",Authority="",Type="", Status=100):
    df=df[(df['Variable']==Var)&(df['Status']<=Status)]
    if len(Site) > 0:
        df=df[(df['Site']==Site)]
    if len(Authority) > 0:
        df=df[(df['Authority']==Authority)]
    if len(Type) > 0:
        df=df[(df['Type']==Type)]
    
    df=df.reset_index()
    df=df.set_index('Date')
    df=df.resample('1H').first()
    return(df)

def writeStation(dfRaw,df):
    df=df.dropna(subset=['index'])
    df=df.reset_index()
    df=df.set_index((df.Site + df.Variable + df.Unit + df.Date.astype(str) + df.Value.astype(str)).apply(hash))
    print("Setting ",len(df[df['Status']>0]),'status')
    dfRaw.loc[df[df['Status']>0].index, 'Status']=df[df['Status']>0]['Status']
    #return(dfRaw)
    
def stuckValue(df,Var='PM2.5 (ug/m3)',diff=0.1,stuckNumber=3):
    print("In stuckValue:",Var,diff,stuckNumber)
    df['diff']=(abs(df[Var]-df[Var].shift())>diff).astype(int)
    df['c'] = (df['diff'] != 0).cumsum()
    df['a'] = (df['c'] == 0).astype(int)
    df['streak'] = df.groupby( 'c' ).cumcount() + df['a']
    df.loc[df['streak'] > stuckNumber,'Status'] = 2
    df.drop(['streak', 'a','c','diff'], axis=1, inplace=True)
    df=df.dropna(subset=['index'])
    return(df[df['Status']==2])

months={1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'}

output=[["Agent", "Period", "Standard", "Exceeds", "Average", "Interval", "N", "N exceeds", "Std Dev", "Median", "25%", "75%", "99%"]]



Vars={"PM10 (ug/m3)",
      "PM2.5 (ug/m3)",
      "SO2 (ppb)",
      "NO2 (ppb)",
      "H2S (ppb)",
      "CO (ppm)",
      "O3 (ppb)"} 

DataAvailable={'1D':1152,
               'A':367920,
               '8H':384,
               '4H':192,
               '1H':48} 

def is_leap_year(year):
    return int(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def numdays(month,year):
    days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if month == 2:
        return(days[month]+is_leap_year(year))
    else:
        return(days[month])

def confidence_interval(data, confidence=0.99):                                                                                                                                                                                                                                    
    a = 1.0*np.array(data)                                                                                                                                                                                                                                                         
    n = len(a)                                                                                                                                                                                                                                                                     
    m, se = np.mean(a), scipy.stats.sem(a)                                                                                                                                                                                                                                         
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)                                                                                                                                                                                                                               
    return( m-h, m+h)  


# # Visualisation functions

# In[151]:


def plotdiurnalstats(df,var='PM10_logger (ug/m3)'):
    df['Time'] = df.index.map(lambda x: x.strftime("%H:00"))
    diurnal = df[['Time',var]].groupby('Time').describe()[var]
    fig, ax = plt.subplots(1, figsize=(7,6))
    ax.set_ylabel(var, fontsize=14, weight='bold')                                                                                                                                                                                                                           
    ax.set_xlabel('Time of Day', fontsize=14)                                                                                                                                                                                                                                    
    print("Plotting mean")                                                                                                                                                                                                                                                       
    ax.plot(diurnal.index, diurnal['50%'], 'g', linewidth=2.0,label=var)
    print("Plotting 75%")                                                                                                                                                                                                                                                        
    ax.plot(diurnal.index, diurnal['75%'], color='g')                                                                                                                                                                                                                            
    print("Plotting 25%")                                                                                                                                                                                                                                                        
    ax.plot(diurnal.index, diurnal['25%'], color='g') 
    ax.fill_between(diurnal.index, diurnal['50%'], diurnal['75%'], alpha=.25, facecolor='g')                                                                                                                                                                                      
    ax.fill_between(diurnal.index, diurnal['50%'], diurnal['25%'], alpha=.25, facecolor='g') 
    ax.set_xlim(0, 23);                                                                                                                                                                                                                                                          
    ax.set_xticks([i for i in range(0,24,3)])  
    plt.tight_layout() 
    
def plotdiurnal(df,var=''):
    df['decimalhour'] = df.index.hour+(df.index.minute/60)
    
    fig, ax = plt.subplots(figsize=(7,6))
    ax.set_ylabel(var, fontsize=14, weight='bold')                                                                                                                                                                                                                           
    ax.set_xlabel('Time of Day', fontsize=14)    
    
    ax.plot(df['decimalhour'].values, df[var].values, 'o', markersize=2, linewidth=0, label=var, alpha=0.3)

    #def format_coord(x, y):
    #    z=np.array_str(df[(df['decimalhour']==x)&(df[var]==y)].index.map(lambda x: x.strftime("%y/%m/%d %H:%M")).values)[1:34]
    #    return('x={}, y={}, date={}'%(x, y,z))

    #ax.format_coord = format_coord
    
    ax.set_xlim(0, 23);                                                                                                                                                                                                                                                          
    ax.set_xticks([i for i in range(0,24,3)])  
    plt.tight_layout() 
    df=df.drop(['decimalhour'], axis = 1)
    
def plottimeseries(df,var=''):
    fig, ax = plt.subplots(1,figsize=(7,6))
    df[[var]].plot(ax=ax)
    ax.set_ylabel(var, fontsize=14, weight='bold')                                                                                                                                                                                                                           
    ax.set_xlabel('', fontsize=14)
    
# Default function to read data format from SAAQIS database
def custom_date_parser(time):
    NoDates=['Max Date', 'Max Time', 'Minimum', 'Min Date', 'Min Time','Avg','Std','Data Percent','Num', 'Maximum']
    if time not in NoDates:
        try:
            time = datetime.datetime.strptime(time, "%H:%M %d/%m/%Y")
        except ValueError:
            time = time.replace('24:', '23:')
            time = datetime.datetime.strptime(time, "%H:%M %d/%m/%Y")
            time += datetime.timedelta(hours=1)
        except:
            return(np.nan)
        return(time)


# # Directories

# In[152]:


# This 'widget' is used to give us interactive graph capabilities in the matplotlib figures
get_ipython().run_line_magic('matplotlib', 'widget')


# In[153]:


HomeDir=Path('/home/roelof/Dropbox (NWU)/CRG_Data/SAAQIS_Data/20211018')


# In[154]:


os.listdir(HomeDir)


# # Read all stations using regular expressions

# ### Read all the data

# In[ ]:


FixVars={'Wdir':'WDir',
        'AmbRelH':'RH', 
        'Amb WDirection':'WindDir',
        'SolRad':'SolarRadiation',
        'Amb WSpeed':'WindSpeed',
        'AmbTemp':'Temperature'}
dfRaw = pd.DataFrame() 
for f in lsR(HomeDir, 'xlsx'):
    Filename=f.split('/')[-1]
    Authority=Filename.split('_')[0]
    Variable=Filename.split('_')[1]
    print(Authority,Variable,Filename,f)
    dftmp=readStation(f,Authority,Variable)
    dfRaw=pd.concat([dfRaw,dftmp])
dfRaw['Variable']=dfRaw['Variable'].replace(FixVars, regex=True)


# ### Rename with Google Sheets 

# In[157]:


for idx, row in Stations[['Station_SAAQIS_Name','Station_Name']].iterrows():
    for i in dfRaw['Site'].unique():
        if i in row['Station_SAAQIS_Name']:
            dfRaw.loc[dfRaw['Site'] == i, 'Site'] = row['Station_Name']
            print(i,row['Station_Name'])


# ### Rename variables

# In[159]:


dfRaw['Variable'].unique()


# In[160]:


FixVars={'AmbWspeed':'WindSpeed',
         'AmbWDirection':'WindDir',
        'AmbWSpeed':'WindSpeed', 
        'Amb WDirection':'WindDir',
        'SRad':'SolarRadiation',
         'WSpeed':'WindSpeed',
         'WDir':'WindDir',
        'Temp':'Temperature'}

dfRaw['Variable']=dfRaw['Variable'].replace(FixVars, regex=True)


# **Total Sites**

# In[161]:


x = np.array(Sites)
np.count_nonzero(x)


# **Min, Max, Mean for each variable**

# In[162]:


for v in Variables:
    dftmp=dfRaw[(dfRaw['Variable']==v)&(dfRaw['Status']==0)]
    print(v,dftmp['Value'].min(),dftmp['Value'].mean(),dftmp['Value'].max())


# # Write backup

# In[164]:


#dfRaw.to_csv(Path(HomeDir / 'SAAQIS_raw01.csv'))


# # Load backup

# In[165]:


dfRaw = pd.read_csv(Path(HomeDir / 'SAAQIS_raw01.csv'), index_col=0)


# In[166]:


dfRaw['Date']=pd.to_datetime(dfRaw['Date'])


# In[167]:


dfRaw.columns


# # Data quality control

# ### Set investigation period

# In[170]:


dfRaw = dfRaw.loc[(dfRaw['Date'] >= '2013') & (dfRaw['Date'] <= '2018')]


# ### Apply all limits to all variables

# In[171]:


# Apply limits to all variables
varlimits={"NO":[0.1,80],
           "NO2":[0.5,250],
           "NOx":[0.5,250],
           "O3":[1,150],
           "PM10":[5,2000],
           "PM2.5":[5,1000],
           "SO2":[2,500],
           "CO":[0.01,20],
           'WindDir':[0,360],
           'SolarRadiation':[-200,2000], 
           'WindSpeed':[0,50], 
           'Temperature':[-20,50],
           'RH':[0,100]
          }

# Set status of out of range values
for v in Variables:
    if v in varlimits.keys():
        print(v,varlimits[v][0],varlimits[v][1])
        df = dfRaw[dfRaw['Variable']==v]
        dfRaw.loc[df[(df['Value'] < varlimits[v][0])].index,'Status']=1
        dfRaw.loc[df[(df['Value'] > varlimits[v][1])].index,'Status']=1    


# In[944]:


for v in Variables:
    dftmp=dfRaw[(dfRaw['Variable']==v)&(dfRaw['Status']==0)]
    print(v,dftmp['Value'].min(),dftmp['Value'].mean(),dftmp['Value'].max())


# ### Stuck values

# In[945]:


def stuckValue(df,Var='PM2.5 (ug/m3)',diff=0.1,stuckNumber=3):
    print("In stuckValue:",Var,diff,stuckNumber)
    df['diff']=(abs(df[Var]-df[Var].shift())>diff).astype(int)
    df['c'] = (df['diff'] != 0).cumsum()
    df['a'] = (df['c'] == 0).astype(int)
    df['streak'] = df.groupby( 'c' ).cumcount() + df['a']
    df.loc[df['streak'] > stuckNumber,'Status'] = 2
    df.drop(['streak', 'a','c','diff'], axis=1, inplace=True)
    df=df.dropna(subset=['index'])
    return(df[df['Status']==2])
    
for s in CStations:
    for v in Variables:
        print(s,v)
        df=extractStation(dfRaw,v,s,Status=0)
        idx=stuckValue(df,Var='Value',diff=0.1,stuckNumber=2)
        idx=idx.reset_index()
        idx['index']=(idx.Site + idx.Variable + idx.Unit + idx.Value.astype(str)).apply(hash)
        #print(idx.head())
        print(idx['index'].values)
        #print(dfRaw.loc[idx['index'].values])


# ### Write Level_0 Data

# In[947]:


#dfRaw.to_csv(HomeDir / 'SAAQIS_2013_2017_Level0.csv')


# ### Import Level_0

# In[141]:


dfRaw = pd.read_csv(Path(HomeDir / 'SAAQIS_2013_2017_Level0.csv'), index_col=0)
dfRaw['Date']=pd.to_datetime(dfRaw['Date'])


# In[144]:


#dfRaw.head()


# ## Select stations with more than 70% annual data recovery

# In[145]:


Sites=dfRaw['Site'].unique()
Variables=dfRaw['Variable'].unique()
Sites.sort()


# In[146]:


np.count_nonzero(Sites)


# ### Data Recovery

# In[147]:


Threshold = 70

var = ['PM10','PM2.5']

dfAnn = pd.DataFrame()

for s in Sites:
    dftmp = pd.DataFrame()
    for v in ['PM10','PM2.5']:
        df = extractStation(dfRaw,v,s,Status=0)
        #Daily
        tValue = df['Value'].dropna().resample('1D').mean()
        tCount = df['Value'].dropna().resample('1D').count()
        tDaily = pd.concat([tValue,tCount],axis=1)
        tDaily.columns=['Mean','N']
        tDaily.loc[tDaily['N']/24*100<Threshold,'Mean'] = np.nan
        
        # Monthly averages
        tValue = tDaily['Mean'].dropna().resample('1M').mean()
        tCount = tDaily['Mean'].dropna().resample('1M').count()
        tMonthly = pd.concat([tValue,tCount],axis=1)
        tMonthly.columns = ['Mean','N']
        tMonthly.loc[tMonthly['N']/tMonthly.index.days_in_month*100<Threshold,'Mean'] = np.nan
        
         # Annual average
        tValue = tMonthly['Mean'].dropna().resample('1Y').mean()
        tCount = tMonthly['Mean'].dropna().resample('1Y').count()/12*100
        tAnnual = pd.concat([tValue,tCount],axis=1)
        tAnnual.columns = ['Mean','N']
        tAnnual.loc[tAnnual['N']<Threshold,'N'] = np.nan
        
        if len(tAnnual) > 0:
            tAnnual['Site'] = s
            tAnnual['Variable'] = v
            tAnnual.drop(columns=['Mean'])
            if len(dftmp) ==  0:
#                print('Empty')
                dftmp = tAnnual
#                print(dftmp['Site'])
            else:
#                print('Filling')
                dftmp = pd.concat([dftmp, tAnnual], axis=0)
    
    dfAnn = pd.concat([dfAnn, dftmp], axis=0)
    dfAnn = dfAnn.dropna()

dfAA = pd.pivot_table(dfAnn.round(1).reset_index().dropna(), values='N', columns=['Date', 'Variable'],index=['Site'])
dfAA = dfAA.fillna('')


# In[127]:


dfAA.sort_index()


# In[129]:


np.count_nonzero(dfAnn['Site'].unique())


# In[130]:


#dfAA.to_excel('DataRecovery.xlsx')


# ### Stations with sufficient data

# ### Years of data per stations

# In[131]:


Sites = dfAnn['Site'].unique().tolist()
dfAnn = dfAnn.reset_index()

Table = {}

Vars = ['PM10','PM2.5']

for i in Sites:
    inst = []
    for var in Vars:
        dftmp = dfAnn.loc[(dfAnn['Site'] == i) & (dfAnn['Variable'] == var)]
        if len(dftmp) > 0:
            Dates = dftmp['Date'].dt.year.tolist()
            inst.append('{}'.format(Dates))
        else:
            inst.append('')
    Table[i] = inst
Table
dfS=pd.DataFrame(data=Table).transpose()
dfS.columns=Vars
dfS


# ### New dataframe with selected stations

# In[132]:


SSites = dfAnn['Site'].unique().tolist()


# In[133]:


Sites


# In[134]:


dfLevel0 = pd.DataFrame()

Threshold = 80

for s in SSites:
    for v in ['PM10','PM2.5']:
        df = extractStation(dfRaw,v,s,Status=0)
        #Daily
        df['dValue'] = df['Value'].dropna().resample('1D').mean()
        df['dCount'] = df['Value'].dropna().resample('1D').count()
        df.loc[df['dCount']/24*100<Threshold,'Value'] = np.nan
        
        # Monthly averages
        df['mValue'] = df['dValue'].dropna().resample('1M').mean()
        df['mCount'] = df['dValue'].dropna().resample('1M').count()
        df.loc[df['mCount']/df['mCount'].index.days_in_month*100<Threshold,'Value'] = np.nan
        
        # Annual average
        df['aValue'] = df['mValue'].dropna().resample('1Y').mean()
        df['aCount'] = df['mValue'].dropna().resample('1Y').count()/12*100
        df.loc[df['aCount']/12*100<Threshold,'Value']=np.nan
        
        if len(dftmp) == 0:
            dftmp = df
        else:
            dftmp = pd.concat([df, dftmp])
        
    if len(dfLevel0) == 0:
        dfLevel0 = dftmp
    else:
        dfLevel0 = pd.concat([dfLevel0, dftmp])
dfLevel0 = dfLevel0.drop(columns=['dValue','dCount','mValue','mCount', 'aValue','aCount'])


# In[135]:


np.count_nonzero(dfLevel0['Site'].unique())


# In[136]:


dfLevel0


# In[137]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[138]:


dfLevel0.loc[(dfLevel0['Site'] == 'Komati')&(dfLevel0['Variable'] == 'PM10'),'Value'].plot()


# ### Update site information from sheets

# In[ ]:


for idx, row in Stations.iterrows():
    for i in Sites:
        if i in row['Station_SAAQIS_Name']:
            dfRaw.loc[dfRaw['Site'] == i, 'Type'] = row['Type']
            print(i, row['Station_SAAQIS_Name'], row['Type'])


# In[ ]:





# ## Data statistics

# In[116]:


dfAnn=pd.pivot_table(pd.DataFrame(data=Data, columns=['Site','Variable','Average','N']),index='Site',columns='Variable',values=['Average','N'])
dfAnn


# In[270]:


dfAnn.sort_values(('Average','PM10'), ascending=False)


# In[271]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[300]:


def SummaryTable(df,month):
    days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    ndur={'1D':1,'8H':3,'1H':24}
    ndays=days[month]
    pols=[["PM10",'1D',75,4],
          ["PM2.5",'1D',40,4],
          ["SO2","1H",134,88],
          ["SO2","1D",48,4],
          ["NO2","1H",106,88],
          ["CO","1H",26,88],
          ["CO","8H",8.7,11],
          ["O3","8H",61,11]]

    output=[["Agent", "Period", "Standard", "Exceeds", "Average", "Interval", "N", "N exceeds", "Std Dev", "Median", "25%", "75%", "99%","DataAvailable (%)"]]
    for p in pols:
        pname=p[0]
        pdur=p[1]
        paqs=p[2]
        pexc=p[3]
        #print("Doing",pname,pdur,paqs,pexc)
        if pdur == "A":
            t1=df[[pname]].dropna().resample('1M').mean()
            t2=df[[pname]].dropna().resample('1M').count()
            t2.columns=['N']
            if t2.sum()[0] < 34560:
                N=0
                Nexc=np.nan
            else:
                N=1
                if t1.mean()[0] > paqs:
                    Nexc=1
                else:
                    Nexc=0
        else:
            if pdur == '8H':
                t1=df[[pname]].resample('1H').mean().rolling(window=8,min_periods=4).mean()
                t2=df[[pname]].dropna().resample('1H').mean().rolling(window=8,min_periods=4).count()
            else:
                t1=df[[pname]].dropna().resample(pdur).mean()
                t2=df[[pname]].dropna().resample(pdur).count()
                # t1.ix[df[pname]<10,pname]=np.nan
                t2.columns=['N']
                t=pd.concat([t1,t2],axis=1)
                t.loc[t['N']<DataAvailable[pdur],pname]=np.nan
                N=len(t[pname].dropna())
                Nexc=len(t[t[pname]>paqs])
        if N>4:
            #print(t[pname].dropna().describe())
            if N<30:
                CIs=confidence_interval(t[pname].dropna().values)
                #bootstrap.ci(data=t[pname].dropna(),statfunction=sp.mean,alpha=0.05)
            elif N>5:
                CIs=confidence_interval(t[pname].dropna().values)
            else:
                CIs=["",""]
            Pave=t[pname].mean()
            Pstd=t[pname].std()
            P50=t[pname].quantile(0.5)
            P25=t[pname].quantile(0.25)
            P75=t[pname].quantile(0.75)
            P99=t[pname].quantile(0.99)
        else:
            CIs=[np.nan,np.nan]
            Pave=t[pname].mean()
            Pstd=np.nan
            P50=np.nan
            P25=np.nan
            P75=np.nan
            P99=np.nan
        #print(t[pname].mean(),CIs,N)
        DA=N/(ndays*ndur[pdur])*100
        output.append([pname,pdur,paqs,pexc,"%.0f" % (Pave),"%.0f-%.0f" % (CIs[0],CIs[1]),N,Nexc,"%.0f" % (Pstd),"%.0f" % (P50),"%.0f" % (P25),"%.0f" % (P75),"%.0f" % (P99),"%.0f" % (DA)])
        a=np.array(output)
        df2=pd.DataFrame(data=a[1:,1:],index=a[1:,0],columns=a[0,1:])
        df2=df2.replace("nan-nan", "")
        df2=df2.replace("nan", "")
        #print(t)
    return(df2)


# In[124]:


def DataAvailableTable(df):
    #output=[["Parameter", "Data Available (mins)", "DataAvailable (%)"]]
    output={}
    TotalHours=len(df['Value'])
    HoursData=len(df['Value'].dropna())
    output['Value']=["{:.0f}".format(HoursData),"{:.0f}".format(HoursData/TotalHours*100)]
    return(output)  


# # Visualization

# In[415]:


def extractStationVars(df,Site="",Vars=[],Status=0):
    df=df[(df['Status']<=Status)&(df['Site']==Site)]
    df=pd.pivot_table(df,index=['Date'],columns=['Variable'],values=['Value'])
    df.index=pd.to_datetime(df.index)
    df.columns=df.columns.droplevel(0)
    if len(Vars) > 0:
        Vars=[v for v in Vars if v in df.columns]
        df=df[Vars]
    df=df.resample('1H').first()
    return(df)


# In[416]:


df01 = extractStation(dfRaw, Var='PM10',Type='Industrial')


# In[423]:


dftmp=extractStationVars(dfRaw,Site='Jabavu')


# In[424]:


dftmp.info()


# In[ ]:





# In[76]:



#dftmp.columns=dftmp.columns.droplevel(0)


# In[280]:


get_ipython().run_line_magic('matplotlib', 'inline')
df2=dftmp[['PM10','PM2.5']].stack().reset_index()
df2.columns=['Date','Variable','Concentration (ug/m3)']
df2.index = df2['Date']

#define figure size
sns.set(rc={"figure.figsize":(10, 10)}) #width=8, height=4
sns.boxplot(x=df2.index.month,y='Concentration (ug/m3)',hue='Variable',data=df2)


# In[281]:


p10=lambda x: np.percentile(x[~np.isnan(x)],10)
p10.__name__='p10'
p25=lambda x: np.percentile(x[~np.isnan(x)],25)
p25.__name__='p25'
p75=lambda x: np.percentile(x[~np.isnan(x)],75)
p75.__name__='p75'
p90=lambda x: np.percentile(x[~np.isnan(x)],90)
p90.__name__='p90'


# In[282]:


df3=pd.pivot_table(dftmp,index=dftmp.index.month,columns=dftmp.index.hour, values=['PM2.5'],aggfunc=[p10,p25,p75,p90]).stack()
df3


# In[283]:


df3.loc[1,0]['p10'].values[0]


# In[284]:


getAQClimate(dftmp,var="PM2.5",start="2021-03-15",end="2021-03-16")


# ## Period plots

# In[285]:


def cleanplot(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)

def getAQClimate(df,var="",start="",end=""):

    p10=lambda x: np.percentile(x[~np.isnan(x)],10)
    p10.__name__='p10'
    p25=lambda x: np.percentile(x[~np.isnan(x)],25)
    p25.__name__='p25'
    p75=lambda x: np.percentile(x[~np.isnan(x)],75)
    p75.__name__='p75'
    p90=lambda x: np.percentile(x[~np.isnan(x)],90)
    p90.__name__='p90'
    df2=pd.pivot_table(dftmp,index=dftmp.index.month,columns=dftmp.index.hour, values=[var],aggfunc=[p10,p25,p75,p90]).stack()

    df1=df[start:end][[var]]
    df1[var+'p10']=np.nan
    df1[var+'p90']=np.nan
    df1[var+'p25']=np.nan
    df1[var+'p75']=np.nan
    for idx,row in df1.iterrows():
        df1.loc[idx,var+'p10']=df2.loc[idx.month,idx.hour]['p10'].values[0]
        df1.loc[idx,var+'p90']=df2.loc[idx.month,idx.hour]['p90'].values[0]
        df1.loc[idx,var+'p25']=df2.loc[idx.month,idx.hour]['p25'].values[0]
        df1.loc[idx,var+'p75']=df2.loc[idx.month,idx.hour]['p75'].values[0]
    return(df1)
    
def plotTimeSeriesPeriod(df,title="", var="", start="",end="",climate=False):
    
    
    # Size of 1x graph y-axis
    Y=2
    
    mpl.style.use('default')
    
    # Set period
    if len(start)>0 and len(end)>0:
        df2=df[start:end]
    elif len(start)>0 and len(end)==0:
        df2=df[start:]
    elif len(start)==0 and len(end)>0:
        df2=df[:end]
    else:
        df2=df
       
    #df=df.resample('1D').mean()
    # Count the number of plots
    n=0
    plotpm10=False
    plotpm25=False
    plotso2=False
    plotno=False
    plotno2=False
    ploto3=False
    plotwinds=True
    
    if 'PM10' in df.columns and len(df2['PM10'].dropna()) > 0:
        n=n+1
        plotpm10=True
    if 'PM2.5' in df.columns and len(df2['PM2.5'].dropna()) > 0:
        n=n+1
        plotpm25=True
    if 'SO2' in df.columns and len(df2['SO2'].dropna()) > 0:
        n=n+1
        plotso2=True
        
    ysize=n*Y
    f,ax = plt.subplots(n,sharex=True, figsize=[8,ysize]) # fig.add_subplot(1,1,1)
    i=0
    
    if plotpm10:
        df3=getAQClimate(df,var="PM10",start=start,end=end)
        ax[i].fill_between(df3.index, df3['PM10p10'], df3['PM10p90'], alpha=.25, facecolor='tab:blue', label='10-90%')                                                                                                                                                                                      
        ax[i].fill_between(df3.index, df3['PM10p25'], df3['PM10p75'], alpha=.5, facecolor='tab:blue', label='25-75%') 
        ax[i].plot(df2.index,df2['PM10'], color='tab:orange', label='PM10 (ug/m3)')
        cleanplot(ax[i])
        ax[i].set_ylabel("ug/m3")     
        ax[i].legend()
        i=i+1
        
    if plotpm25:
        df3=getAQClimate(df,var="PM2.5",start=start,end=end)
        ax[i].fill_between(df3.index, df3['PM2.5p10'], df3['PM2.5p90'], alpha=.25, facecolor='tab:blue')                                                                                                                                                                                      
        ax[i].fill_between(df3.index, df3['PM2.5p25'], df3['PM2.5p75'], alpha=.5, facecolor='tab:blue') 
        ax[i].plot(df2.index,df2['PM2.5'], color='tab:orange', label='PM2.5 (ug/m3)')
        cleanplot(ax[i])
        ax[i].set_ylabel("ug/m3")     
        ax[i].legend()
        i=i+1
                
    if plotso2:
        df3=getAQClimate(df,var="SO2",start=start,end=end)
        ax[i].fill_between(df3.index, df3['SO2p10'], df3['SO2p90'], alpha=.25, facecolor='tab:blue')                                                                                                                                                                                      
        ax[i].fill_between(df3.index, df3['SO2p25'], df3['SO2p75'], alpha=.5, facecolor='tab:blue') 
        ax[i].plot(df2.index,df2['SO2'], color='tab:orange', label='SO2 (ppb)')
        cleanplot(ax[i])
        ax[i].legend()
        ax[i].set_ylabel("ppb")     
        i=i+1
    
    i=i-1
    # Hide the spines of the figure
    ax[i].spines["top"].set_visible(False)
    ax[i].spines["right"].set_visible(False)
    plt.xticks(fontsize=9)
    # Ensure that the ax1is ticks only show up on the bottom and left of the plot.
    # Ticks on the right and top of the plot are generally unnecessary chartjunk.
    ax[i].get_xaxis().tick_bottom()
    ax[i].get_yaxis().tick_left()
    
    if len(title) > 0:
        f.suptitle(title)
    plt.tight_layout()
    #plt.savefig('Figure.png', bbox_inches='tight', dpi=300)


# In[157]:


def plotTimeSeries(df,title=""):
    # Size of 1x graph y-axis
    Y=2
    
    mpl.style.use('default')
    
        
    #df=df.resample('1D').mean()
    # Count the number of plots
    n=0
    plotpm10=False
    plotpm25=False
    plotso2=False
    plotno=False
    plotno2=False
    ploto3=False
    plotwinds=True
    
    if 'PM10' in df.columns and len(df['PM10'].dropna()) > 0:
        n=n+1
        plotpm10=True
    if 'PM2.5' in df.columns and len(df['PM2.5'].dropna()) > 0:
        if not plotpm10:
            n=n+1
        plotpm25=True
    if 'SO2' in df.columns and len(df['SO2'].dropna()) > 0:
        n=n+1
        plotso2=True
    if 'NO' in df.columns and len(df['NO'].dropna()) > 0:
        n=n+1
        plotno=True
    if 'NO2' in df.columns and len(df['NO2'].dropna()) > 0:
        if not plotno:
            n=n+1      
        plotno2=True
    if 'O3' in df.columns and len(df['O3'].dropna()) > 0:
        if not plotno and not plotno2:
            n=n+1
        ploto3=True
        
    if 'WindSpeed' in df.columns and len(df['WindSpeed'].dropna()) > 0 and 'WindDir' in df.columns and len(df['WindDir'].dropna()) > 0:
        n=n+1
        plotwinds=True
        
    print(n)
    ysize=n*Y
    f,ax = plt.subplots(n,sharex=True, figsize=[8,ysize]) # fig.add_subplot(1,1,1)
    i=0
    
    if plotpm10:
        ax[i].plot(df.index,df['PM10'], color='tab:orange', label='PM10 (ug/m3)')
    if plotpm25:
        ax[i].plot(df.index,df['PM2.5'], color='tab:blue', label='PM10 (ug/m3)')
    if plotpm10 or plotpm25:
        cleanplot(ax[i])
        ax[i].legend(ncol=2)
        ax[i].set_ylabel("ug/m3")     
        i=i+1
        
    if plotso2:
        ax[i].plot(df.index,df['SO2'], color='tab:blue', label='SO2 (ppb)')
        cleanplot(ax[i])
        ax[i].legend()
        ax[i].set_ylabel("ppb")     
        i=i+1

    if plotno:
        ax[i].plot(df.index,df['NO'], color='tab:blue', label='NO (ppb)')
    if plotno2:
        ax[i].plot(df.index,df['NO2'], color='tab:green', label='NO2 (ppb)')
    if ploto3:
        ax[i].plot(df.index,df['O3'], color='tab:orange', label='O3 (ppb)')
    if plotno or plotno2 or ploto3:
        cleanplot(ax[i])
        ax[i].legend()
        ax[i].set_ylabel("ppb")  
        i=i+1
    
    if plotwinds:
        axw=ax[i].twinx()

        axw.plot(df.index,df['WindDir'], color='tab:orange', label='Wind Direction', alpha=.25)
        ax[i].plot(df.index,df['WindSpeed'], color='tab:blue', label='Wind Speed')

        ax[i].legend()
        axw.legend()
        ax[i].set_ylabel("m/s") 
        axw.set_ylabel("degrees")
        axw.spines["top"].set_visible(False)
        axw.spines["left"].set_visible(False)
        i=i+1
    
    i=i-1
    # Hide the spines of the figure
    ax[i].spines["top"].set_visible(False)
    ax[i].spines["right"].set_visible(False)

    # Ensure that the ax1is ticks only show up on the bottom and left of the plot.
    # Ticks on the right and top of the plot are generally unnecessary chartjunk.
    ax[i].get_xaxis().tick_bottom()
    ax[i].get_yaxis().tick_left()
    
    if len(title) > 0:
        f.suptitle(title)
    plt.tight_layout()
    #plt.savefig('Figure.png', bbox_inches='tight', dpi=300)


# In[287]:


dfRaw['Date']=pd.to_datetime(dfRaw['Date'])


# # Gauteng

# ## TimeSeries

# In[160]:


Types


# ### Annual averages for sites with complete data 

# In[163]:


df1=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Type']=='Residential - Low Income')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df1.index.get_level_values
df1=(df1.groupby([level_values(0)]+[pd.Grouper(freq='1Y', level=-1)]).mean())
df1 =df1.reset_index()
usesites = pd.pivot_table(df1,index='Site',columns=['Date'],values='PM10')
df1 = usesites
df1.sort_index()

col_map = plt.get_cmap('tab20c')
ax = df1.plot(kind='bar', figsize=(15,10), width=0.6)

plt.axhline(y = 40, color = 'r',label='PM10 daily Standard', linestyle='--')
plt.plot()
plt.legend(loc='upper left')
plt.suptitle('Annual average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[171]:


df1[columns='Site']


# In[162]:


df1=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Type']=='Background')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df1.index.get_level_values
df1=(df1.groupby([level_values(0)]+[pd.Grouper(freq='1Y', level=-1)]).mean())
df1 =df1.reset_index()
usesites = pd.pivot_table(df1,index='Site',columns=['Date'],values='PM10')
df1 = usesites
df1.sort_index()

col_map = plt.get_cmap('tab20c')
ax = df1.plot(kind='bar', figsize=(15,10), width=0.6)

plt.axhline(y = 40, color = 'r',label='PM10 daily Standard', linestyle='--')
plt.plot()
plt.legend(loc='upper left')
plt.suptitle('Annual average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[161]:


df1=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Type']=='Urban')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df1.index.get_level_values
df1=(df1.groupby([level_values(0)]+[pd.Grouper(freq='1Y', level=-1)]).mean())
df1 =df1.reset_index()
usesites = pd.pivot_table(df1,index='Site',columns=['Date'],values='PM10')
df1 = usesites
df1.sort_index()

col_map = plt.get_cmap('tab20c')
ax = df1.plot(kind='bar', figsize=(15,10), width=0.6)

plt.axhline(y = 40, color = 'r',label='PM10 daily Standard', linestyle='--')
plt.plot()
plt.legend(loc='upper left')
plt.suptitle('Annual average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[159]:


df1=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Type']=='Industrial')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df1.index.get_level_values
df1=(df1.groupby([level_values(0)]+[pd.Grouper(freq='1Y', level=-1)]).mean())
df1 =df1.reset_index()
usesites = pd.pivot_table(df1,index='Site',columns=['Date'],values='PM10')
df1 = usesites
df1.sort_index()

col_map = plt.get_cmap('tab20c')
ax = df1.plot(kind='bar', figsize=(15,10), width=0.6)

plt.axhline(y = 40, color = 'r',label='PM10 daily Standard', linestyle='--')
plt.plot()
plt.legend(loc='upper left')
plt.suptitle('Annual average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# ## Box Plots

# ### Daily

# In[379]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[380]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='GJA')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1D', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM10').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM10',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,250)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[381]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM2.5')&(dfRaw['Authority']=='GJA')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1D', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM2.5').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM2.5',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,250)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

plt.plot([40,40],[m,M], color='tab:red', label='PM2.5 daily Standard', linestyle='--') 
plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM25_daily.png', bbox_inches='tight',format='png', dpi=300)


# ### Hourly

# In[386]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='GJA')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1H', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM10').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM10',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,1000)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

#plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
#plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[388]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM2.5')&(dfRaw['Authority']=='GJA')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1H', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM2.5').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM2.5',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,1000)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

#plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
#plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# # Mpumalanga

# ## TimeSeries

# ### Annual Averages

# In[241]:


df1=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='MP')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df1.index.get_level_values
df1=(df1.groupby([level_values(0)]+[pd.Grouper(freq='1Y', level=-1)]).mean())
df1 =df1.reset_index()
usesites = pd.pivot_table(df1,index='Site',columns=['Date'],values='PM10')
df1 = usesites.dropna()
df1.sort_index()

col_map = plt.get_cmap('tab20c')
ax = df1.plot(kind='bar', figsize=(15,10), width=0.6)

plt.axhline(y = 40, color = 'r',label='PM10 daily Standard', linestyle='--')
plt.plot()
plt.legend(loc='upper left')
plt.suptitle('Annual average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# ## Box Plots

# ### Daily

# In[390]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='MP')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1D', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM10').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM10',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,250)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[389]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM2.5')&(dfRaw['Authority']=='MP')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1D', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM2.5').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM2.5',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,250)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

plt.plot([40,40],[m,M], color='tab:red', label='PM2.5 daily Standard', linestyle='--') 
plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM25_daily.png', bbox_inches='tight',format='png', dpi=300)


# ### Hourly

# In[392]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='MP')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1H', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM10').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM10',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,1000)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

#plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
#plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[391]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM2.5')&(dfRaw['Authority']=='MP')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1H', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM2.5').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM2.5',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,1000)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

#plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
#plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# # Limpopo

# ## TimeSeries

# ### Annual Averages

# In[246]:


df1=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='LP')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df1.index.get_level_values
df1=(df1.groupby([level_values(0)]+[pd.Grouper(freq='1Y', level=-1)]).mean())
df1 =df1.reset_index()
usesites = pd.pivot_table(df1,index='Site',columns=['Date'],values='PM10')
df1 = usesites
df1.sort_index()

col_map = plt.get_cmap('tab20c')
ax = df1.plot(kind='bar', figsize=(15,10), width=0.6)

plt.axhline(y = 40, color = 'r',label='PM10 daily Standard', linestyle='--')
plt.plot()
plt.legend(loc='upper left')
plt.suptitle('Annual average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# ## Box Plots

# ### Daily

# In[395]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='LP')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1D', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM10').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM10',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,250)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[396]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM2.5')&(dfRaw['Authority']=='LP')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1D', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM2.5').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM2.5',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,250)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

plt.plot([40,40],[m,M], color='tab:red', label='PM2.5 daily Standard', linestyle='--') 
plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM25_daily.png', bbox_inches='tight',format='png', dpi=300)


# ### Hourly

# In[406]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='LP')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1H', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM10').count()
usesites=list(goodsites[goodsites>500].index.values)
usesites.remove('Steelpoort')
df4=df4[df4['Site'].isin(usesites)]



ax=df4.boxplot(column='PM10',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,1000)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

#plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
#plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[397]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM2.5')&(dfRaw['Authority']=='LP')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1H', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM2.5').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM2.5',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,1000)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

#plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
#plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# # North-West

# ## TimeSeries

# ### Annual Averages

# In[245]:


df1=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='NW')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df1.index.get_level_values
df1=(df1.groupby([level_values(0)]+[pd.Grouper(freq='1Y', level=-1)]).mean())
df1 =df1.reset_index()
usesites = pd.pivot_table(df1,index='Site',columns=['Date'],values='PM10')
df1 = usesites
df1.sort_index()

col_map = plt.get_cmap('tab20c')
ax = df1.plot(kind='bar', figsize=(15,10), width=0.6)

plt.axhline(y = 40, color = 'r',label='PM10 daily Standard', linestyle='--')
plt.plot()
plt.legend(loc='upper left')
plt.suptitle('Annual average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# ## Box Plots

# ### Daily

# In[407]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='NW')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1D', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM10').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM10',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,250)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[408]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM2.5')&(dfRaw['Authority']=='NW')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1D', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM2.5').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM2.5',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,250)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

plt.plot([40,40],[m,M], color='tab:red', label='PM2.5 daily Standard', linestyle='--') 
plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM25_daily.png', bbox_inches='tight',format='png', dpi=300)


# ### Hourly

# In[409]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM10')&(dfRaw['Authority']=='NW')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1H', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM10').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]



ax=df4.boxplot(column='PM10',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,1000)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

#plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
#plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# In[410]:


# Get daily averages from short format quickly
df4=pd.pivot_table(dfRaw[(dfRaw['Status']==0)&(dfRaw['Variable']=='PM2.5')&(dfRaw['Authority']=='NW')],index=['Site','Date'],columns=['Variable'],values='Value')
level_values=df4.index.get_level_values
df4=(df4.groupby([level_values(i) for i in [0]]+[pd.Grouper(freq='1H', level=-1)]).mean())
df4=df4.reset_index()
goodsites=pd.pivot_table(df4,index='Date',columns=['Site'],values='PM2.5').count()
usesites=list(goodsites[goodsites>500].index.values)
df4=df4[df4['Site'].isin(usesites)]

ax=df4.boxplot(column='PM2.5',by='Site', vert=False, figsize=(8,10), return_type='axes')
ax[0].spines["top"].set_visible(False)
ax[0].spines["bottom"].set_visible(False)
ax[0].spines["right"].set_visible(False)
ax[0].set_xlim(0,1000)
ax[0].grid(False)
ax[0].set_xlabel("Concentration (ug/m3)")

(m,M)=ax[0].get_ylim()

#plt.plot([75,75],[m,M], color='tab:red', label='PM10 daily Standard', linestyle='--') 
#plt.legend(loc='upper left', bbox_to_anchor=(0,1.03))
plt.suptitle('Daily average for available data')
plt.tight_layout()
#plt.savefig('GJA_PM10_daily.png', bbox_inches='tight',format='png', dpi=300)


# ## Bivariate polar plots

# In[418]:


import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

wd = [90, 297, 309, 336, 20, 2, 334, 327, 117, 125, 122, 97, 95, 97, 103, 106, 125, 148, 147, 140, 141, 145, 144, 151, 161]
ws = [15, 1.6, 1.8, 1.7, 2.1, 1.6, 2.1, 1.4, 3, 6.5, 7.1, 8.2, 10.2, 10.2, 10.8, 10.2, 11.4, 9.7, 8.6, 7.1, 6.4, 5.5, 5, 5, 6]
oz = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 90, 140, 100, 106, 125, 148, 147, 140, 141, 145, 144, 151, 161]
wd_rad = np.radians(np.array(wd))
oz = np.array(oz, dtype=np.float)


WD, WS = np.meshgrid(np.linspace(0, 2*np.pi, 36), np.linspace(min(ws), max(ws), 16 ))
Z = interpolate.griddata((wd_rad, ws), oz, (WD, WS), method='linear')

fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
cmap = plt.get_cmap('hot')
cmap.set_under('none')
img = ax.pcolormesh(WD, WS, Z, cmap=cmap, vmin=20)
plt.colorbar(img)
plt.show()


# In[303]:


# Define the settings for the windrose that is being created.
def plot_ppollrose(dfc,WD="WindDir",WS="WindSpeed",CO="PM10",title="",output=Path("polar.png")):                                                                                                                                                                                                                                                   
    dfc=dfc[[WD,WS,CO]].dropna()
    wd_rad = np.radians(np.array(dfc[WD]))
    Conc = np.array(dfc[CO], dtype=float)
    WSmax = max(dfc[WS])
    WD1, WS1 = np.meshgrid(np.linspace(0, 2*np.pi, 360), np.linspace(min(dfc[WS]), max(dfc[WS]), 16))
    Z = interpolate.griddata((wd_rad, dfc[WS]), dfc[CO], (WD1, WS1), method='linear')

    levels = MaxNLocator(nbins=10).tick_values(0, 500)
    
    cmap = plt.get_cmap('viridis')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    
    fig, ax = plt.subplots(figsize=(4,4), subplot_kw={"projection": "polar"})
    
    img = ax.pcolormesh(WD1, WS1, Z, cmap=cmap, norm=norm, edgecolor='none', linewidth=0, alpha=1, shading='nearest', snap='bool', capstyle='round')
    
    cbar = plt.colorbar(img, cax=None, ax=None, use_gridspec=True, orientation='vertical', drawedges=True, pad=0.09, shrink=0.5)
    cbar.ax.tick_params(labelsize=10)
    cbar.set_label(CO,size=10, labelpad=+10 )
    
    #To display the grid in the background.
    ax.grid(True)
    # Specify different settings for major and minor grids
    #ax.grid(which = 'minor', alpha = 0.3)
    #ax.grid(which = 'major', alpha = 0.7)
    
    major_yticks = np.arange(0, 15, step=2.5)
    #minor_yticks = np.arange(0, 15, step=0.5)
    #major_xticks = np.arange(0, 8, step=360)
    #minor_xticks = np.arange(0, 360, step=22.5)
    
    ax.tick_params(axis = 'both', which = 'major', labelsize = 10, width=1.5, direction='out', pad=0.8, labelrotation=0, top=True, grid_color='white', grid_linewidth=1)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 0)
    
    ax.set_yticks(major_yticks)
    ax.set_ylim([0,WSmax])
    #ax.set_yticks(minor_yticks, minor=True)
    #ax.set_xticks(major_xticks)
    #ax.set_xticks(minor_xticks, minor=True)
   
    # To rename the x-axis from Degrees to Directions.
    ax.set_xticklabels(['N', 'N-E', 'E', 'S-E', 'S', 'S-W', 'W', 'N-W'], fontsize=10)
       
    # To move the 0 Deg from the E-point to the N-point.
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    
    ax.set_axisbelow(False)
    fig.suptitle(title)
    plt.tight_layout()
    #plt.savefig(output,dpi=300, bbox_inches = "tight")  
    plt.show()
    #plt.close()


# In[304]:


plot_ppollrose(dftmp,CO='PM10', title='Jabavu')


# In[113]:


Stations


# # GJA analysis

# In[249]:


#Sites


# In[250]:


dfRaw[dfRaw['Authority']=='GJA']['Site'].unique()


# In[251]:


dfGJA=dfRaw[dfRaw["Site"].str.contains('(Jabavu|Diepkloof|Springs|Olifantsfontein)', regex=True)]


# In[252]:


dfGJA['Site'].unique()


# In[253]:


GJAsites=['Diepkloof', 'Jabavu', 'Olifantsfontein','Springs', 'Springs-new',
          'Kliprivier', 'Sebokeng', 'Sharpeville',
           'Three Rivers', 'Etwatwa', 'Olifantsfontein', 'Tsakane',
           'Wattville', 'Booysens', 'Ekandustria', 'Rosslyn',
           'Bodibeng', 'Mogale_City', 'Olievenhoutbosch', 'PTA_West',
           'Hammanskraal', 'Thokoza', 'Tswane_Market', 'Randwater',
           'Bedfordview', 'Buccleugh', 'Tembisa', 'Randfontein',
           'Leondale_City', 'Meyerton', 'Vanderbijlpark',
           'Diepsloot', 'Orange_Farm', 'Alexandra', 'NWU_Vaal',
           'Ivory_park']


# In[254]:


Threshold=65
Data=[]

for s in GJAsites:
    for v in ['PM10','PM2.5']:
        df=extractStation(dfRaw,v,s,Status=0)
        # Daily averages
        tThres=df['Value'].dropna().quantile(0.99)
        tValue=df['Value'].dropna().resample('1D').mean()
        tCount=df['Value'].dropna().resample('1D').count()
        tDaily=pd.concat([tValue,tCount],axis=1)
        tDaily.columns=['Mean','N']
        tDaily.loc[tDaily['N']/24*100<Threshold,'Mean']=np.nan

        # Monthly averages
        tValue=tDaily['Mean'].dropna().resample('1M').mean()
        tCount=tDaily['Mean'].dropna().resample('1M').count()
        tMonthly=pd.concat([tValue,tCount],axis=1)
        tMonthly.columns=['Mean','N']
        tMonthly.loc[tMonthly['N']/tMonthly.index.days_in_month*100<Threshold,'Mean']=np.nan

        # Annual average
        tValue=tMonthly['Mean'].dropna().resample('1Y').mean()
        tCount=tMonthly['Mean'].dropna().resample('1Y').count()
        tAnnual=pd.concat([tValue,tCount],axis=1)
        tAnnual.columns=['Mean','N']
        tAnnual.loc[tAnnual['N']/12*100<Threshold,'Mean']=np.nan

        #
        if len(tAnnual['Mean'].dropna()) > 0:
            Data.append([s,v,tAnnual['Mean'].mean(),tAnnual['Mean'].count()])
        else:
            tMonthly['Month']=tMonthly.index.month
            tMonthly=tMonthly.groupby('Month').mean()[['Mean']]
            if tMonthly['Mean'].count()/12*100>Threshold:
                Data.append([s,v,tMonthly['Mean'].mean(),tMonthly['Mean'].count()])
    

dfAnn=pd.pivot_table(pd.DataFrame(data=Data, columns=['Site','Variable','Annual','N']),index='Site',columns='Variable',values=['Annual','N'])
dfAnn


# In[255]:


dfAnn.sort_values(('Annual','PM10'), ascending=False, inplace=True)
ax=dfAnn['Annual'].plot(kind='bar',figsize=(10,5))

plt.plot(dfAnn.index, [40 for x in dfAnn.index], color='tab:blue', label='PM10 Standard', linestyle='--') 
plt.plot(dfAnn.index, [20 for x in dfAnn.index], color='tab:orange', label='PM2.5 Standard', linestyle='--') 

plt.legend()
ax.spines["top"].set_visible(False)
#ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_ylabel("Concentration (ug/m3)")
ax.set_xlabel("")

#ax.set_xlim(0,250)
ax.grid(False)
plt.tight_layout()
#plt.savefig('GJA_PM_annual.png', bbox_inches='tight',format='png', dpi=300)


# In[256]:


pd.options.display.float_format = '{:,.0f}'.format
dfAnn.fillna('')


# In[257]:


len(df['2017'])


# In[258]:


df['Value'].dropna().quantile(0.99)


# In[259]:


int(10<5)


# # Check compliance

# In[264]:


Sites =  GJAsites


# In[265]:


for s in Sites:
    print(",{},,,".format(s),end="")


# In[266]:


int(10>5)


# **Show the number of exceedances per year**

# In[268]:


# 0 above 70% and no exceedances
# -1 not 70% data recovery
# 1 exceeds hourly
# 2 exceeds daily
# 3 exceeds hourly and daily
# 4 exceeds annual
# 5 exceeds hourly and annual
# 6 exceeds daily and annual
# 7 exceeds hourly, daily, and annual

vars=['PM10','PM2.5']
standard=[[134,48,19],[106,0,21],[0,75,40],[0,40,20]]
for s in Sites:
    print(",{}".format(s),end="")
print("")
for v in range(len(vars)):
    print(vars[v])
    print("",end="")
    for y in range(2017,2021):
        print(y,end="")
        for s in Sites:
            df=extractStation(dfRaw,vars[v],s,Status=0)
            df=df[['Value']]
            try:
                dfy=df['{}-01-01'.format(y):'{}-12-31'.format(y)]

                # is there an hourly standard
                if standard[v][0] > 0:
                    HDA=len(dfy['Value'].dropna())/(365*24)*100
                    HComply=dfy['Value'].dropna().quantile(0.99)>standard[v][0]
                else:
                    HDA=len(dfy['Value'].dropna())/(365*24)*100
                    HComply=False

                # is there an daily standard
                if standard[v][1] > 0:
                    DDA=len(dfy['Value'].dropna().resample('1D').mean())/365*100
                    DComply=dfy['Value'].dropna().resample('1D').mean().quantile(0.99)>standard[v][1]
                else:
                    DDA=len(dfy['Value'].dropna().resample('1D').mean())/365*100
                    DComply=False

                # is there an annual standard
                if standard[v][2] > 0:
                    AComply=dfy['Value'].mean()>standard[v][2]
                else:
                    AComply=False

                if HDA < DDA:
                    DA=HDA
                else:
                    DA=DDA

                index=0
                if HComply and not DComply and not AComply:
                    index=1
                if DComply and not HComply and not AComply:
                    index=2
                if HComply and DComply and not AComply:
                    index=3
                if AComply and not HComply and not DComply:
                    index=4
                if HComply and AComply and not DComply:
                    index=5
                if DComply and AComply and not HComply:
                    index=6
                if HComply and DComply and AComply:
                    index=7

                if DA< 70 and index==0:
                    index=-10
                if DA<70 and index>0:
                    index=index*-1

                print(",{:.0f}".format(index), end="")

                #break
                #print(y,s)
            except:
                print(",-10", end="")
        print("")


# In[269]:


dfy


# In[273]:


Threshold=65
Data=[]
for s in GJAsites:
    for v in ['PM10','PM2.5']:
        df=extractStation(dfRaw,v,s,Status=0)
        # Daily averages
        tThres=df['Value'].dropna().quantile(0.99)
        tValue=df['Value'].dropna().resample('1D').mean()
        tCount=df['Value'].dropna().resample('1D').count()
        tDaily=pd.concat([tValue,tCount],axis=1)
        tDaily.columns=['Mean','N']
        tDaily.loc[tDaily['N']/24*100<Threshold,'Mean']=np.nan

        # Monthly averages
        tValue=tDaily['Mean'].dropna().resample('1M').mean()
        tCount=tDaily['Mean'].dropna().resample('1M').count()
        tMonthly=pd.concat([tValue,tCount],axis=1)
        tMonthly.columns=['Mean','N']
        tMonthly.loc[tMonthly['N']/tMonthly.index.days_in_month*100<Threshold,'Mean']=np.nan

        # Annual average
        tValue=tMonthly['Mean'].dropna().resample('1Y').mean()
        tCount=tMonthly['Mean'].dropna().resample('1Y').count()
        tAnnual=pd.concat([tValue,tCount],axis=1)
        tAnnual.columns=['Mean','N']
        tAnnual.loc[tAnnual['N']/12*100<Threshold,'Mean']=np.nan

        #
        if len(tAnnual['Mean'].dropna()) > 0:
            Data.append([s,v,tAnnual['Mean'].mean(),tAnnual['Mean'].count()])
        else:
            tMonthly['Month']=tMonthly.index.month
            tMonthly=tMonthly.groupby('Month').mean()[['Mean']]
            if tMonthly['Mean'].count()/12*100>Threshold:
                Data.append([s,v,tMonthly['Mean'].mean(),tMonthly['Mean'].count()])
    

dfAnn=pd.pivot_table(pd.DataFrame(data=Data, columns=['Site','Variable','Annual','N']),index='Site',columns='Variable',values=['Annual','N'])
dfAnn


# ## Jabavu

# In[288]:


Campaigns=[['2021-04-21','2021-05-29'],['2021-06-27','2021-08-20']]


# In[74]:


dftmp=extractStationVars(dfRaw,Site='Jabavu')
dftmp.tail()


# In[347]:


dftmp.head()


# In[ ]:





# In[290]:


dftmp[Campaigns[0][0]:Campaigns[0][1]]


# In[291]:


plotTimeSeries(dftmp[Campaigns[0][0]:Campaigns[0][1]],title="Jabavu")


# In[292]:


plotTimeSeriesPeriod(dftmp,start=Campaigns[0][0], end=Campaigns[0][1], title="Jabavu Autumn Campaign")


# In[293]:


plotTimeSeriesPeriod(dftmp,start=Campaigns[1][0], end=Campaigns[1][1], title="Jabavu Winter Campaign")


# In[294]:


plotTimeSeries(dftmp[Campaigns[0][0]:Campaigns[0][1]],title="Jabavu Autumn Campaign")


# In[295]:


plotTimeSeries(dftmp[Campaigns[1][0]:Campaigns[1][1]],title="Jabavu Winter Campaign")


# In[305]:


plot_ppollrose(dftmp[Campaigns[0][0]:Campaigns[0][1]],CO='PM10', title="Jabavu Autumn Campaign")


# In[306]:


plot_ppollrose(dftmp[Campaigns[0][0]:Campaigns[0][1]],CO='PM2.5', title="Jabavu Autumn Campaign")


# In[307]:


plot_ppollrose(dftmp[Campaigns[1][0]:Campaigns[1][1]],CO='PM10', title="Jabavu Autumn Campaign")


# In[308]:


plot_ppollrose(dftmp[Campaigns[1][0]:Campaigns[1][1]],CO='PM2.5', title="Jabavu Autumn Campaign")


# ## Diepkloof

# In[309]:


Campaigns=[['2021-04-21','2021-05-29'],['2021-07-31','2021-08-28']]


# In[310]:


dftmp=extractStationVars(dfRaw,Site='Diepkloof')
dftmp.head()


# In[311]:


plotTimeSeriesPeriod(dftmp,start=Campaigns[0][0], end=Campaigns[0][1], title="Diepkloof Autumn Campaign")


# In[312]:


plotTimeSeriesPeriod(dftmp,start=Campaigns[1][0], end=Campaigns[1][1], title="Diepkloof Winter Campaign")


# In[313]:


plotTimeSeries(dftmp[Campaigns[0][0]:Campaigns[0][1]],title="Diepkloof Autumn Campaign")


# In[314]:


plotTimeSeries(dftmp[Campaigns[1][0]:Campaigns[1][1]],title="Diepkloof Winter Campaign")


# In[315]:


plot_ppollrose(dftmp[Campaigns[0][0]:Campaigns[0][1]],CO='PM10', title="Diepkloof Autumn Campaign")


# In[316]:


plot_ppollrose(dftmp[Campaigns[0][0]:Campaigns[0][1]],CO='PM2.5', title="Diepkloof Autumn Campaign")


# In[317]:


plot_ppollrose(dftmp[Campaigns[1][0]:Campaigns[1][1]],CO='PM10', title="Diepkloof Autumn Campaign")


# In[318]:


plot_ppollrose(dftmp[Campaigns[1][0]:Campaigns[1][1]],CO='PM2.5', title="Diepkloof Autumn Campaign")


# ## Springs

# In[319]:


Campaigns=[['2021-01-17','2021-03-03'],['2021-06-16','2021-07-28']]


# In[320]:


dftmp=extractStationVars(dfRaw,Site='Springs')
dftmp.head()


# In[321]:


plotTimeSeriesPeriod(dftmp,start=Campaigns[0][0], end=Campaigns[0][1], title="Springs Summer Campaign")


# In[322]:


plotTimeSeriesPeriod(dftmp,start=Campaigns[1][0], end=Campaigns[1][1], title="Springs Winter Campaign")


# In[324]:


#plotTimeSeries(dftmp[Campaigns[0][0]:Campaigns[0][1]],title="Springs Summer Campaign")


# In[326]:


#plotTimeSeries(dftmp[Campaigns[1][0]:Campaigns[1][1]],title="Springs Winter Campaign")


# In[327]:


#plot_ppollrose(dftmp[Campaigns[0][0]:Campaigns[0][1]],CO='PM10', title="Springs Autumn Campaign")
#plot_ppollrose(dftmp[Campaigns[0][0]:Campaigns[0][1]],CO='PM2.5', title="Springs Autumn Campaign")
#plot_ppollrose(dftmp[Campaigns[1][0]:Campaigns[1][1]],CO='PM10', title="Springs Autumn Campaign")
#plot_ppollrose(dftmp[Campaigns[1][0]:Campaigns[1][1]],CO='PM2.5', title="Springs Autumn Campaign")


# ## Olifantsfontein

# In[328]:


Campaigns=[['2021-04-21','2021-06-04'],['2021-06-16','2021-07-28']]


# In[329]:


dftmp=extractStationVars(dfRaw,Site='Olifantsfontein')
dftmp.head()


# In[330]:


plotTimeSeriesPeriod(dftmp,start=Campaigns[0][0], end=Campaigns[0][1], title="Olifantsfontein Autumn Campaign")


# In[331]:


plotTimeSeriesPeriod(dftmp,start=Campaigns[1][0], end=Campaigns[1][1], title="Olifantsfontein Winter Campaign")


# In[333]:


#plotTimeSeries(dftmp[Campaigns[0][0]:Campaigns[0][1]],title="Olifantsfontein Autumn Campaign")


# In[335]:


#plotTimeSeries(dftmp[Campaigns[1][0]:Campaigns[1][1]],title="Olifantsfontein Autumn Campaign")

