import re

# ==========================================================
# APPLIANCE DATABASE (Estimated Monthly Consumption in kWh)
# ==========================================================

APPLIANCE_DB = {
    "Inverter AC": 120,
    "AC": 150,
    "Refrigerator": 40,
    "Washing Machine": 25,
    "Microwave Oven": 20,
    "Water Heater": 90,
    "Laptop": 25,
    "Television": 30,
    "LED Light": 5,
    "Fan": 20,
    "Desktop Computer": 40,
    "Air Cooler": 60,
    "Water Pump": 50,
}

# ==========================================================
# BILL AMOUNT EXTRACTION
# ==========================================================

def extract_bill_amount(user_input):

    numbers = re.findall(r"\d+", user_input)

    for number in numbers:
        value = int(number)

        # Electricity bill is usually greater than 500
        if value >= 500:
            return value

    return 0


# ==========================================================
# APPLIANCE NORMALIZATION
# ==========================================================

def normalize_appliances(user_input):

    text = user_input.lower()

    appliances = {}

    appliance_keywords = {

        "Inverter AC": ["inverter ac"],
        "AC": [" ac", "air conditioner"],
        "Refrigerator": ["refrigerator", "fridge"],
        "Washing Machine": ["washing machine"],
        "Microwave Oven": ["microwave"],
        "Water Heater": ["water heater", "geyser"],
        "Laptop": ["laptop"],
        "Television": ["tv", "television"],
        "LED Light": ["led", "light"],
        "Fan": ["fan"],
        "Desktop Computer": ["desktop"],
        "Air Cooler": ["cooler"],
        "Water Pump": ["water pump"]
    }

    for appliance, keywords in appliance_keywords.items():

        quantity = 0

        for keyword in keywords:

            pattern = r"(\d+)\s*" + re.escape(keyword.strip())

            match = re.search(pattern, text)

            if match:
                quantity = int(match.group(1))
                break

            elif keyword in text:
                quantity = 1

        if quantity > 0:
            appliances[appliance] = quantity

    return appliances


# ==========================================================
# MONTHLY ENERGY USAGE
# ==========================================================

def estimate_monthly_energy_usage(appliances):

    total_usage = 0

    for appliance, quantity in appliances.items():

        if appliance in APPLIANCE_DB:

            total_usage += APPLIANCE_DB[appliance] * quantity

    return total_usage


# ==========================================================
# ECO SCORE (OUT OF 100)
# ==========================================================

def calculate_eco_score(bill_amount, monthly_usage):

    score = 100

    if bill_amount > 10000:
        score -= 25

    elif bill_amount > 7000:
        score -= 15

    elif bill_amount > 4000:
        score -= 8

    if monthly_usage > 700:
        score -= 25

    elif monthly_usage > 500:
        score -= 15

    elif monthly_usage > 300:
        score -= 8

    return max(score, 0)


# ==========================================================
# POWER STABILITY SCORE
# ==========================================================

def calculate_power_stability_score(user_input):

    text = user_input.lower()

    keywords = [
        "voltage",
        "voltage fluctuation",
        "power fluctuation",
        "low voltage",
        "power cuts"
    ]

    for keyword in keywords:

        if keyword in text:
            return 70

    return 95


# ==========================================================
# CARBON FOOTPRINT
# ==========================================================

def calculate_carbon_footprint(monthly_usage):

    carbon_factor = 0.82

    return round(monthly_usage * carbon_factor, 2)


# ==========================================================
# GREEN ENERGY SCORE
# ==========================================================

def calculate_green_energy_score(eco_score):

    if eco_score >= 90:
        return 95

    elif eco_score >= 80:
        return 85

    elif eco_score >= 70:
        return 75

    return 60


# ==========================================================
# SOLAR SUITABILITY SCORE
# ==========================================================

def calculate_solar_suitability(bill_amount):

    if bill_amount >= 10000:
        return 95

    elif bill_amount >= 7000:
        return 90

    elif bill_amount >= 5000:
        return 80

    return 60


# ==========================================================
# ESTIMATED SAVINGS
# ==========================================================

def calculate_estimated_savings(bill_amount):

    monthly_savings = round(bill_amount * 0.20)

    annual_savings = monthly_savings * 12

    return {

        "monthly_savings": monthly_savings,
        "annual_savings": annual_savings
    }


# ==========================================================
# SOLAR ROI
# ==========================================================

def calculate_solar_roi(annual_savings):

    solar_installation_cost = 100000

    if annual_savings == 0:
        return "N/A"

    roi = round(solar_installation_cost / annual_savings, 1)

    return f"{roi} Years"


# ==========================================================
# HOME SUSTAINABILITY INDEX
# ==========================================================

def calculate_home_sustainability_index(
        eco_score,
        green_score,
        solar_score,
        power_score):

    hsi = round(
        (eco_score +
         green_score +
         solar_score +
         power_score) / 4
    )

    return hsi