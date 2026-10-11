import streamlit as st

st.set_page_config(page_title="JAMB Pro", page_icon="🎓", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700;800&display=swap');
.big-title {font-family:'Poppins'; font-size:42px; font-weight:800; background: linear-gradient(90deg,#6a11cb 0%, #2575fc 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
.card {background: linear-gradient(135deg,#667eea 0%,#764ba2 100%); padding:20px; border-radius:20px; color:white; margin-bottom:15px;}
.free-badge {background:#00ff88; color:black; padding:5px 15px; border-radius:20px; font-weight:800;}
</style>
<div class="big-title">JAMB<br>AGGREGATOR</div>
<p>Calculate your JAMB & UNILAG chances</p>
""", unsafe_allow_html=True)

st.markdown('<div class="card">JAMB Score <span class="free-badge">FREE</span><br>Enter your 4 subjects</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    s1 = st.number_input("Subject 1", 0, 100, 70)
    s2 = st.number_input("Subject 2", 0, 100, 70)
with col2:
    s3 = st.number_input("Subject 3", 0, 100, 70)
    s4 = st.number_input("Subject 4", 0, 100, 77)

if st.button("CALCULATE MY FUTURE", use_container_width=True):
    total = s1+s2+s3+s4
    st.balloons()
    st.success(f"Your JAMB Score: {total} / 400")
    
    if total >= 300:
        st.markdown("**Genius! Recommended: Medicine, Law, Pharmacy**")
    elif total >= 250:
        st.markdown("**You try! Recommended: Engineering, Computer Science**")
    elif total >= 200:
        st.markdown("**Good! Recommended: Microbiology, Business Admin**")
    else:
        st.markdown("**Don't give up! Recommended: Arts, Education**")

    st.divider()
    
    st.markdown("""
    <div style="background: linear-gradient(135deg,#ff512f,#dd2476); padding:20px; border-radius:20px; color:white;">
    <h2>UNILAG Aggregate (PAID)</h2>
    <p>Pay 500 Naira to unlock!</p>
    <p><b>PalmPay: 8028519092</b><br>Name: Shola Taiwo</p>
    <p>WhatsApp receipt to 08028519092</p>
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_input("Enter Unlock Code:", placeholder="Enter code after payment")
    SECRET = "UNILAG2025"
    
    if code == SECRET:
        st.success("UNLOCKED! Welcome boss!")
        waec = st.slider("O'Level Points (5 As = 20)", 0, 20, 20)
        putme = st.number_input("PutMe Score (0-30)", 0, 30, 25)
        if st.button("Calculate UNILAG Aggregate", use_container_width=True):
            aggregate = (total/8) + waec + putme
            st.snow()
            st.metric("Your UNILAG Aggregate", f"{aggregate:.2f} / 100")
    elif code:
        st.error("Wrong code! Pay first")

st.divider()
try:
    st.image("founder.jpg", caption="Founder - Shola Taiwo", use_container_width=True)
except:
    try:
        st.image("IMG-20260211-WA0043.jpg", caption="Founder - Shola Taiwo", use_container_width=True)
    except:
        st.warning("Add founder.jpg to GitHub to show your pic")

st.markdown("""
<div style="background:black; padding:25px; border-radius:20px; border:3px solid #00ff88; text-align:center;">
<h2 style="color:#00ff88;">Support The Founder</h2>
<p style="color:white;">Built by a student for students!</p>
<h1 style="color:#00ff88;">PalmPay: 8028519092</h1>
<p style="color:#aaa;">Shola Taiwo | 08028519092</p>
</div>
""", unsafe_allow_html=True)
