import streamlit as st

st.set_page_config(page_title="JAMB Aggregator Pro", page_icon="🎓", layout="centered")

# --- PREMIUM DESIGN ---
st.markdown("""
<style>
.main-box {background: linear-gradient(135deg,#667eea,#764ba2); padding:30px; border-radius:20px; color:white; text-align:center;}
.founder-card {background:white; padding:15px; border-radius:15px; box-shadow:0 4px 15px rgba(0,0,0,0.1); text-align:center; margin:20px 0;}
.support-box {background:#000; color:#00FF99; padding:20px; border-radius:15px; text-align:center; border:2px solid #00FF99;}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-box"><h1>🎓 JAMB SCORE AGGREGATOR PRO</h1><p>Built by Future Tech Founder</p></div>', unsafe_allow_html=True)

# --- FOUNDER SECTION ---
st.markdown('<div class="founder-card">', unsafe_allow_html=True)
try:
    st.image("founder.jpg", width=180)
    st.markdown("### 👨‍💻 Founder: Taiwo David")
    st.caption("SSS2 | Aspiring Tech Entrepreneur | JAMB 2026")
except:
    st.markdown("### 👨‍💻 Founder: Taiwo David")
    st.info("Upload your picture as founder.jpg to show here")
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# --- CALCULATOR ---
name = st.text_input("👤 Your Full Name")
col1, col2 = st.columns(2)
with col1:
    eng = st.number_input("English", 0, 100, 70)
    sub2 = st.number_input("Subject 2", 0, 100, 65)
with col2:
    sub3 = st.number_input("Subject 3", 0, 100, 65)
    sub4 = st.number_input("Subject 4", 0, 100, 65)

def get_courses(score):
    if score >= 300:
        return "🔥 Medicine, Law, Pharmacy, Architecture"
    if score >= 270:
        return "💻 Computer Science, Nursing, Mass Comm"
    if score >= 240:
        return "📊 Biochemistry, Accounting, Economics"
    if score >= 200:
        return "📚 Education, Business Admin, Sociology"
    return "🛠️ IJMB / Pre-degree / Polytechnic - You can still make it!"

if st.button("🚀 CALCULATE MY FUTURE", use_container_width=True):
    total = eng + sub2 + sub3 + sub4
    st.balloons()
    st.success(f"### {name}, Your Score: {total} / 400")
    st.markdown(f"**🎯 Recommended Courses:** {get_courses(total)}")
    if total >= 250:
        st.snow()

st.divider()

# --- SUPPORT ---
st.markdown("""
<div class="support-box">
<h3>💚 Support The Founder</h3>
<p>This project was built by a student. Your support keeps it alive!</p>
<h2>PalmPay: 8028519092</h2>
<p>Name: Shola Taiwo</p>
<p>Thank you Boss! 🙏</p>
</div>
""", unsafe_allow_html=True)

st.caption("© 2026 Taiwo David - JAMB Aggregator Pro v2.0")
