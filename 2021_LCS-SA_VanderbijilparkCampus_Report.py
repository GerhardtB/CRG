#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#LCS-SA-Project:--Vanderbijilpark,-South-Africa-2021." data-toc-modified-id="LCS-SA-Project:--Vanderbijilpark,-South-Africa-2021.-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>LCS-SA Project:  Vanderbijilpark, South Africa 2021.</a></span><ul class="toc-item"><li><span><a href="#Objectives" data-toc-modified-id="Objectives-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Objectives</a></span></li><li><span><a href="#Libraries,-Packages-and-General-Functions-" data-toc-modified-id="Libraries,-Packages-and-General-Functions--1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Libraries, Packages and General Functions <a id="librariespackagesfunctions"></a></a></span></li><li><span><a href="#Directory-pathways--" data-toc-modified-id="Directory-pathways---1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Directory pathways  <a id="directorypath"></a></a></span></li></ul></li><li><span><a href="#Import-data" data-toc-modified-id="Import-data-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Import data</a></span><ul class="toc-item"><li><span><a href="#Quality-Control-" data-toc-modified-id="Quality-Control--2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Quality Control <a id="level3combinedataframes"></a></a></span><ul class="toc-item"><li><span><a href="#Apply-report-changes-to-data" data-toc-modified-id="Apply-report-changes-to-data-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Apply report changes to data</a></span></li><li><span><a href="#Remove-Zero-and-Span-&amp;-Site-Vists" data-toc-modified-id="Remove-Zero-and-Span-&amp;-Site-Vists-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Remove Zero and Span &amp; Site Vists</a></span></li></ul></li><li><span><a href="#Reference-instruments" data-toc-modified-id="Reference-instruments-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Reference instruments</a></span><ul class="toc-item"><li><span><a href="#Overview-Timeseries" data-toc-modified-id="Overview-Timeseries-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Overview Timeseries</a></span></li><li><span><a href="#Windrose" data-toc-modified-id="Windrose-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Windrose</a></span></li><li><span><a href="#Correction" data-toc-modified-id="Correction-2.2.3"><span class="toc-item-num">2.2.3&nbsp;&nbsp;</span>Correction</a></span></li><li><span><a href="#Pollutant-Rose" data-toc-modified-id="Pollutant-Rose-2.2.4"><span class="toc-item-num">2.2.4&nbsp;&nbsp;</span>Pollutant Rose</a></span></li><li><span><a href="#Data-Availability" data-toc-modified-id="Data-Availability-2.2.5"><span class="toc-item-num">2.2.5&nbsp;&nbsp;</span>Data Availability</a></span></li><li><span><a href="#Data-Statistics" data-toc-modified-id="Data-Statistics-2.2.6"><span class="toc-item-num">2.2.6&nbsp;&nbsp;</span>Data Statistics</a></span></li></ul></li><li><span><a href="#MRC" data-toc-modified-id="MRC-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>MRC</a></span><ul class="toc-item"><li><span><a href="#DF05-&quot;05_Vaisala_S1830003_df5&quot;" data-toc-modified-id="DF05-&quot;05_Vaisala_S1830003_df5&quot;-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>DF05 "05_Vaisala_S1830003_df5"</a></span></li><li><span><a href="#TimeSeries-Plots" data-toc-modified-id="TimeSeries-Plots-2.3.2"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span>TimeSeries Plots</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.3.3"><span class="toc-item-num">2.3.3&nbsp;&nbsp;</span>Scatterplots</a></span></li><li><span><a href="#Accuracy-Metrics" data-toc-modified-id="Accuracy-Metrics-2.3.4"><span class="toc-item-num">2.3.4&nbsp;&nbsp;</span>Accuracy Metrics</a></span></li><li><span><a href="#DF06--&quot;06_S500_5002-2D82-001_df6&quot;" data-toc-modified-id="DF06--&quot;06_S500_5002-2D82-001_df6&quot;-2.3.5"><span class="toc-item-num">2.3.5&nbsp;&nbsp;</span>DF06  "06_S500_5002-2D82-001_df6"</a></span></li><li><span><a href="#TimeSeries-Plots" data-toc-modified-id="TimeSeries-Plots-2.3.6"><span class="toc-item-num">2.3.6&nbsp;&nbsp;</span>TimeSeries Plots</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.3.7"><span class="toc-item-num">2.3.7&nbsp;&nbsp;</span>Scatterplots</a></span></li><li><span><a href="#DF07-&quot;07_S500_ECM-1906191-003_df7&quot;" data-toc-modified-id="DF07-&quot;07_S500_ECM-1906191-003_df7&quot;-2.3.8"><span class="toc-item-num">2.3.8&nbsp;&nbsp;</span>DF07 "07_S500_ECM-1906191-003_df7"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.3.9"><span class="toc-item-num">2.3.9&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplot" data-toc-modified-id="Scatterplot-2.3.10"><span class="toc-item-num">2.3.10&nbsp;&nbsp;</span>Scatterplot</a></span></li></ul></li><li><span><a href="#eroAfrica" data-toc-modified-id="eroAfrica-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>eroAfrica</a></span><ul class="toc-item"><li><span><a href="#DF08-&quot;08_PolludroneSmart_EA01P0001_df8&quot;" data-toc-modified-id="DF08-&quot;08_PolludroneSmart_EA01P0001_df8&quot;-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>DF08 "08_PolludroneSmart_EA01P0001_df8"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.4.2"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplot" data-toc-modified-id="Scatterplot-2.4.3"><span class="toc-item-num">2.4.3&nbsp;&nbsp;</span>Scatterplot</a></span></li><li><span><a href="#DF17-&quot;17_GM-5000_CM21035290_df17&quot;" data-toc-modified-id="DF17-&quot;17_GM-5000_CM21035290_df17&quot;-2.4.4"><span class="toc-item-num">2.4.4&nbsp;&nbsp;</span>DF17 "17_GM-5000_CM21035290_df17"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.4.5"><span class="toc-item-num">2.4.5&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplot" data-toc-modified-id="Scatterplot-2.4.6"><span class="toc-item-num">2.4.6&nbsp;&nbsp;</span>Scatterplot</a></span></li><li><span><a href="#DF27-&quot;27_PolludroneSmart_PM01P0007_df27&quot;" data-toc-modified-id="DF27-&quot;27_PolludroneSmart_PM01P0007_df27&quot;-2.4.7"><span class="toc-item-num">2.4.7&nbsp;&nbsp;</span>DF27 "27_PolludroneSmart_PM01P0007_df27"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.4.8"><span class="toc-item-num">2.4.8&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.4.9"><span class="toc-item-num">2.4.9&nbsp;&nbsp;</span>Scatterplots</a></span></li></ul></li><li><span><a href="#Simplicity" data-toc-modified-id="Simplicity-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Simplicity</a></span><ul class="toc-item"><li><span><a href="#&quot;09_SimplicityV1_CCSENV011_df9&quot;" data-toc-modified-id="&quot;09_SimplicityV1_CCSENV011_df9&quot;-2.5.1"><span class="toc-item-num">2.5.1&nbsp;&nbsp;</span>"09_SimplicityV1_CCSENV011_df9"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.5.2"><span class="toc-item-num">2.5.2&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.5.3"><span class="toc-item-num">2.5.3&nbsp;&nbsp;</span>Scatterplots</a></span></li><li><span><a href="#&quot;10_SimplicityV1_CCSENV020_df10&quot;" data-toc-modified-id="&quot;10_SimplicityV1_CCSENV020_df10&quot;-2.5.4"><span class="toc-item-num">2.5.4&nbsp;&nbsp;</span>"10_SimplicityV1_CCSENV020_df10"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.5.5"><span class="toc-item-num">2.5.5&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.5.6"><span class="toc-item-num">2.5.6&nbsp;&nbsp;</span>Scatterplots</a></span></li><li><span><a href="#&quot;11_SimplicityV2_IMTAQS0001_df11&quot;" data-toc-modified-id="&quot;11_SimplicityV2_IMTAQS0001_df11&quot;-2.5.7"><span class="toc-item-num">2.5.7&nbsp;&nbsp;</span>"11_SimplicityV2_IMTAQS0001_df11"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.5.8"><span class="toc-item-num">2.5.8&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.5.9"><span class="toc-item-num">2.5.9&nbsp;&nbsp;</span>Scatterplots</a></span></li><li><span><a href="#&quot;12_SimplicityV2_IMTAQS0002_df12&quot;" data-toc-modified-id="&quot;12_SimplicityV2_IMTAQS0002_df12&quot;-2.5.10"><span class="toc-item-num">2.5.10&nbsp;&nbsp;</span>"12_SimplicityV2_IMTAQS0002_df12"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.5.11"><span class="toc-item-num">2.5.11&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.5.12"><span class="toc-item-num">2.5.12&nbsp;&nbsp;</span>Scatterplots</a></span></li><li><span><a href="#&quot;13_SimplicityV2_IMTAQS0003_df13&quot;" data-toc-modified-id="&quot;13_SimplicityV2_IMTAQS0003_df13&quot;-2.5.13"><span class="toc-item-num">2.5.13&nbsp;&nbsp;</span>"13_SimplicityV2_IMTAQS0003_df13"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.5.14"><span class="toc-item-num">2.5.14&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.5.15"><span class="toc-item-num">2.5.15&nbsp;&nbsp;</span>Scatterplots</a></span></li><li><span><a href="#&quot;14_SimplicityV2_IMTAQS0004_df14&quot;" data-toc-modified-id="&quot;14_SimplicityV2_IMTAQS0004_df14&quot;-2.5.16"><span class="toc-item-num">2.5.16&nbsp;&nbsp;</span>"14_SimplicityV2_IMTAQS0004_df14"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.5.17"><span class="toc-item-num">2.5.17&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.5.18"><span class="toc-item-num">2.5.18&nbsp;&nbsp;</span>Scatterplots</a></span></li></ul></li><li><span><a href="#Envirocon" data-toc-modified-id="Envirocon-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Envirocon</a></span><ul class="toc-item"><li><span><a href="#DF15-&quot;15_ICOMSMART_20149_df15&quot;" data-toc-modified-id="DF15-&quot;15_ICOMSMART_20149_df15&quot;-2.6.1"><span class="toc-item-num">2.6.1&nbsp;&nbsp;</span>DF15 "15_ICOMSMART_20149_df15"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.6.2"><span class="toc-item-num">2.6.2&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.6.3"><span class="toc-item-num">2.6.3&nbsp;&nbsp;</span>Scatterplots</a></span></li></ul></li><li><span><a href="#Sensors.Africa" data-toc-modified-id="Sensors.Africa-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Sensors.Africa</a></span><ul class="toc-item"><li><span><a href="#DF18-&quot;18_Plantower_108_df18&quot;" data-toc-modified-id="DF18-&quot;18_Plantower_108_df18&quot;-2.7.1"><span class="toc-item-num">2.7.1&nbsp;&nbsp;</span>DF18 "18_Plantower_108_df18"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.7.2"><span class="toc-item-num">2.7.2&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.7.3"><span class="toc-item-num">2.7.3&nbsp;&nbsp;</span>Scatterplots</a></span></li></ul></li><li><span><a href="#University-of-L" data-toc-modified-id="University-of-L-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>University of L</a></span><ul class="toc-item"><li><span><a href="#DF20-&quot;20_Zephyr_642-SA_df20&quot;" data-toc-modified-id="DF20-&quot;20_Zephyr_642-SA_df20&quot;-2.8.1"><span class="toc-item-num">2.8.1&nbsp;&nbsp;</span>DF20 "20_Zephyr_642-SA_df20"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.8.2"><span class="toc-item-num">2.8.2&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.8.3"><span class="toc-item-num">2.8.3&nbsp;&nbsp;</span>Scatterplots</a></span></li><li><span><a href="#DF21-&quot;21_Zephyr_729-SA_df21&quot;" data-toc-modified-id="DF21-&quot;21_Zephyr_729-SA_df21&quot;-2.8.4"><span class="toc-item-num">2.8.4&nbsp;&nbsp;</span>DF21 "21_Zephyr_729-SA_df21"</a></span></li><li><span><a href="#Timeseries" data-toc-modified-id="Timeseries-2.8.5"><span class="toc-item-num">2.8.5&nbsp;&nbsp;</span>Timeseries</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.8.6"><span class="toc-item-num">2.8.6&nbsp;&nbsp;</span>Scatterplots</a></span></li></ul></li><li><span><a href="#Skyside" data-toc-modified-id="Skyside-2.9"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>Skyside</a></span><ul class="toc-item"><li><span><a href="#DF22-&quot;22_Atmos_84CCA8B167D2_df22&quot;" data-toc-modified-id="DF22-&quot;22_Atmos_84CCA8B167D2_df22&quot;-2.9.1"><span class="toc-item-num">2.9.1&nbsp;&nbsp;</span>DF22 "22_Atmos_84CCA8B167D2_df22"</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.9.2"><span class="toc-item-num">2.9.2&nbsp;&nbsp;</span>Scatterplots</a></span></li><li><span><a href="#DF23-&quot;23_Atmos_98F4ABDCA328_df23&quot;" data-toc-modified-id="DF23-&quot;23_Atmos_98F4ABDCA328_df23&quot;-2.9.3"><span class="toc-item-num">2.9.3&nbsp;&nbsp;</span>DF23 "23_Atmos_98F4ABDCA328_df23"</a></span></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.9.4"><span class="toc-item-num">2.9.4&nbsp;&nbsp;</span>Scatterplots</a></span></li></ul></li><li><span><a href="#Sedulitas" data-toc-modified-id="Sedulitas-2.10"><span class="toc-item-num">2.10&nbsp;&nbsp;</span>Sedulitas</a></span><ul class="toc-item"><li><span><a href="#DF26-26_Zephyr_533_df26" data-toc-modified-id="DF26-26_Zephyr_533_df26-2.10.1"><span class="toc-item-num">2.10.1&nbsp;&nbsp;</span>DF26 26_Zephyr_533_df26</a></span></li></ul></li><li><span><a href="#Scatterplots" data-toc-modified-id="Scatterplots-2.11"><span class="toc-item-num">2.11&nbsp;&nbsp;</span>Scatterplots</a></span></li><li><span><a href="#AfriqAir" data-toc-modified-id="AfriqAir-2.12"><span class="toc-item-num">2.12&nbsp;&nbsp;</span>AfriqAir</a></span></li><li><span><a href="#Data-analysis--" data-toc-modified-id="Data-analysis---2.13"><span class="toc-item-num">2.13&nbsp;&nbsp;</span>Data analysis  <a id="dataanalysis"></a></a></span><ul class="toc-item"><li><span><a href="#Diurnal-plots" data-toc-modified-id="Diurnal-plots-2.13.1"><span class="toc-item-num">2.13.1&nbsp;&nbsp;</span>Diurnal plots</a></span></li><li><span><a href="#Data-recovery" data-toc-modified-id="Data-recovery-2.13.2"><span class="toc-item-num">2.13.2&nbsp;&nbsp;</span>Data recovery</a></span></li><li><span><a href="#Factors" data-toc-modified-id="Factors-2.13.3"><span class="toc-item-num">2.13.3&nbsp;&nbsp;</span>Factors</a></span></li><li><span><a href="#Reference-air-quality" data-toc-modified-id="Reference-air-quality-2.13.4"><span class="toc-item-num">2.13.4&nbsp;&nbsp;</span>Reference air quality</a></span></li><li><span><a href="#Bivariate-plots" data-toc-modified-id="Bivariate-plots-2.13.5"><span class="toc-item-num">2.13.5&nbsp;&nbsp;</span>Bivariate plots</a></span></li></ul></li></ul></li></ul></div>

# # LCS-SA Project:  Vanderbijilpark, South Africa 2021.

# ## Objectives
# 
# __Aim:__
# 1. Environmental health in sub-Saharan-Africa - leveraging local and global air pollution data for epidemiological research (LEAP-Epi)
# 
# __Objectives:__
# 1. Determine the precision, accuracy, reliability, rigidity and usability within a South African setting.
# 2. Provide information which could be used to improve the low- and medium-cost sensors.
# 
# __Specific research questions:__
# 1. XXX
# 2. XXX

# ## Libraries, Packages and General Functions <a id="librariespackagesfunctions"></a>
# [Back to the top](#TOP)

# In[1695]:


# Import the necessary packages.

#
import glob

#
from datetime import datetime
import pytz

# The matplotlip library is used to visualize data.
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.style
import matplotlib.dates as mdates
import matplotlib.cm as cm
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
# Numpy is the numerical library. It is used by many of the ones before, but we import it for in case.
import numpy as np
from numpy.polynomial.polynomial import polyfit
# From Numpy we also import the nan 'missing-value' object that we use alot.
from numpy import nan

# The os library is used to list and access files and directories on the hard drive.
import os

# Used to manipulate data.
import pandas as pd

# Used to plot data.
import seaborn as sns
sns.set_theme(style="darkgrid")

# The pathlib library is used to manage access to disk. It helps us to keep things the same between Windows and Linux.
from pathlib import Path

# Used for statistical analysis such as boxplots and histograms.
from scipy import interpolate
from scipy.stats import linregress

# Used to create windroses or pollution plots.
from windrose import WindroseAxes

# For fancy matching of strings, we use re.
import re

# String libary for temporary file import.
from io import StringIO

#
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# Create tooltips for interactive plots.
import mpld3

# For connecting to google sheet.
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import ipywidgets as widgets
from ipywidgets import interact, interact_manual


# In[1696]:


timezonesa = pytz.timezone("Africa/Johannesburg")
timezoneutc = pytz.timezone("UTC")


# In[1697]:


# Configure the connection 
scope = ['https://spreadsheets.google.com/feeds']

# Give the path to the Service Account Credential json file 
# 1. Go to Google Development Console (https://console.developers.google.com/project)
# 2. Create new project
# 3. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
# 4. Fill out the form
# 5. Click “Create key”
# 6. Select “JSON” and click “Create”

credentials = ServiceAccountCredentials.from_json_keyfile_name('key/crgprojects-b66f872bd816.json',
                                                               scope)
# Authorise your Notebook
gc = gspread.authorize(credentials)

# The sprad sheet ID, which can be taken from the link to the sheet
#https://docs.google.com/spreadsheets/d/1Fe1P2QEiCjl7KK6YEckzGLC_VqOuGtaChaDGbn2SOhE/edit?usp=sharing
#spreadsheet_key = '1pwJDzIl1O8gQSHD8SekW6442rrLRgLVTYA90dQb7chg'
spreadsheet_key = '1Fe1P2QEiCjl7KK6YEckzGLC_VqOuGtaChaDGbn2SOhE'

#Opening the worksheet by using Worksheet ID
def readSheet():
    workbook = gc.open_by_key(spreadsheet_key)#Selecting which sheet to pulling the data
    reports = workbook.worksheet('LCS-QC')#Pulling the data and transform it to the data frame
    values = reports.get_all_values()
    Reports = pd.DataFrame(values[1:], columns=values[0])
    #Reports=Reports[Reports['What is the site']=='Northam AQMS']
    return(reports,Reports)
reports, Reports = readSheet()


# In[1698]:


# This 'widget' is used to give us interactive graph capabilities in the matplotlib figures.
get_ipython().run_line_magic('matplotlib', 'widget')


# In[1699]:


# Handle date time conversions between pandas and matplotlib.
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# In[1700]:


#
def head(filename,N=10):
    n=0
    with open(Path(filename)) as fp:
        for l in fp.readlines():
            if n<N:
                print(l,end="")
                n=n+1


# In[1701]:


#
def tail(filename,N=10):
    n=0
    with open(Path(filename)) as fp:
        lines=[i for i in fp.readlines()]
        Nlines=len(lines)
        for l in lines[Nlines-N:]:
            if n<N:
                print(l,end="")
                n=n+1


# In[1702]:


#
def ConvertNumeric(df,var):
    df[var]= pd.to_numeric(df[var],errors='coerce')


# In[1703]:


#
def testLogger(filename):
    Sep=","
    Data=[]
    with open(filename) as fp:
        for line in fp.readlines():
            row=line.split(Sep)
            Data.append(len(row))
    print(pd.DataFrame({"Columns":Data}).describe())


# In[1704]:


#
def ncolumnsLogger(filename):
    Sep=","
    Data=[]
    with open(filename) as fp:
        for line in fp.readlines():
            row=line.split(Sep)
            Data.append(len(row))
    return(np.median(np.array(Data)))


# In[1705]:


#
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


# In[1706]:


#
def readRM(filename, nLines=18):
    DataString=""
    Sep=","
    with open(filename) as fp:
        for line in fp.readlines():
            row=line.split(Sep)
            if len(row) == nLines and re.match('\W*(\d{4})[/.-](\d{2})[/.-](\d{2})\s{1}(\d{2}):(\d{2}):(\d{2})\W*',row[0]):
                DataString=DataString+line
    return(DataString)


# In[1707]:


# List all the files in the specified directory containing the given extention.
def lsR(dir,pattern=".csv",prefix="",postfix=""):
    list=[]
    for path,dirs,files in os.walk(Path(dir)):
        for f in files:
            if f.count(pattern) > 0 and f.startswith(prefix) and f.endswith(postfix):
                list.append(os.path.join(path,f))
    return(list)


# In[1708]:


#
def clearplots():
    plt.clf()


# In[1709]:


def instruments(nr):
    for i in df.columns:
        if i.startswith('{}'.format(nr)):
            print("'{}',".format(i))


# In[ ]:





# ## Directory pathways  <a id="directorypath"></a>
# [Back to the top](#TOP)

# In[1710]:


# Set the main DropBox directory.
DropboxDir=Path("/home/roelof/Dropbox (NWU)")


# In[1711]:


# Set the main data directory pathway. This is where the main data files are stored.
DataDir=Path(DropboxDir / "CRG_Projects/01_Research_Campaigns/2021_Low-CostSensorSouthAfrica/01_FieldCampaigns")


# In[1712]:


# Set a pathway for where the figures/images will be saved.
FigDir=Path(DropboxDir / "CRG_Projects/01_Research_Campaigns/2021_Low-CostSensorSouthAfrica/03_DataAnalysisOutputs/Figures")


# In[1713]:


# Set a pathway for where the tables/data files will be saved.
TabDir=Path(DropboxDir / "CRG_Projects/01_Research_Campaigns/2021_Low-CostSensorSouthAfrica/03_DataAnalysisOutputs/Tables")


# In[1714]:


QCQA = Path(DropboxDir/'CRG_Projects/01_Research_Campaigns/2021_Low-CostSensorSouthAfrica/03_DataAnalysisOutputs/QCQA_DATA')


# In[1715]:


QCQA


# # Import data

# In[1718]:


InstrumentNames=["00_Reference_SAWS_df0",
                 "01_ES642_U16486_df1",
                "02_ES642_U16489_df2",
                "03_ARISense_SN000-57_df3",
                "04_ARISense_SN000-59_df4",
                "05_Vaisala_S1830003_df5",
                "06_S500_5002-2D82-001_df6",
                "07_S500_ECM-1906191-003_df7",
                "08_PolludroneSmart_EA01P0001_df8",
                "09_SimplicityV1_CCSENV011_df9",
                "10_SimplicityV1_CCSENV020_df10",
                "11_SimplicityV2_IMTAQS0001_df11",
                "12_SimplicityV2_IMTAQS0002_df12",
                "13_SimplicityV2_IMTAQS0003_df13",
                "14_SimplicityV2_IMTAQS0004_df14",
                "15_ICOMSMART_20149_df15",
                 "16_RAMP_173_df16",
                "17_GM-5000_CM21035290_df17",
                "18_Plantower_xxx_df18",
                "19_Plantower_xxx_df19",
                "20_Zephyr_642-SA_df20",
                "21_Zephyr_729-SA_df21",
                "22_Atmos_84CCA8B167D2_df22",
                "23_Atmos_98F4ABDCA328_df23",
                #"24_Dylos_xxx_df24",
                #"25_RAMP_xxx_df25",
                '26_Zephyr_533_df26' 
                "27_PolludroneSmart_PM01P0007_df27",
                "28_RAMP_177_df28"]


# In[1719]:


df=pd.DataFrame()
Files = [f for f in sorted(os.listdir(TabDir)) if f.startswith("df") and 'level1' not in f]

for f in Files:
    print(f)
    dftmp=pd.read_csv(TabDir/f, parse_dates=[0], index_col=0 )
    dftmp=dftmp.resample('10min').mean()
    df = pd.concat([df,dftmp], axis=1)
    
df=df.loc['2021-04-26':'2021-10-29']


# ## Quality Control <a id="level3combinedataframes"></a>
# [Back to the top](#TOP)
# 
# 1. Vaisala, Aeroqual (PM),  Aeroqual (CO) - MRC
# 2. Polludrone Smart (1), Polludrone Smart (2), GM-5000- eroAfrica
# 3. Simplicity V1 (1), Simplicity V1 (2), Simplicity V2 (1), Simplicity V2(2), Simplicity V2 (3), Simplicity V2 (4)    - Simplicity
# 4. ECOMSMART - Envirocon
# 5. Planttower (1),Planttower (2) - Sensors.Africa
# 6. Zephyr (1), Zephyr (2) - UL 
# 7. Atmos (1), Atmos (2) - SkySide
# 8. Zypher (3) - Sedulitas
# 9. RAMP (1), RAMP (2) - AfriqAir
# 

# In[1720]:


sorted(os.listdir(QCQA))


# ### Apply report changes to data
# 

# https://docs.google.com/spreadsheets/d/1Fe1P2QEiCjl7KK6YEckzGLC_VqOuGtaChaDGbn2SOhE/edit?usp=sharing

# In[1721]:


# Update google sheet
reports, Reports = readSheet()

Units={"Ambient_Relative_Humidity":"(%)",
    "Humidity":"(%)",
    "Internal_Battery":"(%)",
    "Internal_Relative_Humidity":"(%)",
    "Relative_Humidity":"(%)",
    "Internal_Temp":"(C)",
    "Noise":"(dB)",
    "Wind_Direction":"(deg)",
    "Ambient_Temperature":"(degC)",
    "Internal_Temperature":"(degC)",
    "Sensor_Temperature":"(degC)",
    "Temperature":"(degC)",
    "Wind_Direction":"(degrees)",
    "Winds_Speed":"(degrees)",
    "Atmospheric_Pressure":"(hPa)",
    "Pressure":"(hPa)",
    "Flow":"(l/m)",
    "CO":"(mg/m3)",
    "Rain":"(mm)",
    "Wind_Direction":"(m/s)",
    "Wind_Speed":"(m/s)",
    "H2S":"(ppb)",
    "NO2":"(ppb)",
    "NO":"(ppb)",
    "NOx":"(ppb)",
    "O3":"(ppb)",
    "SO2":"(ppb)",
    "TVOC":"(ppb)",
    "CO2":"(ppm)",
    "CO":"(ppm)",
    "eCO2":"(ppm)",
    "H2S":"(ug/m3)",
    "NO2":"(ug/m3)",
    "NO":"(ug/m3)",
    "O3":"(ug/m3)",
    "PM10":"(ug/m3)",
    "PM1":"(ug/m3)",
    "PM2.5":"(ug/m3)",
    "SO2":"(ug/m3)",
    "Line_Voltage":"(V)",
    "Solar_Radiation":"(W/m2)"
}

for index,row in Reports.iterrows():
    ins='What is the instrument?'
    var='Which instrument variable failed?'
    sdate='When did the instrument start failing?'
    stime='What time did the instrument start to fail?'
    edate='When was the instrument failure fixed?'
    etime='What time was the instrument failure fixed?'
    
    S=pd.to_datetime("{} {}".format(row[sdate],row[stime])).tz_localize('Africa/Johannesburg')
    E=pd.to_datetime("{} {}".format(row[edate],row[etime])).tz_localize('Africa/Johannesburg')

    v="{:02.0f}_{}".format(int(row[ins].replace("df","")),row[var])
    
    if v in df.columns:
        print("Correcting ",v)
        df.loc[(df.index >= S)&(df.index <= E), v] = nan   
    elif 'All' in v:
        print("Correcting ",v)
        x = [i for i in df.columns if i.startswith('{}'.format(v[:2]))]
        df.loc[(df.index >= S)&(df.index <= E), x] = nan
    else:
        print("{} not in dataset".format(v))


# ### Remove Zero and Span & Site Vists

# In[1722]:


sitev = ['4/26/2021','5/3/2021','5/6/2021','5/6/2021','5/10/2021',
        '5/17/2021',
        '5/21/2021',
        '5/25/2021',
        '5/30/2021',
        '6/15/2021',
        '6/21/2021',
         '7/2/2021',
        '7/5/2021',
        '7/19/2021',
        '7/23/2021',
        '7/26/2021',
        '8/2/2021',
        '8/2/2021',
        '8/10/2021',
        '8/16/2021',
        '8/16/2021',
        '8/23/2021',
        '8/26/2021',
        '8/31/2021',
         '9/6/2021',
        '9/9/2021',
        '9/13/2021',
        '9/20/2021',
        '9/23/2021',
        '10/29/2021',
        '4/26/2021',
        '5/3/2021',
        '5/6/2021',
        '5/6/2021',
        '5/10/2021',
        '5/17/2021',
        '5/21/2021',
        '5/25/2021',
        '5/30/2021',
        '6/15/2021',
        '6/21/2021',
        '7/2/2021',
        '7/5/2021',
        '7/19/2021',
        '7/23/2021',
        '7/26/2021',
        '8/2/2021',
        '8/2/2021',
        '8/10/2021',
        '8/16/2021',
        '8/16/2021',
        '8/23/2021',
        '8/26/2021',
        '8/31/2021',
        '9/6/2021',
        '9/9/2021',
        '9/13/2021',
        '9/20/2021',
        '9/23/2021',
        '10/5/2021',
        '10/11/2021',
        '10/29/2021']

sitev = pd.to_datetime(sitev, format='%m/%d/%Y')

sitev = sitev.strftime('%Y-%m-%d')
sitev = sitev.tolist()


# In[1723]:


df[sitev] = nan


# **Save Dataset**

# In[1726]:


#df.to_csv(Path(TabDir / 'LCS2022_level1.csv'))


# In[1727]:


TabDir


# ## Reference instruments

# In[825]:


reference = ['00_Wind_Speed (m/s)',
'00_Wind_Direction (deg)',
'00_Ambient_Temp (degC)',
'00_Relative_Humidity (%)',
'00_Solar_Radiation (W/m2)',
'00_Atmospheric_Pressure (hPa)',
'00_Internal_Temp (degC)',
'00_Line_Voltage (V)',
'00_Rain (mm)',
'00_SO2 (ppb)',
'00_PM10 (ug/m3)',
'00_PM2.5 (ug/m3)',
'00_NO (ppb)',
'00_NO2 (ppb)',
'00_NOx (ppb)',
'00_O3 (ppb)',
'00_CO (ppm)',
'00_Horiba_SO2 (ppb)']


# In[826]:


df[reference].columns


# In[1133]:


PVars = ['00_SO2 (ppb)', '00_PM10 (ug/m3)', '00_PM2.5 (ug/m3)', '00_NO (ppb)',
       '00_NO2 (ppb)', '00_NOx (ppb)', '00_O3 (ppb)', '00_CO (ppm)',
       '00_Horiba_SO2 (ppb)']


# ### Overview Timeseries

# In[1540]:



#Create figure

fig, axs = plt.subplots(2,2, figsize=(10,10))

VarNames = ['00_PM10 (ug/m3)','00_PM2.5 (ug/m3)','00_Ambient_Temp (degC)','00_Wind_Speed (m/s)']

#Ad axis

axs[0,0].plot(df.resample('1H').mean().index.values, df[['00_PM10 (ug/m3)']].resample('1H').mean(),df[['00_PM2.5 (ug/m3)']].resample('1H').mean())
axs[0, 0].set(title='1-Hour Averaged PM (ug/m3)')
axs[0,0].set_ylabel('PM (ug/m3)', fontsize=12, labelpad=10)

axs[1,0].plot(df.resample('1H').mean().index.values, df[['00_Ambient_Temp (degC)']].resample('1H').mean(), color='0.3')
axs[1, 0].set(title='1-Hour Averaged Ambient Temperature (degC)')
axs[1,0].set_xlabel('Date', fontsize=12, labelpad=10)
axs[1,0].set_ylabel('Ambient Temperature (degC)', fontsize=12, labelpad=10)


dftmp =  df[VarNames].resample('1H').mean()
dftmp['Time'] = dftmp.index.map(lambda x: x.strftime("%H:00"))
diurnal = dftmp[['Time']+VarNames].groupby('Time').describe()[VarNames]

axs[0,1].plot(diurnal.index, diurnal['00_PM10 (ug/m3)']['50%'].values,diurnal['00_PM2.5 (ug/m3)']['50%'].values, linewidth=2.0, alpha=0.5)
axs[0, 1].set(title='1-Hour Averaged Diurnal PM (ug/m3)')
axs[0,1].set_xlim(0, 23)
axs[0,1].set_xticks([i for i in range(0,24,3)])


axs[1,1].plot(diurnal.index, diurnal['00_Ambient_Temp (degC)']['50%'].values, linewidth=2.0, alpha=0.5, color='0.3')
axs[1,1].plot(diurnal.index, diurnal['00_Ambient_Temp (degC)']['75%'], color='0.3')
axs[1,1].plot(diurnal.index, diurnal['00_Ambient_Temp (degC)']['25%'], color='0.3')
axs[1,1].fill_between(diurnal.index, diurnal['00_Ambient_Temp (degC)']['50%'], diurnal['00_Ambient_Temp (degC)']['75%'], alpha=.25, facecolor='0.3')
axs[1,1].fill_between(diurnal.index, diurnal['00_Ambient_Temp (degC)']['50%'], diurnal['00_Ambient_Temp (degC)']['25%'], alpha=.25, facecolor='0.3')
axs[1,1].set_xlim(0, 23)
axs[1,1].set_xticks([i for i in range(0,24,3)])
axs[1, 1].set(title='1-Hour Averaged Diurnal Ambient Temperature (degC)')
axs[1,1].set_xlabel('Time', fontsize=12, labelpad=10)




line_labels = ['PM10 (ug/m3)','PM2.5 (ug/m3)'] 
fig.legend(labels=line_labels, 
           borderaxespad=0.1,
           bbox_to_anchor=(0.99, 0.95))

fig.subplots_adjust(hspace=0.3)

fig.autofmt_xdate()
plt.tight_layout()

plt.savefig(Path(QCQA/'Overview_TimeSeries_Diurnal_1HR.png'), dpi=300)


# In[1535]:


QCQA


# In[1539]:


sorted(os.listdir(QCQA))


# ### Windrose

# In[1536]:


# Define the settings for the windrose that is being created.
def plot_windrose(dfc,WD="00_Wind_Direction (deg)",WS="00_Wind_Speed (m/s)"):                                                                                                                                                                                                                                                   
    
    # THe following two lines rounds the edges of the windrose bars to follow the bend in the circles, otherwise it is just a straight line.
    #plt.hist([0, 1])
    #plt.close()
    ax = WindroseAxes.from_ax()

    ax.bar(direction=dfc[WD], 
           var=dfc[WS],
           bins=np.arange(0, 8, 1), 
           normed=True, opening=0.95, 
           edgecolor='white', 
           cmap=cm.viridis, linewidth=0.5)
    ax.set_xticklabels(['N','NE','E','SE','S','SW','W','NW'])
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    #ax.set_yticks(np.arange(0, 60, step=5))
    #ax.set_yticklabels(np.arange(0, 60, step=5))
    
    ax.set_legend()
    ##ax.legend(loc='center left', numpoints=2, markerscale=0.5, markerfirst=True, 
    #          scatterpoints=None, scatteryoffsets=None, prop=None, fontsize=12.0, 
    #          borderpad=0.5, labelspacing=0.5, handlelength=2.0, handleheight=0.5, 
    #          handletextpad=1.0, borderaxespad=1.0, columnspacing=1.0, ncol=1, mode=None, 
    #          fancybox=True, shadow=True, title='Wind Speed (m/s)', title_fontsize=12.0, 
    #          framealpha=0.95, edgecolor='inherit', facecolor='inherit', 
    #          bbox_to_anchor=(1.1,0.5), bbox_transform=None, frameon=None, handler_map=None)
    
plot_windrose(df)
plt.savefig(Path(QCQA/'LCS_Overview_Windrose.png'), dpi=300)


# ### Correction

# **Box Plots of Correction Factor**

# In[1691]:


dfc = pd.DataFrame()

Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '18',
             '20',
             '21',
             '22',
             '23',
             '26',
             '27']

for i in Instruments:
    dftmp = pd.DataFrame()
    for var in Vars:
        refvar='00_{}'.format(var)
        varname='{}_{}'.format(i,var)
        if varname in df.columns:
            x = df[refvar].resample('10min').mean().dropna(how='any')
            y = df[varname].resample('10min').mean().dropna(how='any')
            dftmp[varname] = x.div(y)
        else:
            dftmp[varname] = nan
    dfc = pd.concat([dfc, dftmp], axis=0)


# In[1692]:


dfc1 = dfc[[i for i in dfc.columns if 'PM10' in i]].dropna()


# In[1685]:


fig = plt.figure(figsize =(10, 7))
 
# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])
 
# Creating plot
bp = ax.boxplot(dfc1)
 
# show plot
plt.show()


# **Correction Factor all variables**

# In[1541]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '18',
             '20',
             '21',
             '22',
             '23',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        refvar='00_{}'.format(var)
        varname='{}_{}'.format(i,var)
        if varname in df.columns:            
            x = df[refvar].resample('10min').mean().dropna(how='any')
            y = df[varname].resample('10min').mean().dropna(how='any')
            if len(x) > 10:
                CF = x.div(y).mean()
                mn = x.div(y).min()
                mx = x.div(y).max()
                md = x.div(y).median()
                inst.append("{:.2f},{:.2f},{:.2f},{:.2f}".format(CF, mn, mx, md))
            else:
                inst.append("")
        else:
            inst.append("")
    Table[i]=inst

dfCF=pd.DataFrame(data=Table).transpose()
dfCF.columns=Vars
dfCF


# In[1542]:


dfCF.to_csv(Path(QCQA/ 'Table_CF_Min_Max_Med_10Min.csv'),float_format='%.2f')


# **Hourly Correction Factor**

# In[1543]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '18',
             '20',
             '21',
             '22',
             '23',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        refvar='00_{}'.format(var)
        varname='{}_{}'.format(i,var)
        if varname in df.columns:            
            x = df[refvar].resample('1H').mean().dropna(how='any')
            y = df[varname].resample('1H').mean().dropna(how='any')
            if len(x) > 10:
                CF = x.div(y).mean()
                mn = x.div(y).min()
                mx = x.div(y).max()
                md = x.div(y).median()
                inst.append("{:.2f},{:.2f},{:.2f},{:.2f}".format(CF, mn, mx, md))
            else:
                inst.append("")
        else:
            inst.append("")
    Table[i]=inst

dfCFH=pd.DataFrame(data=Table).transpose()
dfCFH.columns=Vars
dfCFH


# In[1544]:


dfCFH.to_csv(Path(QCQA/ 'Table_CF_Min_Max_Med_1H.csv'),float_format='%.2f')


# ### Pollutant Rose

# In[1545]:


# Define the settings for the windrose that is being created.
def plot_ppollrose(dfc,WD="00_Wind_Direction (deg)",WS="00_Wind_Speed (m/s)",CO="PM10",title="",output=Path("polar.png")):                                                                                                                                                                                                                                                   
    dfc=dfc[[WD,WS,CO]].dropna()
    wd_rad = np.radians(np.array(dfc[WD]))
    Conc = np.array(dfc[CO], dtype=float)
    WSmax = max(dfc[WS])
    WD1, WS1 = np.meshgrid(np.linspace(0, 2*np.pi, 360), np.linspace(min(dfc[WS]), max(dfc[WS]), 16))
    Z = interpolate.griddata((wd_rad, dfc[WS]), dfc[CO], (WD1, WS1), method='linear')

    levels = MaxNLocator(nbins=10).tick_values(0, 500)
    
    cmap = plt.get_cmap('viridis')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    
    fig, ax = plt.subplots(figsize=(10,10), subplot_kw={"projection": "polar"})
    
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


# In[1555]:


#plot_ppollrose(df, CO='00_PM10 (ug/m3)')


# ### Data Availability

# In[1582]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['00',
             '01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '18',
             '20',
             '21',
             '22',
             '23',
             '24',
             '25',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        varname='{}_{}'.format(i,var)
        if varname in df.columns:
            inst.append("{:.1f}".format(len(df[varname].dropna())/len(df[varname])*100))
            #print(varname,"{:.1f}".format(len(df[varname].dropna())/len(df[varname])*100))
        else:
            inst.append("")
    Table[i]=inst
    
dfDR=pd.DataFrame(data=Table).transpose()
dfDR.columns=Vars
dfDR


# In[1583]:


dfDR.to_csv(Path(QCQA/ 'DataAvailability_20210426_20211029.csv'),float_format='%.1f')


# **Data Recovery per deployment date**

# In[1584]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['00',
             '01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '18',
             '20',
             '21',
             '22',
             '23',
             '24',
             '25',
             '26',
             '27']

#Installed on 2021-04-01

one = ['00',
             '01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14']

#Installed on 2021-04-08

two = ['18, 22, 23']

#Installed on 2021-04-21

three = ['20','21']


#Installed on 2021-05-03
four = ['07']

#Installed on 2021-05-10

five = ['15']

#Installed on 2021-06-15

six = ['24','26']



Table={}

for i in Instruments:
    inst=[]
    if i in one:
        for var in Vars:
            varname='{}_{}'.format(i,var)
            dftmp = df.loc['2021-04-01':]
            if varname in dftmp.columns:
                inst.append("{:.1f}".format(len(dftmp[varname].dropna())/len(dftmp[varname])*100))
            else:
                inst.append("")
    elif i in two:
        for var in Vars:
            varname='{}_{}'.format(i,var)
            dftmp = df.loc['2021-04-08':]
            if varname in dftmp.columns:
                inst.append("{:.1f}".format(len(dftmp[varname].dropna())/len(dftmp[varname])*100))
            else:
                inst.append("")
    elif i in three:
        for var in Vars:
            varname='{}_{}'.format(i,var)
            dftmp = df.loc['2021-04-21':]
            if varname in dftmp.columns:
                inst.append("{:.1f}".format(len(dftmp[varname].dropna())/len(dftmp[varname])*100))
            else:
                inst.append("")
    elif i in four:
        for var in Vars:
            varname='{}_{}'.format(i,var)
            dftmp = df.loc['2021-05-10':]
            if varname in dftmp.columns:
                inst.append("{:.1f}".format(len(dftmp[varname].dropna())/len(dftmp[varname])*100))
            else:
                inst.append("")
    elif i in five:
        for var in Vars:
            varname='{}_{}'.format(i,var)
            dftmp = df.loc['2021-05-15':]
            if varname in dftmp.columns:
                inst.append("{:.1f}".format(len(dftmp[varname].dropna())/len(dftmp[varname])*100))
            else:
                inst.append("")
    elif i in six:
        for var in Vars:
            varname='{}_{}'.format(i,var)
            dftmp = df.loc['2021-06-15':]
            if varname in dftmp.columns:
                inst.append("{:.1f}".format(len(dftmp[varname].dropna())/len(dftmp[varname])*100))
            else:
                inst.append("")
    else:
        for var in Vars:
            varname='{}_{}'.format(i,var)
            if varname in df.columns:
                inst.append("{:.1f}".format(len(df[varname].dropna())/len(df[varname])*100))
            else:
                inst.append("")
    Table[i]=inst
    
dfDr=pd.DataFrame(data=Table).transpose()
dfDr.columns=Vars
dfDr


# In[1585]:


dfDr.to_csv(Path(QCQA/ 'DataAvailabilityFromInstallation_10Min_20210426_20211029.csv'),float_format='%.1f')


# In[1574]:


#%cp -r '/home/roelof/Dropbox (NWU)/CRG_Projects/01_Research_Campaigns/2021_Low-CostSensorSouthAfrica/03_DataAnalysisOutputs/QCQA_DATA' '/home/roelof/brigitte-jupyter/2021_Low-CostSensorSouthAfrica(LCS-SA)'


# ### Data Statistics

# **Intercept, Slope, Rvalue**

# In[1557]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '18',
             '20',
             '21',
             '22',
             '23',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        refvar='00_{}'.format(var)
        varname='{}_{}'.format(i,var)
        if varname in df.columns:            
            dftmp=df[[refvar,varname]].resample('1H').mean()
            dftmp=dftmp.dropna(how='any')
            if len(dftmp) > 10:
                X=dftmp[varname].values
                Y=dftmp[refvar].values
                res = linregress(X,Y)
                inst.append("{:.1f}, {:.1f}, {:.2f}".format(res.intercept,res.slope, res.rvalue))
            else:
                inst.append("")
        else:
            inst.append("")
    Table[i]=inst

dfDS=pd.DataFrame(data=Table).transpose()
dfDS.columns=Vars
dfDS


# In[1558]:


dfDS.to_csv(Path(QCQA/ 'DataStatistics_Intercept_Slope_RValue_1H_20210426_20211029.csv'),float_format='%.1f')


# **Mean, Std, Quantile 99**

# In[1560]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['00',
             '01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '20',
             '21',
             '22',
             '23',
             '24',
             '25',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        varname='{}_{}'.format(i,var)
        if varname in df.columns:
            inst.append("{:.1f}, {:.1f}, {:.1f}".format(df[varname].mean(),df[varname].std(),df[varname].quantile(0.99)))
            #print(varname,"{:.1f}".format(len(df[varname].dropna())/len(df[varname])*100))
        else:
            inst.append("")
    Table[i]=inst
    
dfDs=pd.DataFrame(data=Table).transpose()
dfDs.columns=Vars
dfDs


# In[1561]:


dfDs.to_csv(Path(QCQA/ 'DataStatistics_Mean_Std_q99_10Min_20210426_20211029.csv'),float_format='%.1f')


# **Mean, Std, Quantile 99 for 1H**

# In[1565]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['00',
             '01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '20',
             '21',
             '22',
             '23',
             '24',
             '25',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        varname='{}_{}'.format(i,var)
        dftmp = df.resample('1H').mean()
        if varname in df.columns:
            inst.append("{:.1f}, {:.1f}, {:.1f}".format(dftmp[varname].mean(),dftmp[varname].std(),dftmp[varname].quantile(0.99)))
            #print(varname,"{:.1f}".format(len(df[varname].dropna())/len(df[varname])*100))
        else:
            inst.append("")
    Table[i]=inst
    
dfDSH=pd.DataFrame(data=Table).transpose()
dfDSH.columns=Vars
dfDSH


# In[1566]:


dfDSH.to_csv(Path(QCQA/ 'DataStatistics_Mean_Std_q99_1H_20210426_20211029.csv'),float_format='%.1f')


# 

# #### Write to QCQA Directory

# In[830]:


#df[reference].to_csv(Path(QCQA/'df0.csv'), float_format="%.3f")


# In[831]:


#os.listdir(Path(DropboxDir/'CRG_Projects/01_Research_Campaigns/2021_Low-CostSensorSouthAfrica/03_DataAnalysisOutputs/QCQA_DATA'))


# In[832]:


#dftest = pd.read_csv(QCQA/'df0.csv', index_col=0, parse_dates=True)


# In[833]:


#dftest.describe()


# In[834]:


#dftest.plot(subplots=True, figsize=(15,15))


# ## MRC

# In[835]:


MRC = ['05_SO2 (ppb)',
'05_CO (ppm)',
'05_O3 (ppb)',
'05_PM2.5 (ug/m3)',
'05_PM10 (ug/m3)',
'05_Ambient_Temperature (degC)',
'05_Relative_Humidity (%)',
'05_Pressure (hPa)',
'05_Validity','06_PM10 (ug/m3)',
'06_PM2.5 (ug/m3)','07_CO (ppm)']


# ### DF05 "05_Vaisala_S1830003_df5"

# In[836]:


df.info()


# ### TimeSeries Plots

# In[1446]:


x = df['00_PM10 (ug/m3)'].dropna(how='any')
y = df['05_PM10 (ug/m3)'].dropna(how='any')

cf = x.div(y).mean()
cf


# In[1376]:


x = df['00_PM10 (ug/m3)'].dropna().mean()/df['05_PM10 (ug/m3)'].dropna().mean()
x


# In[837]:


variables = ['05_SO2 (ppb)',
                '05_CO (ppm)',
                '05_O3 (ppb)',
                '05_PM2.5 (ug/m3)',
                '05_PM10 (ug/m3)']

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','Vaisala_S1830003']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)
    #Plot
#    plt.tight_layout()
#     
    
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_05_Vaisala_S1830003_df5_{}.png'.format(x[1])), dpi=90)


# In[838]:


#clearplots()


# ### Scatterplots

# In[839]:


variables = ['05_SO2 (ppb)',
                '05_CO (ppm)',
                '05_O3 (ppb)',
                '05_PM2.5 (ug/m3)',
                '05_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Vaisala_S1830003 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Vaisala_S1830003 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_05_Vaisala_S1830003_df5_{}.png'.format(x[1])), dpi=90)


# ### Accuracy Metrics

# In[1055]:


#Create Dataframe with hourly and daily statistics 

hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
hrmse = mean_squared_error(Xhr, Yhr, squared=False)
drmse = mean_squared_error(Xday, Yday, squared=False)
stats = {'Slope':[hslope, dslope],'Intercept':[hintercept,dintercept],'Pearson R':[hr_value,dr_value], 'RMSE':[hrmse, drmse]}
df_Stats = pd.DataFrame(stats,index=['Hourly','Daily'])

df_Stats.plot(subplots=True, kind='bar', figsize=(10,10))


# In[1083]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[1117]:


variables = ['05_SO2 (ppb)',
                '05_CO (ppm)',
                '05_O3 (ppb)',
                '05_PM2.5 (ug/m3)',
                '05_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,4,figsize=(10,10))
    
    #Create Dataframe with hourly and daily statistics 
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    hrmse = mean_squared_error(Xhr, Yhr, squared=False)
    drmse = mean_squared_error(Xday, Yday, squared=False)
    stats = {'Slope':[hslope, dslope],'Intercept':[hintercept,dintercept],'Pearson R':[hr_value,dr_value], 'RMSE':[hrmse, drmse]}
    df_Stats = pd.DataFrame(stats,index=['Hourly','Daily'])
    
    # Add x-axis and y-axis
    df_Stats['Slope'].plot(ax=axs[0], kind='bar', color='0.4' )
    df_Stats['Intercept'].plot(ax=axs[1], kind='bar', color='0.4')
    df_Stats['Pearson R'].plot(ax=axs[2], kind='bar', color= '0.4')
    df_Stats['RMSE'].plot(ax=axs[3], kind='bar', color = '0.4')
    

    #Set title and labels for axis
    axs[0].set(title='Slope')
    #axs[0].set_ylim(-10, 250)
    axs[1].set(title='Intercept')
    #axs[1].set_ylim(-10,250)
    axs[2].set(
         title='Pearson R')
    #axs[2].set_ylim(-10,250)
    axs[3].set(
         title='RMSE')
    #axs[3].set_ylim(-10,250)
   
    fig.suptitle('Vaisala_S1830003 {} - FRM/FEM Accuracy'.format(i[3:]), fontsize=16)
    fig.supxlabel('Averaging Period')
    #Plotp
    plt.tight_layout()
    #Save
    x = re.split('_|\s',i)
  #  plt.savefig('AccuracyMetrics_05_Vaisala_S1830003_df5_{}.png'.format(x[1]), dpi=90)


# In[1088]:


variables = ['05_SO2 (ppb)',
                '05_CO (ppm)',
                '05_O3 (ppb)',
                '05_PM2.5 (ug/m3)',
                '05_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,4,figsize=(10,10))
    
    #Create Dataframe with hourly and daily statistics 
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    hrmse = mean_squared_error(Xhr, Yhr, squared=False)
    drmse = mean_squared_error(Xday, Yday, squared=False)
    stats = {'Slope':[hslope, dslope],'Intercept':[hintercept,dintercept],'Pearson R':[hr_value,dr_value], 'RMSE':[hrmse, drmse]}
    df_Stats = pd.DataFrame(stats,index=['Hourly','Daily'])
    
    # Add x-axis and y-axis
    axs[0].plot(df_Stats.index, df_Stats['Slope'], kind='bar', linestyle='none')
    axs[1].plot(df_Stats.index, df_Stats['Intercept'],marker='o')
    axs[2].plot(df_Stats.index, df_Stats['Pearson R'],marker='o')
    axs[3].plot(df_Stats.index, df_Stats['RMSE'],marker='o')
    
    #Set title and labels for axis
    axs[0].set(xlabel='Average Interval',
         title='Slope')
    axs[1].set(xlabel='Average Interval',
         title='Intercept')
    axs[2].set(xlabel='Average Interval',
         title='Pearson R')
    axs[3].set(xlabel='Average Interval',
         title='RMSE')
    
    
    fig.suptitle('Vaisala_S1830003 {} - FRM/FEM Accuracy'.format(i[3:]), fontsize=16)

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
#    plt.savefig('AccuracyMetrics_05_Vaisala_S1830003_df5_{}.png'.format(x[1]), dpi=90)


# ### DF06  "06_S500_5002-2D82-001_df6"

# ### TimeSeries Plots

# In[841]:


for i in df.columns:
    if i.startswith('06'):
        print(i)


# In[842]:


variables = ['06_PM10 (ug/m3)',
            '06_PM2.5 (ug/m3)']

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','S500_5002-2D82-001']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_06_S500_5002-2D82-001_df6_{}.png'.format(x[1])), dpi=90)


# In[843]:


#clearplots()


# ### Scatterplots

# In[844]:


variables = ['06_PM10 (ug/m3)',
            '06_PM2.5 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='S500_5002-2D82-001 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='S500_5002-2D82-001 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_06_S500_5002-2D82-001_df6_{}.png'.format(x[1])), dpi=90)


# ### DF07 "07_S500_ECM-1906191-003_df7"

# ### Timeseries

# In[845]:


for i in df.columns:
    if i.startswith('07'):
        print(i)


# In[846]:


variables = ['07_CO (ppm)']

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','S500_ECM-1906191-003']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_07_S500_ECM-1906191-003_df7_{}.png'.format(x[1])), dpi=90)


# ### Scatterplot

# In[847]:


DropboxDir/'CRG_Projects/01_Research_Campaigns/2021_Low-CostSensorSouthAfrica/03_DataAnalysisOutputs/QCQA_DATA'variables = ['07_CO (ppm)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='S500_ECM-1906191-003 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='S500_ECM-1906191-003 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_07_S500_ECM-1906191-003_df7_{}.png'.format(x[1])), dpi=90)


# In[848]:


QCQA


# ## eroAfrica

# In[849]:


eroAfrica = ['08_CO2 (ppm)',
'08_CO (ppm)',
'08_NO2 (ppb)',
'08_O3 (ppb)',
'08_NO (ppb)',
'08_SO2 (ppb)',
'08_Relative_Humidity (%)',
'08_PM2.5 (ug/m3)',
'08_PM10 (ug/m3)',
'08_Ambient_Temperature (degC)','27_CO2 (ppm)',
'27_CO (ppm)',
'27_NO2 (ppb)',
'27_O3 (ppb)',
'27_NO (ppb)',
'27_SO2 (ppb)',
'27_Relative_Humidity (%)',
'27_PM2.5 (ug/m3)',
'27_PM10 (ug/m3)',
'27_Ambient_Temperature (degC)','17_CO (ppm)',
'17_O3 (ppb)',
'17_NO2 (ppb)',
'17_SO2 (ppb)',
'17_NO (ppb)',
'17_PM2.5 (ug/m3)',
'17_PM10 (ug/m3)',
'17_Relative Humidity (%)']


# ### DF08 "08_PolludroneSmart_EA01P0001_df8"

# ### Timeseries

# In[850]:


variables = ['08_CO (ppm)',
                '08_NO2 (ppb)',
                '08_O3 (ppb)',
                '08_NO (ppb)',
                '08_SO2 (ppb)',
                '08_PM2.5 (ug/m3)',
                '08_PM10 (ug/m3)']

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','PolludroneSmart_EA01P0001']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_08_PolludroneSmart_EA01P0001_df8_{}.png'.format(x[1])), dpi=90)


# ### Scatterplot

# In[851]:


variables = ['08_CO (ppm)',
                '08_NO2 (ppb)',
                '08_O3 (ppb)',
                '08_NO (ppb)',
                '08_SO2 (ppb)',
                '08_PM2.5 (ug/m3)',
                '08_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='PolludroneSmart_EA01P0001 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='PolludroneSmart_EA01P0001 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_08_PolludroneSmart_EA01P0001_df8_{}.png'.format(x[1])), dpi=90)


# ### DF17 "17_GM-5000_CM21035290_df17"

# ### Timeseries

# In[852]:


variables = ['17_O3 (ppb)',
            '17_NO2 (ppb)',
            '17_SO2 (ppb)',
            '17_NO (ppb)',
            '17_PM2.5 (ug/m3)',
            '17_PM10 (ug/m3)']

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','GM-5000_CM21035290']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_17_GM-5000_CM21035290_df17_{}.png'.format(x[1])), dpi=90)


# ### Scatterplot

# In[853]:


variables = ['17_O3 (ppb)',
            '17_NO2 (ppb)',
            '17_SO2 (ppb)',
            '17_NO (ppb)',
            '17_PM2.5 (ug/m3)',
            '17_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='GM-5000_CM21035290 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='GM-5000_CM21035290 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_17_GM-5000_CM21035290_df17_{}.png'.format(x[1])), dpi=90)


# ### DF27 "27_PolludroneSmart_PM01P0007_df27"

# ### Timeseries

# In[854]:



variables = ['27_CO (ppm)',
            '27_NO2 (ppb)',
            '27_O3 (ppb)',
            '27_NO (ppb)',
            '27_SO2 (ppb)',
            '27_PM2.5 (ug/m3)',
            '27_PM10 (ug/m3)']

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','PolludroneSmart_PM01P0007_df27']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_27_PolludroneSmart_PM01P0007_df27_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[855]:


variables = ['27_CO (ppm)',
            '27_NO2 (ppb)',
            '27_O3 (ppb)',
            '27_NO (ppb)',
            '27_SO2 (ppb)',
            '27_PM2.5 (ug/m3)',
            '27_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='PolludroneSmart_PM01P0007 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='PolludroneSmart_PM01P0007 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_27_PolludroneSmart_PM01P0007_df27_{}.png'.format(x[1])), dpi=90)


# ## Simplicity

# In[856]:


Simplicity = ['09_CO (ppm)',
'09_Pressure (hPa)',
'09_TVOC (ppb)',
'09_eCO2 (ppm)',
'09_Internal_Temperature (degC)',
'09_Ambient_Temperature (degC)',
'09_Internal_Relative_Humidity (%)',
'09_Ambient_Relative_Humidity (%)',
'09_PM1 (ug/m3)',
'09_PM2.5 (ug/m3)',
'09_PM10 (ug/m3)',
'09_NO2 (ppb)',
'09_O3 (ppb)',
'09_SO2 (ppb)',
'10_CO (ppm)',
'10_Pressure (hPa)',
'10_TVOC (ppb)',
'10_eCO2 (ppm)',
'10_Internal_Temperature (degC)',
'10_Ambient_Temperature (degC)',
'10_Internal_Relative_Humidity (%)',
'10_Ambient_Relative_Humidity (%)',
'10_PM1 (ug/m3)',
'10_PM2.5 (ug/m3)',
'10_PM10 (ug/m3)',
'10_NO2 (ppb)',
'10_O3 (ppb)',
'10_SO2 (ppb)',
'11_CO (ppm)',
'11_Pressure (hPa)',
'11_TVOC (ppb)',
'11_eCO2 (ppm)',
'11_Internal_Temperature (degC)',
'11_Ambient_Temperature (degC)',
'11_Internal_Relative_Humidity (%)',
'11_Ambient_Relative_Humidity (%)',
'11_PM1 (ug/m3)',
'11_PM2.5 (ug/m3)',
'11_PM10 (ug/m3)',
'11_NO2 (ppb)',
'11_O3 (ppb)',
'11_SO2 (ppb)',
'12_CO (ppm)',
'12_Pressure (hPa)',
'12_TVOC (ppb)',
'12_eCO2 (ppm)',
'12_Internal_Temperature (degC)',
'12_Ambient_Temperature (degC)',
'12_Internal_Relative_Humidity (%)',
'12_Ambient_Relative_Humidity (%)',
'12_PM1 (ug/m3)',
'12_PM2.5 (ug/m3)',
'12_PM10 (ug/m3)',
'12_NO2 (ppb)',
'12_O3 (ppb)',
'12_SO2 (ppb)',
'13_CO (ppm)',
'13_Pressure (hPa)',
'13_TVOC (ppb)',
'13_eCO2 (ppm)',
'13_Internal_Temperature (degC)',
'13_Ambient_Temperature (degC)',
'13_Internal_Relative_Humidity (%)',
'13_Ambient_Relative_Humidity (%)',
'13_PM1 (ug/m3)',
'13_PM2.5 (ug/m3)',
'13_PM10 (ug/m3)',
'13_NO2 (ppb)',
'13_O3 (ppb)',
'13_SO2 (ppb)',
'14_CO (ppm)',
'14_Pressure (hPa)',
'14_TVOC (ppb)',
'14_eCO2 (ppm)',
'14_Internal_Temperature (degC)',
'14_Ambient_Temperature (degC)',
'14_Internal_Relative_Humidity (%)',
'14_Ambient_Relative_Humidity (%)',
'14_PM1 (ug/m3)',
'14_PM2.5 (ug/m3)',
'14_PM10 (ug/m3)',
'14_NO2 (ppb)',
'14_O3 (ppb)',
'14_SO2 (ppb)']


# ### "09_SimplicityV1_CCSENV011_df9"

# In[857]:


instruments('09')


# ### Timeseries

# In[858]:



variables = ['09_PM2.5 (ug/m3)',
                '09_PM10 (ug/m3)',
                '09_NO2 (ppb)',
                '09_O3 (ppb)',
                '09_SO2 (ppb)','09_CO (ppm)' ]

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','SimplicityV1_CCSENV011']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_09_SimplicityV1_CCSENV011_df9_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[859]:


variables = ['09_PM2.5 (ug/m3)',
                '09_PM10 (ug/m3)',
                '09_NO2 (ppb)',
                '09_O3 (ppb)',
                '09_SO2 (ppb)','09_CO (ppm)' ]

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV1_CCSENV011 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV1_CCSENV011 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_09_SimplicityV1_CCSENV011_df9_{}.png'.format(x[1])), dpi=90)


# ###  "10_SimplicityV1_CCSENV020_df10"

# In[860]:


instruments('10')


# ### Timeseries

# In[861]:



variables = ['10_PM2.5 (ug/m3)',
            '10_PM10 (ug/m3)',
            '10_NO2 (ppb)',
            '10_O3 (ppb)',
            '10_SO2 (ppb)','10_CO (ppm)']

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','SimplicityV1_CCSENV020']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_10_SimplicityV1_CCSENV020_df10_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[862]:


variables = ['10_PM2.5 (ug/m3)',
            '10_PM10 (ug/m3)',
            '10_NO2 (ppb)',
            '10_O3 (ppb)',
            '10_SO2 (ppb)','10_CO (ppm)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV1_CCSENV020 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV1_CCSENV020 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_10_SimplicityV1_CCSENV020_df10_{}.png'.format(x[1])), dpi=90)


# ### "11_SimplicityV2_IMTAQS0001_df11"

# In[863]:


instruments('11')


# ### Timeseries

# In[864]:



variables = ['11_PM2.5 (ug/m3)',
                '11_PM10 (ug/m3)',
                '11_NO2 (ppb)',
                '11_O3 (ppb)',
                '11_SO2 (ppb)','11_CO (ppm)' ]

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','SimplicityV2_IMTAQS0001']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_11_SimplicityV2_IMTAQS0001_df11_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[865]:


variables = ['11_PM2.5 (ug/m3)',
                '11_PM10 (ug/m3)',
                '11_NO2 (ppb)',
                '11_O3 (ppb)',
                '11_SO2 (ppb)','11_CO (ppm)'  ]

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV2_IMTAQS0001 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV2_IMTAQS0001 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_11_SimplicityV2_IMTAQS0001_df11_{}.png'.format(x[1])), dpi=90)


# ### "12_SimplicityV2_IMTAQS0002_df12"

# In[866]:


instruments('12')


# ### Timeseries

# In[867]:



variables = ['12_PM2.5 (ug/m3)',
                '12_PM10 (ug/m3)',
                '12_NO2 (ppb)',
                '12_O3 (ppb)',
                '12_SO2 (ppb)','12_CO (ppm)' ]

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','SimplicityV2_IMTAQS0002']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_12_SimplicityV2_IMTAQS0002_df12_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[868]:


variables = ['12_PM2.5 (ug/m3)',
                '12_PM10 (ug/m3)',
                '12_NO2 (ppb)',
                '12_O3 (ppb)',
                '12_SO2 (ppb)','12_CO (ppm)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV2_IMTAQS0002 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV2_IMTAQS0002 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_12_SimplicityV2_IMTAQS0002_df12_{}.png'.format(x[1])), dpi=90)


# ### "13_SimplicityV2_IMTAQS0003_df13"

# In[869]:


instruments('13')


# ### Timeseries

# In[870]:



variables = ['13_PM2.5 (ug/m3)',
                '13_PM10 (ug/m3)',
                '13_NO2 (ppb)',
                '13_O3 (ppb)',
                '13_SO2 (ppb)','13_CO (ppm)' ]

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','SimplicityV2_IMTAQS0003']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_13_SimplicityV2_IMTAQS0003_df13_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[871]:


variables = ['09_PM2.5 (ug/m3)',
                '09_PM10 (ug/m3)',
                '09_NO2 (ppb)',
                '09_O3 (ppb)',
                '09_SO2 (ppb)','09_CO (ppm)' ]

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV2_IMTAQS0003 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV2_IMTAQS0003 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_13_SimplicityV2_IMTAQS0003_df13_{}.png'.format(x[1])), dpi=90)


# ### "14_SimplicityV2_IMTAQS0004_df14"

# In[872]:


instruments('14')


# ### Timeseries

# In[873]:



variables = ['14_PM2.5 (ug/m3)',
                '14_PM10 (ug/m3)',
                '14_NO2 (ppb)',
                '14_O3 (ppb)',
                '14_SO2 (ppb)','14_CO (ppm)' ]

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','SimplicityV2_IMTAQS0004']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_14_SimplicityV2_IMTAQS0004_df14_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[874]:


variables = ['14_PM2.5 (ug/m3)',
                '14_PM10 (ug/m3)',
                '14_NO2 (ppb)',
                '14_O3 (ppb)',
                '14_SO2 (ppb)','14_CO (ppm)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV2_IMTAQS0004 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='SimplicityV2_IMTAQS0004 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_14_SimplicityV2_IMTAQS0004_df14_{}.png'.format(x[1])), dpi=90)


# ## Envirocon

# In[875]:


Envirocon = ['15_Ambient_Temperature (degC)',
'15_Relative_Humidity (%)',
'15_Pressure (hPa)',
'15_SO2 (ppb)',
'15_NO2 (ppb)',
'15_O3 (ppb)',
'15_PM1 (ug/m3)',
'15_PM2.5 (ug/m3)',
'15_PM10 (ug/m3)',
'15_Internal_Battery (%)',
'15_Wind_Direction (m/s)',
'15_Winds_Speed (degrees)']


# ### DF15 "15_ICOMSMART_20149_df15"

# ### Timeseries

# In[876]:



variables = ['15_SO2 (ppb)',
'15_NO2 (ppb)',
'15_O3 (ppb)',
'15_PM2.5 (ug/m3)',
'15_PM10 (ug/m3)']

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','ICOMSMART_20149']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)

    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_15_ICOMSMART_20149_df15_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[877]:


variables = ['15_SO2 (ppb)',
'15_NO2 (ppb)',
'15_O3 (ppb)',
'15_PM2.5 (ug/m3)',
'15_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='ICOMSMART_20149 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='ICOMSMART_20149 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_15_ICOMSMART_20149_df15_{}.png'.format(x[1])), dpi=90)


# ## Sensors.Africa

# In[878]:


Sensors_Africa = ['18_PM1 (ug/m3)',
'18_PM10 (ug/m3)',
'18_PM2.5 (ug/m3)',
'18_Relative_Humidity (%)',
'18_Ambient_Temperature (degC)']


# ### DF18 "18_Plantower_108_df18"

# ### Timeseries

# In[879]:



variables = ['18_PM10 (ug/m3)','18_PM2.5 (ug/m3)']

for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','Plantower_108']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)
    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_18_Plantower_108_df18_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[880]:


variables = ['18_PM10 (ug/m3)','18_PM2.5 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Plantower_108 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Plantower_108 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
  

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_18_Plantower_108_df18_{}.png'.format(x[1])), dpi=90)


# ## University of L

# In[881]:


UL = ['20_NO2 (ug/m3)',
'20_O3 (ug/m3)',
'20_NO (ug/m3)',
'20_PM2.5 (ug/m3)',
'20_PM1 (ug/m3)',
'20_SO2 (ug/m3)',
'20_PM10 (ug/m3)',
'20_CO (mg/m3)',
'20_H2S (ug/m3)',
'20_Ambient_Temperature (degC)',
'20_Relative_Humidity (%)',
'20_Pressure (hPa)',
'20_NO2 (ppb)',
'20_O3 (ppb)',
'20_CO (ppm)',
'20_NO (ppb)',
'20_H2S (ppb)',
'21_NO2 (ug/m3)',
'21_O3 (ug/m3)',
'21_NO (ug/m3)',
'21_SO2 (ug/m3)',
'21_PM1 (ug/m3)',
'21_PM2.5 (ug/m3)',
'21_PM10 (ug/m3)',
'21_CO (mg/m3)',
'21_H2S (ug/m3)',
'21_Ambient_Temperature (degC)',
'21_Relative_Humidity (%)',
'21_Pressure (hPa)',
'21_NO2 (ppb)',
'21_SO2 (ppb)',
'21_O3 (ppb)',
'21_CO (ppm)',
'21_NO (ppb)',
'21_H2S (ppb)']


# ### DF20 "20_Zephyr_642-SA_df20"

# In[882]:


instruments('20')


# ### Timeseries

# In[1132]:



variables20 = ['20_NO2 (ppb)',
'20_O3 (ppb)',
'20_CO (ppm)',
'20_NO (ppb)','20_PM2.5 (ug/m3)',
'20_PM10 (ug/m3)']
    
variables21 = ['21_NO2 (ppb)',
'21_SO2 (ppb)',
'21_O3 (ppb)',
'21_CO (ppm)',
'21_NO (ppb)','21_PM2.5 (ug/m3)',
'21_PM10 (ug/m3)']

pollutants = ['NO2 (ppb)',
'SO2 (ppb)',
'O3 (ppb)',
'CO (ppm)',
'NO (ppb)','PM2.5 (ug/m3)',
'PM10 (ug/m3)']


# In[883]:



variables = ['20_NO2 (ppb)',
'20_O3 (ppb)',
'20_CO (ppm)',
'20_NO (ppb)','20_PM2.5 (ug/m3)',
'20_PM10 (ug/m3)']
    
variables21 = ['21_NO2 (ppb)',
'21_SO2 (ppb)',
'21_O3 (ppb)',
'21_CO (ppm)',
'21_NO (ppb)','21_PM2.5 (ug/m3)',
'21_PM10 (ug/m3)']

    
for i in variables:
    if '21' and '22'
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','Zephyr_642-SA']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)
    #Plot
    plt.tight_layout()
    #Save
    x = re.split('_|\s',i)
#    plt.savefig(Path(QCQA/'TimeSeries_20_Zephyr_642-SA_df20_{}.png'.format(x[1])), dpi=90) 


# ### Scatterplots

# In[884]:


variables = ['20_NO2 (ppb)',
'20_O3 (ppb)',
'20_CO (ppm)',
'20_NO (ppb)','20_PM2.5 (ug/m3)',
'20_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Zephyr_642-SA {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Zephyr_642-SA {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
    

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_20_Zephyr_642-SA_df20_{}.png'.format(x[1])), dpi=90)


# ### DF21 "21_Zephyr_729-SA_df21"

# ### Timeseries

# In[885]:


instruments('21')


# In[954]:



variables = ['21_NO2 (ppb)',
'21_SO2 (ppb)',
'21_O3 (ppb)',
'21_CO (ppm)',
'21_NO (ppb)','21_PM2.5 (ug/m3)',
'21_PM10 (ug/m3)']
    
    
for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','Zephyr_729-SA']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)
    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_21_Zephyr_729-SA_df21_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[887]:


variables = ['21_NO2 (ppb)',
'21_SO2 (ppb)',
'21_O3 (ppb)',
'21_CO (ppm)',
'21_NO (ppb)','21_PM2.5 (ug/m3)',
'21_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Zephyr_729-SA {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Zephyr_729-SA {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
    

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_21_Zephyr_729-SA_df21_{}.png'.format(x[1])), dpi=90)


# ## Skyside

# In[888]:


SkySide = ['22_PM1 (ug/m3)',
'22_PM2.5 (ug/m3)',
'22_PM10 (ug/m3)',
'22_Relative_Humidity (%)',
'22_Ambient_Temperature (degC)',
'23_PM1 (ug/m3)',
'23_PM2.5 (ug/m3)',
'23_PM10 (ug/m3)',
'23_Relative_Humidity (%)',
'23_Ambient_Temperature (degC)']


# ### DF22 "22_Atmos_84CCA8B167D2_df22"

# In[889]:



variables = ['22_PM2.5 (ug/m3)',
'22_PM10 (ug/m3)']
    
    
for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','Atmos_84CCA8B167D2']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)
    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_22_Atmos_84CCA8B167D2_df22_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[890]:


variables = ['22_PM2.5 (ug/m3)',
'22_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Atmos_84CCA8B167D2 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Atmos_84CCA8B167D2 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
    

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_22_Atmos_84CCA8B167D2_df22_{}.png'.format(x[1])), dpi=90)


# ### DF23 "23_Atmos_98F4ABDCA328_df23"

# In[891]:



variables = ['23_PM2.5 (ug/m3)',
'23_PM10 (ug/m3)']
    
    
for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','Atmos_98F4ABDCA328']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)
    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)
    plt.savefig(Path(QCQA/'TimeSeries_23_Atmos_98F4ABDCA328_df23_{}.png'.format(x[1])), dpi=90)


# ### Scatterplots

# In[892]:


variables = ['23_PM2.5 (ug/m3)',
'23_PM10 (ug/m3)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Atmos_98F4ABDCA328 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Atmos_98F4ABDCA328 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
    

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_23_Atmos_98F4ABDCA328_df23_{}.png'.format(x[1])), dpi=90)


# ## Sedulitas

# In[893]:


instruments('26')


# In[894]:


Sedulitas = ['26_Longitude',
'26_Internal_Temerature (degC)',
'26_Internal_Relative_Humidity (%)',
'26_NO2 (ug/m3)',
'26_O3 (ug/m3)',
'26_NO (ug/m3)',
'26_SO2 (ug/m3)',
'26_PM1 (ug/m3)',
'26_PM2.5 (ug/m3)',
'26_PM10 (ug/m3)',
'26_CO (mg/m3)',
'26_H2S (ug/m3)',
'26_Ambient_Temperature (degC)',
'26_Relative_Humidity (%)',
'26_Pressure (hPa)']


# ### DF26 26_Zephyr_533_df26 

# In[895]:



variables = ['26_NO2 (ppb)',
'26_SO2 (ppb)',
'26_O3 (ppb)',
'26_CO (ppm)',
'26_NO (ppb)']
    
    
for i in variables:
    #Create figure and plot space
    fig, axs = plt.subplots(2, figsize=(10,10))

    line_labels = ['FRM/FEM','Zephyr_533']
                       
    # Add x-axis and y-axis
    axs[0].plot(df.resample('1H').mean().index.values,
        df[['00_{}'.format(i[3:])]].resample('1H').mean(),
       df[[i]].resample('1H').mean())

    axs[1].plot(df.resample('1D').mean().index.values,
            df[['00_{}'.format(i[3:])]].resample('1D').mean(),
            df[[i]].resample('1D').mean())

    #Set title and labels for axis
    axs[0].set(xlabel='Date',
          ylabel=i[3:],
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Date',
          ylabel=i[3:],
          title='24-hour averaged {}'.format(i[3:]))

    # Set the legend
    fig.legend(labels=line_labels,
           borderaxespad=0.1,
           bbox_to_anchor=(1, 0.5))
    fig.subplots_adjust(hspace=0.3)
    #Plot
    plt.tight_layout()
     
    #Save
    x = re.split('_|\s',i)

    plt.savefig(Path(QCQA/'TimeSeries_26_Zephyr_533_df26_{}.png'.format(x[1])), dpi=90)


# ## Scatterplots

# In[896]:


variables = ['26_NO2 (ppb)',
'26_SO2 (ppb)',
'26_O3 (ppb)',
'26_CO (ppm)',
'26_NO (ppb)']

for i in variables:
    
    hr = df[[i,'00_{}'.format(i[3:])]].resample('1H').mean().dropna(how='any')
    
    day = df[[i,'00_{}'.format(i[3:])]].resample('1D').mean().dropna(how='any')
    
    Xhr = hr[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yhr = hr[i].values.reshape(-1,1)
    
    Xday = day[['00_{}'.format(i[3:])]].values.reshape(-1,1)
    Yday = day[i].values.reshape(-1,1)
    
    #Create figure and plot space
    fig, axs = plt.subplots(1,2, figsize=(10,10), sharex=True, sharey=True)
    
    # Add x-axis and y-axis
    axs[0].scatter(Xhr,Yhr, alpha=0.25)
    hslope, hintercept, hr_value, hp_value, hstd_err = linregress(Xhr[:,0], Yhr[:,0])
    axs[0].plot(Xhr, hintercept+hslope*Xhr, 'r')
    axs[0].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(hintercept,hslope, hr_value), fontsize=10, transform=axs[0].transAxes)

    
    axs[1].scatter(Xday,Yday, alpha=0.35)
    dslope, dintercept, dr_value, dp_value, dstd_err = linregress(Xday[:,0], Yday[:,0])
    axs[1].plot(Xday, dintercept+dslope*Xday, 'r')
    axs[1].text(0.6,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(dintercept,dslope, dr_value), fontsize=10, transform=axs[1].transAxes)
    
    #Set title and labels for axis
    axs[0].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Zephyr_533 {}'.format(i[3:]),
          title='1-hour averaged {}'.format(i[3:]))

    axs[1].set(xlabel='Reference {}'.format(i[3:]),
          ylabel='Zephyr_533 {}'.format(i[3:]),
          title='24-hour averaged {}'.format(i[3:]))
    

    #Plot
    plt.tight_layout()
     
   
    #Save
    x = re.split('_|\s',i)
    
    plt.savefig(Path(QCQA/'ScatterPlot_26_Zephyr_533_df26_{}.png'.format(x[1])), dpi=90,bbox_inches='tight')


# ## AfriqAir

# In[ ]:





# In[897]:


#AfriqAir = []


# In[ ]:





# ## Data analysis  <a id="dataanalysis"></a>
# [Back to the top](#TOP)
# 
# 1. xxx
# 2. xxx
# 3. xxx
# 4. xxx
# 5. xxx
# 6. xxx

# In[ ]:





# In[ ]:





# In[898]:


df.info()


# In[899]:


ax=df[[i for i in df.columns if 'PM10' in i]].resample('1H').mean().plot()
ax.get_legend().remove()


# In[900]:


df[[i for i in df.columns if 'PM10' in i]].resample('1H').mean()


# In[901]:


pm10l=[i for i in df.columns if 'PM10' in i and i != '00_PM10 (ug/m3)']


# In[902]:


df[pm10l].resample('1H').mean()


# In[903]:


len([i for i in df.columns if 'PM10' in i and i != '00_PM10 (ug/m3)'])


# In[904]:


Y=df['00_PM10 (ug/m3)'].resample('1H').mean().values

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

for p in [i for i in df.columns if 'PM10' in i and i != '00_PM10 (ug/m3)']:
    ax.scatter(df[p].resample('1H').mean().values,Y)
    print(p)

ax.set_ylabel('Reference PM10 (ug/m3)')
ax.set_xlabel('Low cost PM10 (ug/m3)')
ax.set_xlim([0,200])
ax.set_ylim([0,200])


# In[905]:


Y=df['00_PM10 (ug/m3)'].resample('1H').mean().values

lcvars=[i for i in df.columns if 'PM10' in i and i != '00_PM10 (ug/m3)']

fig, axs = plt.subplots(5,4, sharex='col',sharey='row',gridspec_kw={'hspace':0.1, 'wspace':0.1}, figsize=(12,12))

for i in range(len(lcvars)):
    dftmp=df[['00_PM10 (ug/m3)',lcvars[i]]].resample('1H').mean()
    dftmp=dftmp.dropna(how='any')
    X=dftmp[lcvars[i]].values
    Y=dftmp['00_PM10 (ug/m3)'].values
    if len(X)>0 and len(Y)>0:
        axs[int(i/4),i%4].scatter(X,Y, alpha=0.25)
        axs[int(i/4),i%4].set_xlim(0,200)
        axs[int(i/4),i%4].set_ylim(0,200)
        res = linregress(X,Y)

        axs[int(i/4),i%4].text(0.3,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(res.intercept,res.slope, res.rvalue), fontsize=10, transform=axs[int(i/4),i%4].transAxes)

        axs[int(i/4),i%4].set_title(lcvars[i].split("_")[0], y=1.0, pad=-14, fontsize=14)
        #axs[int(i/4),i%4].set_ylabel('Reference PM10 (ug/m3)')
        #axs[int(i/4),i%4].set_xlabel('Low cost PM10 (ug/m3)')

        axs[int(i/4),i%4].plot(X, res.intercept+res.slope*X, 'r')
        #print(b,m,r,p)
    
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False )
plt.grid(False)
plt.xlabel("Low cost PM10 (ug/m3)", fontsize=16)
plt.ylabel("Reference PM10 (ug/m3)", fontsize=16)

#plt.savefig(Path(FigDir / '20210929_CorrMatrix_{}.png'.format('PM10')), dpi=90, bbox_inches='tight', pad_inches=0)


# In[906]:


res


# In[907]:


lcvars


# In[908]:


lcvars=[i for i in df.columns if 'PM10' in i]

for i in range(len(lcvars)):
    print(lcvars[i])


# In[909]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[910]:


for i in df.columns:
    if i.startswith("00"):
        print(i)


# In[911]:


df = df.reindex(sorted(df.columns), axis=1)


# In[912]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

for var in Vars:
    refvar='00_{}'.format(var)
    Y=df[refvar].resample('1H').mean().values

    lcvars=[i for i in df.columns if var in i and i != refvar]

    fig, axs = plt.subplots(6,4,sharex='col',sharey='row',gridspec_kw={'hspace':0.1, 'wspace':0.1}, figsize=(12,12))

    for i in range(len(lcvars)):
        dftmp=df[[refvar,lcvars[i]]].resample('1H').mean()
        dftmp=dftmp.dropna(how='any')
        X=dftmp[lcvars[i]].values
        Y=dftmp[refvar].values
        if len(X)>0 and len(Y)>0:
            axs[int(i/4),i%4].scatter(X,Y, alpha=0.25)
            axs[int(i/4),i%4].set_xlim(0,dftmp[refvar].max())
            axs[int(i/4),i%4].set_ylim(0,dftmp[refvar].max())
            res = linregress(X,Y)

            axs[int(i/4),i%4].text(0.3,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(res.intercept,res.slope, res.rvalue), fontsize=10, transform=axs[int(i/4),i%4].transAxes)

            axs[int(i/4),i%4].set_title(lcvars[i].split("_")[0], y=1.0, pad=-14, fontsize=14)
            #axs[int(i/4),i%4].set_ylabel('Reference PM10 (ug/m3)')
            #axs[int(i/4),i%4].set_xlabel('Low cost PM10 (ug/m3)')

            axs[int(i/4),i%4].plot(X, res.intercept+res.slope*X, 'r')

    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False )
    plt.grid(False)
    plt.xlabel("Low cost {}".format(var), fontsize=16)
    plt.ylabel("Reference {}".format(var), fontsize=16)

    plt.savefig(Path(QCQA/'AllVars_CorrMatrix_{}.png'.format(var.split()[0])), dpi=90, bbox_inches='tight', pad_inches=0)


# In[913]:


Pvars = ["03_PM10 (ug/m3)",
        "04_PM10 (ug/m3)",
        "05_PM10 (ug/m3)",
        "06_PM10 (ug/m3)",
        "08_PM10 (ug/m3)",
        "09_PM10 (ug/m3)",
        "10_PM10 (ug/m3)",
        "11_PM10 (ug/m3)",
        "12_PM10 (ug/m3)",
        "13_PM10 (ug/m3)",
        "14_PM10 (ug/m3)",
        "15_PM10 (ug/m3)",
        "17_PM10 (ug/m3)",
        "18_PM10 (ug/m3)",
        "20_PM10 (ug/m3)",
        "21_PM10 (ug/m3)",
        "22_PM10 (ug/m3)",
        "23_PM10 (ug/m3)",
        "26_PM10 (ug/m3)",
        "27_PM10 (ug/m3)"]

varname="00_PM10 (ug/m3)"
dftmp=df[[varname]].resample('1H').mean()
dftmp['Time'] = dftmp.index.map(lambda x: x.strftime("%H:00"))
diurnal = dftmp[['Time',varname]].groupby('Time').describe()[varname]

fig, ax = plt.subplots(1, figsize=(12,6))
ax.plot(diurnal.index, diurnal['50%'], linewidth=2.0,label=varname, alpha=0.5) 

for var in Pvars:
    dftmp=df[[var]].resample('1H').mean()
    dftmp['Time'] = dftmp.index.map(lambda x: x.strftime("%H:00"))
    diurnal = dftmp[['Time',var]].groupby('Time').describe()[var]
    ax.plot(diurnal.index, diurnal['50%'], linewidth=2.0,label=var, alpha=0.5)
ax.set_xlim(0, 23)                                                                                                                                                                                                                                                          
ax.set_xticks([i for i in range(0,24,3)])                                                                                                                                                                                                                                    

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


# In[914]:


pm10=[i for i in df.columns if 'PM10' in i and i != '00_PM10 (ug/m3)']


# In[915]:


get_ipython().run_line_magic('matplotlib', 'widget')


# In[916]:


#df[pm10].plot(subplots=True, figsize=(20,20))


# ### Diurnal plots

# In[ ]:





# In[917]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

for var in Vars:
    refvar='00_{}'.format(var)
    dftmp=df[[refvar]].resample('5min').mean()
    dftmp['Time'] = dftmp.index.map(lambda x: x.strftime("%H:00"))
    diurnalref = dftmp[['Time',refvar]].groupby('Time').describe()[refvar]

    lcvars=[i for i in df.columns if var in i and i != refvar]

    fig, axs = plt.subplots(6,4, sharex='col',sharey='row',gridspec_kw={'hspace':0.1, 'wspace':0.1}, figsize=(12,12))

    for i in range(len(lcvars)):
        dftmp=df[[lcvars[i]]].resample('5min').mean()
        dftmp['Time'] = dftmp.index.map(lambda x: x.strftime("%H:00"))
        diurnal = dftmp[['Time',lcvars[i]]].groupby('Time').describe()[lcvars[i]]
        axs[int(i/4),i%4].plot(diurnal.index, diurnal['50%'], linewidth=2.0,label=var, alpha=0.5)
        axs[int(i/4),i%4].plot(diurnalref.index, diurnalref['50%'], linewidth=2.0,label='Reference', alpha=0.5)

        #axs[int(i/4),i%4].set_xlim(0,dftmp[refvar].max())
        #axs[int(i/4),i%4].set_ylim(0,dftmp[refvar].max())
        
        #axs[int(i/4),i%4].text(0.3,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(res.intercept,res.slope, res.rvalue), fontsize=10, transform=axs[int(i/4),i%4].transAxes)

        axs[int(i/4),i%4].set_title(lcvars[i].split("_")[0], y=1.0, pad=-14, fontsize=14)

    for i in range(4):
        axs[4,i%4].set_xlim(0, 23)                                                                                                                                                                                                                                                          
        axs[4,i%4].set_xticks([i for i in range(0,24,6)])

            
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False )
    plt.grid(False)
    plt.xlabel("Time of day", fontsize=16)
    plt.ylabel("Reference (orange) vs low-cost (blue) {}".format(var), fontsize=16)

    plt.savefig(Path(QCQA/ 'AllVars_Diurnal_{}.png'.format(var.split()[0])), dpi=90, bbox_inches='tight', pad_inches=0)


# In[951]:


#%cp -r '/home/roelof/Dropbox (NWU)/CRG_Projects/01_Research_Campaigns/2021_Low-CostSensorSouthAfrica/03_DataAnalysisOutputs/QCQA_DATA/' '/home/roelof/brigitte-jupyter/2021_Low-CostSensorSouthAfrica(LCS-SA)'   


# In[952]:


QCQA


# In[953]:


sorted(os.listdir(QCQA))


# ### Data recovery

# In[918]:


df.columns


# In[ ]:


dfDA=pd.DataFrame(data=Table).transpose()
dfDA.columns=Vars
dfDA


# In[947]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['00',
             '01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '20',
             '21',
             '22',
             '23',
             '24',
             '25',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        varname='{}_{}'.format(i,var)
        if varname in df.columns:
            inst.append("{:.1f}".format(len(df[varname].dropna())/len(df[varname])*100))
            #print(varname,"{:.1f}".format(len(df[varname].dropna())/len(df[varname])*100))
        else:
            inst.append("")
    Table[i]=inst


# In[ ]:





# In[948]:


Table


# In[949]:


dfDA=pd.DataFrame(data=Table).transpose()
dfDA.columns=Vars
dfDA


# In[950]:


dfDA.to_csv(Path(QCQA/ 'DataAvailability.csv'),float_format='%.1f')


# ### Factors

# In[1410]:


x = df["00_PM10 (ug/m3)"].dropna()/df['09_PM10 (ug/m3)'].dropna()
x.mean()


# In[1427]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '18',
             '20',
             '21',
             '22',
             '23',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        refvar='00_{}'.format(var)
        varname='{}_{}'.format(i,var)
        if varname in df.columns:            
            dftmp=df[[refvar,varname]].resample('1H').mean()
            dftmp=dftmp.dropna(how='any')
            if len(dftmp) > 10:
                X=dftmp[varname].values
                Y=dftmp[refvar].values
                res = linregress(X,Y)
                CF = dftmp[refvar]/dftmp[varname]
                CF = CF.mean()
                inst.append("{:.2f}".format(CF))
            else:
                inst.append("")
        else:
            inst.append("")
    Table[i]=inst

dfDA=pd.DataFrame(data=Table).transpose()
dfDA.columns=Vars
dfDA


# In[940]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '18',
             '20',
             '21',
             '22',
             '23',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        refvar='00_{}'.format(var)
        varname='{}_{}'.format(i,var)
        if varname in df.columns:            
            dftmp=df[[refvar,varname]].resample('1H').mean()
            dftmp=dftmp.dropna(how='any')
            if len(dftmp) > 10:
                X=dftmp[varname].values
                Y=dftmp[refvar].values
                res = linregress(X,Y)
                inst.append("{:.1f}, {:.1f}, {:.2f}".format(res.intercept,res.slope, res.rvalue))
            else:
                inst.append("")
        else:
            inst.append("")
    Table[i]=inst

dfDA=pd.DataFrame(data=Table).transpose()
dfDA.columns=Vars
dfDA


# In[941]:


dfDA.to_csv(Path(QCQA / 'CorrelationWithReference.csv'))


# In[946]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['00',
             '01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '20',
             '21',
             '22',
             '23',
             '24',
             '25',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        varname='{}_{}'.format(i,var)
        if varname in df.columns:
            inst.append("{:.1f}, {:.1f}, {:.1f}".format(df[varname].mean(),df[varname].std(),df[varname].quantile(0.99)))
            #print(varname,"{:.1f}".format(len(df[varname].dropna())/len(df[varname])*100))
        else:
            inst.append("")
    Table[i]=inst
    
dfDA=pd.DataFrame(data=Table).transpose()
dfDA.columns=Vars
dfDA.to_csv(Path(QCQA / 'DataStatistics_Mean_Std_q99.csv'))
dfDA


# In[945]:


Vars=['PM10 (ug/m3)', 'PM2.5 (ug/m3)', 'O3 (ppb)', 'SO2 (ppb)', 'NO2 (ppb)', 'CO (ppm)']

Instruments=['00',
             '01',
             '02',
             '03',
             '04',
             '05',
             '06',
             '07',
             '08',
             '09',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '17',
             '20',
             '21',
             '22',
             '23',
             '24',
             '25',
             '26',
             '27']

Table={}

for i in Instruments:
    inst=[]
    for var in Vars:
        varname='{}_{}'.format(i,var)
        if varname in df.columns:
            inst.append("{:.1f} ({:.1f})".format(df[varname].mean(),df[varname].std()))
            #print(varname,"{:.1f}".format(len(df[varname].dropna())/len(df[varname])*100))
        else:
            inst.append("")
    Table[i]=inst
    
dfDA=pd.DataFrame(data=Table).transpose()
dfDA.columns=Vars
dfDA
dfDA.to_csv(Path(QCQA / 'DataMeanSTD.csv'))


# ### Reference air quality

# In[928]:


for i in df.columns:
    if i.startswith('00'):
        print(i)


# In[929]:


df[['00_Relative_Humidity (%)','00_Ambient_Temp (degC)']].plot(subplots=True,figsize=(12,12))
#plt.savefig(Path(FigDir / 'Ref_T_and_RH.png'), dpi=90, bbox_inches='tight', pad_inches=0)


# In[930]:


for i in df.columns:
    if i.startswith('00'):
        print(i)


# In[931]:


df[['00_SO2 (ppb)']].plot(subplots=True,figsize=(12,12))
#plt.savefig(Path(FigDir / '20210928_Ref_SO2.png'), dpi=90, bbox_inches='tight', pad_inches=0)


# In[932]:


df[['00_PM10 (ug/m3)','00_PM2.5 (ug/m3)','00_SO2 (ppb)', '00_CO (ppm)', '00_O3 (ppb)', '00_NO2 (ppb)']].plot(subplots=True,figsize=(12,12))
#plt.savefig(Path(FigDir / '20210928_Ref_aqs.png'), dpi=90, bbox_inches='tight', pad_inches=0)


# In[933]:


VarNames=['00_PM10 (ug/m3)', '00_PM2.5 (ug/m3)', '00_O3 (ppb)', '00_SO2 (ppb)', '00_NO2 (ppb)', '00_CO (ppm)']
VarNames.append('Time')


# In[934]:


VarNames+['Time']


# In[935]:


VarNames=['00_PM10 (ug/m3)', '00_PM2.5 (ug/m3)', '00_O3 (ppb)', '00_SO2 (ppb)', '00_NO2 (ppb)', '00_CO (ppm)']

dftmp=df[VarNames].resample('5min').mean()
dftmp['Time'] = dftmp.index.map(lambda x: x.strftime("%H:00"))
diurnal = dftmp[['Time']+VarNames].groupby('Time').describe()[VarNames]



# In[936]:


diurnal['00_PM10 (ug/m3)']['50%']


# In[937]:


VarNames=['00_PM10 (ug/m3)', '00_PM2.5 (ug/m3)', '00_O3 (ppb)', '00_SO2 (ppb)', '00_NO2 (ppb)', '00_CO (ppm)']

for row in range(len(VarNames)):
    print(row,diurnal[VarNames[i]]['50%'].values)


# In[ ]:


fig, axs = plt.subplots(6,1, sharex='col',sharey='row',gridspec_kw={'hspace':0.1, 'wspace':0.1}, figsize=(12,12))

VarNames=['00_PM10 (ug/m3)', '00_PM2.5 (ug/m3)', '00_O3 (ppb)', '00_SO2 (ppb)', '00_NO2 (ppb)', '00_CO (ppm)']

dftmp=df[VarNames].resample('5min').mean()
dftmp['Time'] = dftmp.index.map(lambda x: x.strftime("%H:00"))
diurnal = dftmp[['Time']+VarNames].groupby('Time').describe()[VarNames]

for i in range(len(VarNames)):
    axs[i].plot(diurnal.index, diurnal[VarNames[i]]['50%'].values, linewidth=2.0,label=VarNames[i], alpha=0.5, color='b')
    #axs[i,0].plot(diurnalref.index, diurnal['50%'], linewidth=2.0,label='Reference', alpha=0.5)
    axs[i].plot(diurnal.index, diurnal[VarNames[i]]['75%'], color='b')
    axs[i].plot(diurnal.index, diurnal[VarNames[i]]['25%'], color='b')
    axs[i].fill_between(diurnal.index, diurnal[VarNames[i]]['50%'], diurnal[VarNames[i]]['75%'], alpha=.25, facecolor='b')
    axs[i].fill_between(diurnal.index, diurnal[VarNames[i]]['50%'], diurnal[VarNames[i]]['25%'], alpha=.25, facecolor='b')


    axs[i].set_ylabel(VarNames[i].replace("00_",""))
#axs[int(i/4),i%4].set_xlim(0,dftmp[refvar].max())
#axs[int(i/4),i%4].set_ylim(0,dftmp[refvar].max())

#axs[int(i/4),i%4].text(0.3,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(res.intercept,res.slope, res.rvalue), fontsize=10, transform=axs[int(i/4),i%4].transAxes)

#axs[int(i/4),i%4].set_title(lcvars[i].split("_")[0], y=1.0, pad=-14, fontsize=14)

axs[i].set_xlim(0, 23)                                                                                                                                                                                                                                                          
axs[i].set_xticks([i for i in range(0,24,3)])


fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False )
plt.grid(False)
plt.xlabel("Time of day", fontsize=16)
#plt.ylabel("Reference (orange) vs low-cost (blue) {}".format(VarNames[i]), fontsize=16)

#plt.savefig(Path(FigDir / '20210928_Diurnal_refvars.png'), dpi=90, bbox_inches='tight', pad_inches=0)


# In[ ]:


'00_Relative_Humidity (%)','00_Ambient_Temp (degC)'


# In[ ]:


fig, axs = plt.subplots(2,1, sharex='col',sharey='row',gridspec_kw={'hspace':0.1, 'wspace':0.1}, figsize=(12,6))

VarNames=['00_Relative_Humidity (%)','00_Ambient_Temp (degC)']

dftmp=df[VarNames].resample('5min').mean()
dftmp['Time'] = dftmp.index.map(lambda x: x.strftime("%H:00"))
diurnal = dftmp[['Time']+VarNames].groupby('Time').describe()[VarNames]

for i in range(len(VarNames)):
    axs[i].plot(diurnal.index, diurnal[VarNames[i]]['50%'].values, linewidth=2.0,label=VarNames[i], alpha=0.5, color='b')
    #axs[i,0].plot(diurnalref.index, diurnal['50%'], linewidth=2.0,label='Reference', alpha=0.5)
    axs[i].plot(diurnal.index, diurnal[VarNames[i]]['75%'], color='b')
    axs[i].plot(diurnal.index, diurnal[VarNames[i]]['25%'], color='b')
    axs[i].fill_between(diurnal.index, diurnal[VarNames[i]]['50%'], diurnal[VarNames[i]]['75%'], alpha=.25, facecolor='b')
    axs[i].fill_between(diurnal.index, diurnal[VarNames[i]]['50%'], diurnal[VarNames[i]]['25%'], alpha=.25, facecolor='b')


    axs[i].set_ylabel(VarNames[i].replace("00_",""))
#axs[int(i/4),i%4].set_xlim(0,dftmp[refvar].max())
#axs[int(i/4),i%4].set_ylim(0,dftmp[refvar].max())

#axs[int(i/4),i%4].text(0.3,0.1,"y={:.1f}x+{:.1f} ({:.2f})".format(res.intercept,res.slope, res.rvalue), fontsize=10, transform=axs[int(i/4),i%4].transAxes)

#axs[int(i/4),i%4].set_title(lcvars[i].split("_")[0], y=1.0, pad=-14, fontsize=14)

axs[i].set_xlim(0, 23)                                                                                                                                                                                                                                                          
axs[i].set_xticks([i for i in range(0,24,3)])


fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False )
plt.grid(False)
plt.xlabel("Time of day", fontsize=16)
#plt.ylabel("Reference (orange) vs low-cost (blue) {}".format(VarNames[i]), fontsize=16)

#plt.savefig(Path(FigDir / '20210928_Diurnal_refTandRH.png'), dpi=90, bbox_inches='tight', pad_inches=0)


# In[ ]:





# ### Bivariate plots

# In[ ]:


# Define the settings for the windrose that is being created.
def plot_ppollrose(dfc,WD='00_Wind_Direction (deg)',WS='00_Wind_Speed (m/s)',CO='00_PM10 (ug/m3)',title=""):                                                                                                                                                                                                                                                   
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
    #plt.savefig(output,dpi=90, bbox_inches = "tight")  
     
    #plt.close()


# In[ ]:


#plot_ppollrose(df.loc['2021-09-15'],CO='00_PM10 (ug/m3)', title='Vaal')


# In[ ]:




