import re 
import streamlit as st

#Page styling
st.set_page_config(page_title="Password Strength Checkar by Sabzsals", page_icon="🔑", layout="centered")

#Custom CSS
st.markdown(""" 
<style>
    .main {text-align: center;}
    .stTextInput {width:60% !important; margin: }
    .stButton button {width:50%, background: Black; color: white; font-size: 18px}
    .stButton button:hover {background-color: }
</style>
""", unsafe_allow_html=True)

#Page description and title
st.title("🔐 Password strength Generator")
st.write("Enter your password below to check it's security level 🔎")

#Function to check your password strength
def password_strength_checker(password):
    score = 0
    feedback = []

    if len(password) >= 8: 
        score += 1 #increase score by 1
    else:
        feedback.append("❌ Password should be atleast 8 characters long")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
    else:
        feedback.append("❌ Password should include both uppercase and lowercase letter")
    if re.search(r"/d",password):
            score += 1
    else:
        feedback.append("❌ Password should include atleast one number(0-9)")

#Special Characters
    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedback.append("❌ Password should be atleast one special character(!@#$%^&*)")

#Password strength results
    if score == 4:
        st.success("✅ Strong Password - Your password is secured")

    elif score == 3:
        st.info("⚠️ Add more character to make your password strong.")
    else:
        st.error("❌ Weak password - Follow the instructions below")

#Feedback
    if feedback:
        with st.expander("🔎 Improve your password"):
            for item in feedback:
                st.write(item)
password= st.text_input("Please enter your password:", type="password", help="Ensure your password is strong 🔐")

#Button working
if st.button("Check Strength"):
    if password:
        password_strength_checker(password)
    else:
        st.warning("⚠️Please enter a password") #show warning if password not defined       
