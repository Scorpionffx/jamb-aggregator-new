import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="JAMB PRO MAX", page_icon="🔥", layout="centered")

# --- SUPER CSS TO MAKE IT NOT DULL ---
st.markdown("""
<style>
.stButton>button {
    background: linear-gradient(90deg,#ff0080,#7928ca)!important;
    color:white!important;
    border-radius: 30px!important;
    font-weight: bold!important;
    font-size: 18px!important;
    height: 55px!important;
    box-shadow: 0 10px 20px rgba(255,0,128,0.3)!important;
    border: none!important;
    animation: pulse 2s infinite;
}
@keyframes pulse {
  0% {transform: scale(1);}
  50% {transform: scale(1.03);}
  100% {transform: scale(1);}
}
.score-box {
    background: linear-gradient(135deg,#6a11cb 0%,#2575fc 100%);
    padding: 25px; border-radius: 25px; color: white; text-align:center;
    box-shadow: 0 15px 30px rgba(0,0,0,0.2);
}
.glass {
    background: rgba(255,255,255,0.9);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 20px;
    border: 2px solid #00ff88;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

CODES = {
    "UNILAG2025": ["UNILAG"],
    "BENIN2025": ["UNIBEN"],
    "OAU2025": ["OAU"],
    "UI2025": ["UI"],
    "ALLIN2025": ["UNILAG","UNIBEN","OAU","UI"],
    "FIRE2025": ["UNILAG","UNIBEN","OAU","UI"] # secret promo code
}

def get_courses(score):
    if score >= 300:
        return ["🔥 Medicine, Law, Pharmacy", "💻 Engineering, Computer Science", "💰 Accounting, Economics"]
    elif score >= 260:
        return ["⚙️ Mechanical/Civil Eng", "🧬 Biochemistry, Microbiology", "📢 Business Admin, Mass Comm"]
    elif score >= 220:
        return ["🏛️ Public Admin, Poli Sci", "📚 Education, Sociology", "🌱 Agric, Botany"]
    else:
        return ["🚀 Polytechnic / Change Course - You Still Got This!"]

def create_card(score):
    img = Image.new('RGB', (1080, 1350), color=(0,0,0))
    draw = ImageDraw.Draw(img)
    # crazy gradient background
    for i in range(1350):
        r = int(106 + i*0.1); g = int(17 + i*0.15); b = int(203 - i*0.05)
        draw.line([(0,i),(1080,i)], fill=(r%255,g%255,b%255))
    draw.rectangle([30,30,1050,1320], fill=(255,255,255), outline=(0,255,136), width=15)
    try:
        fb = ImageFont.truetype("DejaVuSans-Bold.ttf", 100)
        fm = ImageFont.truetype("DejaVuSans-Bold.ttf", 55)
        fs = ImageFont.truetype("DejaVuSans.ttf", 38)
    except:
        fb = fm = fs = ImageFont.load_default()
    draw.text((540,200), "🔥 JAMB PRO MAX 🔥", font=fm, fill=(106,17,203), anchor="mm")
    draw.text((540,450), f"{score}", font=fb, fill=(0,0,0), anchor="mm")
    draw.text((540,550), "/400", font=fm, fill=(100,100,100), anchor="mm")
    draw.text((540,680), "I'M A GENIUS! 🧠", font=fm, fill=(255,0,128), anchor="mm")
    draw.text((540,820), "Can you beat me?", font=fs, fill=(0,0,0), anchor="mm")
    draw.text((540,900), "jamb-pro.streamlit.app", font=fs, fill=(37,117,252), anchor="mm")
    draw.text((540,1050), "PalmPay: 8028519092", font=fm, fill=(221,36,118), anchor="mm")
    draw.text((540,1130), "Shola Taiwo - Founder", font=fs, fill=(0,0,0), anchor="mm")
    return img

if "total" not in st.session_state:
    st.session_state.total = 0
if "qi" not in st.session_state:
    st.session_state.qi = 0
    st.session_state.qscore = 0

# HEADER FIRE
st.markdown("<h1 style='text-align:center; font-size:60px; background: linear-gradient(90deg,#ff0080,#7928ca,#ff8a00); -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>🔥 JAMB PRO MAX 🔥</h1><p style='text-align:center; font-size:20px;'>Not Boring Like ChatGPT Apps 😎</p>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; background:#00ff88; padding:8px; border-radius:20px; font-weight:bold;'>⚡ 2,847 students using it RIGHT NOW ⚡</div>", unsafe_allow_html=True)

c1,c2 = st.columns(2)
with c1:
    s1 = st.number_input("English 📖", 0, 100, 70)
    s2 = st.number_input("Maths 🔢", 0, 100, 70)
with c2:
    s3 = st.number_input("Subject 3 🧪", 0, 100, 70)
    s4 = st.number_input("Subject 4 📚", 0, 100, 70)

if st.button("🚀 CALCULATE MY FUTURE - MAKE ME BLOW!"):
    total = s1+s2+s3+s4
    st.session_state.total = total
    st.balloons()
    st.snow()
    st.markdown(f"<div class='score-box'><h2 style='font-size:70px; margin:0;'>{total}</h2><p style='font-size:25px; margin:0;'>/400 🔥🔥🔥</p></div>", unsafe_allow_html=True)
    if total >= 300:
        st.success("🔥🔥🔥 OMO YOU BE GENIUS! UNILAG IS YOURS!")
    elif total >= 200:
        st.warning("💪 You try! You fit still enter good course!")
    else:
        st.error("😅 No worry, we go help you upgrade!")

    # COURSE FINDER - GLASS
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("1️⃣ Courses You Fit Get (No Lie)")
    for crs in get_courses(total):
        st.markdown(f"<div style='background:#f0f0ff; padding:10px; border-radius:10px; margin:5px 0; border-left:5px solid #7928ca;'>✅ {crs}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # SHARE CARD - VIRAL
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("2️⃣ Go Viral On WhatsApp 😎")
    card = create_card(total)
    buf = io.BytesIO()
    card.save(buf, format="PNG")
    st.image(card)
    st.download_button("📲 DOWNLOAD & POST ON STATUS (Make them jealous)", buf.getvalue(), "jamb_pro_max.png", "image/png", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# QUIZ - HARD & FUN
st.divider()
st.markdown("### 3️⃣ Daily WAHALA Quiz (Only Legends Pass) 🧠💥")

real_quiz = [
    {"q": "Which is correct? 'The boys ___ playing'", "opts": ["is", "are", "was", "has"], "ans": "are", "exp": "Boys = plural = are"},
    {"q": "Find x: 2x + 6 = 14", "opts": ["4", "8", "3", "5"], "ans": "4", "exp": "2x=8 => x=4"},
    {"q": "What is Osmosis?", "opts": ["Movement of water", "Movement of air", "Eating", "Sleeping"], "ans": "Movement of water", "exp": "Water moves from high to low concentration"},
    {"q": "Opposite of 'Ancient'?", "opts": ["Old", "Modern", "Past", "Future"], "ans": "Modern", "exp": "Ancient = old, opposite = modern"},
    {"q": "Simplify: (3²)² =?", "opts": ["81", "9", "18", "27"], "ans": "81", "exp": "3²=9, 9²=81"},
    {"q": "Which blood group is universal donor?", "opts": ["O", "AB", "A", "B"], "ans": "O", "exp": "O negative is universal donor"},
]

curr = real_quiz[st.session_state.qi % len(real_quiz)]
st.markdown(f"<div style='background:black; color:#00ff88; padding:15px; border-radius:15px;'><b>🔥 Q{st.session_state.qi+1}: {curr['q']}</b></div>", unsafe_allow_html=True)
choice = st.radio("Pick one (No cheating):", curr["opts"], key=f"q{st.session_state.qi}")

a,b = st.columns(2)
with a:
    if st.button("Check Am! 👀"):
        if choice == curr["ans"]:
            st.session_state.qscore += 1
            st.success(f"GBAM! CORRECT! 🎉 {curr['exp']}")
            st.balloons()
        else:
            st.error(f"OLODO! 😂 Answer na {curr['ans']}. {curr['exp']}")
        st.metric("Your Street Score", f"{st.session_state.qscore}/{st.session_state.qi+1}")
with b:
    if st.button("Next Wahala ➡️"):
        st.session_state.qi += 1
        st.rerun()

# PAID SECTION - LOUD
st.divider()
st.markdown("""
<div style="background: linear-gradient(135deg,#ff512f 0%,#dd2476 50%,#7928ca 100%); padding:22px; border-radius:25px; color:white; text-align:center; animation: pulse 2s infinite;">
<h2 style='margin:0;'>💰 UNLOCK AGGREGATOR = BLOW 💰</h2>
<p style='font-size:18px;'>UNILAG 500 | UNIBEN 500 | ALL SCHOOLS 1200</p>
<p>PalmPay: 8028519092 - Shola Taiwo<br>WhatsApp: 08028519092</p>
<p style='background:white; color:black; border-radius:10px; padding:5px;'>Use Code: FIRE2025 for 20% OFF today only!</p>
</div>
""", unsafe_allow_html=True)

code_input = st.text_input("🔑 Enter Code Make You Blow", placeholder="e.g. UNILAG2025, ALLIN2025, FIRE2025").upper().strip()
unlocked = CODES.get(code_input, [])

if code_input and not unlocked:
    st.error("❌ Oga invalid code! Go pay!")

tabs = st.tabs(["🔥 UNILAG", "👑 UNIBEN", "🦁 OAU", "🎓 UI"])
for idx, uni in enumerate(["UNILAG","UNIBEN","OAU","UI"]):
    with tabs[idx]:
        if uni in unlocked:
            st.success(f"✅ {uni} DON OPEN! YOU BE BIG BOY NOW!")
            if st.session_state.total == 0:
                st.warning("Calculate JAMB first for top!")
            else:
                olevel = st.slider(f"{uni} O-Level Points (A1=6)", 0, 30, 20, key=uni+"ol")
                putme = st.number_input(f"{uni} Post-UTME Score", 0, 100, 70, key=uni+"pu")
                if st.button(f"💥 CALCULATE {uni} AGGREGATE", key=uni+"btn"):
                    agg = (st.session_state.total/8) + olevel + (putme*0.3 if uni=="UNILAG" else putme*0.5)
                    st.markdown(f"<div class='score-box'><h1>{agg:.2f}%</h1><p>{uni} Aggregate</p></div>", unsafe_allow_html=True)
                    if agg >= 70: st.success("🔥 ADMISSION SURE! Go buy form!")
                    elif agg >= 55: st.warning("😐 50/50 - Put more effort!")
                    else: st.error("😭 Low! Change course asap!")
        else:
            st.markdown(f"<div style='background:#222; color:white; padding:20px; border-radius:15px; text-align:center;'><h3>🔒 {uni} LOCKED</h3><p>Pay 500 to unlock<br>Or 1200 for ALL</p></div>", unsafe_allow_html=True)

# FOUNDER
st.divider()
try:
    st.image("founder.jpg", caption="Real Founder - No AI - Original Photo ✊", use_container_width=True)
except:
    try:
        st.image("IMG-20261011-WA0011.jpg", use_container_width=True)
    except:
        st.write("Founder pic coming soon")

st.markdown("<div style='background:black; padding:15px; border-radius:15px; text-align:center; color:white;'><h2 style='color:#00ff88; margin:0;'>PalmPay: 8028519092</h2><p>Shola Taiwo - The
