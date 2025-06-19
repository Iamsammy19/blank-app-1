import streamlit as st
import time
import random
from datetime import datetime

# Nigerian threat database
THREATS = {
    "email_scams": {
        "subjects": [
            "Urgent: Your BVN has been blocked",
            "Congratulations! You won 500,000 Naira",
            "Access Bank Security Alert"
        ],
        "senders": [
            "security@accessbank-update.com",
            "noreply@gtbank-alerts.com",
            "support@firstbank-verify.org"
        ]
    },
    "social_media": {
        "whatsapp": [
            "Hi dear, I need your account number",
            "Click this link to claim your prize",
            "Your SIM card will be blocked today"
        ],
        "instagram": [
            "Double-tap to get 50k followers",
            "Account verification required",
            "You've been tagged in a fake giveaway"
        ]
    },
    "sms_scams": [
        "Your Zenith account has been limited",
        "MTN: You won 10GB data. Click here",
        "GLO: Your line will be disconnected"
    ]
}

# Simulated access functions
def scan_emails():
    st.write("📧 Scanning emails...")
    time.sleep(2)
    scam_emails = []
    if random.random() > 0.5:
        scam_emails.append((
            random.choice(THREATS["email_scams"]["senders"]),
            random.choice(THREATS["email_scams"]["subjects"])
        )
    return scam_emails

def scan_social_media():
    st.write("📱 Checking social media...")
    time.sleep(3)
    threats = []
    if random.random() > 0.4:
        threats.append((
            "WhatsApp", 
            random.choice(THREATS["social_media"]["whatsapp"])
        ))
    if random.random() > 0.4:
        threats.append((
            "Instagram", 
            random.choice(THREATS["social_media"]["instagram"])
        ))
    return threats

def scan_sms():
    st.write("💬 Checking messages...")
    time.sleep(1.5)
    scam_sms = []
    if random.random() > 0.6:
        scam_sms.append(random.choice(THREATS["sms_scams"]))
    return scam_sms

# Streamlit UI
st.set_page_config(
    page_title="NaijaShield Pro",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("📱 NaijaShield Pro")
st.markdown("**Full device protection for Nigerian users**")

if st.button("🔍 SCAN MY MESSAGES & SOCIALS", type="primary"):
    with st.status("Scanning your personal communications...", expanded=True) as status:
        emails = scan_emails()
        social = scan_social_media()
        sms = scan_sms()
        status.update(label="Scan Complete!", state="complete")
    
    # Display results
    st.subheader("Threat Report")
    
    if emails:
        st.error("**Email Threats**")
        for sender, subject in emails:
            st.write(f"- From: {sender}")
            st.write(f"  Subject: {subject}")
    
    if social:
        st.error("**Social Media Threats**")
        for platform, message in social:
            st.write(f"- {platform}: {message}")
    
    if sms:
        st.error("**SMS Scams**")
        for msg in sms:
            st.write(f"- {msg}")
    
    if not emails and not social and not sms:
        st.success("✅ No threats found in your communications")

# What a real app would need
st.markdown("---")
st.markdown("""
**For true message access**:  
This demo simulates scanning. A real app would require:
- Android: `READ_SMS` and `READ_CONTACTS` permissions
- iOS: Restricted entitlements
- Email: IMAP access with user credentials
""")

# Nigerian emergency contacts
st.markdown("""
**Emergency Options**:  
📞 *322# - NCC Scam Reporting  
📞 08006322222 - EFCC Cybercrime Unit  
""")
