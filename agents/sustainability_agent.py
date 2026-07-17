# agents/sustainability_agent.py

from AI.intelligent_engine import (
    calculate_carbon_footprint,
    calculate_green_energy_score,
    calculate_solar_suitability,
    calculate_home_sustainability_index
)


def sustainability_analysis(information, energy, faults):

    # ------------------------------------------------------
    # Required Data
    # ------------------------------------------------------

    bill_amount = information.get("Electricity Bill", 0)
    monthly_usage = energy.get("Monthly Energy Usage (kWh)", 0)
    eco_score = energy.get("Eco Score", 0)
    power_score = faults.get("Power Stability Score", 0)

    # ------------------------------------------------------
    # Sustainability Calculations
    # ------------------------------------------------------

    carbon_footprint = calculate_carbon_footprint(
        monthly_usage
    )

    green_energy_score = calculate_green_energy_score(
        eco_score
    )

    solar_suitability_score = calculate_solar_suitability(
        bill_amount
    )

    home_sustainability_index = (
        calculate_home_sustainability_index(
            eco_score,
            green_energy_score,
            solar_suitability_score,
            power_score
        )
    )

    # ------------------------------------------------------
    # Sustainability Level
    # ------------------------------------------------------

    if home_sustainability_index >= 90:
        sustainability_level = "EXCELLENT"

    elif home_sustainability_index >= 75:
        sustainability_level = "GOOD"

    elif home_sustainability_index >= 60:
        sustainability_level = "AVERAGE"

    else:
        sustainability_level = "POOR"

    # ------------------------------------------------------
    # LED Recommendation
    # ------------------------------------------------------

    if green_energy_score < 85:
        led_recommendation = "YES"
    else:
        led_recommendation = "OPTIONAL"

    # ------------------------------------------------------
    # Annual Carbon Reduction Estimate
    # ------------------------------------------------------

    annual_carbon_reduction = round(
        carbon_footprint * 0.20 * 12,
        2
    )

    # ------------------------------------------------------
    # SDG Mapping
    # ------------------------------------------------------

    sdgs_covered = [

        "SDG 7 - Affordable and Clean Energy",

        "SDG 9 - Industry, Innovation and Infrastructure",

        "SDG 11 - Sustainable Cities and Communities",

        "SDG 12 - Responsible Consumption and Production",

        "SDG 13 - Climate Action"

    ]

    # ------------------------------------------------------
    # Final Sustainability Report
    # ------------------------------------------------------

    sustainability_report = {

        "Carbon Footprint (kg CO2/month)": carbon_footprint,

        "Green Energy Score": green_energy_score,

        "Solar Suitability Score": solar_suitability_score,

        "LED Recommendation": led_recommendation,

        "Annual Carbon Reduction Estimate (kg)": (
            annual_carbon_reduction
        ),

        "Sustainability Level": sustainability_level,

        "Home Sustainability Index": (
            home_sustainability_index
        ),

        "SDGs Covered": sdgs_covered

    }

    return sustainability_report