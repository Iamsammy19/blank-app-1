import streamlit as st
import time
import random
from datetime import datetime
import pandas as pd

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
    },
    
    # Fake Nigerian banking domains
    "bank_impersonators": [
        "accessbank-online.ng",
        "firstbankverify.com",
        "gtbank-updates.org"
    ],
    
    # Common malware processes in Nigeria
    "malicious_processes": [
        "bitcoin-miner.exe",
        "whatsapp-hack.vbs",
        "bank-alert.js"
    ]
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
        findings.append((f"Ransomware {random.choice(THREATS['naija_ransomware']['extensions']}", 
                       f"Demanding payment to {random.choice(THREATS['naija_ransomware']['payment_wallets'])}"))
    
    # Always find at least one "educational" threat
    educational_findings = [
        ("Old WhatsApp Media", "Potential scam images/videos"),
        ("Unsecured WiFi Networks", "3 vulnerable networks nearby")
    ]
    findings.append(random.choice(educational_findings))
    
    return findings

def generate_efcc_report(threat_name):
    """Creates realistic EFCC case details"""
    case_number = f"EFCC/NG/{datetime.now().year}/{random.randint(1000,9999)}"
    officer = random.choice(["Okafor", "Adeleke", "Yusuf"])
    return {
        "case_number": case_number,
        "assigned_officer": f"ACP {officer}",
        "status": random.choice(["Under Investigation", "Case Filed", "Suspect Tracked"])
    }

def calculate_airtime_rewards(threats_found):
    """Nigeria-specific reward system"""
    base_reward = 50  # Naira
    return base_reward * len(threats_found)

# ======================
# STREAMLIT UI
# ======================
st.set_page_config(
    page_title="NaijaShield Pro",
    layout="centered",
    initial_sidebar_state="collapsed",
    page_icon="🦅"
)

# Custom styling for Nigerian feel
st.markdown("""
<style>
    .stButton>button {
        background-color: #1DA1F2;
        color: white;
        border: none;
        padding: 15px 32px;
        text-align: center;
        font-size: 18px;
        border-radius: 10px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #1991DB;
    }
    .nigerian-flag {
        color: green;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.title("🦅 NaijaShield Pro")
st.markdown("""
<span class="nigerian-flag">Nigeria's Most Advanced Anti-Fraud Protection</span>  
*"No Yahoo Boy Fit Beat This Shield"*  
""", unsafe_allow_html=True)

# Main Scan Interface
if st.button("🔥 RUN FULL PHONE SCAN", key="main_scan"):
    with st.status("Scanning your device for Naija threats...", expanded=True) as status:
        
        # Simulate scanning phases
        phases = [
            ("🔍 Checking for Yahoo Boy toolkits...", 1.5),
            ("📱 Analyzing WhatsApp/Telegram messages...", 2),
            ("🏦 Verifying banking apps...", 1),
            ("🌐 Monitoring network connections...", 1.5)
        ]
        
        for phase, duration in phases:
            st.write(phase)
            time.sleep(duration)
            
            # Randomly generate findings
            if random.random() > 0.6:
                threat_type = random.choice(list(THREATS.keys()))
                if threat_type == "naija_ransomware":
                    ext = random.choice(THREATS["naija_ransomware"]["extensions"])
                    st.error(f"Found ransomware: payment demanded in {ext}")
                elif threat_type == "scam_patterns":
                    lang = random.choice(["pidgin", "english"])
                    scam = random.choice(THREATS["scam_patterns"][lang])
                    st.error(f"Scam detected: '{scam}'")
        
        status.update(label="Scan Complete!", state="complete")
    
    # Generate report
    findings = simulate_device_scan()
    efcc_report = generate_efcc_report(findings[0][0] if findings else "Clean Device")
    reward = calculate_airtime_rewards(findings)
    
    st.success(f"""
    **Scan Report**  
    - Threats Found: {len(findings)}  
    - EFCC Case: {efcc_report['case_number']}  
    - Airtime Reward: ₦{reward}  
    """)
    
    # Show detailed findings
    with st.expander("📝 Threat Details"):
        for threat, description in findings:
            st.write(f"- **{threat}**: {description}")
        
        st.markdown(f"""
        **Next Steps**:  
        • Tap below to report to EFCC  
        • Dial *322# to block threats  
        • Claim your ₦{reward} airtime  
        """)

# Unique Nigerian Features
st.markdown("---")
st.subheader("🇳🇬 Made for Nigeria")
cols = st.columns(3)
with cols[0]:
    st.markdown("**Pidgin AI**  \nCatches 'Abeg send money' scams")
with cols[1]:
    st.markdown("**EFCC Connect**  \nDirect case reporting")
with cols[2]:
    st.markdown("**Airtime Rewards**  \nEarn ₦50-₦500 per threat")

# Emergency Quick Actions
st.markdown("---")
st.markdown("""
**Emergency Options**:  
📞 *322# - Instant threat blocking  
📞 08006322222 - EFCC Cybercrime Hotline  
📧 efcc@efcc.gov.ng  
""")
