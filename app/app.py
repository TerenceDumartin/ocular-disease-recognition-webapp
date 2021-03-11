import streamlit as st
from  datetime import datetime
import pandas as pd
import requests
from PIL import Image

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

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
# .css-9eqr5v{
#     display: none !important;
# }

# .css-1syfshr {
#     background-color: #ffdd54;
# }

# .css-9ycgxx{
#     color: #ffffff;
# }

# .css-6hirgd {
#     color: #ffffff;
# }
# .css-paap06-EmotionIconBase {
#     color: #ffffff
# }

# .css-2trqyj {
#     color: #ffce06 !important;
#     width: auto;
#     border: 1px solid rgb(255 255 255) !important;
# }

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

row1_1, row1_2 = st.beta_columns((2,2))

prediction = None

with row1_1:
    st.markdown("""

        # O-D Recognition

        ##

        Upload an eye fundus !

        Our **Artificial Intelligence** trained with more than **100 000 000** parameters
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        gonna tell you what you have.
        #####
        """)

    uploaded_file = st.file_uploader("Upload an eye", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, width=100, use_column_width='never')



    st.set_option('deprecation.showfileUploaderEncoding', False)

    params = {
        'X': uploaded_file
    }

    if st.button('Let me see'):
        response = requests.get('https://odrdockerimage-4rkl6m35oq-ew.a.run.app/predict/', params=params)
        prediction = (response.json()['X'])

with row1_2:
    st.write("""Ceci est notre réponse !""")
    if prediction:
        st.write(f'{prediction}')


#######################################
# Button Resquest API
#######################################
