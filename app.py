# =============================================================================
# CALDYA Analytics Dashboard - Enhanced Professional Edition with Complete Features
# 
# EXACT SAME functionality as original with sophisticated visual design enhancements
# =============================================================================

import streamlit as st
import pandas as pd
import pymongo
import requests
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import base64
import json
from datetime import datetime, timedelta
import time
from difflib import SequenceMatcher

# Page configuration
st.set_page_config(
    page_title="CALDYA Dashboard", 
    page_icon="logo.png", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Enhanced Authentication System
def check_password():
    """Professional authentication with enhanced UX"""
    if st.session_state.authenticated:
        return True
    
    def password_entered():
        if st.session_state["password"] == st.secrets["auth"]["password"]:
            st.session_state["authenticated"] = True
            del st.session_state["password"]
        else:
            st.session_state["authenticated"] = False

    # Professional login styling
    st.markdown("""
    <style>
        .login-container {
            background: linear-gradient(135deg, #0a0e1a 0%, #1a1d2e 50%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        
        .login-card {
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(40px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 4rem 3rem;
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.4),
                0 0 0 1px rgba(255, 255, 255, 0.04) inset;
            text-align: center;
            max-width: 480px;
            width: 100%;
            position: relative;
        }
        
        .login-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        }
        
        .login-header {
            margin-bottom: 3rem;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: center;
            gap: 1.5rem;
        }
        
        .login-logo {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            border: 2px solid #3b82f6;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
            object-fit: cover;
            order: 2;
        }
        
        .login-logo-placeholder {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            border: 2px solid #3b82f6;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
            order: 2;
        }
        
        .login-text {
            order: 1;
            text-align: left;
        }
        
        .login-title {
            background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 3rem;
            font-weight: 700;
            margin: 0 0 0.5rem 0;
            line-height: 1.1;
            letter-spacing: -0.02em;
        }
        
        .login-subtitle {
            color: rgba(255, 255, 255, 0.6);
            margin: 0;
            font-size: 1.1rem;
            font-weight: 400;
            letter-spacing: 0.02em;
        }
        
        .stTextInput > div > div > input {
            background: rgba(255, 255, 255, 0.04) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 16px !important;
            color: rgba(255, 255, 255, 0.9) !important;
            padding: 1.25rem 1.5rem !important;
            font-size: 1rem !important;
            text-align: center !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #667eea !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
            background: rgba(255, 255, 255, 0.06) !important;
        }
        
        .stTextInput > div > div > input::placeholder {
            color: rgba(255, 255, 255, 0.4) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Login form
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            # Try to load logo for login page
            try:
                import base64
                import os
                if os.path.exists("logo.png"):
                    with open("logo.png", "rb") as f:
                        logo_data = base64.b64encode(f.read()).decode()
                    logo_html = f'<img src="data:image/png;base64,{logo_data}" class="login-logo" alt="CALDYA Logo">'
                else:
                    logo_html = '<div class="login-logo-placeholder">⚡</div>'
            except:
                logo_html = '<div class="login-logo-placeholder">⚡</div>'
            
            st.markdown(f"""
            <div class="login-card">
                <div class="login-header">
                    <div class="login-text">
                        <h1 class="login-title">CALDYA</h1>
                        <p class="login-subtitle">LFL2 Dashboard</p>
                    </div>
                    {logo_html}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.text_input("", type="password", key="password", on_change=password_entered, placeholder="Enter access code...")
            
            if "password" in st.session_state and st.session_state.get("password"):
                if not st.session_state.authenticated:
                    st.error("Access denied. Please check your credentials.")

    return st.session_state.authenticated

# Stop execution if not authenticated
if not check_password():
    st.stop()

# Professional CSS Framework - COMPLETE WITH ALL ORIGINAL STYLING
st.markdown("""
<style>
    /* Professional Design System Variables */
    :root {
        --bg-primary: #0f172a;
        --bg-secondary: #1e293b;
        --bg-card: #334155;
        --accent-primary: #3b82f6;
        --accent-secondary: #60a5fa;
        --accent-tertiary: #2563eb;
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
        --success: #10b981;
        --warning: #f59e0b;
        --danger: #ef4444;
        --border: #475569;
        --shadow: rgba(0, 0, 0, 0.25);
        
        --primary-50: #eff6ff;
        --primary-100: #dbeafe;
        --primary-200: #bfdbfe;
        --primary-300: #93c5fd;
        --primary-400: #60a5fa;
        --primary-500: #3b82f6;
        --primary-600: #2563eb;
        --primary-700: #1d4ed8;
        --primary-800: #1e40af;
        --primary-900: #1e3a8a;
        
        --neutral-50: #f8fafc;
        --neutral-100: #f1f5f9;
        --neutral-200: #e2e8f0;
        --neutral-300: #cbd5e1;
        --neutral-400: #94a3b8;
        --neutral-500: #64748b;
        --neutral-600: #475569;
        --neutral-700: #334155;
        --neutral-800: #1e293b;
        --neutral-900: #0f172a;
        
        --success-500: #10b981;
        --warning-500: #f59e0b;
        --error-500: #ef4444;
        
        --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --radius-xl: 24px;
        
        --spacing-xs: 0.25rem;
        --spacing-sm: 0.5rem;
        --spacing-md: 1rem;
        --spacing-lg: 1.5rem;
        --spacing-xl: 2rem;
        --spacing-2xl: 3rem;
    }
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, var(--bg-primary) 0%, #1a2332 100%);
        color: var(--text-primary);
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    .main .block-container {
        padding: var(--spacing-xl) var(--spacing-lg);
        max-width: 1400px;
    }
    
    /* Modern Typography */
    h1, h2, h3, h4 {
        color: var(--text-primary);
        font-weight: 700;
        line-height: 1.2;
        letter-spacing: -0.025em;
    }
    
    h1 {
        text-align: center;
        font-size: clamp(2rem, 4vw, 3rem);
        background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        padding-bottom: 2rem;
        margin-bottom: 3rem;
        position: relative;
    }
    
    h1::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 3px;
        background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
        border-radius: 2px;
    }
    
    h2 {
        font-size: 1.75rem;
        color: var(--accent-secondary);
        margin: 2.5rem 0 1.5rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid var(--border);
        position: relative;
    }
    
    h3 {
        font-size: 1.5rem;
        color: var(--text-primary);
        margin: 2rem 0 1rem 0;
    }
    
    /* Professional Glass Morphism Cards */
    .stat-card, .modern-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px var(--shadow);
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    }
    
    .stat-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        border-color: rgba(255, 255, 255, 0.12);
    }
    
    /* Enhanced Team Colors */
    .gmb-blue {
        color: var(--accent-primary) !important;
        font-weight: 600;
        text-shadow: 0 0 10px rgba(59, 130, 246, 0.3);
    }
    
    .opponent-red {
        color: var(--danger) !important;
        font-weight: 600;
        text-shadow: 0 0 10px rgba(239, 68, 68, 0.3);
    }
    
    .win {
        color: var(--success) !important;
        font-weight: 700;
        text-shadow: 0 0 10px rgba(16, 185, 129, 0.3);
    }
    
    .loss {
        color: var(--danger) !important;
        font-weight: 700;
        text-shadow: 0 0 10px rgba(239, 68, 68, 0.3);
    }
    
    /* Modern Sidebar Enhancement */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.02) 0%, rgba(255, 255, 255, 0.01) 100%);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    .css-1d391kg .css-17eq0hr, [data-testid="stSidebar"] .css-17eq0hr {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        margin-bottom: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    /* Sidebar Header Centering */
    .sidebar-header {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 1rem 0;
        gap: 0.5rem;
    }
    
    .sidebar-header img {
        display: block;
        margin: 0 auto;
    }
    
    .sidebar-header div {
        text-align: center;
    }
    
    /* Enhanced DataFrames */
    .dataframe-container {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(15px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        overflow: hidden;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px var(--shadow);
    }
    
    .stDataFrame {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: var(--radius-lg);
        overflow: hidden;
    }
    
    .stDataFrame table {
        font-size: 0.875rem;
    }
    
    .stDataFrame th {
        background: rgba(255, 255, 255, 0.04) !important;
        color: var(--neutral-200) !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        font-size: 0.75rem !important;
    }
    
    .stDataFrame td {
        color: var(--neutral-100) !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.04) !important;
    }
    
    /* Modern Buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--accent-primary), var(--accent-tertiary)) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.2) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.025em !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: var(--shadow-lg);
        background: linear-gradient(135deg, var(--primary-500) 0%, var(--primary-600) 100%);
    }
    
    /* Enhanced Form Elements */
    .stSelectbox > div > div > div, .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        color: var(--text-primary) !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
    }
    
    .stSelectbox > div > div > div:focus, .stTextInput > div > div > input:focus {
        border-color: var(--accent-primary) !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
    }
    
    /* Modern Radio Buttons */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.02) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Enhanced Progress Bars */
    .stProgress > div {
        background-color: rgba(51, 65, 85, 0.3) !important;
        border-radius: 20px !important;
        height: 12px !important;
        overflow: hidden !important;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1) !important;
    }
    
    .stProgress > div > div > div {
        background: linear-gradient(90deg, var(--accent-tertiary), var(--accent-primary)) !important;
        border-radius: 20px !important;
        transition: all 0.5s ease !important;
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3) !important;
    }
    
    /* Champion Icons Enhancement */
    .champion-icon {
        border: 3px solid var(--accent-primary);
        border-radius: 50%;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.2);
    }
    
    /* Alert Boxes */
    .stAlert {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid var(--accent-primary) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(15px) !important;
    }
    
    /* Metric Cards Enhancement */
    .metric-value {
        font-size: 2.25rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, var(--accent-secondary), var(--accent-primary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0.5rem 0 !important;
    }
    
    .metric-label {
        color: var(--text-secondary) !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        margin-bottom: 0.25rem !important;
    }
    
    .metric-delta {
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        margin-top: 0.5rem !important;
    }
    
    /* Player Cards for Items Display */
    .player-items-row {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(15px);
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        display: flex;
        align-items: center;
        gap: 1rem;
        transition: all 0.3s ease;
    }
    
    .player-items-row:hover {
        transform: translateY(-1px);
        border-color: rgba(255, 255, 255, 0.12);
    }
    
    .champion-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        min-width: 80px;
    }
    
    .items-section {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        flex-wrap: wrap;
    }
    
    .player-info-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 0.5rem;
    }
    
    .player-name {
        font-weight: 600;
        font-size: 0.9rem;
        color: var(--text-primary);
        margin: 0;
        text-align: center;
    }
    
    .player-score {
        font-size: 0.8rem;
        color: var(--text-secondary);
        text-align: center;
        margin: 0;
    }
    
    /* Status Indicators */
    .status-win {
        color: var(--success-500);
        background: rgba(16, 185, 129, 0.1);
        padding: var(--spacing-xs) var(--spacing-sm);
        border-radius: var(--radius-sm);
        font-weight: 600;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .status-loss {
        color: var(--error-500);
        background: rgba(239, 68, 68, 0.1);
        padding: var(--spacing-xs) var(--spacing-sm);
        border-radius: var(--radius-sm);
        font-weight: 600;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Champion Cards */
    .champion-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: var(--radius-lg);
        padding: var(--spacing-lg);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .champion-card:hover {
        transform: translateY(-2px);
        border-color: rgba(255, 255, 255, 0.12);
    }
    
    .champion-image {
        width: 64px;
        height: 64px;
        border-radius: 50%;
        border: 2px solid var(--primary-500);
        margin: 0 auto var(--spacing-md) auto;
        display: block;
    }
    
    .champion-name {
        font-weight: 600;
        color: var(--neutral-100);
        margin: 0 0 var(--spacing-xs) 0;
    }
    
    .champion-stats {
        font-size: 0.875rem;
        color: rgba(255, 255, 255, 0.6);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main .block-container {
            padding: var(--spacing-md) var(--spacing-sm);
        }
        
        .stat-card {
            padding: var(--spacing-lg);
        }
        
        .metric-value {
            font-size: 2rem;
        }
        
        h2 {
            font-size: 1.5rem;
        }
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Enhanced metric cards function - EXACTLY AS ORIGINAL
def styled_metric(label, value, delta=None, delta_color="normal"):
    html = f"""
    <div class="stat-card">
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <p class="metric-label">{label}</p>
        </div>
        <p class="metric-value">{value}</p>
    """
    
    if delta:
        color_class = "gmb-blue" if delta_color == "blue" else "win" if delta_color == "good" else "loss" if delta_color == "bad" else ""
        html += f'<p class="metric-delta {color_class}">{delta}</p>'
    
    html += "</div>"
    return st.markdown(html, unsafe_allow_html=True)

# Connect to MongoDB Atlas - EXACTLY AS ORIGINAL
@st.cache_resource
def get_db():
    connection_string = st.secrets["database"]["mongodb_connection_string"]
    client = pymongo.MongoClient(connection_string)
    return client.CALDYA

# Get champion data - EXACTLY AS ORIGINAL
@st.cache_data(ttl=3600)
def get_champion_data():
    versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
    latest = versions[0]
    champs = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{latest}/data/en_US/champion.json").json()
    
    champ_mapping = {}
    for key, data in champs["data"].items():
        champ_name = data["name"]
        champ_mapping[champ_name.lower()] = key
        champ_mapping[champ_name.lower().replace(" ", "")] = key
        champ_mapping[champ_name.lower().replace("'", "")] = key
        champ_mapping[champ_name.lower().replace(" ", "").replace("'", "")] = key
        
        if champ_name == "Wukong":
            champ_mapping["monkeyking"] = key
        elif champ_name == "Nunu & Willump":
            champ_mapping["nunu"] = key
        
    return champs["data"], latest, champ_mapping

# Helper function to find champion key - EXACTLY AS ORIGINAL
def find_champion_key(champion_name, champion_data, champ_mapping):
    if not champion_name:
        return None
    
    champ_key = next((k for k, v in champion_data.items() if v["name"] == champion_name), None)
    if champ_key:
        return champ_key
    
    normalized_name = champion_name.lower().replace(" ", "").replace("'", "")
    if normalized_name in champ_mapping:
        return champ_mapping[normalized_name]
    
    for key, data in champion_data.items():
        if champion_name.lower() in data["name"].lower() or data["name"].lower() in champion_name.lower():
            return key
    
    if champion_name in champion_data:
        return champion_name
    
    return None

# Load data functions - EXACTLY AS ORIGINAL
@st.cache_data(ttl=300)
def load_games():
    db = get_db()
    return list(db.CLA_Games.find().sort("date", -1))

@st.cache_data(ttl=300)
def load_players():
    db = get_db()
    return list(db.CLA_Players.find())

@st.cache_data(ttl=300)
def load_scrims():
    db = get_db()
    return list(db.CLA_Scrims.find())

# Format time difference - EXACTLY AS ORIGINAL
def format_time_diff(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds:02d}"

# Champion card creation functions - EXACTLY AS ORIGINAL
def create_champion_card(champ_data, role_color, champion_data, champ_mapping, ddragon_version):
    """Create a simple champion card with clear separation using only native Streamlit components"""
    champion_name = champ_data["champion"]
    win_rate = champ_data["win_rate"]
    games = champ_data["games"]
    wins = champ_data["wins"]
    losses = champ_data["losses"]
    
    # Get champion key for image
    champ_key = find_champion_key(champion_name, champion_data, champ_mapping)
    
    # Determine win rate status
    if win_rate >= 70:
        wr_status = "Excellent"
    elif win_rate >= 50:
        wr_status = "Good"
    else:
        wr_status = "Needs Work"
    
    # Champion icon centered
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if champ_key:
            st.image(
                f"https://ddragon.leagueoflegends.com/cdn/{ddragon_version}/img/champion/{champ_key}.png",
                width=100
            )
        else:
            st.write("❓")
    
    # Champion name centered
    st.markdown(f"### {champion_name}")
    
    # Win rate as main metric
    st.metric(label="Win Rate", value=f"{win_rate:.1f}%", delta=wr_status)
    
    # Stats in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Wins", wins)
    with col2:
        st.metric("Games", games)
    with col3:
        st.metric("Losses", losses)
    
    # Extra spacing
    st.write("")

def create_champion_row(champ_data, role_color, champion_data, champ_mapping, ddragon_version):
    """Create a compact champion row for detailed view"""
    champion_name = champ_data["champion"]
    win_rate = champ_data["win_rate"]
    games = champ_data["games"]
    wins = champ_data["wins"]
    losses = champ_data["losses"]
    
    champ_key = find_champion_key(champion_name, champion_data, champ_mapping)
    wr_color = "#10b981" if win_rate >= 60 else "#f59e0b" if win_rate >= 40 else "#ef4444"
    
    col1, col2, col3, col4 = st.columns([1, 3, 2, 2])
    
    with col1:
        if champ_key:
            st.image(f"https://ddragon.leagueoflegends.com/cdn/{ddragon_version}/img/champion/{champ_key}.png", width=50)
        else:
            st.markdown(f"""
            <div style="width: 50px; height: 50px; background: #334155; border-radius: 8px; 
                        display: flex; align-items: center; justify-content: center; border: 2px solid {role_color};">
                <span style="color: white;">?</span>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"**{champion_name}**")
    
    with col3:
        st.metric("Win Rate", f"{win_rate:.1f}%")
    
    with col4:
        st.markdown(f"**{wins}W - {losses}L** ({games}g)")

# Load data
games = load_games()
players_db = load_players()
champion_data, ddragon_version, champ_mapping = get_champion_data()

# Enhanced sidebar with modern design - EXACTLY AS ORIGINAL
with st.sidebar:
    # Header with logo and text inline
    st.markdown("""
    <div class="sidebar-header">
        <img src="data:image/png;base64,{}" width="40" style="border-radius: 50%;">
        <div>
            <h1 style="font-size: 1.8rem; margin: 0; background: linear-gradient(135deg, #3b82f6, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                CALDYA
            </h1>
            <p style="color: #94a3b8; font-size: 0.9rem; margin: 0;">Analytics Dashboard</p>
        </div>
    </div>
    """.format(
        # Try to load logo and convert to base64, or use empty string if it fails
        __import__('base64').b64encode(open("logo.png", "rb").read()).decode() if __import__('os').path.exists("logo.png") else ""
    ), unsafe_allow_html=True)
    
    # Modern navigation - Main pages
    main_page = st.radio(
        "Main Navigation",
        ["Officials", "Scrims"]
    )
    
    # Sub-navigation for Officials page
    if main_page == "Officials":
        page = st.radio(
            "Officials Analysis",
            ["Officials", "Team Stats", "Player Stats", "Champion Analysis"]
        )
    
    # Add some stats in sidebar
    st.markdown("---")
    
    # Quick stats
    if games:
        total_games = len(games)
        wins = sum(1 for game in games if game.get("win"))
        win_rate = (wins / total_games * 100) if total_games > 0 else 0
        
        st.markdown(f"""
        <div class="modern-card" style="padding: 1rem; margin: 1rem 0;">
            <h4 style="margin: 0 0 0.5rem 0; color: #60a5fa;">Quick Stats</h4>
            <p style="margin: 0.25rem 0; font-size: 0.9rem;"><strong>{total_games}</strong> Total Games</p>
            <p style="margin: 0.25rem 0; font-size: 0.9rem;"><strong>{wins}W - {total_games-wins}L</strong></p>
            <p style="margin: 0.25rem 0; font-size: 0.9rem; color: {'#10b981' if win_rate >= 50 else '#ef4444'};">
                <strong>{win_rate:.1f}%</strong> Win Rate
            </p>
        </div>
        """, unsafe_allow_html=True)

# Page routing based on selection - EXACTLY AS ORIGINAL BUT WITH ENHANCED STYLING
if main_page == "Officials":
    # Use original page routing from the provided code
    if page == "Officials":
        st.title("Officials Overview")
        
        if not games:
            st.warning("No games found in database. Please import game data first.")
        else:
            # Create games table for listing
            games_df = pd.DataFrame([
                {
                    "id": str(game.get("_id")),
                    "date": game.get("date"),
                    "opponent": game.get("opponent_team", {}).get("name", "Unknown"),
                    "result": "WIN" if game.get("win") else "LOSS",
                    "side": game.get("Caldya_side", "").upper(),
                    "duration": game.get("game_duration", "0:00")
                } for game in games
            ])
            
            # Enhanced filtering section - EXACTLY AS ORIGINAL
            with st.container():
                st.subheader("Find an Official")
                
                # Extract all champions for filtering
                all_caldya_champions = set()
                all_enemy_champions = set()
                caldya_player_names = ["Nille", "SPOOKY", "Nafkelah", "Soldier", "Steeelback"]
                
                for game in games:
                    caldya_team_id = game.get("Caldya_id")
                    if "final_items" in game:
                        for player, item_data in game["final_items"].items():
                            champion = item_data.get("champion", "")
                            team_id = item_data.get("team_id")
                            
                            if champion:
                                is_caldya_player = any(player.upper() == caldya_name.upper() for caldya_name in caldya_player_names)
                                
                                if is_caldya_player and team_id == caldya_team_id:
                                    all_caldya_champions.add(champion)
                                elif team_id != caldya_team_id:
                                    all_enemy_champions.add(champion)
                
                # Sort champion lists
                caldya_champions_list = ["All"] + sorted(list(all_caldya_champions))
                enemy_champions_list = ["All"] + sorted(list(all_enemy_champions))
                
                col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
                
                with col1:
                    # Date filtering
                    min_date = games_df["date"].min() if not games_df.empty else ""
                    max_date = games_df["date"].max() if not games_df.empty else ""
                    date_range = st.date_input("Date Range", 
                                               value=[min_date, max_date] if min_date and max_date else None,
                                               key="date_filter")
                    
                    # Result filter
                    result_filter = st.radio("Result", ["All", "WIN", "LOSS"])
                
                with col2:
                    # Side filter
                    side_filter = st.radio("Side", ["All", "BLUE", "RED"])
                    
                    # Opponent filter
                    opponents = ["All"] + sorted(list(set(games_df["opponent"].tolist())))
                    opponent_filter = st.selectbox("Opponent", opponents)
                
                with col3:
                    # Champion filters
                    st.markdown("**Champion Filters**")
                    allied_champion_filter = st.selectbox("Allied Champion", caldya_champions_list, 
                                                         help="Filter games where Caldya played this champion")
                    enemy_champion_filter = st.selectbox("Enemy Champion", enemy_champions_list,
                                                        help="Filter games where opponent played this champion")
                
                with col4:
                    # Apply filters - EXACTLY AS ORIGINAL
                    filtered_games = games_df.copy()
                    
                    # Date filter
                    if len(date_range) == 2:
                        try:
                            start_date, end_date = date_range
                            filtered_games = filtered_games[(filtered_games["date"] >= str(start_date)) & 
                                                           (filtered_games["date"] <= str(end_date))]
                        except:
                            pass
                    
                    # Basic filters
                    if result_filter != "All":
                        filtered_games = filtered_games[filtered_games["result"] == result_filter]
                    if side_filter != "All":
                        filtered_games = filtered_games[filtered_games["side"] == side_filter]
                    if opponent_filter != "All":
                        filtered_games = filtered_games[filtered_games["opponent"] == opponent_filter]
                    
                    # Champion filters - need to check actual game data - EXACTLY AS ORIGINAL
                    if allied_champion_filter != "All" or enemy_champion_filter != "All":
                        valid_game_ids = []
                        
                        for game in games:
                            game_id = str(game.get("_id"))
                            caldya_team_id = game.get("Caldya_id")
                            
                            # Check if this game matches current filters (before champion filter)
                            if game_id not in filtered_games["id"].values:
                                continue
                            
                            caldya_champions_in_game = set()
                            enemy_champions_in_game = set()
                            
                            if "final_items" in game:
                                for player, item_data in game["final_items"].items():
                                    champion = item_data.get("champion", "")
                                    team_id = item_data.get("team_id")
                                    
                                    if champion:
                                        is_caldya_player = any(player.upper() == caldya_name.upper() for caldya_name in caldya_player_names)
                                        
                                        if is_caldya_player and team_id == caldya_team_id:
                                            caldya_champions_in_game.add(champion)
                                        elif team_id != caldya_team_id:
                                            enemy_champions_in_game.add(champion)
                            
                            # Check champion filters
                            allied_match = (allied_champion_filter == "All" or 
                                          allied_champion_filter in caldya_champions_in_game)
                            enemy_match = (enemy_champion_filter == "All" or 
                                         enemy_champion_filter in enemy_champions_in_game)
                            
                            if allied_match and enemy_match:
                                valid_game_ids.append(game_id)
                        
                        # Filter dataframe to only include games that match champion criteria
                        filtered_games = filtered_games[filtered_games["id"].isin(valid_game_ids)]
                    
                    # Game selection
                    if not filtered_games.empty:
                        game_options = [f"{row['date']} | {row['opponent']} ({row['result']}, {row['side']} side)" 
                                      for _, row in filtered_games.iterrows()]
                        
                        selected_index = st.selectbox("Select an Official", 
                                                    range(len(game_options)),
                                                    format_func=lambda i: game_options[i])
                        
                        selected_id = filtered_games.iloc[selected_index]["id"]
                        
                        # Display selection summary with champion info
                        selected_row = filtered_games.iloc[selected_index]
                        result_color = "#10b981" if selected_row['result'] == "WIN" else "#ef4444"
                        
                        # Add champion info to summary if filters are active
                        champion_info = ""
                        if allied_champion_filter != "All":
                            champion_info += f" • Allied: {allied_champion_filter}"
                        if enemy_champion_filter != "All":
                            champion_info += f" • Enemy: {enemy_champion_filter}"
                        
                        st.markdown(f"""
                        <div style="background: rgba(51, 65, 85, 0.3); padding: 1rem; border-radius: 8px; margin-top: 1rem; border-left: 4px solid {result_color};">
                            <strong>Selected:</strong> {selected_row['date']} vs {selected_row['opponent']} • 
                            <span style="color: {result_color}; font-weight: 600;">{selected_row['result']}</span> • 
                            {selected_row['side']} side • Duration: {selected_row['duration']}{champion_info}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.warning("No officials match the selected filters.")
                        selected_id = None
            
            # Game details section - EXACTLY AS ORIGINAL WITH ENHANCED STYLING
            if selected_id:
                game = next((g for g in games if str(g.get("_id")) == selected_id), None)
                
                if game:
                    st.header("Game Details")
                    
                    # Game header with enhanced styling
                    result_color = "#10b981" if game.get("win") else "#ef4444"
                    result_text = "VICTORY" if game.get("win") else "DEFEAT"
                    
                    st.markdown(f"""
                    <div class="modern-card" style="text-align: center; padding: 2rem;">
                        <h2 style="margin: 0; color: {result_color}; font-size: 2.5rem; text-shadow: 0 0 20px {result_color}50;">
                            {result_text}
                        </h2>
                        <h3 style="margin: 0.5rem 0 0 0; color: #94a3b8;">
                            vs {game.get('opponent_team', {}).get('name', 'Unknown')}
                        </h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Game metadata with modern cards
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        styled_metric("Date", game.get('date'))
                        styled_metric("Duration", game.get('game_duration', '0:00'))
                    
                    with col2:
                        styled_metric("Side", game.get('Caldya_side', '').upper())
                        # First blood
                        first_blood = game.get('first_blood', {})
                        if first_blood.get('team'):
                            fb_team = "Caldya" if first_blood.get('team') == "NAFKELAH_TEAM" else "Opponent"
                            styled_metric("First Blood", fb_team)
                    
                    with col3:
                        # Objectives with enhanced display
                        caldya_objectives = game.get('objectives', {}).get('blue_team' if game.get('Caldya_side') == 'blue' else 'red_team', {}).get('objectives', {})
                        enemy_objectives = game.get('objectives', {}).get('red_team' if game.get('Caldya_side') == 'blue' else 'blue_team', {}).get('objectives', {})
                        
                        dragons_caldya = caldya_objectives.get('dragon', {}).get('kills', 0)
                        dragons_enemy = enemy_objectives.get('dragon', {}).get('kills', 0)
                        styled_metric("Dragons", f"{dragons_caldya} - {dragons_enemy}")
                        
                        barons_caldya = caldya_objectives.get('baron', {}).get('kills', 0)
                        barons_enemy = enemy_objectives.get('baron', {}).get('kills', 0)
                        styled_metric("Barons", f"{barons_caldya} - {barons_enemy}")
                    
                    # Enhanced Final Items Section - EXACTLY AS ORIGINAL
                    st.header("Scoreboard")
                    if "final_items" in game and "player_data" in game:
                        caldya_team_id = game.get("Caldya_id")
                        caldya_player_items = []
                        opponent_player_items = []
                        
                        for player, item_data in game["final_items"].items():
                            # Get player KDA from game data
                            player_stats = game["player_data"].get(player, {})
                            kda = player_stats.get("kda", "0/0/0")
                            
                            if item_data.get("team_id") == caldya_team_id:
                                caldya_player_items.append((player, item_data, kda))
                            else:
                                opponent_player_items.append((player, item_data, kda))
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("Caldya Final Items")
                            
                            for player, item_data, kda in caldya_player_items:
                                champ_name = item_data.get("champion")
                                champ_key = find_champion_key(champ_name, champion_data, champ_mapping)
                                
                                st.markdown('<div class="player-items-row">', unsafe_allow_html=True)
                                
                                # Layout: Champion section (icon + name/KDA below) | Items section
                                champion_col, items_col = st.columns([1, 4])
                                
                                with champion_col:
                                    # Champion icon
                                    if champ_key:
                                        st.image(
                                            f"https://ddragon.leagueoflegends.com/cdn/{ddragon_version}/img/champion/{champ_key}.png", 
                                            width=60
                                        )
                                    
                                    # Player info under champion
                                    st.markdown(f"""
                                    <div class="player-info-section">
                                        <div class="player-name">{player}</div>
                                        <div class="player-score">{kda}</div>
                                    </div>
                                    """, unsafe_allow_html=True)
                                
                                with items_col:
                                    # Items right after champion - EXACTLY AS ORIGINAL
                                    items_html = '<div class="items-section">'
                                    trinket_id = item_data.get("trinket", 0)
                                    player_items = item_data.get("items", [])
                                    
                                    # Si le dernier item est égal au trinket, ne pas l'afficher dans les items
                                    if player_items and trinket_id > 0 and len(player_items) > 0 and player_items[-1] == trinket_id:
                                        player_items = player_items[:-1]  # Enlever le dernier item
                                    
                                    for i, item_id in enumerate(player_items):
                                        if i < 6 and item_id > 0:
                                            items_html += f'<img src="https://ddragon.leagueoflegends.com/cdn/{ddragon_version}/img/item/{item_id}.png" width="35" style="margin:2px; border-radius:4px; border:1px solid var(--border);" />'
                                    
                                    # Afficher le trinket avec un style spécial
                                    if trinket_id > 0:
                                        items_html += f'<img src="https://ddragon.leagueoflegends.com/cdn/{ddragon_version}/img/item/{trinket_id}.png" width="35" style="margin:2px 2px 2px 8px; border-radius:4px; border:2px solid var(--accent-primary);" />'
                                    
                                    items_html += '</div>'
                                    st.markdown(items_html, unsafe_allow_html=True)
                                
                                st.markdown('</div>', unsafe_allow_html=True)
                        
                        with col2:
                            st.subheader("Opponent Final Items")
                            
                            for player, item_data, kda in opponent_player_items:
                                champ_name = item_data.get("champion")
                                champ_key = find_champion_key(champ_name, champion_data, champ_mapping)
                                
                                st.markdown('<div class="player-items-row">', unsafe_allow_html=True)
                                
                                # Layout: Champion section (icon + name/KDA below) | Items section
                                champion_col, items_col = st.columns([1, 4])
                                
                                with champion_col:
                                    # Champion icon
                                    if champ_key:
                                        st.image(
                                            f"https://ddragon.leagueoflegends.com/cdn/{ddragon_version}/img/champion/{champ_key}.png", 
                                            width=60
                                        )
                                    
                                    # Player info under champion
                                    st.markdown(f"""
                                    <div class="player-info-section">
                                        <div class="player-name" style="color: var(--danger);">{player}</div>
                                        <div class="player-score">{kda}</div>
                                    </div>
                                    """, unsafe_allow_html=True)
                                
                                with items_col:
                                    # Items right after champion - EXACTLY AS ORIGINAL
                                    items_html = '<div class="items-section">'
                                    trinket_id = item_data.get("trinket", 0)
                                    player_items = item_data.get("items", [])
                                    
                                    # Si le dernier item est égal au trinket, ne pas l'afficher dans les items
                                    if player_items and trinket_id > 0 and len(player_items) > 0 and player_items[-1] == trinket_id:
                                        player_items = player_items[:-1]  # Enlever le dernier item
                                    
                                    for i, item_id in enumerate(player_items):
                                        if i < 6 and item_id > 0:
                                            items_html += f'<img src="https://ddragon.leagueoflegends.com/cdn/{ddragon_version}/img/item/{item_id}.png" width="35" style="margin:2px; border-radius:4px; border:1px solid var(--border);" />'
                                    
                                    # Afficher le trinket avec un style spécial
                                    if trinket_id > 0:
                                        items_html += f'<img src="https://ddragon.leagueoflegends.com/cdn/{ddragon_version}/img/item/{trinket_id}.png" width="35" style="margin:2px 2px 2px 8px; border-radius:4px; border:2px solid var(--danger);" />'
                                    
                                    items_html += '</div>'
                                    st.markdown(items_html, unsafe_allow_html=True)
                                
                                st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Enhanced Player Performance - EXACTLY AS ORIGINAL
                    st.header("Player Performance")
                    
                    if "player_data" in game and "player_positions" in game:
                        caldya_player_names = ["Nille", "SPOOKY", "Nafkelah", "Soldier", "Steeelback"]
                        caldya_players = []
                        opponent_players = []
                        
                        for player, stats in game["player_data"].items():
                            player_data = {
                                "Player": player,
                                "KDA": stats.get("kda", "0/0/0"),
                                "Gold@15": stats.get("gold_15min", 0),
                                "CS@15": stats.get("cs_15min", 0),
                                "Gold Diff@15": stats.get("gold_diff_15min", 0),
                                "CS Diff@15": stats.get("cs_diff_15min", 0)
                            }
                            
                            if player in caldya_player_names or player.upper() in [p.upper() for p in caldya_player_names]:
                                caldya_players.append(player_data)
                            else:
                                opponent_players.append(player_data)
                        
                        column_config = {
                            "Gold Diff@15": st.column_config.NumberColumn(
                                "Gold Diff@15",
                                help="Gold difference at 15 minutes",
                                format="%d"
                            ),
                            "CS Diff@15": st.column_config.NumberColumn(
                                "CS Diff@15",
                                help="CS difference at 15 minutes",
                                format="%.1f"
                            ),
                        }
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            if caldya_players:
                                st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                                st.subheader("Caldya Players")
                                caldya_df = pd.DataFrame(caldya_players)
                                st.dataframe(
                                    caldya_df,
                                    column_config=column_config,
                                    hide_index=True,
                                    use_container_width=True
                                )
                                st.markdown('</div>', unsafe_allow_html=True)
                        
                        with col2:
                            if opponent_players:
                                st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                                st.subheader("Opponent Players")
                                opponent_df = pd.DataFrame(opponent_players)
                                st.dataframe(
                                    opponent_df,
                                    column_config=column_config,
                                    hide_index=True,
                                    use_container_width=True
                                )
                                st.markdown('</div>', unsafe_allow_html=True)

    elif page == "Team Stats":
        st.title("Team Statistics")
        
        if not games:
            st.warning("No games found in database. Please import game data first.")
        else:
            # Calculate stats - EXACTLY AS ORIGINAL
            total_games = len(games)
            wins = sum(1 for game in games if game.get("win"))
            losses = total_games - wins
            win_rate = (wins / total_games * 100) if total_games > 0 else 0
            
            # Side stats
            blue_games = sum(1 for game in games if game.get("Caldya_side") == "blue")
            blue_wins = sum(1 for game in games if game.get("Caldya_side") == "blue" and game.get("win"))
            blue_win_rate = (blue_wins / blue_games * 100) if blue_games > 0 else 0
            
            red_games = sum(1 for game in games if game.get("Caldya_side") == "red")
            red_wins = sum(1 for game in games if game.get("Caldya_side") == "red" and game.get("win"))
            red_win_rate = (red_wins / red_games * 100) if red_games > 0 else 0
            
            # Modern metrics display
            col1, col2, col3 = st.columns(3)
            
            with col1:
                styled_metric("Overall Record", f"{wins}W - {losses}L", f"Win Rate: {win_rate:.1f}%", "blue")
                st.progress(win_rate/100)
            
            with col2:
                styled_metric("Blue Side Record", f"{blue_wins}W - {blue_games-blue_wins}L", f"Win Rate: {blue_win_rate:.1f}%", "blue")
                st.progress(blue_win_rate/100)
            
            with col3:
                styled_metric("Red Side Record", f"{red_wins}W - {red_games-red_wins}L", f"Win Rate: {red_win_rate:.1f}%", "blue") 
                st.progress(red_win_rate/100)
            
            # Enhanced Objective Control section - EXACTLY AS ORIGINAL
            st.header("Objective Control")
            
            # Calculate objective stats (excluding first blood from dataframe)
            dragons_total = 0
            barons_total = 0
            first_dragon_games = 0
            first_dragon_wins = 0
            first_baron_games = 0
            first_baron_wins = 0
            first_herald_games = 0
            first_herald_wins = 0
            
            for game in games:
                caldya_team_data = None
                if game.get("Caldya_side") == "blue" and "objectives" in game:
                    caldya_team_data = game["objectives"].get("blue_team", {})
                elif game.get("Caldya_side") == "red" and "objectives" in game:
                    caldya_team_data = game["objectives"].get("red_team", {})
                
                if caldya_team_data and "objectives" in caldya_team_data:
                    dragons_total += caldya_team_data["objectives"].get("dragon", {}).get("kills", 0)
                    barons_total += caldya_team_data["objectives"].get("baron", {}).get("kills", 0)
                    
                    if caldya_team_data["objectives"].get("dragon", {}).get("first", False):
                        first_dragon_games += 1
                        if game.get("win"):
                            first_dragon_wins += 1
                    
                    if caldya_team_data["objectives"].get("baron", {}).get("first", False):
                        first_baron_games += 1
                        if game.get("win"):
                            first_baron_wins += 1
                    
                    if caldya_team_data["objectives"].get("riftHerald", {}).get("first", False):
                        first_herald_games += 1
                        if game.get("win"):
                            first_herald_wins += 1
            
            # Calculate rates
            first_dragon_rate = (first_dragon_wins / first_dragon_games * 100) if first_dragon_games > 0 else 0
            first_baron_rate = (first_baron_wins / first_baron_games * 100) if first_baron_games > 0 else 0
            first_herald_rate = (first_herald_wins / first_herald_games * 100) if first_herald_games > 0 else 0
            
            # Create modern visualization with Plotly (excluding first blood) - EXACTLY AS ORIGINAL
            objective_df = pd.DataFrame({
                "Objective": ["First Dragon", "First Herald", "First Baron"],
                "Win Rate": [first_dragon_rate, first_herald_rate, first_baron_rate],
                "Total Games": [first_dragon_games, first_herald_games, first_baron_games]
            })
            
            col1, col2 = st.columns([3, 2])
            
            with col1:
                # Create Plotly chart
                fig = go.Figure(data=[
                    go.Bar(
                        x=objective_df["Objective"], 
                        y=objective_df["Win Rate"],
                        marker=dict(
                            color=['#f59e0b', '#8b5cf6', '#3b82f6'],
                            line=dict(color='#1e293b', width=2)
                        ),
                        text=[f"{rate:.1f}%" for rate in objective_df["Win Rate"]],
                        textposition='auto',
                        textfont=dict(color='white', size=12, family='Inter')
                    )
                ])
                
                fig.update_layout(
                    title=dict(
                        text="Win Rate When Securing Objectives",
                        font=dict(color='#f8fafc', size=16, family='Inter'),
                        x=0.5
                    ),
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#f8fafc', family='Inter'),
                    yaxis=dict(
                        range=[0, 100],
                        title="Win Rate (%)",
                        gridcolor='#334155',
                        gridwidth=1
                    ),
                    xaxis=dict(
                        title="",
                        tickfont=dict(size=10)
                    ),
                    margin=dict(l=20, r=20, t=50, b=20),
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                styled_metric("Avg. Dragons per Game", f"{dragons_total / total_games:.1f}" if total_games > 0 else "0")
                styled_metric("Avg. Barons per Game", f"{barons_total / total_games:.1f}" if total_games > 0 else "0")
                
                st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                st.dataframe(
                    objective_df,
                    column_config={
                        "Win Rate": st.column_config.ProgressColumn(
                            "Win Rate",
                            help="Win rate when securing objective",
                            format="%.1f%%",
                            min_value=0,
                            max_value=100,
                        ),
                    },
                    hide_index=True,
                    use_container_width=True
                )
                st.markdown('</div>', unsafe_allow_html=True)

    elif page == "Player Stats":
        st.title("Player Statistics")
        
        if not players_db:
            st.warning("No player data found in database.")
        else:
            # Convert player data - EXACTLY AS ORIGINAL
            players_data = []
            for player in players_db:
                players_data.append({
                    "name": player.get("name", "Unknown"),
                    "games_played": player.get("games_played", 0),
                    "avg_gold_15min": player.get("avg_player_data", {}).get("gold_15min", 0),
                    "avg_cs_15min": player.get("avg_player_data", {}).get("cs_15min", 0),
                    "avg_gold_diff_15min": player.get("avg_player_data", {}).get("gold_diff_15min", 0),
                    "avg_cs_diff_15min": player.get("avg_player_data", {}).get("cs_diff_15min", 0),
                    "kda_kills": player.get("avg_player_data", {}).get("kda_kills", 0),
                    "kda_deaths": player.get("avg_player_data", {}).get("kda_deaths", 0),
                    "kda_assists": player.get("avg_player_data", {}).get("kda_assists", 0),
                    "kda_ratio": player.get("avg_player_data", {}).get("kda_ratio", 0),
                    "avg_kda": player.get("avg_player_data", {}).get("kda", "0/0/0"),
                    "avg_control_wards": player.get("avg_control_wards", 0),
                    "avg_vision_score": player.get("avg_challenges", {}).get("vision_score", 0),
                    "avg_damage_per_minute": player.get("avg_challenges", {}).get("damage_per_minute", 0)
                })
            
            players_df = pd.DataFrame(players_data)
            
            # Enhanced player selector
            players = sorted(list(players_df["name"]))
            selected_player = st.selectbox("Select Player", players)
            
            if selected_player:
                player_data = players_df[players_df["name"] == selected_player].iloc[0]
                
                # Header with player stats
                st.markdown(f"""
                <div class="modern-card" style="text-align: center; padding: 2rem;">
                    <h2 style="margin: 0; background: linear-gradient(135deg, #3b82f6, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                        {selected_player}
                    </h2>
                    <p style="color: #94a3b8; margin: 0.5rem 0 0 0;">Player Statistics Overview</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Key metrics
                col1, col2, col3 = st.columns(3)
                with col1:
                    styled_metric("Games Played", str(player_data["games_played"]))
                with col2:
                    styled_metric("KDA Ratio", f"{player_data['kda_ratio']:.2f}")
                with col3:
                    styled_metric("Average KDA", player_data["avg_kda"])
                
                # Performance metrics - EXACTLY AS ORIGINAL
                st.header("Performance Metrics")
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    styled_metric("Avg Gold@15", f"{player_data['avg_gold_15min']:.0f}")
                    diff_color = "good" if player_data['avg_gold_diff_15min'] >= 0 else "bad"
                    styled_metric("Avg Gold Diff@15", f"{player_data['avg_gold_diff_15min']:+.0f}", delta_color=diff_color)
                
                with col2:
                    styled_metric("Avg CS@15", f"{player_data['avg_cs_15min']:.1f}")
                    cs_diff_color = "good" if player_data['avg_cs_diff_15min'] >= 0 else "bad"
                    styled_metric("Avg CS Diff@15", f"{player_data['avg_cs_diff_15min']:+.1f}", delta_color=cs_diff_color)
                
                with col3:
                    styled_metric("Avg Vision Score", f"{player_data['avg_vision_score']:.1f}")
                    styled_metric("Avg Control Wards", f"{player_data['avg_control_wards']:.1f}")
                
                with col4:
                    styled_metric("Avg Damage/Min", f"{player_data['avg_damage_per_minute']:.1f}")
                
                # Player Challenges (without visualization) - EXACTLY AS ORIGINAL
                st.header("Player Challenges")
                
                player_challenges = {}
                for player in players_db:
                    if player.get("name") == selected_player:
                        player_challenges = player.get("avg_challenges", {})
                        break
                
                if player_challenges:
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        styled_metric("Vision Score", f"{player_challenges.get('vision_score', 0):.1f}")
                        styled_metric("Damage Per Minute", f"{player_challenges.get('damage_per_minute', 0):.1f}")
                        styled_metric("Buffs Stolen", f"{player_challenges.get('buffs_stolen', 0):.1f}")
                    
                    with col2:
                        styled_metric("Skillshots Hit", f"{player_challenges.get('skill_shots_hit', 0):.1f}")
                        styled_metric("Skillshots Dodged", f"{player_challenges.get('skill_shots_dodged', 0):.1f}")
                        styled_metric("Perfect Game", f"{player_challenges.get('perfect_game', 0):.2f}")
                    
                    with col3:
                        styled_metric("Turret Plates Taken", f"{player_challenges.get('turret_plates_taken', 0):.1f}")
                        danced = "Yes" if player_challenges.get('dance_with_rift_herald', False) else "No"
                        styled_metric("Danced with Herald", danced)
                else:
                    st.warning(f"No challenge data found for player {selected_player}")
                
                # Game history - EXACTLY AS ORIGINAL
                player_games = []
                for game in games:
                    if selected_player in game.get("player_data", {}):
                        player_stats = game["player_data"][selected_player]
                        player_games.append({
                            "game_id": str(game.get("_id")),
                            "date": game.get("date"),
                            "opponent": game.get("opponent_team", {}).get("name", "Unknown"),
                            "win": game.get("win", False),
                            "kda": player_stats.get("kda", "0/0/0"),
                            "gold_15min": player_stats.get("gold_15min", 0),
                            "cs_15min": player_stats.get("cs_15min", 0),
                            "gold_diff_15min": player_stats.get("gold_diff_15min", 0),
                            "cs_diff_15min": player_stats.get("cs_diff_15min", 0),
                            "position": game.get("player_positions", {}).get(selected_player, "")
                        })
                
                if player_games:
                    st.header("Game History")
                    
                    games_df = pd.DataFrame(player_games)
                    games_df = games_df.sort_values("date", ascending=False)
                    
                    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
                    st.dataframe(
                        games_df,
                        column_config={
                            "game_id": None,
                            "date": "Date",
                            "opponent": "Opponent",
                            "win": st.column_config.CheckboxColumn("Win"),
                            "kda": "KDA",
                            "gold_15min": st.column_config.NumberColumn("Gold@15", format="%d"),
                            "cs_15min": st.column_config.NumberColumn("CS@15", format="%.1f"),
                            "gold_diff_15min": st.column_config.NumberColumn("Gold Diff@15", format="%+d"),
                            "cs_diff_15min": st.column_config.NumberColumn("CS Diff@15", format="%+.1f")
                        },
                        hide_index=True,
                        use_container_width=True
                    )
                    st.markdown('</div>', unsafe_allow_html=True)

    elif page == "Champion Analysis":
        st.title("Champion Analysis")
        
        if not games:
            st.warning("No games found in database. Please import game data first.")
        else:
            # Define player roles - EXACTLY AS ORIGINAL
            caldya_players = {
                "Nille": "Top",
                "SPOOKY": "Jungle", 
                "Nafkelah": "Mid",
                "Soldier": "ADC",
                "Steeelback": "Support"
            }
            
            # Role colors for better visual distinction
            role_colors = {
                "Top": "#e11d48",      # Red
                "Jungle": "#10b981",   # Green  
                "Mid": "#3b82f6",      # Blue
                "ADC": "#f59e0b",      # Orange
                "Support": "#8b5cf6"   # Purple
            }
            
            # Collect champion data for Caldya players - EXACTLY AS ORIGINAL
            caldya_champion_data = {}
            opponent_champion_data = {}
            
            for game in games:
                game_win = game.get("win", False)
                caldya_team_id = game.get("Caldya_id")
                
                if "final_items" in game:
                    for player, item_data in game["final_items"].items():
                        champion = item_data.get("champion", "Unknown")
                        team_id = item_data.get("team_id")
                        
                        # Check if this is a Caldya player
                        caldya_player = None
                        for caldya_name, role in caldya_players.items():
                            if player.upper() == caldya_name.upper() or player == caldya_name:
                                caldya_player = caldya_name
                                break
                        
                        if caldya_player and team_id == caldya_team_id:
                            # Caldya player
                            role = caldya_players[caldya_player]
                            if role not in caldya_champion_data:
                                caldya_champion_data[role] = {}
                            if champion not in caldya_champion_data[role]:
                                caldya_champion_data[role][champion] = {"wins": 0, "games": 0}
                            
                            caldya_champion_data[role][champion]["games"] += 1
                            if game_win:
                                caldya_champion_data[role][champion]["wins"] += 1
                        
                        elif team_id != caldya_team_id:
                            # Opponent player
                            if "Opponent" not in opponent_champion_data:
                                opponent_champion_data["Opponent"] = {}
                            if champion not in opponent_champion_data["Opponent"]:
                                opponent_champion_data["Opponent"][champion] = {"wins": 0, "games": 0}
                            
                            opponent_champion_data["Opponent"][champion]["games"] += 1
                            if not game_win:  # Opponent wins when Caldya loses
                                opponent_champion_data["Opponent"][champion]["wins"] += 1
            
            # Create tabs for different views - EXACTLY AS ORIGINAL
            tab1, tab2 = st.tabs(["🏆 Caldya Champions", "⚔️ Opponent Analysis"])
            
            with tab1:
                st.markdown("""
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h2 style="background: linear-gradient(135deg, #3b82f6, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;">
                        Caldya Champion Performance by Role
                    </h2>
                    <p style="color: #94a3b8; font-size: 1.1rem;">Analyzing champion win rates for each team member</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Create role sections - EXACTLY AS ORIGINAL
                for role in ["Top", "Jungle", "Mid", "ADC", "Support"]:
                    player_name = [k for k, v in caldya_players.items() if v == role][0]
                    role_color = role_colors.get(role, "#3b82f6")
                    
                    if role in caldya_champion_data and caldya_champion_data[role]:
                        # Prepare data for this role
                        role_data = []
                        for champion, stats in caldya_champion_data[role].items():
                            if stats["games"] > 0:
                                win_rate = (stats["wins"] / stats["games"]) * 100
                                role_data.append({
                                    "champion": champion,
                                    "games": stats["games"],
                                    "wins": stats["wins"],
                                    "losses": stats["games"] - stats["wins"],
                                    "win_rate": win_rate
                                })
                        
                        # Sort by games played, then by win rate
                        role_data.sort(key=lambda x: (x["games"], x["win_rate"]), reverse=True)
                        
                        # Role header with modern styling
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, {role_color}20, {role_color}10); 
                                    border-left: 4px solid {role_color}; 
                                    border-radius: 12px; 
                                    padding: 1.5rem; 
                                    margin: 2rem 0 1rem 0;
                                    backdrop-filter: blur(10px);">
                            <h3 style="color: {role_color}; margin: 0; display: flex; align-items: center; gap: 1rem;">
                                <span style="font-size: 1.8rem;">{role}</span>
                                <span style="color: #94a3b8; font-size: 1.2rem; font-weight: 400;">• {player_name}</span>
                            </h3>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Create champion cards layout - EXACTLY AS ORIGINAL
                        if len(role_data) <= 3:
                            # Few champions - display in columns with vertical separators
                            if len(role_data) == 1:
                                cols = st.columns([1, 2, 1])
                                with cols[1]:
                                    create_champion_card(role_data[0], role_color, champion_data, champ_mapping, ddragon_version)
                            elif len(role_data) == 2:
                                cols = st.columns([2, 1, 2])
                                with cols[0]:
                                    create_champion_card(role_data[0], role_color, champion_data, champ_mapping, ddragon_version)
                                with cols[1]:
                                    st.markdown("", unsafe_allow_html=True)  # Separator space
                                with cols[2]:
                                    create_champion_card(role_data[1], role_color, champion_data, champ_mapping, ddragon_version)
                            elif len(role_data) == 3:
                                cols = st.columns([3, 1, 3, 1, 3])
                                with cols[0]:
                                    create_champion_card(role_data[0], role_color, champion_data, champ_mapping, ddragon_version)
                                with cols[1]:
                                    st.markdown('<div style="border-left: 2px solid #475569; height: 400px; margin: 2rem 0;"></div>', unsafe_allow_html=True)
                                with cols[2]:
                                    create_champion_card(role_data[1], role_color, champion_data, champ_mapping, ddragon_version)
                                with cols[3]:
                                    st.markdown('<div style="border-left: 2px solid #475569; height: 400px; margin: 2rem 0;"></div>', unsafe_allow_html=True)
                                with cols[4]:
                                    create_champion_card(role_data[2], role_color, champion_data, champ_mapping, ddragon_version)
                        else:
                            # Many champions - display in grid with metrics + detailed table
                            # Top 3 champions as cards with separators
                            cols = st.columns([3, 1, 3, 1, 3])
                            for i in range(min(3, len(role_data))):
                                col_index = i * 2  # 0, 2, 4
                                with cols[col_index]:
                                    create_champion_card(role_data[i], role_color, champion_data, champ_mapping, ddragon_version)
                                # Add separator after first two champions
                                if i < 2:
                                    with cols[col_index + 1]:
                                        st.markdown('<div style="border-left: 2px solid #475569; height: 400px; margin: 2rem 0;"></div>', unsafe_allow_html=True)
                            
                            # Remaining champions in detailed view
                            if len(role_data) > 3:
                                with st.expander(f"View All {role} Champions ({len(role_data)} total)", expanded=False):
                                    # Create detailed champion grid
                                    remaining_champs = role_data[3:]
                                    for champ_data in remaining_champs:
                                        create_champion_row(champ_data, role_color, champion_data, champ_mapping, ddragon_version)
                    else:
                        # No data for this role
                        st.markdown(f"""
                        <div style="background: rgba(51, 65, 85, 0.3); 
                                    border-left: 4px solid {role_color}; 
                                    border-radius: 12px; 
                                    padding: 1.5rem; 
                                    margin: 2rem 0 1rem 0;
                                    text-align: center;">
                            <h3 style="color: {role_color}; margin: 0 0 0.5rem 0;">{role} • {player_name}</h3>
                            <p style="color: #94a3b8; margin: 0;">No champion data available</p>
                        </div>
                        """, unsafe_allow_html=True)
            
            with tab2:
                st.markdown("""
                <div style="text-align: center; margin-bottom: 2rem;">
                    <h2 style="background: linear-gradient(135deg, #ef4444, #f87171); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;">
                        Enemy Champion Analysis
                    </h2>
                    <p style="color: #94a3b8; font-size: 1.1rem;">Champions that opponents use against Caldya</p>
                </div>
                """, unsafe_allow_html=True)
                
                if "Opponent" in opponent_champion_data:
                    # Prepare opponent data - EXACTLY AS ORIGINAL
                    opponent_data = []
                    for champion, stats in opponent_champion_data["Opponent"].items():
                        if stats["games"] > 0:
                            win_rate = (stats["wins"] / stats["games"]) * 100
                            opponent_data.append({
                                "champion": champion,
                                "games": stats["games"],
                                "wins": stats["wins"],
                                "losses": stats["games"] - stats["wins"],
                                "win_rate": win_rate
                            })
                    
                    if opponent_data:
                        # Sort by games played, then by win rate
                        opponent_data.sort(key=lambda x: (x["games"], x["win_rate"]), reverse=True)
                        
                        # Summary stats cards
                        total_unique_champs = len(opponent_data)
                        high_winrate_champs = len([d for d in opponent_data if d["win_rate"] > 60])
                        most_played = opponent_data[0] if opponent_data else None
                        
                        # Top stats
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            styled_metric("Unique Champions Faced", str(total_unique_champs))
                        with col2:
                            styled_metric("High Win Rate vs Caldya", f"{high_winrate_champs} champions", "> 60% win rate", "bad")
                        with col3:
                            if most_played:
                                styled_metric("Most Played Against Us", most_played["champion"], f"{most_played['games']} games", "blue")
                        
                        # Threat Level Analysis - EXACTLY AS ORIGINAL
                        st.subheader("🚨 Threat Level Analysis")
                        
                        # Categorize threats
                        high_threat = [d for d in opponent_data if d["win_rate"] >= 70 and d["games"] >= 2]
                        medium_threat = [d for d in opponent_data if 50 <= d["win_rate"] < 70 and d["games"] >= 2]
                        low_threat = [d for d in opponent_data if d["win_rate"] < 50 and d["games"] >= 2]
                        
                        # High threat champions
                        if high_threat:
                            st.markdown("""
                            <h4 style="color: #ef4444; margin: 1.5rem 0 1rem 0;">
                                🔥 High Threat Champions (≥70% win rate, min 2 games)
                            </h4>
                            """, unsafe_allow_html=True)
                            
                            # Display threat champions in rows
                            for champ_data in high_threat:
                                create_champion_row(champ_data, "#ef4444", champion_data, champ_mapping, ddragon_version)
                        
                        # Medium threat champions  
                        if medium_threat:
                            st.markdown("""
                            <h4 style="color: #f59e0b; margin: 1.5rem 0 1rem 0;">
                                ⚠️ Medium Threat Champions (50-69% win rate, min 2 games)
                            </h4>
                            """, unsafe_allow_html=True)
                            
                            # Display threat champions in rows
                            for champ_data in medium_threat:
                                create_champion_row(champ_data, "#f59e0b", champion_data, champ_mapping, ddragon_version)
                        
                        # Low threat champions
                        if low_threat:
                            st.markdown("""
                            <h4 style="color: #10b981; margin: 1.5rem 0 1rem 0;">
                                ✅ Favorable Matchups (<50% win rate vs us, min 2 games)
                            </h4>
                            """, unsafe_allow_html=True)
                            
                            # Display threat champions in rows
                            for champ_data in low_threat:
                                create_champion_row(champ_data, "#10b981", champion_data, champ_mapping, ddragon_version)
                        
                        # Detailed table for all opponents
                        with st.expander("📊 Complete Opponent Champion Statistics", expanded=False):
                            # Display all opponent data in detailed format
                            for champ_data in opponent_data:
                                create_champion_row(champ_data, "#94a3b8", champion_data, champ_mapping, ddragon_version)
                else:
                    st.info("No opponent champion data available")

elif main_page == "Scrims":
    st.title("Scrims Analysis")
    
    # Load scrims data
    scrims_data = load_scrims()
    
    if not scrims_data:
        st.warning("No scrims data found in database. Please import scrim data first.")
    else:
        # Define player roles - EXACTLY AS ORIGINAL
        players = {
            "Nille": "Top",
            "SPOOKY": "Jungle", 
            "Nafkelah": "Mid",
            "Soldier": "ADC",
            "Steeelback": "Support"
        }
        
        # Role colors for better visual distinction
        role_colors = {
            "Top": "#e11d48",      # Red
            "Jungle": "#10b981",   # Green  
            "Mid": "#3b82f6",      # Blue
            "ADC": "#f59e0b",      # Orange
            "Support": "#8b5cf6"   # Purple
        }
        
        # Create tabs for different views - EXACTLY AS ORIGINAL
        tab1, tab2 = st.tabs(["Champion Analysis", "Game Browser"])
        
        with tab1:
            # ALL THE SCRIMS CHAMPION ANALYSIS CODE - EXACTLY AS ORIGINAL
            # Collect champion data for players
            team_champion_data = {}
            
            # Process each scrim
            for scrim in scrims_data:
                participants = scrim.get("participants", [])
                
                # Find team ID by looking for our players
                team_id = None
                for participant in participants:
                    riot_name = participant.get("RIOT_ID_GAME_NAME", "")
                    # Extract player name without prefix
                    clean_player_name = riot_name
                    for prefix in ["VLT ", "CLA "]:
                        if riot_name.startswith(prefix):
                            clean_player_name = riot_name[len(prefix):]
                            break
                    
                    if clean_player_name in players:
                        team_id = participant.get("TEAM")
                        break
                
                # Process each participant
                for participant in participants:
                    riot_name = participant.get("RIOT_ID_GAME_NAME", "")
                    champion = participant.get("SKIN", "")
                    win_status = participant.get("WIN", "")
                    participant_team_id = participant.get("TEAM")
                    
                    # Extract player name without prefix
                    clean_player_name = riot_name
                    for prefix in ["VLT ", "CLA "]:
                        if riot_name.startswith(prefix):
                            clean_player_name = riot_name[len(prefix):]
                            break
                    
                    # Check if this is one of our players
                    if clean_player_name in players and participant_team_id == team_id:
                        role = players[clean_player_name]
                        
                        # Initialize role data if needed
                        if role not in team_champion_data:
                            team_champion_data[role] = {}
                        if champion not in team_champion_data[role]:
                            team_champion_data[role][champion] = {"wins": 0, "games": 0}
                        
                        # Count the game
                        team_champion_data[role][champion]["games"] += 1
                        if win_status == "Win":
                            team_champion_data[role][champion]["wins"] += 1
            
            # Display results - EXACTLY AS ORIGINAL
            st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <h2 style="background: linear-gradient(135deg, #3b82f6, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;">
                    Champion Performance by Role
                </h2>
                <p style="color: #94a3b8; font-size: 1.1rem;">Analyzing champion win rates for each team member in scrims</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Create 5 columns layout for roles - EXACTLY AS ORIGINAL
            roles = ["Top", "Jungle", "Mid", "ADC", "Support"]
            cols = st.columns(5)
            
            for i, role in enumerate(roles):
                with cols[i]:
                    player_name = [k for k, v in players.items() if v == role][0]
                    role_color = role_colors.get(role, "#3b82f6")
                    
                    # Role header
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, {role_color}20, {role_color}10); 
                                border: 2px solid {role_color}; 
                                border-radius: 16px; 
                                padding: 1rem; 
                                margin-bottom: 1rem;
                                text-align: center;
                                backdrop-filter: blur(10px);
                                display: flex;
                                flex-direction: column;
                                align-items: center;
                                justify-content: center;">
                        <h3 style="color: {role_color}; margin: 0; font-size: 1.4rem; font-weight: 700; text-align: center; width: 100%;">
                            {role}
                        </h3>
                        <p style="color: #94a3b8; margin: 0.25rem 0 0 0; font-size: 0.9rem; text-align: center; width: 100%;">
                            {player_name}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Champions for this role - Enhanced with full display option
                    if role in team_champion_data and team_champion_data[role]:
                        # Prepare data for this role
                        role_data = []
                        for champion, stats in team_champion_data[role].items():
                            if stats["games"] > 0:
                                win_rate = (stats["wins"] / stats["games"]) * 100
                                role_data.append({
                                    "champion": champion,
                                    "games": stats["games"],
                                    "wins": stats["wins"],
                                    "losses": stats["games"] - stats["wins"],
                                    "win_rate": win_rate
                                })
                        
                        # Sort by games played, then by win rate
                        role_data.sort(key=lambda x: (x["games"], x["win_rate"]), reverse=True)
                        
                        # Initialize session state for this role's expansion
                        expand_key = f"expand_{role.lower()}_champions"
                        if expand_key not in st.session_state:
                            st.session_state[expand_key] = False
                        
                        # Determine how many champions to show
                        show_all = st.session_state[expand_key]
                        champions_to_show = role_data if show_all else role_data[:5]
                        
                        # Display champions in compact cards
                        for j, champ_data in enumerate(champions_to_show):
                            champion_name = champ_data["champion"]
                            win_rate = champ_data["win_rate"]
                            games = champ_data["games"]
                            wins = champ_data["wins"]
                            
                            # Get champion image
                            champ_key = find_champion_key(champion_name, champion_data, champ_mapping)
                            
                            # Champion card with role color theme
                            st.markdown(f"""
                            <div style="background: rgba(51, 65, 85, 0.4); 
                                        border: 1px solid {role_color}50; 
                                        border-radius: 12px; 
                                        padding: 0.75rem; 
                                        margin-bottom: 0.75rem;
                                        text-align: center;
                                        transition: all 0.3s ease;">
                                <div style="margin-bottom: 0.5rem;">
                                    {'<img src="https://ddragon.leagueoflegends.com/cdn/' + ddragon_version + '/img/champion/' + champ_key + '.png" width="50" style="border-radius: 8px; border: 2px solid ' + role_color + ';">' if champ_key else '<div style="width: 50px; height: 50px; background: ' + role_color + '30; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin: 0 auto; border: 2px solid ' + role_color + ';"><span style="color: ' + role_color + ';">?</span></div>'}
                                </div>
                                <div style="font-weight: 600; color: {role_color}; font-size: 0.85rem; margin-bottom: 0.25rem;">
                                    {champion_name}
                                </div>
                                <div style="color: #f8fafc; font-size: 0.75rem; margin-bottom: 0.25rem;">
                                    <strong>{win_rate:.0f}%</strong> WR
                                </div>
                                <div style="color: #94a3b8; font-size: 0.7rem;">
                                    {wins}W-{games-wins}L ({games}g)
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Show expand/collapse button if there are more than 5 champions
                        if len(role_data) > 5:
                            remaining_count = len(role_data) - 5
                            button_text = "Show Less" if show_all else f"Show {remaining_count} More"
                            button_icon = "▲" if show_all else "▼"
                            
                            if st.button(f"{button_icon} {button_text}", key=f"toggle_{role.lower()}_champions", use_container_width=True):
                                st.session_state[expand_key] = not st.session_state[expand_key]
                                st.rerun()
                    else:
                        # No data for this role
                        st.markdown(f"""
                        <div style="background: rgba(51, 65, 85, 0.2); 
                                    border: 1px dashed {role_color}50; 
                                    border-radius: 12px; 
                                    padding: 1rem; 
                                    text-align: center;
                                    color: #94a3b8;">
                            <p style="margin: 0; font-size: 0.8rem;">No champions played</p>
                        </div>
                        """, unsafe_allow_html=True)
            
            # Summary statistics - EXACTLY AS ORIGINAL
            st.header("📊 Scrims Summary")
            
            # Calculate overall stats
            total_scrims = len(scrims_data)
            team_wins = 0
            team_games = 0
            
            for scrim in scrims_data:
                participants = scrim.get("participants", [])
                our_team_id = None
                
                # Find our team ID
                for participant in participants:
                    riot_name = participant.get("RIOT_ID_GAME_NAME", "")
                    clean_player_name = riot_name
                    for prefix in ["VLT ", "CLA "]:
                        if riot_name.startswith(prefix):
                            clean_player_name = riot_name[len(prefix):]
                            break
                    
                    if clean_player_name in players:
                        our_team_id = participant.get("TEAM")
                        break
                
                # Count team wins
                if our_team_id:
                    team_games += 1
                    for participant in participants:
                        riot_name = participant.get("RIOT_ID_GAME_NAME", "")
                        clean_player_name = riot_name
                        for prefix in ["VLT ", "CLA "]:
                            if riot_name.startswith(prefix):
                                clean_player_name = riot_name[len(prefix):]
                                break
                        
                        if (clean_player_name in players and 
                            participant.get("TEAM") == our_team_id and 
                            participant.get("WIN") == "Win"):
                            team_wins += 1
                            break
            
            team_win_rate = (team_wins / team_games * 100) if team_games > 0 else 0
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                styled_metric("Total Scrims", str(total_scrims))
            with col2:
                styled_metric("Team Record", f"{team_wins}W - {team_games - team_wins}L")
            with col3:
                styled_metric("Team Win Rate", f"{team_win_rate:.1f}%", delta_color="blue")
        
        with tab2:
            # ALL THE GAME BROWSER CODE - EXACTLY AS ORIGINAL
            st.markdown("""
            <div style="text-align: center; margin-bottom: 2rem;">
                <h2 style="background: linear-gradient(135deg, #3b82f6, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;">
                    Scrim Games Browser
                </h2>
                <p style="color: #94a3b8; font-size: 1.1rem;">Browse all scrim games with draft information and filtering</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Prepare game data for browsing - EXACTLY AS ORIGINAL
            scrim_games = []
            all_our_champions = set()
            all_enemy_champions = set()
            
            for scrim_index, scrim in enumerate(scrims_data):
                participants = scrim.get("participants", [])
                
                # Find our team ID
                our_team_id = None
                for participant in participants:
                    riot_name = participant.get("RIOT_ID_GAME_NAME", "")
                    clean_player_name = riot_name
                    for prefix in ["VLT ", "CLA "]:
                        if riot_name.startswith(prefix):
                            clean_player_name = riot_name[len(prefix):]
                            break
                    
                    if clean_player_name in players:
                        our_team_id = participant.get("TEAM")
                        break
                
                if our_team_id is None:
                    continue
                
                # Separate teams
                our_team = []
                enemy_team = []
                game_result = None
                
                for participant in participants:
                    riot_name = participant.get("RIOT_ID_GAME_NAME", "")
                    champion = participant.get("SKIN", "Unknown")
                    win_status = participant.get("WIN", "")
                    team_id = participant.get("TEAM")
                    
                    clean_player_name = riot_name
                    for prefix in ["VLT ", "CLA "]:
                        if riot_name.startswith(prefix):
                            clean_player_name = riot_name[len(prefix):]
                            break
                    
                    participant_data = {
                        "player": clean_player_name,
                        "champion": champion,
                        "full_name": riot_name
                    }
                    
                    if team_id == our_team_id:
                        our_team.append(participant_data)
                        all_our_champions.add(champion)
                        if win_status == "Win":
                            game_result = "WIN"
                        elif win_status == "Fail":
                            game_result = "LOSS"
                    else:
                        enemy_team.append(participant_data)
                        all_enemy_champions.add(champion)
                
                # Determine side (assuming team 100 is blue, 200 is red)
                our_side = "BLUE" if our_team_id == 100 else "RED"
                enemy_side = "RED" if our_team_id == 100 else "BLUE"
                
                if len(our_team) == 5 and len(enemy_team) == 5:
                    scrim_games.append({
                        "index": scrim_index,
                        "our_team": our_team,
                        "enemy_team": enemy_team,
                        "result": game_result,
                        "our_side": our_side,
                        "enemy_side": enemy_side
                    })
            
            if not scrim_games:
                st.warning("No valid scrim games found with complete team data.")
            else:
                # Filtering section - EXACTLY AS ORIGINAL
                st.subheader("🔍 Filter Games")
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    result_filter = st.radio("Result", ["All", "WIN", "LOSS"], key="scrim_result_filter")
                    
                with col2:
                    side_filter = st.radio("Our Side", ["All", "BLUE", "RED"], key="scrim_side_filter")
                
                with col3:
                    our_champions_list = ["All"] + sorted(list(all_our_champions))
                    our_champion_filter = st.selectbox("Our Champion", our_champions_list, key="scrim_our_champ")
                
                with col4:
                    enemy_champions_list = ["All"] + sorted(list(all_enemy_champions))
                    enemy_champion_filter = st.selectbox("Enemy Champion", enemy_champions_list, key="scrim_enemy_champ")
                
                # Apply filters - EXACTLY AS ORIGINAL
                filtered_games = scrim_games.copy()
                
                if result_filter != "All":
                    filtered_games = [g for g in filtered_games if g["result"] == result_filter]
                
                if side_filter != "All":
                    filtered_games = [g for g in filtered_games if g["our_side"] == side_filter]
                
                if our_champion_filter != "All":
                    filtered_games = [g for g in filtered_games if any(p["champion"] == our_champion_filter for p in g["our_team"])]
                
                if enemy_champion_filter != "All":
                    filtered_games = [g for g in filtered_games if any(p["champion"] == enemy_champion_filter for p in g["enemy_team"])]
                
                # Display filtered results - EXACTLY AS ORIGINAL
                st.subheader(f"📋 Games ({len(filtered_games)} games)")
                
                if not filtered_games:
                    st.warning("No games match the selected filters.")
                else:
                    # Display games - EXACTLY AS ORIGINAL
                    for game in filtered_games:
                        result_color = "#10b981" if game["result"] == "WIN" else "#ef4444"
                        
                        with st.container():
                            # Game header
                            st.markdown(f"""
                            <div style="background: linear-gradient(135deg, {result_color}20, {result_color}10); 
                                        border-left: 4px solid {result_color}; 
                                        border-radius: 12px; 
                                        padding: 1rem; 
                                        margin: 1rem 0;
                                        backdrop-filter: blur(10px);">
                                <h4 style="color: {result_color}; margin: 0; display: flex; align-items: center; gap: 1rem;">
                                    <span>{game["result"]}</span>
                                    <span style="color: #94a3b8; font-size: 1rem; font-weight: 400;">
                                        • Our Side: {game["our_side"]} • Game #{game["index"] + 1}
                                    </span>
                                </h4>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Team drafts - EXACTLY AS ORIGINAL
                            col1, col_sep, col2 = st.columns([5, 1, 5])
                            
                            with col1:
                                st.markdown(f"""
                                <h5 style="color: #3b82f6; margin-bottom: 1rem; text-align: center;">
                                    Caldya ({game["our_side"]} Side)
                                </h5>
                                """, unsafe_allow_html=True)
                                
                                # Our team champions
                                for player_data in game["our_team"]:
                                    champion = player_data["champion"]
                                    player = player_data["player"]
                                    champ_key = find_champion_key(champion, champion_data, champ_mapping)
                                    
                                    # Get role for player
                                    role = players.get(player, "Unknown")
                                    role_color = role_colors.get(role, "#94a3b8")
                                    
                                    st.markdown(f"""
                                    <div style="display: flex; align-items: center; gap: 1rem; 
                                                background: rgba(51, 65, 85, 0.3); 
                                                border-radius: 8px; 
                                                padding: 0.75rem; 
                                                margin-bottom: 0.5rem;
                                                border-left: 3px solid {role_color};">
                                        {'<img src="https://ddragon.leagueoflegends.com/cdn/' + ddragon_version + '/img/champion/' + champ_key + '.png" width="40" style="border-radius: 6px;">' if champ_key else '<div style="width: 40px; height: 40px; background: #475569; border-radius: 6px; display: flex; align-items: center; justify-content: center;"><span style="color: white;">?</span></div>'}
                                        <div>
                                            <div style="font-weight: 600; color: #f8fafc;">{champion}</div>
                                            <div style="color: {role_color}; font-size: 0.8rem;">{player} ({role})</div>
                                        </div>
                                    </div>
                                    """, unsafe_allow_html=True)
                            
                            with col_sep:
                                st.markdown(f"""
                                <div style="text-align: center; margin-top: 3rem;">
                                    <div style="font-size: 2rem; color: {result_color};">
                                        {"⚔️" if game["result"] == "WIN" else "💀"}
                                    </div>
                                    <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 0.5rem;">
                                        VS
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                            
                            with col2:
                                st.markdown(f"""
                                <h5 style="color: #ef4444; margin-bottom: 1rem; text-align: center;">
                                    Enemy ({game["enemy_side"]} Side)
                                </h5>
                                """, unsafe_allow_html=True)
                                
                                # Enemy team champions
                                for player_data in game["enemy_team"]:
                                    champion = player_data["champion"]
                                    player = player_data["player"]
                                    champ_key = find_champion_key(champion, champion_data, champ_mapping)
                                    
                                    st.markdown(f"""
                                    <div style="display: flex; align-items: center; gap: 1rem; 
                                                background: rgba(51, 65, 85, 0.3); 
                                                border-radius: 8px; 
                                                padding: 0.75rem; 
                                                margin-bottom: 0.5rem;
                                                border-left: 3px solid #ef4444;">
                                        {'<img src="https://ddragon.leagueoflegends.com/cdn/' + ddragon_version + '/img/champion/' + champ_key + '.png" width="40" style="border-radius: 6px;">' if champ_key else '<div style="width: 40px; height: 40px; background: #475569; border-radius: 6px; display: flex; align-items: center; justify-content: center;"><span style="color: white;">?</span></div>'}
                                        <div>
                                            <div style="font-weight: 600; color: #f8fafc;">{champion}</div>
                                            <div style="color: #ef4444; font-size: 0.8rem;">{player}</div>
                                        </div>
                                    </div>
                                    """, unsafe_allow_html=True)

# Logout button at the end of the application - EXACTLY AS ORIGINAL
st.markdown("---")
st.markdown('<div style="text-align: center; padding: 2rem 0;">', unsafe_allow_html=True)
if st.button("🔓 Logout", key="logout_button"):
    st.session_state.authenticated = False
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)