# agents/recommendation_agent.py

from AI.intelligent_engine import (
    calculate_estimated_savings,
    calculate_solar_roi
)

def generate_recommendations(information, energy, faults, sustainability):
    recommendations = []
    future_improvements = []

    # ------------------------------------------------------
    # Financial Failsafes & Savings
    # ------------------------------------------------------
    bill_amount = information.get("Electricity Bill", 0)
    
    if bill_amount > 0:
        savings = calculate_estimated_savings(bill_amount)
        monthly_savings = savings.get("monthly_savings", 0)
        annual_savings = savings.get("annual_savings", 0)
        solar_roi = calculate_solar_roi(annual_savings)
    else:
        monthly_savings = 0
        annual_savings = 0
        solar_roi = "N/A (Insufficient Data)"

    # ------------------------------------------------------
    # Dynamic Contextual Recommendations
    # ------------------------------------------------------
    consumption_level = energy.get("Consumption Level", "UNKNOWN")
    efficiency = energy.get("Energy Efficiency", "UNKNOWN")
    voltage_fault = faults.get("Voltage Fault", "No")

    # Handle Anomaly: High bill but no heavy appliances detected
    if consumption_level == "HIGH" and "AC" not in information.get("Appliances", {}):
        recommendations.append("Investigate potential phantom loads or hidden electrical leaks causing high bills.")
    elif consumption_level == "HIGH":
        recommendations.append("Shift heavy appliance usage (ACs, Heaters) to off-peak hours.")

    if sustainability.get("Solar Suitability Score", 0) >= 75:
        recommendations.append("High solar viability detected. Installing rooftop solar is highly recommended.")
        future_improvements.append("Adopt full renewable energy grid integration.")

    if efficiency in ["AVERAGE", "POOR"]:
        recommendations.append("Phased replacement of aging appliances with 5-Star BEE-rated alternatives.")

    if voltage_fault == "Yes" or faults.get("Risk Level") == "HIGH":
        recommendations.append("URGENT: Install whole-house surge protection and appliance-level voltage stabilizers.")
        future_improvements.append("Conduct a comprehensive wiring health and ground-fault audit.")

    # Fallback if the home is already perfect
    if not recommendations:
        recommendations.append("Maintain current excellent energy habits.")

    # ------------------------------------------------------
    # AI Verdict Generation
    # ------------------------------------------------------
    hsi = sustainability.get("Home Sustainability Index", 0)

    if bill_amount == 0 and not information.get("Appliances"):
        verdict = "Insufficient data provided to generate a comprehensive verdict. Please provide detailed appliance or bill information."
    elif hsi >= 90:
        verdict = "Outstanding! Your household operates at peak sustainability and energy efficiency."
    elif hsi >= 75:
        verdict = "Your home is reasonably efficient. Addressing minor usage patterns can unlock further savings."
    elif hsi >= 60:
        verdict = "Moderate performance. Prioritize stabilizing electrical faults and upgrading aging appliances."
    else:
        verdict = "Critical energy inefficiency detected. Immediate hardware optimization and habit changes are advised."

    # Base Future Improvements
    base_improvements = [
        "Deploy IoT-based smart energy monitoring systems.",
        "Transition all ambient lighting to automated LED setups."
    ]
    future_improvements.extend(base_improvements)

    # ------------------------------------------------------
    # Final Recommendation Report
    # ------------------------------------------------------
    return {
        "Estimated Monthly Savings (₹)": monthly_savings,
        "Estimated Annual Savings (₹)": annual_savings,
        "Solar ROI": solar_roi,
        "Recommendations": list(set(recommendations)), # Remove duplicates
        "AI Verdict": verdict,
        "Future Improvements": list(set(future_improvements))
    }