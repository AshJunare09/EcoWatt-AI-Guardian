# utils/graphs.py

import plotly.graph_objects as go
import plotly.express as px


# ---------------------------------------------------------
# ECO SCORE GAUGE
# ---------------------------------------------------------

def create_eco_score_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Eco Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "green"}
        }
    ))

    return fig


# ---------------------------------------------------------
# HOME SUSTAINABILITY INDEX
# ---------------------------------------------------------

def create_hsi_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Home Sustainability Index"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "blue"}
        }
    ))

    return fig


# ---------------------------------------------------------
# POWER STABILITY SCORE
# ---------------------------------------------------------

def create_power_stability_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Power Stability Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "orange"}
        }
    ))

    return fig


# ---------------------------------------------------------
# GREEN ENERGY SCORE
# ---------------------------------------------------------

def create_green_energy_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Green Energy Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "green"}
        }
    ))

    return fig


# ---------------------------------------------------------
# SOLAR SUITABILITY SCORE
# ---------------------------------------------------------

def create_solar_suitability_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Solar Suitability Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "gold"}
        }
    ))

    return fig


# ---------------------------------------------------------
# MONTHLY ENERGY USAGE
# ---------------------------------------------------------

def create_monthly_usage_chart(units):

    fig = px.bar(

        x=["Monthly Usage"],
        y=[units],

        labels={

            "x": "",
            "y": "kWh"

        },

        title="Monthly Energy Usage"

    )

    return fig


# ---------------------------------------------------------
# CARBON FOOTPRINT
# ---------------------------------------------------------

def create_carbon_footprint_chart(carbon):

    fig = px.bar(

        x=["Carbon Footprint"],
        y=[carbon],

        labels={

            "x": "",
            "y": "kg CO2 / Month"

        },

        title="Carbon Footprint"

    )

    return fig


# ---------------------------------------------------------
# SAVINGS CHART
# ---------------------------------------------------------

def create_savings_chart(monthly, annual):

    fig = px.bar(

        x=["Monthly Savings", "Annual Savings"],

        y=[monthly, annual],

        labels={

            "x": "",
            "y": "Amount (₹)"

        },

        title="Estimated Savings"

    )

    return fig