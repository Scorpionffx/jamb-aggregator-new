import streamlit as st

st.set_page_config(page_title="JAMB Aggregator")

try:
    st.image("founder.jpg", width=200)
    st.caption("Founder: Taiwo David - SSS2")
except:
    st.write("Founder: Taiwo David")

st.title("JAMB Score Aggregator")

def courses(s):
    if s>=300:
        return "Medicine, Law, Pharmacy"
    if s>=270:
        return "Computer Science, Nursing"
    if s>=240:
        return "Biochem, Accounting"
    if s>=200:
        return "Education, Business"
    return "IJMB / Polytechnic"

name=st.text_input("Name")
e=st.number_input("English",0,100,70)
s2=st.number_input("Subj 2",0,100,65)
s3=st.number_input("Subj 3",0,100,65)
s4=st.number_input("Subj 4",0,100,65)

if st.button("Calculate"):
    t=e+s2+s3+s4
    st.balloons()
    st.success(f"{name}, Total {t}/400")
    st.info(f"Course: {courses(t)}")

st.write("---")
st.write("Support: PalmPay 8028519092")
st.write("Name: Shola Taiwo")
