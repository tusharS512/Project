from json import load
from xmlrpc.client import Boolean
import streamlit as st
import base64
import pandas as pd
import numpy as np
import time 
import matplotlib.pyplot as plt
from multiapp import MultiApp
from Apps import asg1, asg2, asg3, asg5, asg6, asg7, asg8
@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("image.jpg")
img1 = get_img_as_base64("im.jpg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img1}");
background-size: 100%;
}}
[data-testid="stSidebar"] > div:first-child {{
backgroud-color: black;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#variables
disrad = False

st.title("Data Analysis Tool")

file = st.file_uploader("Enter Dataset first to Proceed", type=['csv','txt'], accept_multiple_files=False, disabled=False)
# data = pd.read_csv(file)

def load_file():
    df = pd.read_csv(file)
    # st.header("Dataset Table")
    # st.dataframe(df, width=1000, height=500)
    return df
if file:
    data = load_file()  
    
    app = MultiApp()
    
    app.add_app("Assignment 1", asg1.app)
    app.add_app("Assignment 2", asg2.app)
    app.add_app("Assignment 3", asg3.app)
    app.add_app("Assignment 5", asg5.app)
    app.add_app("Assignment 6", asg6.app)
    app.add_app("Assignment 7", asg7.app)
    app.add_app("Assignment 8", asg8.app)
   
    # The main app
    app.run(data)

