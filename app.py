import streamlit as st

st.set_page_config(page_title="JAMB PRO", page_icon="🎓", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700;800&display=swap');
.big-title {font-family:'Poppins'; font-size:42px; font-weight:800; line-height:1.1; background: linear-gradient(90deg,#6a11cb 0%, #2575fc 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
.card {background: linear-gradient(135deg,#667eea 0%,#764ba2 100%); padding:20px; border-radius:20px; color:white; margin-bottom:15px; box-shadow: 0 10px 20px rgba(0,0,0,0.2);}
.free-badge {background:#00ff88; color:black; padding:5px 15px; border-radius:20px; font-weight:800;}
</style>
<div class="big-title">JAMB<br>AGGREGATOR</div>
<p style="font-size:18px;">✨ Calculate your JAMB & UNILAG chances ✨</p>
""", unsafe_allow_html=True)

st.markdown('<div class="card">🎓 <b>JAMB Score</b> <span class="free-badge">FREE</span><br>Enter your 4 subjects</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    s1 = st.number_input("Subject 1 📚", 0, 100, 70)
    s2 = st.number_input("Subject 2 📚", 0, 100, 70)
with col2:
    s3 = st.number_input("Subject 3 📚", 0, 100, 70)
    s4 = st.number_input("Subject 4 📚", 0, 100, 77)

if st.button("🚀 CALCULATE MY FUTURE ✨", use_container_width=True):
    total = s1+s2+s3+s4
    st.balloons()
    st.success(f"### 🎉 Your JAMB Score: **{total} / 400**")
    
    if total >= 300:
        st.markdown("#### 🎯 Omo you be genius! Recommended: 🔥 **Medicine, Law, Pharmacy**")
    elif total >= 250:
        st.markdown("#### 🔥 You try! Recommended: **Engineering, Computer Science, Nursing**")
    elif total >= 200:
        st.markdown("#### ✅ Good! Recommended: **Microbiology, Business Admin**")
    else:
        st.markdown("#### 💪 Don't give up! Recommended: **Arts, Education**")

    st.divider()
    
    # --- PAID UNILAG ---
    st.markdown("""
    <div style="background: linear-gradient(135deg,#ff512f,#dd2476); padding:20px; border-radius:20px; color:white;">
    <h2>🔒 UNILAG Aggregate (PAID)</h2>
    <p>💰 Pay ₦500 to unlock!</p>
    <p><b>PalmPay: 8028519092</b><br>Name: Shola Taiwo</p>
    <p>WhatsApp receipt to 08028519092</p>
    </div>
    """, unsafe_allow_html=True)
    
    code = st.text_input("🔑 Enter Unlock Code:",
