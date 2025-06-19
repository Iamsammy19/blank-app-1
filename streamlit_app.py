import streamlit as st
import time
import random
from datetime import datetime

# ======================
# NIGERIAN THREAT DATABASE
# ======================
THREATS = {
    # Ransomware targeting Nigerian businesses
    "naija_ransomware": {
        "extensions": [".lagoslock", ".nairacrypt", ".yahoomoney"],
        "payment_wallets": [
            "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
            "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq"
        ]
    },
    
    # Advanced Yahoo Boy patterns (Pidgin + English)
    "scam_patterns": {
        "pidgin": [
            "my pikin don sick", 
            "wire me small money",
            "na urgent matter"
        ],
        "english": [
            "Your BVN has been blocked",
            "Click to claim your airtime reward",
            "Dear Valued Customer"
        ]
    }
}

# ======================
# UNIQUE FEATURES
# ======================
def simulate_device_scan():
    """Generates realistic scan results with Nigerian context"""
    findings = []
    
    # 60% chance of finding common Nigerian threats
    if random.random() > 0.4:
        findings.append(("Yahoo Boy Toolkit", "Advanced 419 software"))
        
    if random.random() > 0.7:
        ext = random.choice(THREATS['naija_ransomware']['extensions'])  # Fixed parenthesis
        wallet = random.choice(THREATS['naija_ransomware']['payment_wallets'])
        findings.append((f"Ransomware {ext}", f"Demanding payment to {wallet}"))
    
    # Always find at least one "educational" threat
    educational_findings = [
        ("Old WhatsApp Media", "Potential scam images/videos"),
        ("Unsecured WiFi Networks", "3 vulnerable networks nearby")
    ]
    findings.append(random.choice(educational_findings))
    
    return findings

# ======================
# STREAMLIT UI
# ======================
st.set_page_config(
    page_title="NaijaShield Pro",
    layout="centered",
    initial_sidebar_state="collapsed",
    page_icon="🦅"
)

st.title("🦅 NaijaShield Pro")
st.markdown("Nigeria's Most Advanced Anti-Fraud Protection")

if st.button("🔥 RUN FULL PHONE SCAN"):
    with st.status("Scanning your device for Naija threats...", expanded=True) as status:
        time.sleep(1.5)
        st.write("🔍 Checking for Yahoo Boy toolkits...")
        time.sleep(2)
        st.write("📱 Analyzing WhatsApp messages...")
        time.sleep(1)
        st.write("🏦 Verifying banking apps...")
        status.update(label="Scan Complete!", state="complete")
    
    findings = simulate_device_scan()
    
    st.success(f"""
    **Scan Report**  
    - Threats Found: {len(findings)}  
    - Top Threat: {findings[0][0] if findings else 'None'}  
    """)
    
    with st.expander("View all threats"):
        for threat, desc in findings:
            st.write(f"- **{threat}**: {desc}")

# Emergency contacts
st.markdown("""
**Emergency Options**:  
📞 *322# - Instant threat blocking  
📞 08006322222 - EFCC Cybercrime Hotline  
""")
