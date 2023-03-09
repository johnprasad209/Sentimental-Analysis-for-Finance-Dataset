import streamlit as st
import joblib
st.title('Financial News classification')
test_model = joblib.load('Finance News')
ip = st.text_input('Enter your Tweet : ')
op = test_model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
