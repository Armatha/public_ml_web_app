# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:35:48 2024

@author: amrut
"""
import os
os.chdir('C:/Users/amrut/Downloads/Deploy_Machine_Learning/')


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
# C:/Users/amrut/Downloads/Deploy_Machine_Learning/
Diabetis_model=pickle.load(open('diabetis_model.sav','rb'))
Heart_model=pickle.load(open('heart_model.sav','rb'))

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetis prediction',
                          'Heart disease prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)

if selected=='Diabetis prediction':
    st.title('Diabetis prediction webpage')
    col1,col2,col3=st.columns(3)
    with col1:
            Pregnancies=st.text_input('No of pregnancies')
    with col2:
            Glucose=st.text_input('Glucose level')
    with col3:
            BloodPressure=st.text_input('BloodPressure')
    with col1:
            SkinThickness=st.text_input('SkinThickness')
    with col2:
            Insulin=st.text_input('Insulin')
    with col3:    
            BMI=st.text_input('BMI')
    with col1:
            DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
    with col2:
            Age=st.text_input('Age')
    diabetis=[]
    if st.button('Diabetis Test'):
        diabetis_pred=Diabetis_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if diabetis_pred[0]==0:
            diabetis= 'Non diabetic patient'
        else:
            diabetis= 'diabetic patient'
    st.success(diabetis)             
    
if selected=='Heart disease prediction':
    st.title('Heart disease prediction web page')
    col1,col2,col3=st.columns(3)
    with col1:
            age=st.number_input('Age')
    with col2:
            sex=st.number_input('sex')
    with col3:
            cp=st.number_input('cp')
    with col1:
            trestbps=st.number_input('trestbps')
    with col2:
            chol=st.number_input('chol')
    with col3:    
            fbs=st.number_input('fbsst')
    with col1:
            restecg=st.number_input('restecgst')
    with col2:
            thalach=st.number_input('thalach')
    with col3:    
            exang=st.number_input('exang')
    with col1:
            oldpeak=st.number_input('oldpeak')
    with col2:
            slope=st.number_input('slope')
    with col3:
            ca=st.number_input('ca')
    with col1:
            thal=st.number_input('thal')

    heart=[]
    if st.button('heart test'):
        heart_pred=Heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if heart_pred[0]==0:
            heart='no heart disease'
        else:
            heart='patient has heart disease'
    st.success(heart)
    


