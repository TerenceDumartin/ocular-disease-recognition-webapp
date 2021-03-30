import streamlit as st
import streamlit.components.v1 as components
from  datetime import datetime
import pandas as pd
import requests
from PIL import Image
import os
import time
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(
    layout="wide",
    page_title="A-EYE - Detect ocular disease",
    page_icon="👁",
    )


###########################
# 👇      CSS        👇 #
###########################

###### #191919 #FFCD00 #F5D95A #DCDCDC #FFFFFF
CSS = """
h1 {

    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
}
body {
    background-image: url(https://i.stack.imgur.com/HLiKD.jpg);
    background-size: cover;
}

footer {
    display: none !important;
}

.css-1y0tads {
    flex: 1 1 0%;
    width: 100%;
    padding: 5rem 5rem 0rem !important;
}

.stProgress .st-bo {
    background-color: #ffffff !important;
}

.st-bq {
    background-color: #000000 !important;
}

.css-2trqyj {
    color: black;
}

#MainMenu {
    visibility: hidden;
}

.css-a0ecc6 {
    padding-right: 45px;
}

.stButton {
    text-align: center;
}

.stButton > .css-2trqyj {
    color: #ffc001;
    background-color: white;
    border-color: #ffc001;
    border: 2px solid;
    margin-top: 15px;
}

.css-4esp1m {
    padding-left: 3rem;
}

.css-j8zjtb {
    margin-top: -15px;
    padding-left: 1rem;
}

.css-z8kais > stMarkdown > p {
    position: absolute;
    font-size: 10px;
    bottom: -8rem;
    margin-left: 41%;
}

.element-container > iframe  p {
    font-size: 12px;
    text-align: center;
    font-family: 'IBM Plex Sans';
}

iframe {
    position: fixed;
    bottom: 0;
}

.css-1o4i7as {
    height: 170px;
}

.css-9eqr5v {
    display: none;
}

.css-tsy3mu:nth-last-child {
    margin-left: 3rem;
    margin-top: 1rem;
}

.stProgress {
    padding-left: 15px;
    padding-right: 35%;
}

.css-a0ecc6 > div > .element-container:nth-child(5) > .css-tsy3mu {
    margin-top: -4.9em;
    width: 100px !important;
    pointer-events:none;
}

"""
###########################
# BACKGROUND COLOR EXAMPLE
###########################
#https://cdn.wallpapersafari.com/84/18/9EUHPo.jpg

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


###########################
# 👇      CODE        👇 #
###########################

row1_1, row1_2 = st.beta_columns((2,2))

prediction = None
response = None

with row1_1:

    st.image('img/logo-test.png', width=200)
    st.markdown("""
        ##
        """)
    st.markdown("""
        ####

        Upload an eye fundus !

        Our **Artificial Intelligence** trained with more than **100 000 000** parameters<br>
        gonna analyse your eye.
        ###
        """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload an eye", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img_file = uploaded_file
        img = Image.open(img_file)
        st.image(uploaded_file, width=50)

    #st.set_option('deprecation.showfileUploaderEncoding', False)


    if st.button('🩺 Analyse it'):
        #url = 'https://odrdockerimagelight0-4rkl6m35oq-ew.a.run.app/predict'
        url = 'https://odrfinal-4rkl6m35oq-ew.a.run.app/predict'
        temp_image = str(int(time.time())) + "_" + 'img.jpg'
        img.save(temp_image)

        multipart_form_data = {
            "inputImage" : (open(temp_image, "rb"))
        }
        response = requests.post(url, files=multipart_form_data)
        prediction = response.json()

        if os.path.exists(temp_image):
            os.remove(temp_image)


with row1_2:
    if uploaded_file is None:
        st.markdown('''
            #
            #####
            ''')
        st.image('img/gif-to-jpeg.jpg')
    # else:
    #     st.markdown('''
    #         #
    #         #####
    #         ''')
    #     st.image('bg-img-not-gif.png')
    if uploaded_file is not None and response == None:
        st.markdown('''
            #
            #####
            ''')
        st.image('img/bg-img.gif')
        #st.write('Waiting for your upload')
    if response:
        st.markdown('''
            ### Analysing...

            #####

            ''')

        # Add a placeholder
        #latest_iteration = st.empty()
        #bar = st.progress(0)
        list_ = ['- Resizing...', '- Compute image to number...', '- Features Extraction...', '- Neural Analysis...']

        for i in list_:
            # Update the progress bar with each iteration.
            st.text( i + '  ✓')
            #bar.progress(i + 1)
            time.sleep(0.5)
        st.markdown("""
                #####
                """)

    if prediction:
        if prediction == 'Not an eye, upload again !':
            st.markdown("""
                ### Result:
                #####
                """)
            st.image('img/failure.png', width=50)
            st.write('**Oopsi**...')
            #st.image(uploaded_file, width=50)
            st.write('''
                We detect that, the image you just upload is **not an eye fundus** !<br>
                <span style='text-align: center;'>Upload another image.</span>
                ''', unsafe_allow_html=True)
        if prediction == 'Normal':
            st.markdown("""
                ### Result:
                #####
                """)
            #st.image(uploaded_file, width=50)
            st.write(f'''
                Disease: **Normal**
                ''')
            st.write('''
                We detect nothing about your eye ! <br>
                It looks like **normal** ! 👌🏿
                ''', unsafe_allow_html=True)
            st.markdown('''
                ##
                #####
                ''')
            st.text('''
                👈🏿 Don't hesitate to upload another one !
                ''')
        if "prediction" in prediction:
            st.markdown("""
                ### Result:
                #####
                """)

            df = pd.DataFrame(prediction['prediction'], index=['G', 'C', 'A', 'H', 'M', 'O' ]).T

            names = df.columns
            dico_names = {
                'G' : 'Glaucoma',
                'C' : 'Cataract',
                'H' : 'Hypertension',
                'A' : 'Age related Macular Degeneration (A)',
                'M' : 'Pathological Myopia',
                'O' : 'Other diseases/abnormalities ',
                }

            def argm(ser):
                return dico_names[names[np.argmax(ser)]], ser[np.argmax(ser)]
            res = df.apply(argm, axis = 1).item()

            st.write(f'''
                Disease: **{res[0]}** – Certainty: **{round(res[1]*100,2)}%**
                ''')
            #st.write(f' %**')

            #############

            #############

            df_ = pd.DataFrame(df).T.sort_values(by = 0, ascending = False).head(3)
            st.markdown("""
                <style>
                    .stProgress > div > div > div > div {
                        background-color: black;
                    }
                </style>""",unsafe_allow_html=True)

            for i, item in df_.iterrows():
                st.progress(item[0])
                st.text(f'{dico_names[i]}: {round(item[0]*100,2)}%')



components.html(
    """
        <p class='LILOL' style="text-align: center;font-size: 11px;font-family: sans-serif;">Made by <a href="https://github.com/LeoVeron" target= "_blank" style="color: black;text-decoration: none;font-weight: 600;">Léo Véron</a> - <a href="https://github.com/TerenceDumartin" target= "_blank" style="color: black;text-decoration: none;font-weight: 600;">Térence Dumartin</a> - <a href="https://github.com/tom1731" target= "_blank" style="color: black;text-decoration: none;font-weight: 600;">Tom Desire</a> @ Le Wagon Bordeaux</p>
    """,
    height=40,
)

