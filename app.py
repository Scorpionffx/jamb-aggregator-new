import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import random

st.set_page_config(page_title="JAMB Pro", page_icon="🎓", layout="centered")

# CODES
CODES = {
    "UNILAG2025": ["UNILAG"],
    "BENIN2025": ["UNIBEN"],
    "OAU2025": ["OAU"],
    "UI2025": ["UI"],
    "ALLIN2025": ["UNILAG", "UNIBEN", "OAU", "UI"]
}

# COURSE FINDER LOGIC
def get_courses(score):
    if score >= 300:
        return ["Medicine", "Law", "Pharmacy", "Nursing", "Engineering (All)", "Computer Science", "Accounting", "Economics"]
    elif score >= 260:
        return ["Engineering (Civil, Mech)", "Computer Science", "Architecture", "Microbiology", "Business Admin", "Mass Comm", "Biochemistry"]
    elif score >= 220:
        return ["Microbiology", "Business Admin", "Public Admin", "Political Science", "Sociology", "Education Courses", "Botany", "Zoology"]
    elif score >= 180:
        return ["Education", "Arts (English, History)", "Agric Science", "Adult Education"]
    else:
        return ["Consider Polytechnics / Change of Institution - Don't Give Up!"]

# RESULT CARD GENERATOR
def create_card(score):
    img = Image.new('RGB', (1080, 1080), color=(106, 17, 203))
    draw = ImageDraw.Draw(img)
    # gradient effect with rectangles
    draw.rectangle([0,0,1080,1080], fill=(37,117,252))
    draw.rectangle([50,50,1030,1030], fill=(255,255,255), outline=(0,255,136), width=10)
    try:
        font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", 90)
        font_mid = ImageFont.truetype("DejaVuSans-Bold.ttf", 50)
        font_small = ImageFont.truetype("DejaVuSans.ttf", 40)
    except:
        font_big = ImageFont.load_default()
        font_mid = ImageFont.load_default()
        font_small = ImageFont.load_default()

    draw.text((540,200), "JAMB PRO", font=font_mid, fill=(106,17,203), anchor="mm")
    draw.text((540,350), f"{score}/400", font=font_big, fill=(0,0,0), anchor="mm")
    draw.text((540,500), "I calculated my JAMB score!", font=font_mid, fill=(0,0,0), anchor="mm")
    draw.text((540,650), "Check yours: jamb-pro.streamlit.app", font=font_small, fill=(100,100,100), anchor="mm")
    draw.text((540,750), "PalmPay: 8028519092", font=font_small, fill=(221,36,118), anchor="mm")
    return img

# UI START
st.markdown("<h1 style='text-align:center; background: linear-gradient(90deg,#6a11cb,#2575fc); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-size:45px;'>JAMB PRO</h1><p style='text-align:center;'>Free Calculator + Course Finder</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    s1 = st.number_input("English", 0, 100, 70)
    s2 = st.number_input("Maths", 0, 100, 70)
with col2:
    s3 = st.number_input("Subject 3", 0, 100, 70)
    s4 = st.number_input("Subject 4", 0, 100, 70)

if "total" not in st.session_state:
    st.session_state.total = 0

if st.button("CALCULATE MY FUTURE", use_container_width=True, type="primary"):
    total = s1+s2+s3+s4
    st.session_state.total = total
    st.balloons()
    st.success(f"Total: {total} / 400")

    # 1. COURSE FINDER
    st.subheader("1. Courses You Can Get")
    courses = get_courses(total)
    for c in courses:
        st.markdown(f"- {c}")

    # 2. SHARE CARD
    st.subheader("2. Share Your Result")
    img = create_card(total)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    st.image(img, caption="Your Viral Result Card")
    st.download_button("Download Card For WhatsApp Status", buf.getvalue(), "jamb_pro_result.png", "image/png", use_container_width=True)

# QUIZ - FEATURE 7
st.divider()
st.subheader("3. Daily Post-UTME Quiz (FREE)")
quiz_q = [
    {"q": "What is the capital of Nigeria?", "opts": ["Lagos", "Abuja", "Kano"], "ans": "Abuja"},
    {"q": "JAMB is scored out of?", "opts": ["400", "500", "300"], "ans": "400"},
    {"q": "UNILAG was founded in?", "opts": ["1962", "1970", "1960"], "ans": "1962"},
]
if "qi" not in st.session_state:
    st.session_state.qi = 0

q = quiz_q[st.session_state.qi % len(quiz_q)]
st.write(f"**Q: {q['q']}**")
choice = st.radio("Answer", q["opts"], key=f"q{st.session_state.qi}")
if st.button("Check Answer"):
    if choice == q["ans"]:
        st.success("Correct! Omo you sabi!")
    else:
        st.error(f"Wrong! Answer is {q['ans']}")
    st.session_state.qi += 1
    st.rerun()

# 5. PAID AGGREGATORS WITH DIFFERENT CODES
st.divider()
st.markdown("""
<div style="background: linear-gradient(135deg,#ff512f,#dd2476); padding:20px; border-radius:20px; color:white; text-align:center;">
<h2>UNLOCK UNIVERSITY AGGREGATORS</h2>
<p>Pay to PalmPay 8028519092 - Shola Taiwo</p>
<p>UNILAG:500 | UNIBEN:500 | ALL SCHOOLS:1200</p>
<p>WhatsApp receipt to 08028519092 to get code</p>
</div>
""", unsafe_allow_html=True)

code_input = st.text_input("Enter Your Unlock Code Here", placeholder="e.g. UNILAG2025 or ALLIN2025").upper().strip()
unlocked = CODES.get(code_input, [])

if code_input and not unlocked:
    st.error("Invalid code! Pay first")

tabs = st.tabs(["UNILAG", "UNIBEN", "OAU", "UI"])
formulas = {
    "UNILAG": "(JAMB/8) + Olevel(20) + Putme(30)",
    "UNIBEN": "(JAMB/8) + Putme(70) + Olevel(30) then /1.7",
    "OAU": "(JAMB/8) + Putme(50) + Olevel(20)",
    "UI": "(JAMB/8) + Putme(50)"
}

for idx, uni in enumerate(["UNILAG", "UNIBEN", "OAU", "UI"]):
    with tabs[idx]:
        if uni in unlocked:
            st.success(f"{uni} UNLOCKED!")
            if st.session_state.total == 0:
                st.warning("Calculate JAMB score first at top!")
            else:
                st.write(f"Formula: {formulas[uni]}")
                olevel = st.slider(f"{uni} OLevel Points", 0, 30, 20, key=uni+"ol")
                putme = st.number_input(f"{uni} Post-UTME Score", 0, 100, 70, key=uni+"pu")
                if st.button(f"Calculate {uni}", key=uni+"btn"):
                    agg = (st.session_state.total/8) + olevel + (putme*0.3 if uni=="UNILAG" else putme*0.5)
                    st.metric(f"{uni} Aggregate", f"{agg:.2f}")
        else:
            st.markdown(f"LOCKED! Need code for {uni}")
            st.caption(f"Code for {uni}: {uni[:3]}...2025 or buy ALLIN2025")

st.divider()
try:
    st.image("founder.jpg", caption="Founder Support", use_container_width=True)
except:
    st.info("Add founder.jpg to GitHub to show your support pic")

st.markdown("<div style='background:black;padding:15px;border-radius:15px;text-align:center;color:white;'><h3 style='color:#00ff88;'>PalmPay: 8028519092</h3><p>Shola Taiwo - Founder</p></div>", unsafe_allow_html=True)
