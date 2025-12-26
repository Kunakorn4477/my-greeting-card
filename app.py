import streamlit as st
import time

# ตั้งค่าหน้าเว็บเบื้องต้น
st.set_page_config(
    page_title="Merry Christmas",
    page_icon="💌",
    layout="centered"
)

# --- ส่วนตกแต่ง CSS ---
st.markdown("""
<style>
    .card-container {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        border: 2px solid #f0f0f0;
    }
    .signature {
        color: #888;
        font-style: italic;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- ส่วนรับข้อมูล ---
st.sidebar.header("กรุณาเลือกการ์ด")
theme = st.sidebar.selectbox("เลือกโอกาสพิเศษ:", ["Merry Christmas"])
sender_name = st.sidebar.text_input("ชื่อผู้ส่ง:", "จาก... (ใส่ชื่อคุณ)")
receiver_name = st.text_input("กรุณาพิมพ์ชื่อผู้รับการ์ด 👇", "")

# --- ส่วนแสดงผล ---
if receiver_name:
    st.write("---")
    
    if st.button(f"💌 คลิกเพื่อเปิดการ์ดถึง {receiver_name}"):
        
        with st.spinner('กำลังเขียนคำอวยพร...'):
            time.sleep(1.5)
        
        if "วันเกิด" in theme:
            bg_color = "#FFF8DC"
            msg_color = "#FF4500"
            emoji_decor = "🎂 🎁 🍰"
            st.balloons()
            main_msg = f"สุขสันต์วันเกิดนะ {receiver_name}!"
            sub_msg = "ขอให้มีความสุขมากๆ คิดสิ่งใดสมปรารถนา ร่างกายแข็งแรงนะ!"
            
        elif "ปีใหม่" in theme:
            bg_color = "#E0F7FA"
            msg_color = "#006064"
            emoji_decor = "🎉 🎆 🥂"
            st.snow()
            main_msg = f"สวัสดีปีใหม่แด่ {receiver_name}!"
            sub_msg = "ขอให้ปีนี้เป็นปีที่ดี เริ่มต้นใหม่ด้วยความสดใส และประสบความสำเร็จในทุกเรื่องเลย"
        elif "Merry Christmas" in theme:
            bg_color = "#FFF0F5"
            msg_color = "#C71585"
            emoji_decor = "🎉  🎅🏻 "
            main_msg = f"Merry Christmas na {receiver_name} "
            sub_msg = "ขอให้เธอน่ารัก ๆ ขึ้นทุกวัน ไปเที่ยวกับเค้าทุก ๆ ที่ ที่อยากไป รักเธอนะ"
            
        else:
            bg_color = "#FFF0F5"
            msg_color = "#C71585"
            emoji_decor = "💖 🌹 🍫"
            st.balloons()
            main_msg = f"Happy Valentine's Day {receiver_name}"
            sub_msg = "ขอบคุณที่อยู่เคียงข้างกันนะ รักและห่วงใยเสมอ"

        html_card = f"""
        <div class="card-container" style="background-color: {bg_color};">
            <h1 style="color: {msg_color};">{emoji_decor}</h1>
            <h2 style="color: {msg_color}; margin-top: 20px;">{main_msg}</h2>
            <p style="font-size: 1.2em; color: #555; margin-top: 20px;">
                {sub_msg}
            </p>
            <div class="signature">
                ด้วยรักและห่วงใย<br>
                {sender_name}
            </div>
        </div>
        """
        st.markdown(html_card, unsafe_allow_html=True)
        st.success("ส่งความสุขเรียบร้อยแล้ว! 🥰")

else:
    st.info("👈 พิมพ์ชื่อผู้รับ แล้วกด Enter เพื่อเริ่มสร้างการ์ดครับ")
