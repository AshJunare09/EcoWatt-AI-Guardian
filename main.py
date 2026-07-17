# Load environment variables FIRST before initializing any AI modules
from dotenv import load_dotenv
load_dotenv()

from agents.information_agent import extract_information
from agents.energy_agent import analyze_energy
from agents.fault_agent import detect_faults
from agents.sustainability_agent import sustainability_analysis
from agents.recommendation_agent import generate_recommendations

# Import dynamic plotting utilities
from utils.graphs import *

# Import PDF generator
from reports.pdf_report import generate_pdf_report

# Import the core AI Consultant Router
from AI.ai_engine import generate_ai_response

import streamlit as st
import pandas as pd
import time
import json
import ast
import re


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="EcoWatt AI Guardian",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR HIGH-TECH METRIC CARDS ---
st.markdown("""
<style>
div[data-testid="stMetric"] {
    background-color: rgba(28, 30, 33, 0.5);
    border: 1px solid rgba(0, 255, 0, 0.2);
    border-left: 5px solid #00ff41;
    padding: 15px 20px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
    transition: transform 0.2s ease;
}
div[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    border-left: 5px solid #00c800;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.title("⚡ EcoWatt AI Guardian")
    st.markdown("### AI Multi-Agent System")
    st.markdown("""
    **Agents Deployed:**
    - 🔍 Information Agent
    - 📊 Energy Agent
    - 🔌 Fault Detection Agent
    - 🌱 Sustainability Agent
    - 💡 Recommendation Agent
    """)
    
    st.markdown("---")
    st.markdown("### SDGs Supported")
    st.markdown("""
    - **SDG 7** : Affordable & Clean Energy
    - **SDG 9** : Industry Innovation
    - **SDG 11** : Sustainable Cities
    - **SDG 12** : Responsible Consumption
    - **SDG 13** : Climate Action
    """)
    st.success("IBM SkillsBuild Academic Internship 2026")


# ---------------------------------------------------------
# HEADER / TITLE
# ---------------------------------------------------------
st.title("⚡ EcoWatt AI Guardian")
st.subheader("AI Multi-Agent Sustainable Energy Management System")
st.info("EcoWatt AI Guardian intelligently analyzes your energy usage, detects electrical faults, evaluates sustainability, and provides AI-generated recommendations to reduce electricity consumption and improve environmental sustainability.", icon="ℹ️")


# ---------------------------------------------------------
# USER INPUT CONTAINER
# ---------------------------------------------------------
with st.container():
    st.markdown("### 📝 Enter Energy Usage Information")
    user_input = st.text_area(
        "Describe your electricity usage below:",
        height=200,
        placeholder="My monthly electricity bill is ₹4500.\nI use:\n- 2 ACs\n- Refrigerator\n- Washing Machine\n- 4 Fans\nVoltage fluctuations are common.\nSuggest how I can save electricity."
    )


# ---------------------------------------------------------
# BUTTON / PIPELINE EXECUTION
# ---------------------------------------------------------
if st.button("🚀 Analyze with AI Agents", use_container_width=True):

    if user_input.strip() == "":
        st.error("Please enter your electricity usage information to begin the analysis.", icon="🚨")
    else:
        # Loading State
        with st.status("Initializing AI Multi-Agent Pipeline...", expanded=True) as status:
            st.write("🔍 Extracting Information...")
            information = extract_information(user_input)
            time.sleep(0.3)
            
            st.write("📊 Analyzing Energy Consumption...")
            energy = analyze_energy(information)
            time.sleep(0.3)
            
            st.write("🔌 Scanning for Electrical Faults...")
            faults = detect_faults(information, energy)
            time.sleep(0.3)
            
            st.write("🌱 Evaluating Sustainability Metrics...")
            sustainability = sustainability_analysis(information, energy, faults)
            time.sleep(0.3)
            
            st.write("💡 Generating Recommendations...")
            recommendation = generate_recommendations(information, energy, faults, sustainability)
            time.sleep(0.1)
            
            st.write("🧠 Consulting Core AI Engine...")
            ai_response_raw = generate_ai_response(
                information=information,
                energy=energy,
                faults=faults,
                sustainability=sustainability,
                recommendation=recommendation
            )
            status.update(label="AI Analysis Completed Successfully!", state="complete", expanded=False)

        # ---------------------------------------------------------
        # INDESTRUCTIBLE AI PARSER (Failsafe for Strings AND Dicts)
        # ---------------------------------------------------------
        ai_consultant_data = {
            "AI Mode": "GOOGLE GEMINI AI",
            "AI Verdict": "Analysis successful. Please review the specific recommendations below.",
            "Personalized Energy Summary": energy.get("Energy Efficiency", "N/A"),
            "Top Recommendations": recommendation.get("Recommendations", []),
            "Sustainability Suggestions": [],
            "Energy Optimization Tips": [],
            "Future Improvements": recommendation.get("Future Improvements", [])
        }

        # THE FIX: If the engine returned a dictionary directly, just use it!
        if isinstance(ai_response_raw, dict):
            ai_consultant_data.update(ai_response_raw)
        else:
            # It's a string, so we parse it safely.
            raw_str = str(ai_response_raw)
            try:
                clean_raw = raw_str.replace("```json", "").replace("```", "").strip()
                clean_raw = re.sub(r'(\{|,)\s*[\'"]?\d+[\'"]?\s*:\s*', r'\1 ', clean_raw)
                clean_raw = re.sub(r'\[\s*[\'"]?\d+[\'"]?\s*:\s*', r'[ ', clean_raw)
                
                parsed = json.loads(clean_raw)
                ai_consultant_data.update(parsed)
                
            except Exception:
                try:
                    parsed = ast.literal_eval(clean_raw)
                    if isinstance(parsed, dict):
                        ai_consultant_data.update(parsed)
                except Exception:
                    # Regex Rescue for shattered JSON strings
                    def extract_array(key, text):
                        match = re.search(rf'[\'"]{key}[\'"]\s*:\s*\[(.*?)\]', text, re.IGNORECASE | re.DOTALL)
                        if match:
                            inner = match.group(1)
                            items = re.findall(r'"([^"]+)"', inner)
                            if not items:
                                items = re.findall(r"'([^']+)'", inner)
                            return items
                        return []

                    v_match = re.search(r'[\'"]AI Verdict[\'"]\s*:\s*[\'"]([^\'"]+)[\'"]', raw_str, re.IGNORECASE)
                    if v_match:
                        ai_consultant_data["AI Verdict"] = v_match.group(1)

                    recs = extract_array("Top Recommendations", raw_str)
                    if recs: ai_consultant_data["Top Recommendations"] = recs
                    
                    sugs = extract_array("Sustainability Suggestions", raw_str)
                    if sugs: ai_consultant_data["Sustainability Suggestions"] = sugs
                    
                    tips = extract_array("Energy Optimization Tips", raw_str)
                    if tips: ai_consultant_data["Energy Optimization Tips"] = tips
                    
                    imps = extract_array("Future Improvements", raw_str)
                    if imps: ai_consultant_data["Future Improvements"] = imps
                    
                    ai_consultant_data["AI Mode"] = "GOOGLE GEMINI AI (Regex Rescue)"


# ---------------------------------------------------------
# DASHBOARD TABS
# ---------------------------------------------------------
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Overview & Energy", 
            "🔌 Faults & Grid", 
            "🌱 Sustainability", 
            "🧠 AI Consultant & Reports"
        ])

        # --- TAB 1: OVERVIEW & ENERGY ---
        with tab1:
            st.markdown("### Energy Analysis")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Monthly Usage (kWh)", energy.get("Monthly Energy Usage (kWh)", "N/A"))
            with col2:
                st.metric("Eco Score", energy.get("Eco Score", "N/A"))
            with col3:
                st.metric("Consumption Level", energy.get("Consumption Level", "N/A"))

            st.success(energy.get("Energy Efficiency", "N/A"), icon="✅")
            
            st.markdown("### Sustainability & Eco Metrics")
            gauge_col1, gauge_col2 = st.columns(2)
            with gauge_col1:
                st.plotly_chart(create_eco_score_gauge(energy.get("Eco Score", 0)), use_container_width=True)
            with gauge_col2:
                st.plotly_chart(create_hsi_gauge(sustainability.get("Home Sustainability Index", 0)), use_container_width=True)

            with st.expander("View Raw Extracted Appliance Data"):
                st.write(f"**Electricity Bill:** {information.get('Electricity Bill','N/A')}")
                st.write("**Appliances Detected:**")
                for appliance, quantity in information.get("Appliances", {}).items():
                    st.write(f"- {appliance} : {quantity}")
                st.write(f"**Voltage Issue:** {information.get('Voltage Issue','N/A')}")


        # --- TAB 2: FAULTS & GRID ---
        with tab2:
            st.markdown("### Fault Detection & Stability")
            col4, col5, col6 = st.columns(3)
            with col4:
                st.metric("Risk Level", faults.get("Risk Level", "N/A"))
            with col5:
                st.metric("Electrical Health", faults.get("Electrical Health", "N/A"))
            with col6:
                st.metric("Power Stability Score", faults.get("Power Stability Score", "N/A"))

            st.warning(faults.get("Possible Appliance Risk", "No Risk Detected."), icon="⚠️")

            st.markdown("### Power & Grid Performance Indicators")
            fault_col1, fault_col2 = st.columns(2)
            with fault_col1:
                st.plotly_chart(create_power_stability_gauge(faults.get("Power Stability Score", 0)), use_container_width=True)
            with fault_col2:
                st.plotly_chart(create_green_energy_gauge(sustainability.get("Green Energy Score", 0)), use_container_width=True)


        # --- TAB 3: SUSTAINABILITY & SAVINGS ---
        with tab3:
            st.markdown("### Sustainability Analysis")
            col7, col8, col9 = st.columns(3)
            with col7:
                st.metric("Carbon Footprint", f"{sustainability.get('Carbon Footprint (kg CO2/month)', 'N/A')} kg")
            with col8:
                st.metric("Green Energy Score", sustainability.get("Green Energy Score", "N/A"))
            with col9:
                st.metric("Solar Suitability", sustainability.get("Solar Suitability Score", "N/A"))

            sus_text1, sus_text2 = st.columns(2)
            with sus_text1:
                st.success(f"**Sustainability Level:** {sustainability.get('Sustainability Level', 'N/A')}", icon="🌍")
                st.info(f"**LED Recommendation:** {sustainability.get('LED Recommendation','N/A')}", icon="💡")
            with sus_text2:
                st.info(f"**Home Sustainability Index:** {sustainability.get('Home Sustainability Index','N/A')}", icon="📊")
                st.success(f"**Annual Carbon Reduction:** {sustainability.get('Annual Carbon Reduction Estimate (kg)','N/A')} kg", icon="📉")

            st.markdown("### Green Transition & Savings Potential")
            solar_col1, solar_col2 = st.columns(2)
            with solar_col1:
                st.plotly_chart(create_solar_suitability_gauge(sustainability.get("Solar Suitability Score", 0)), use_container_width=True)
            with solar_col2:
                st.plotly_chart(create_savings_chart(
                    recommendation.get("Estimated Monthly Savings (₹)", 0),
                    recommendation.get("Estimated Annual Savings (₹)", 0)
                ), use_container_width=True)
            
            st.markdown("### Energy Consumption & Carbon Overview")
            chart_col1, chart_col2 = st.columns(2)
            with chart_col1:
                st.plotly_chart(create_monthly_usage_chart(energy.get("Monthly Energy Usage (kWh)", 0)), use_container_width=True)
            with chart_col2:
                st.plotly_chart(create_carbon_footprint_chart(sustainability.get("Carbon Footprint (kg CO2/month)", 0)), use_container_width=True)


        # --- TAB 4: AI CONSULTANT & REPORTS ---
        with tab4:
            st.markdown("## 🧠 AI Sustainability Consultant Insights")
            
            active_mode = ai_consultant_data.get("AI Mode", "GOOGLE GEMINI AI")
            if "Regex Rescue" in active_mode:
                st.warning(f"🤖 **Active Core Engine**: {active_mode}")
            elif "OFFLINE" in active_mode:
                st.warning(f"🤖 **Active Core Engine**: {active_mode}")
            else:
                st.success(f"✨ **Active Core Engine**: {active_mode}")

            # 1. AI Verdict
            st.markdown("### 📋 AI Executive Verdict")
            verdict_text = ai_consultant_data.get("AI Verdict", "No core verdict generated.")
            st.info(verdict_text, icon="💡")

            # 2. Extract & Display Core Metrics (Hides if empty or just says 'GOOD')
            summary_text = str(ai_consultant_data.get("Personalized Energy Summary", ""))
            if summary_text and summary_text not in ["N/A", "GOOD", "POOR", "MODERATE", "None"]:
                st.markdown("### 📊 Metric Insights")
                st.write(summary_text.replace("\n", " | "))

            # 3. Recommendations & Suggestions Grid
            st.markdown("---")
            rec_col, sug_col = st.columns(2)

            with rec_col:
                st.markdown("### 🎯 Top Actionable Recommendations")
                top_recs = ai_consultant_data.get("Top Recommendations", recommendation.get("Recommendations", []))
                if isinstance(top_recs, list) and len(top_recs) > 0:
                    for item in top_recs:
                        st.write(f"🔹 **{item}**")
                else:
                    st.write("_No recommendations provided._")

            with sug_col:
                st.markdown("### 🌱 Sustainability Suggestions")
                sus_sugs = ai_consultant_data.get("Sustainability Suggestions", [])
                if isinstance(sus_sugs, list) and len(sus_sugs) > 0:
                    for item in sus_sugs:
                        st.write(f"🌿 {item}")
                else:
                    st.write("_No explicit sustainability suggestions listed._")

            # 4. Energy Optimization Tips & Improvements Grid
            st.markdown("---")
            tip_col, imp_col = st.columns(2)

            with tip_col:
                st.markdown("### ⚡ Energy Optimization Tips")
                opt_tips = ai_consultant_data.get("Energy Optimization Tips", [])
                if isinstance(opt_tips, list) and len(opt_tips) > 0:
                    for item in opt_tips:
                        st.write(f"✅ {item}")
                else:
                    st.write("_No specific optimization tips generated._")

            with imp_col:
                st.markdown("### 🚀 Future Improvements")
                future_imps = ai_consultant_data.get("Future Improvements", recommendation.get("Future Improvements", []))
                if isinstance(future_imps, list) and len(future_imps) > 0:
                    for item in future_imps:
                        st.write(f"📈 {item}")
                else:
                    st.write("_No future upgrades specified._")

            # 5. Financial Overview Row
            st.markdown("---")
            st.markdown("### 💰 Financial Projections")
            rec_col1, rec_col2, rec_col3 = st.columns(3)
            with rec_col1:
                st.metric("Est. Monthly Savings", f"₹{recommendation.get('Estimated Monthly Savings (₹)','0')}")
            with rec_col2:
                st.metric("Est. Annual Savings", f"₹{recommendation.get('Estimated Annual Savings (₹)','0')}")
            with rec_col3:
                st.metric("Solar ROI", f"{recommendation.get('Solar ROI','N/A')}")

            # 6. Document Generation & Downloads
            st.markdown("---")
            st.markdown("### 📥 Download Generated Reports")
            
            pdf_path = generate_pdf_report(
                user_input, information, energy, faults, 
                sustainability, recommendation, ai_consultant_data
            )

            pdf_col, txt_col = st.columns(2)
            with pdf_col:
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="📥 Download High-Res PDF Report",
                        data=pdf_file,
                        file_name="EcoWatt_AI_Report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

            with txt_col:
                report_txt = f"""
ECO WATT AI GUARDIAN REPORT
---------------------------
Electricity Bill: {information.get("Electricity Bill","N/A")}
Monthly Energy Usage: {energy.get("Monthly Energy Usage (kWh)","N/A")}
Eco Score: {energy.get("Eco Score","N/A")}
Consumption Level: {energy.get("Consumption Level","N/A")}
Risk Level: {faults.get("Risk Level","N/A")}
Carbon Footprint: {sustainability.get("Carbon Footprint (kg CO2/month)","N/A")}
Home Sustainability Index: {sustainability.get("Home Sustainability Index","N/A")}
Estimated Monthly Savings: ₹{recommendation.get("Estimated Monthly Savings (₹)","0")}
Estimated Annual Savings: ₹{recommendation.get("Estimated Annual Savings (₹)","0")}
Solar ROI: {recommendation.get("Solar ROI","N/A")}

AI Verdict: {verdict_text}

Recommendations:
{chr(10).join(f"- {r}" for r in (top_recs if isinstance(top_recs, list) else [])) if top_recs else "N/A"}
"""
                st.download_button(
                    label="📄 Download Plain Text Summary",
                    data=report_txt,
                    file_name="EcoWatt_Report.txt",
                    mime="text/plain",
                    use_container_width=True
                )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")
footer_col1, footer_col2 = st.columns(2)
with footer_col1:
    st.markdown("### Developed By")
    st.markdown("**Team Electro Archons**")
    st.markdown("Team Leader: Ashutosh Bhaskar Junare")
    st.markdown("Team Member: Nikhil Haridas Dhurve")
with footer_col2:
    st.markdown("### Program")
    st.markdown("IBM SkillsBuild Academic Internship 2026")
    st.markdown("AI Multi-Agent Sustainable Energy Management System")