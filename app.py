import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="JAMB PRO MAX", page_icon="🎓", layout="centered")

st.markdown("""
<style>
.stButton>button {
    background: linear-gradient(90deg,#ff0080,#7928ca)!important;
    color:white!important;
    border-radius: 30px!important;
    font-weight: bold!important;
    height: 55px!important;
    border: none!important;
}
.score-box {
    background: linear-gradient(135deg,#6a11cb,#2575fc);
    padding: 25px; border-radius: 25px; color: white; text-align:center;
}
</style>
""", unsafe_allow_html=True)

CODES = {
    "UNILAG2025": ["UNILAG"],
    "BENIN2025": ["UNIBEN"],
    "OAU2025": ["OAU"],
    "UI2025": ["UI"],
    "ALLIN2025": ["UNILAG","UNIBEN","OAU","UI"],
    "FIRE2025": ["UNILAG","UNIBEN","OAU","UI"]
}

def get_courses(score):
    if score >= 300:
        return ["Medicine, Law, Pharmacy", "Engineering, Computer Science", "Accounting"]
    elif score >= 260:
        return ["Mechanical Eng", "Biochemistry", "Business Admin"]
    elif score >= 220:
        return ["Public Admin", "Education", "Agric"]
    else:
        return ["Polytechnic / Change Course"]

def create_card(score):
    img = Image.new("RGB", (1080, 1080), color=(37,117,252))
    draw = ImageDraw.Draw(img)
    draw.rectangle([40,40,1040,1040], fill=(255,255,255), outline=(0,255,136), width=12)
    try:
        fb = ImageFont.truetype("DejaVuSans-Bold.ttf", 90)
        fm = ImageFont.truetype("DejaVuSans-Bold.ttf", 48)
        fs = ImageFont.truetype("DejaVuSans.ttf", 38)
    except:
        fb = fm = fs = ImageFont.load_default()
    draw.text((540,300), "JAMB PRO MAX", font=fm, fill=(106,17,203), anchor="mm")
    draw.text((540,500), f"{score}/400", font=fb, fill=(0,0,0), anchor="mm")
    draw.text((540,650), "jamb-pro.streamlit.app", font=fs, fill=(37,117,252), anchor="mm")
    return img

if "total" not in st.session_state:
    st.session_state.total = 0
if "qi" not in st.session_state:
    st.session_state.qi = 0
    st.session_state.qscore = 0

# LIVELY BANNER
try:
    st.image("banner.jpg", use_container_width=True)
except:
    st.markdown("<h1 style='text-align:center; color:#6a11cb;'>JAMB PRO MAX</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; background:#fff3cd; padding:12px; border-radius:15px; font-weight:bold;'>Trusted by 2,847+ Students for Admission Success 🎓✨</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:green;'>University Admission Made Easy - Your Path to 350+ Score!</p>", unsafe_allow_html=True)

c1,c2 = st.columns(2)
with c1:
    s1 = st.number_input("English", 0, 100, 70)
    s2 = st.number_input("Maths", 0, 100, 70)
with c2:
    s3 = st.number_input("Subject 3", 0, 100, 70)
    s4 = st.number_input("Subject 4", 0, 100, 70)

if st.button("CALCULATE MY FUTURE - MAKE ME BLOW!"):
    total = s1+s2+s3+s4
    st.session_state.total = total
    st.balloons()
    st.snow()
    st.markdown(f"<div class=score-box><h1>{total}/400</h1><p>Your JAMB Score 🔥</p></div>", unsafe_allow_html=True)
    if total >= 300:
        st.success("OMO YOU BE GENIUS! 🎉")
    st.subheader("Courses You Fit Get")
    for crs in get_courses(total):
        st.write(f"- {crs}")
    card = create_card(total)
    buf = io.BytesIO()
    card.save(buf, format="PNG")
    st.image(card)
    st.download_button("DOWNLOAD FOR WHATSAPP STATUS", buf.getvalue(), "jamb.png", "image/png", use_container_width=True)

st.divider()
st.subheader("Daily Wahala Quiz - Only Legends Pass 🧠")

real_quiz = [
    {"q": "The boys ___ playing", "opts": ["is", "are", "was", "has"], "ans": "are", "exp": "Boys = plural"},
    {"q": "Find x: 2x + 6 = 14", "opts": ["4", "8", "3", "5"], "ans": "4", "exp": "2x=8"},
    {"q": "What is Osmosis?", "opts": ["Movement of water", "Movement of air", "Eating", "Sleeping"], "ans": "Movement of water", "exp": "Water moves"},
    {"q": "Opposite of Ancient?", "opts": ["Old", "Modern", "Past", "Future"], "ans": "Modern", "exp": "Modern is opposite"},
]

curr = real_quiz[st.session_state.qi % len(real_quiz)]
st.write(f"Q{st.session_state.qi+1}: {curr['q']}")
choice = st.radio("Pick one:", curr["opts"], key=f"q{st.session_state.qi}")
a,b = st.columns(2)
with a:
    if st.button("Check Am!"):
        if choice == curr["ans"]:
            st.session_state.qscore += 1
            st.success(f"CORRECT! {curr['exp']}")
            st.balloons()
        else:
            st.error(f"WRONG! Answer is {curr['ans']}")
        st.metric("Score", f"{st.session_state.qscore}/{st.session_state.qi+1}")
with b:
    if st.button("Next Wahala"):
        st.session_state.qi += 1
        st.rerun()

st.divider()
st.subheader("UNLOCK AGGREGATOR 🔓")
st.write("UNILAG 500 | UNIBEN 500 | ALL 1200")
st.write("PalmPay: 8028519092 - Shola Taiwo")
st.write("Code: FIRE2025 for discount today!")

code_input = st.text_input("Enter Code", placeholder="UNILAG2025").upper().strip()
unlocked = CODES.get(code_input, [])
if code_input and not unlocked:
    st.error("Invalid code!")

tabs = st.tabs(["UNILAG", "UNIBEN", "OAU", "UI"])
for idx, uni in enumerate(["UNILAG","UNIBEN","OAU","UI"]):
    with tabs[idx]:
        if uni in unlocked:
            st.success(f"{uni} OPEN!")
            if st.session_state.total == 0:
                st.warning("Calculate JAMB first")
            else:
                olevel = st.slider(f"{uni} O-Level", 0, 30, 20, key=uni+"ol")
                putme = st.number_input(f"{uni} Post-UTME", 0, 100, 70, key=uni+"pu")
                if st.button(f"CALCULATE {uni}", key=uni+"btn"):
                    agg = (st.session_state.total/8) + olevel + (putme*0.3 if uni=="UNILAG" else putme*0.5)
                    st.metric(f"{uni} Aggregate", f"{agg:.2f}")
                    if agg >= 70: st.success("ADMISSION SURE!")
                    elif agg >= 55: st.warning("50/50")
                    else: st.error("Low!")
        else:
            st.info(f"{uni} LOCKED - Pay to unlock")

st.divider()
try:
    st.image("founder.jpg", caption="Founder - Shola Taiwo", use_container_width=True)
except:
    try:
        st.image("IMG-20261011-WA0011.jpg", use_container_width=True)
    except:
        st.write("")

st.markdown("<div style='background:black; padding:15px; border-radius:15px; text-align:center; color:white;'><h3 style='color:#00ff88;'>PalmPay: 8028519092</h3><p>Shola Taiwo - Founder</p></div>", unsafe_allow_html=True)
