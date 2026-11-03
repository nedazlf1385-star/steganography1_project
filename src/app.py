from stegano import lsb
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Stegano Project')
option = st.sidebar.selectbox('Select Your option: ',
                              ('Hide Text', 'Reveal Text'))

if option == 'Hide Text':
    host_pic = st.file_uploader('Select Your Image', type=['png', 'jpg'])
    secret_text = st.text_area('Enter Your text to Hide')

    if host_pic and secret_text:
        if st.button('Hide'):
            temp_img = Image.open(host_pic)
            final_img = lsb.hide(temp_img, secret_text)
            final_img.save('./final_img_pars.png')
            st.success('Data Hide in Your pic')

elif option == 'Reveal Text':
    final_secreted_image = st.file_uploader('Select Image for reval', type=['png'])

    if final_secreted_image:
        temp_image = Image.open(final_secreted_image)

        secret_txt_reaveld = lsb.reveal(temp_image)

        if st.button('Reveal:'):

            if secret_txt_reaveld != None:
                st.write(secret_txt_reaveld)
                st.success('Data Revealed')
            else:
                st.write(f"text can not extract")