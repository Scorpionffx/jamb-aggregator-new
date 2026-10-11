import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="JAMB PRO - Ultimate Calculator", page_icon="🎓", layout="centered")

# --- CODES FOR DIFFERENT SCHOOLS ---
CODES = {
    "UNILAG2025": ["UNILAG"],
    "BENIN2025": ["UNIBEN"],
    "OAU2025": ["OAU"],
    "UI2025": ["UI"],
    "ALLIN2025": ["UNILAG", "UNIBEN", "OAU", "UI"]
}

# --- COURSE FINDER ---
def get_courses(score):
    if score >= 300:
        return ["Medicine, Law, Pharmacy, Nursing", "Engineering (All), Computer Science", "Accounting, Economics, Architecture"]
    elif score >= 260:
        return ["Mechanical/Civil Engineering", "Computer Science, Biochemistry", "Business Admin, Mass Comm, Microbiology"]
    elif score >= 220:
        return ["Public Admin, Political Science", "Sociology, Education, Botany", "Zoology, Adult Education"]
    elif score >= 180:
        return ["Education Courses, Arts", "Agric Science, History", "English, Adult Education"]
    else:
        return ["Try Change of Institution / Polytechnic - Don't Give Up!"]

# --- RESULT CARD ---
def create_card(score):
    img = Image.new('RGB', (1080, 1080), color=(37,117,252))
    draw = ImageDraw.Draw(img)
    draw.rectangle([40,40,1040,1040], fill=(255,255,255), outline=(0,255,136), width=12)
    try:
        font_big = ImageFont.truetype("DejaVuSans-Bold.ttf", 90)
        font_mid = ImageFont.truetype("DejaVuSans-Bold.ttf", 48)
        font_small = ImageFont.truetype("DejaVuSans.ttf", 38)
    except:
        font_big = ImageFont.load_default()
        font_mid = ImageFont.load_default()
        font_small = ImageFont.load_default()
    draw.text((540,220), "JAMB PRO", font=font_mid, fill=(106,17,203), anchor="mm")
    draw.text((540,380), f"{score}/400", font=font_big, fill=(0,0,0), anchor="mm")
    draw.text((540,520), "My JAMB Score!", font=font_mid, fill=(0,0,0), anchor="mm")
    draw.text((540,650), "Calculate yours:", font=font_small, fill=(100,100,100), anchor="mm")
    draw.text((540,700), "jamb-pro.streamlit.app", font=font_small, fill=(37,117,252), anchor="mm")
    draw.text((540,800), "Pay: PalmPay 8028519092", font=font_small, fill=(221,36,118), anchor="mm")
    return img

# --- HEADER ---
st.markdown("<h1 style='text-align:center;color:#6a11cb;'>JAMB PRO</h1><p style='text-align:center;'>Free Calculator + Paid Aggregators</p>", unsafe_allow_html=True)

# --- INPUTS ---
if "total" not in st.session_state:
    st.session_state.total = 0

c1,c2 = st.columns(2)
with c1:
    s1 = st.number_input("English", 0, 100, 70)
    s2 = st.number_input("Maths", 0, 100, 70)
with c2:
    s3 = st.number_input("Subject 3", 0, 100, 70)
    s4 = st.number_input("Subject 4", 0, 100, 70)

if st.button("CALCULATE MY FUTURE", use_container_width=True, type="primary"):
    total = s1+s2+s3+s4
    st.session_state.total = total
    st.balloons()
    st.success(f"Your Total JAMB: {total} / 400")

    # 1. COURSE FINDER
    st.subheader("1. Courses You Can Get")
    for crs in get_courses(total):
        st.markdown(f"- {crs}")

    # 2. SHARE CARD
    st.subheader("2. Share Your Result (Viral)")
    card = create_card(total)
    buf = io.BytesIO()
    card.save(buf, format="PNG")
    st.image(card, caption="Your Share Card")
    st.download_button("Download For WhatsApp Status", buf.getvalue(), "jamb_result.png", "image/png", use_container_width=True)

# --- 7. HARD POST-UTME QUIZ ---
st.divider()
st.subheader("3. Daily Post-UTME Quiz (REAL JAMB LEVEL)")

real_quiz = [
    {"q": "Choose nearest meaning to UNDERLINE: 'Teacher will underline importance of discipline'", "opts": ["Emphasize", "Ignore", "Cancel", "Draw"], "ans": "Emphasize", "exp": "Underline means emphasize."},
    {"q": "Solve: If x + 2 = 7, find x squared", "opts": ["25", "49", "9", "5"], "ans": "25", "exp": "x=5, x^2=25"},
    {"q": "Which organelle is powerhouse of cell?", "opts": ["Nucleus", "Mitochondria", "Ribosome", "Chloroplast"], "ans": "Mitochondria", "exp": "Mitochondria produces energy."},
    {"q": "Past participle of 'go'?", "opts": ["Went", "Gone", "Going", "Goes"], "ans": "Gone", "exp": "Go-went-gone"},
    {"q": "Factorize: 2x^2 - 8", "opts": ["2(x-2)(x+2)", "(x-2)(x+2)", "2(x-2)^2", "2x(x-4)"], "ans": "2(x-2)(x+2)", "exp": "2(x^2-4)=2(x-2)(x+2)"},
    {"q": "Most abundant gas in air?", "opts": ["Oxygen", "Nitrogen", "CO2", "Hydrogen"], "ans": "Nitrogen", "exp": "Nitrogen 78% of air"},
    {"q": "Synonym for 'Benevolent'?", "opts": ["Wicked", "Kind", "Selfish", "Rude"], "ans": "Kind", "exp": "Benevolent = kind"},
    {"q": "If 3y = 12, find y + 3", "opts": ["7", "4", "15", "9"], "ans": "7", "exp": "y=4, so y+3=7"},
]

if "qi" not in st.session_state:
    st.session_state.qi = 0
    st.session_state.qscore = 0

current = real_quiz[st.session_state.qi % len(real_quiz)]
st.write(f"**Q{st.session_state.qi+1}: {current['q']}**")
choice = st.radio("Choose:", current["opts"], key=f"quiz_{st.session_state.qi}")

col_a, col_b = st.columns(2)
with col_a:
    if st.button("Check Answer"):
        if choice == current["ans"]:
            st.session_state.qscore += 1
            st.success(f"CORRECT! {current['exp']}")
        else:
            st.error(f"WRONG! Answer is {current['ans']}. {current['exp']}")
        st.info(f"Score: {st.session_state.qscore}/{st.session_state.qi+1}")
with col_b:
    if st.button("Next Question"):
        st.session_state.qi += 1
        st.rerun()

# --- 5. PAID AGGREGATORS WITH DIFFERENT CODES ---
st.divider()
st.markdown("""
<div style="background: linear-gradient(135deg,#ff512f,#dd2476); padding:18px; border-radius:18px; color:white; text-align:center;">
<h3>UNLOCK UNIVERSITY AGGREGATORS</h3>
<p>PalmPay: 8028519092 (Shola Taiwo)</p>
<p>UNILAG=500 | UNIBEN=500 | ALL=1200</p>
<p>WhatsApp receipt to 08028519092 to get code</p>
</div>
""", unsafe_allow_html=True)

code_input = st.text_input("Enter Unlock Code", placeholder="e.g. UNILAG2025 or ALLIN2025").upper().strip()
unlocked = CODES.get(code_input, [])

if code_input and not unlocked:
    st.error("Invalid code! Pay first to get code")

tabs = st.tabs(["UNILAG", "UNIBEN", "OAU", "UI"])
formulas = {
    "UNILAG": "(JAMB/8) + Olevel(20) + Putme*0.3",
    "UNIBEN": "(JAMB/8) + Olevel + Putme*0.7 then /1.7",
    "OAU": "(JAMB/8) + Putme*0.5 + Olevel",
    "UI": "(JAMB/8) + Putme*0.5"
}

for idx, uni in enumerate(["UNILAG", "UNIBEN", "OAU", "UI"]):
    with tabs[idx]:
        if uni in unlocked:
            st.success(f"{uni} UNLOCKED!")
            if st.session_state.total == 0:
                st.warning("Calculate JAMB score at top first")
            else:
                st.caption(f"Formula: {formulas[uni]}")
                olevel = st.slider(f"{uni} OLevel Points", 0, 30, 20, key=uni+"ol")
                putme = st.number_input(f"{uni} Post-UTME", 0, 100, 70, key=uni+"pu")
                if st.button(f"Calculate {uni} Aggregate", key=uni+"btn"):
                    agg = (st.session_state.total/8) + olevel + (putme*0.3 if uni=="UNILAG" else putme*0.5)
                    st.metric(f"{uni} Aggregate", f"{agg:.2f}")
                    if agg >= 65:
                        st.success("High chance of admission!")
                    elif agg >= 50:
                        st.warning("Average - try lower course")
                    else:
                        st.error("Low - consider change of institution")
        else:
            st.info(f"LOCKED! Need code for {uni}")
            st.write(f"Code is {uni}2025 or buy ALLIN2025 for all schools")

# --- FOUNDER PHOTO ---
st.divider()
st.subheader("Founder Support")
try:
    st.image("founder.jpg", caption="Support the founder - Thanks!", use_container_width=True)
except:
    try:
        st.image("IMG-20261011-WA0011.jpg", use_container_width=True)
    except:
        st.write("Add founder.jpg to show your photo here")

st.markdown("<div style='background:black;padding:12px;border-radius:12px;text-align:center;color:white;'><h3 style='color:#00ff88;'>PalmPay: 8028519092</h3><p>Shola Taiwo - Founder</p></div>", unsafe_allow_html=True)
