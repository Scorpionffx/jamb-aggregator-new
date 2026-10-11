import streamlit as st

st.set_page_config(page_title="JAMB AGGREGATOR", page_icon="🎓", layout="centered")

# --- HEADER ---
st.markdown("""
<style>
.big-title {font-size:38px; font-weight:800; background: linear-gradient(90deg,#6a11cb,#2575fc); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
</style>
<div class="big-title">JAMB AGGREGATOR</div>
<p>Calculate your JAMB & UNILAG chances</p>
""", unsafe_allow_html=True)

# --- JAMB FREE ---
st.subheader("JAMB Score (FREE)")
s1 = st.number_input("Subject 1", 0, 100, 70)
s2 = st.number_input("Subject 2", 0, 100, 70)
s3 = st.number_input("Subject 3", 0, 100, 70)
s4 = st.number_input("Subject 4", 0, 100, 77)

if st.button("🚀 CALCULATE MY FUTURE"):
    total = s1+s2+s3+s4
    st.success(f"Your Score: {total} / 400")
    if total >= 300:
        st.write("🎯 Recommended: 🔥 Medicine, Law, Pharmacy, Architecture")
    elif total >= 200:
        st.write("🎯 Recommended: Computer Science, Engineering, Nursing")
    else:
        st.write("🎯 Recommended: Education, Arts, Management")

    st.divider()
    
    # --- UNILAG PAID LOCK ---
    st.subheader("🔒 UNILAG Aggregate (PAID - ₦500)")
    st.warning("Pay ₦500 to PalmPay: 8028519092 | Name: Shola Taiwo\nThen WhatsApp 08028519092 for unlock code")
    
    code = st.text_input("Enter Unlock Code:", type="password")
    
    # YOUR SECRET UNLOCK CODE - Change it!
    SECRET_CODE = "UNILAG2025"
    
    if code == SECRET_CODE:
        st.success("✅ Unlocked! Now calculate UNILAG")
        jamb = total
        waec = st.slider("O'Level Points (5 As = 20)", 0, 20, 20)
        putme = st.number_input("PutMe Score (0-30)", 0, 30, 25)
        if st.button("Calculate UNILAG Aggregate"):
            aggregate = (jamb/8) + waec + putme
            st.balloons()
            st.metric("Your UNILAG Aggregate", f"{aggregate:.2f}")
            if aggregate >= 70:
                st.success("🔥 High chance for Medicine/Law!")
            elif aggregate >= 60:
                st.info("✅ Good chance for competitive courses")
            else:
                st.warning("Try less competitive course")
    elif code != "":
        st.error("❌ Wrong code! Pay first and WhatsApp for correct code")

# --- SUPPORT FOUNDER (OPTIONAL) ---
st.divider()
st.markdown("""
<div style="background:black; padding:20px; border-radius:15px; border:2px solid #00ff88;">
<h2 style="color:#00ff88; text-align:center;">💚 Support The Founder</h2>
<p style="color:#00ff88; text-align:center;">This project was built by a student. Your support keeps it alive!</p>
<h1 style="color:#00ff88; text-align:center;">PalmPay: 8028519092</h1>
<p style="color:white; text-align:center;">Shola Taiwo</p>
</div>
""", unsafe_allow_html=True)
