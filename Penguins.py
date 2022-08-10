import streamlit as st
import pandas as pd
import numpy as np
import joblib

from PIL import Image

# Side bar
st.sidebar.title('Sidebar')
side_button = st.sidebar.button('Press Me!')
if side_button:
    st.write('Sidebar pressed')

# Header
st.image('Images/penguins.jpg')
st.title('Streamlit with Penguins')
st.header('This is a header')
st.subheader('This is a subheader')
st.write('Standard st.write')
st.markdown('Markdown **syntax** *works*')
'Markdown'
'# Magic'
st.header('Widget Functionality')

button1 = st.button('This is a button')
if button1:
    st.write('You clicked me')
st.subheader('Checkbox')
check = st.checkbox('Please check this box')
button2 = st.button('Is box checked?')
if button2:
    if check:
        st.write('The box was checked!')
    else:
        st.write('The box was not checked!')
st.subheader('Radio Button')
animal_options = ['Cats', 'Dogs', 'Guinea Pigs', 'Bearded Dragons', 'Fish']
fav_animal = st.radio('Which animal is your favorite?', animal_options)
button3 = st.button('Submit Animal')
if button3:
    st.write(f'You selected {fav_animal} as your favorite animal')
    if fav_animal == 'Cats':
        st.write('MEOW')
    elif fav_animal == 'Dogs':
        st.write('WHOOF')
    elif fav_animal == 'Guinea Pigs':
        st.write('SQUEAL')
    elif fav_animal == 'Bearded Dragons':
        st.write('HISS')
    else:
        st.write('GLOG GLOG')

st.subheader('SelectBox')
fav_animal2 = st.selectbox('Which animal is your favorite', animal_options)
button4 = st.button('Submit your animal')
if button4:
    st.write(f'You selected {fav_animal2} as your favorite animal')
    if fav_animal2 == 'Cats':
        st.write('MEOW')
    elif fav_animal2 == 'Dogs':
        st.write('WHOOF')
    elif fav_animal2 == 'Guinea Pigs':
        st.write('SQUEAL')
    elif fav_animal2 == 'Bearded Dragons':
        st.write('HISS')
    else:
        st.write('GLOG GLOG')

st.subheader('Multiple Selections')
like_animal = st.multiselect('Which animals do you like?', animal_options)
button5 = st.button('Animals you like')
if button5:
    st.write(like_animal)
    st.write(f'Your first submission was {like_animal[0]}')

st.subheader('Slider Input')
num_pets = st.slider('How many pets is too much?', 2, 20, 2, 2)
if st.button('All the pets'):
    st.write(num_pets)

st.subheader('Text and Numeric Input')
in_text = st.text_input("What is your pet's name?", value="I don't have a pet")
st.write("Pet's name:", in_text)
st.write(in_text)
in_num = st.number_input("How many pets do you have?", min_value=0)
st.write(f"I have {in_num} pets")
st.write(in_num)    


