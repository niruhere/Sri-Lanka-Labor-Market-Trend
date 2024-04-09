import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import requests
import pickle
from sklearn.model_selection import train_test_split
rfmodel= st.sidebar.checkbox('Random Forest Regression')
url = 'https://raw.githubusercontent.com/niruhere/Sri-Lanka-Labor-Market-Trend/main/ILOSTAT_SriLanka_LabourMarketTrenddata.csv'
data = pd.read_csv(url)

# Remove unwanted columns "Country", "Source" from the data
data.drop(['Country', 'Source'], axis=1, inplace=True)

# Remove rows having null values(removes 38 out of 1314 records)
data.dropna(axis=0, inplace=True)

# Rename column "Area type" to "Sector", "Sex" to Gender
data.rename(columns = {'Area type':'Sector', 'Sex': 'Gender'}, inplace = True)

if rfmodel:
    
    with st.form("my_form1"):
        
        st.title('Prediction of Labor Force Participation Rate %')
        st.subheader("Please Choose")
        gendergp = st.selectbox("What's your Gender:", ('Female', 'Male'))
        educgp = st.selectbox("What's your Education Level", (data['Education'].unique()))
        secgp = st.selectbox("What's your Sector:", ('Area type: Urban', 'Area type: Rural', 'Area type: National'))
        #yrgp = st.text_input("Select the Year:", max_chars=4)
        yrgp = 0

        """You selected"""
        st.write("Gender:", gendergp )
        st.write("Education Level: ",  educgp)
        st.write("Sector: ",  secgp)
        # st.write("Year: ", yrgp)
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            inputdata = {'Gender': gendergp,
                        'Education': educgp, 
                        'Sector': secgp,
                        'Year': yrgp}
            features = pd.DataFrame(inputdata, index=[0])
            st.dataframe(features, column_order=['Gender', 'Education', 'Sector'], column_config={'Year': None}, hide_index=[0])
            
           
            X = data.Value
            Y = data.drop(['Value'], axis=1)
            # load pickld model from url/path
            url = 'https://raw.githubusercontent.com/niruhere/Sri-Lanka-Labor-Market-Trend/main/random_forest_model.pkl'
            # filename = 'random_forest_model.pkl'
            # loaded_model = pickle.load(open(filename, "rb"))
            # Download the pickle file
            response = requests.get(url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Load the pickle file
                 loaded_model = pickle.loads(response.content)
            else:
                 # Handle the case when the request fails
                 print("Failed to download the pickle file")
            
            predicted_LFPR = loaded_model.predict(features)
            # Print the original prediction
            print("Original prediction:", predicted_LFPR)
            
            st.write("Predicted Labor Force Participation Rate in % :", predicted_LFPR)
        