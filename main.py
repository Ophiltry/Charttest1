# This programmed is made to practing making charts using streamlit and Pandas
# dataframes


import json
import streamlit as st
import pandas as pd
import glob
import datetime
import plotly.express as px  
from streamlit_extras.grid import grid






#grab JSON files 
#===========================================

jsonFilePath = "c:/Users/prest/Desktop/coding/python/graphproject/data/*"

loc_schedules = []
files = glob.glob(jsonFilePath)

for schedules in files:
    with open(schedules, 'r') as f:
        loc_schedules.append(json.load(f))

#creates data frame
schedule_Frame = pd.DataFrame(loc_schedules)

#organizes data frame into usable times


#creates radar chart
#chart_frame = pd.schedule_Frame(dict(
#    number_opens = [len(schedule_Frame['opens'])] ,
#    time = [schedule_Frame['opens']]

#))



#fig = px.line_polar(schedule_Frame, r = len(schedule_Frame['opens']), theta = schedule_Frame['opens'], line_close=True )

fig = px.line_polar(schedule_Frame, r = 'opens', theta ='location', line_close=True )










#st.plotly_chart(schedule_Frame)