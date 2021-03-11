import streamlit as st
from  datetime import datetime
import pandas as pd
import requests
from PIL import Image

'''
# Ocular Disease Recognition


'''

'''

'''
###### #191919 #FFCD00 #F5D95A #DCDCDC #FFFFFF
CSS = """
h1 {
    color: #191919;
    text-align: center;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
}
body {
    background-color: #FFFFFF ;
}


"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

st.sidebar.markdown('''
                    # Ocular Disease Recognition
                    '''
        )



uploaded_file = st.sidebar.file_uploader("Upload an eye", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, width=100, use_column_width='never')



st.set_option('deprecation.showfileUploaderEncoding', False)



params = {
        'X': uploaded_file
    }

#######################################
# Button Resquest API
#######################################
if st.button('Let me see'):
    response = requests.get('https://odrdockerimage-4rkl6m35oq-ew.a.run.app/predict/', params=params)
    prediction = (response.json()['X'])

    st.write(f'{prediction}')

