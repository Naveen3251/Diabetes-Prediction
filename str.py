import pickle as pk
import streamlit as st
model=pk.load(open('Diabetes.pkl','rb'))
def run():
    st.title("DIABETES PREDICTION")
    st.image('diabetes.jpg')
    #name
    name=st.text_input("Enter your name")
    #Id number
    id=st.text_input("Patient ID Number")
    #Pregnencies
    pr=st.number_input("Enter Pregnencies",value=0)
    #Glucose
    gl=st.number_input("Enter Glucose Level")
    #bp
    bp=st.number_input("Enter Blood Pressure")
    #skinthickness
    sk=st.number_input("Enter Skin Thickness")
    #insulin
    ins=st.number_input("Enter Insulin Level")
    #bmi
    Bmi=st.number_input("Enter BMI")
    #dpf
    dpf=st.number_input("Enter Diabetes Pedigree Function")
    #Age
    age=st.number_input("Enter Your Age")
    if(st.button("SUBMIT")):
        lis=[[pr,gl,bp,sk,ins,Bmi,dpf,age]]
        prediction=model.predict(lis)
        lc=[str(i) for i in prediction]
        ans=int("".join(lc))
        if ans==0:
            st.success("Name: "+name)
            st.success("ID: "+id)
            st.success("No Diabetes !!!")
        else:
            st.error("Name: " + name)
            st.error("ID: " + id)
            st.error("You have Diabetes !!!")
            st.error("No Worry!!! Follow the Doctor's Prescription")
run()