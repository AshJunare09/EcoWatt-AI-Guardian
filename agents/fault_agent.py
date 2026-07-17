# agents/fault_agent.py

from AI.intelligent_engine import (
    calculate_power_stability_score
)


def detect_faults(information, energy):

    # Get values from Information Agent
    user_input = information.get("Raw Input", "")
    voltage_issue = information.get("Voltage Issue", "No")
    appliances = information.get("Appliances", {})
    monthly_usage = energy.get("Monthly Energy Usage (kWh)", 0)

    # Calculate Power Stability Score
    power_score = calculate_power_stability_score(user_input)

    # Risk Level
    if power_score >= 90 and monthly_usage < 500:
        risk_level = "LOW"

    elif power_score >= 70:
        risk_level = "MODERATE"

    else:
        risk_level = "HIGH"

    # Electrical Health
    if power_score >= 90:
        electrical_health = "EXCELLENT"

    elif power_score >= 70:
        electrical_health = "GOOD"

    elif power_score >= 50:
        electrical_health = "MODERATE"

    else:
        electrical_health = "POOR"

    # Possible Appliance Risk
    if voltage_issue == "Yes":
        appliance_risk = (
            "Voltage fluctuations may damage sensitive appliances "
            "such as ACs, TVs, Refrigerators, and Laptops."
        )
    else:
        appliance_risk = "No significant appliance risk detected."

    # Final Fault Report
    fault_report = {

        "Risk Level": risk_level,
        "Electrical Health": electrical_health,
        "Voltage Fault": voltage_issue,
        "Power Stability Score": power_score,
        "Possible Appliance Risk": appliance_risk

    }

    return fault_report