# agents/information_agent.py

from AI.intelligent_engine import (
    extract_bill_amount,
    normalize_appliances,
    estimate_monthly_energy_usage
)

def extract_information(user_input):
    
    # 1. Clean and sanitize input
    if not isinstance(user_input, str) or not user_input.strip():
        user_input = "No input provided."

    # 2. Extract Base Data
    bill_amount = extract_bill_amount(user_input)
    appliances = normalize_appliances(user_input)

    # ---------------------------------------------------------
    # 🧠 AI INFERENCE ENGINE (Handles Missing Data Scenarios)
    # ---------------------------------------------------------
    
    # Scenario A: User forgot appliances, but gave a high bill
    if not appliances and bill_amount > 1000:
        if bill_amount > 5000:
            appliances = {"AC": 2, "Refrigerator": 1, "Water Heater": 1, "Fan": 4}
        else:
            appliances = {"Refrigerator": 1, "Fan": 3, "Television": 1}
            
    # Scenario B: User forgot the bill, but listed appliances
    elif bill_amount == 0 and appliances:
        # Infer bill assuming an average rate of ₹8 per kWh
        estimated_kwh = estimate_monthly_energy_usage(appliances)
        bill_amount = int(estimated_kwh * 8)

    # ---------------------------------------------------------
    # ⚡ ROBUST FAULT DETECTION
    # ---------------------------------------------------------
    voltage_keywords = [
        "voltage", "fluctuation", "low voltage", "power fluctuation", 
        "power cut", "dim", "trip", "spark", "flicker", "surge"
    ]

    voltage_issue = "No"
    for keyword in voltage_keywords:
        if keyword in user_input.lower():
            voltage_issue = "Yes"
            break

    # Final Information Report
    information_report = {
        "Raw Input": user_input,
        "Electricity Bill": bill_amount,
        "Appliances": appliances if appliances else {"None Detected": 0},
        "Voltage Issue": voltage_issue
    }

    return information_report