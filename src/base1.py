# start with imports
 
import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


#wrangle 
def wrangle(filepath):
    return pd.read_csv(filepath)
def wrangle(filepath):
    df = pd.read_csv(filepath)

    # drop the columns that has not approprite data information

    drop_columns = ['AGE', 'Flag and Footnotes']
    # I am dropping "Flag and Footnotes" becasue the entire columns has no data on it

    df = df.drop(columns=drop_columns)
    return df 



if __name__ == '__main__':
 df = wrangle(r'C:\Users\xende\Downloads\CausesOfDeath_France_2001-2008.csv')
 df.to_csv('capstone002_Cleaned.csv', index=False)