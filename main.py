import os
import streamlit as st
dossier = os.path.dirname(__file__)
st.write (os.path.dirname(__file__))
file_to_check = os.path.join(dossier, 'static')
if os.path.isdir(file_to_check) : 
        st.write("YEEEEEEESSSSSSS...!!!!")
else: 
        st.write("NO !... :/")

items = os.listdir(file_to_check)
for item in items : 
        st.write(item)
