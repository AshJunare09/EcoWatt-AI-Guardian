# agents/energy_agent.py

from AI.intelligent_engine import (
    estimate_monthly_energy_usage,
    calculate_eco_score
)


def analyze_energy(information):

    # Get extracted data from Information Agent
    bill_amount = information.get("Electricity Bill", 0)
    appliances = information.get("Appliances", {})

    # Safety check
    if bill_amount == "Not Mentioned":
        bill_amount = 0

    # Calculate Monthly Energy Usage
    monthly_usage = estimate_monthly_energy_usage(appliances)

    # Calculate Eco Score
    eco_score = calculate_eco_score(
        bill_amount,
        monthly_usage
    )

    # Consumption Level
    if monthly_usage < 200:
        consumption_level = "LOW"

    elif monthly_usage < 500:
        consumption_level = "MODERATE"

    else:
        consumption_level = "HIGH"

    # Energy Efficiency
    if eco_score >= 85:
        energy_efficiency = "EXCELLENT"

    elif eco_score >= 70:
        energy_efficiency = "GOOD"

    elif eco_score >= 50:
        energy_efficiency = "AVERAGE"

    else:
        energy_efficiency = "POOR"

    # Saving Potential
    if eco_score >= 85:
        saving_potential = "LOW"

    elif eco_score >= 70:
        saving_potential = "MEDIUM"

    else:
        saving_potential = "HIGH"

    # Final Energy Report
    energy_report = {

        "Monthly Energy Usage (kWh)": monthly_usage,
        "Consumption Level": consumption_level,
        "Eco Score": eco_score,
        "Energy Efficiency": energy_efficiency,
        "Energy Saving Potential": saving_potential

    }

    return energy_report