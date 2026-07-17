# AI/local_ai_consultant.py


def local_ai_consultant(
        information,
        energy,
        faults,
        sustainability,
        recommendation
):

    # ---------------------------------------------------------
    # FETCH REQUIRED VALUES
    # ---------------------------------------------------------

    eco_score = energy.get("Eco Score", 0)

    power_score = faults.get(
        "Power Stability Score",
        0
    )

    solar_score = sustainability.get(
        "Solar Suitability Score",
        0
    )

    sustainability_index = sustainability.get(
        "Home Sustainability Index",
        0
    )

    monthly_savings = recommendation.get(
        "Estimated Monthly Savings (₹)",
        0
    )

    # ---------------------------------------------------------
    # AI VERDICT
    # ---------------------------------------------------------

    if sustainability_index >= 90:

        ai_verdict = (
            "Excellent! Your household demonstrates "
            "outstanding sustainability and energy "
            "efficiency practices."
        )

    elif sustainability_index >= 75:

        ai_verdict = (
            "Your household is performing well in "
            "energy management. A few improvements "
            "can further increase sustainability."
        )

    elif sustainability_index >= 60:

        ai_verdict = (
            "Your household has moderate sustainability "
            "performance. Energy optimization is "
            "recommended."
        )

    else:

        ai_verdict = (
            "Your household has significant potential "
            "for improving energy efficiency and "
            "sustainability."
        )

    # ---------------------------------------------------------
    # PERSONALIZED ENERGY SUMMARY
    # ---------------------------------------------------------

    energy_summary = (

        f"Eco Score : {eco_score}/100\n"
        f"Home Sustainability Index : {sustainability_index}/100\n"
        f"Power Stability Score : {power_score}/100\n"
        f"Estimated Monthly Savings : ₹{monthly_savings}"

    )

    # ---------------------------------------------------------
    # TOP RECOMMENDATIONS
    # ---------------------------------------------------------

    top_recommendations = []

    if solar_score >= 80:
        top_recommendations.append(
            "Install rooftop solar panels for long-term savings."
        )

    if eco_score < 80:
        top_recommendations.append(
            "Reduce unnecessary electricity consumption."
        )

    if power_score < 80:
        top_recommendations.append(
            "Install a voltage stabilizer for sensitive appliances."
        )

    top_recommendations.append(
        "Regularly monitor your monthly electricity usage."
    )

    top_recommendations.append(
        "Adopt sustainable energy-saving practices."
    )

    # ---------------------------------------------------------
    # SUSTAINABILITY SUGGESTIONS
    # ---------------------------------------------------------

    sustainability_suggestions = [

        "Use energy-efficient appliances whenever possible.",

        "Switch to LED lighting for better efficiency.",

        "Reduce your household carbon footprint by adopting green energy practices.",

        "Utilize renewable energy solutions wherever feasible."

    ]

    # ---------------------------------------------------------
    # ENERGY OPTIMIZATION TIPS
    # ---------------------------------------------------------

    energy_tips = [

        "Turn off appliances when not in use.",

        "Avoid peak electricity consumption periods.",

        "Perform regular maintenance of electrical appliances.",

        "Use smart plugs and timers for better energy management."

    ]

    # ---------------------------------------------------------
    # FUTURE IMPROVEMENTS
    # ---------------------------------------------------------

    future_improvements = [

        "Install rooftop solar panels.",

        "Implement smart energy monitoring systems.",

        "Upgrade to BLDC fans for lower power consumption.",

        "Consider smart home energy automation.",

        "Adopt renewable and sustainable energy technologies."

    ]

    # ---------------------------------------------------------
    # RETURN FINAL REPORT
    # ---------------------------------------------------------

    return {

        "AI Mode": "OFFLINE INTELLIGENT ENGINE",

        "AI Verdict": ai_verdict,

        "Personalized Energy Summary":
            energy_summary,

        "Top Recommendations":
            top_recommendations,

        "Sustainability Suggestions":
            sustainability_suggestions,

        "Energy Optimization Tips":
            energy_tips,

        "Future Improvements":
            future_improvements

    }