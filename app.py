import streamlit as st
import pickle
import time

st.title("Credit Card Fraud Detection Model")
st.wrtite("Enter the following features to check if the transaction is legitimate or fraudulent")

#load model
model = pickle.load(open("fraud_detection.pkl"), "rb")

features = st.text_input("Input All features")

submit = st.button("Submit")

if submit:
    start = time.time()
    prediction = model.predict(features)
    end = time.time()
    st.write("Prediction time taken: ", round(end - start, 2), "seconds")
    if prediction[0] == 1:
        print("Fraud transaction")
    else:
        print("Legitimate transaction")
