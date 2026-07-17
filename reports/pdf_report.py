# reports/pdf_report.py

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def generate_pdf_report(user_input, information, energy, faults, sustainability, recommendation, ai_consultant):
    """
    Generates a highly formatted, professional PDF report using ReportLab Platypus.
    """
    os.makedirs("reports", exist_ok=True)
    file_path = "reports/EcoWatt_AI_Report.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    story = []
    styles = getSampleStyleSheet()
    
    # =========================================================
    # CUSTOM STYLES
    # =========================================================
    title_style = ParagraphStyle(
        name="ReportTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=24,
        textColor=colors.HexColor("#004d00"), 
        alignment=TA_CENTER,
        spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        name="ReportSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=12,
        textColor=colors.HexColor("#555555"),
        alignment=TA_CENTER,
        spaceAfter=20
    )
    
    header_style = ParagraphStyle(
        name="SectionHeader",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        textColor=colors.HexColor("#1a252f"), 
        spaceBefore=20,
        spaceAfter=10,
    )
    
    body_style = styles["BodyText"]
    
    bullet_style = ParagraphStyle(
        name="BulletText",
        parent=styles["BodyText"],
        leftIndent=20,
        spaceAfter=6,
        bulletIndent=10
    )

    # Style specifically for table cells to force word wrapping
    cell_style = ParagraphStyle(
        name="TableCell",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=12
    )

    # Helper function to wrap text in a paragraph for tables
    def wrap_text(text):
        return Paragraph(str(text), cell_style)

    # =========================================================
    # 1. HEADER SECTION
    # =========================================================
    story.append(Paragraph("EcoWatt AI Guardian", title_style))
    story.append(Paragraph("AI Multi-Agent Sustainable Energy Management System", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#2ecc71"), spaceAfter=20))

    # =========================================================
    # 2. AI CONSULTANT VERDICT
    # =========================================================
    story.append(Paragraph("1. AI Executive Verdict", header_style))
    verdict = ai_consultant.get("AI Verdict", recommendation.get("AI Verdict", "No verdict generated."))
    story.append(Paragraph(verdict, body_style))
    
    ai_mode = ai_consultant.get("AI Mode", "N/A")
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"<b>Active Engine:</b> {ai_mode}", body_style))

    # =========================================================
    # 3. CORE METRICS TABLE (Energy, Faults, Sustainability)
    # =========================================================
    story.append(Paragraph("2. System Analysis & Metrics", header_style))
    
    # We use the wrap_text() helper on the 3rd column so long strings wrap properly
    metrics_data = [
        ["Metric Category", "Assessed Value", "Detail / Level"],
        ["Monthly Energy Usage", f"{energy.get('Monthly Energy Usage (kWh)', 'N/A')} kWh", wrap_text(energy.get('Consumption Level', 'N/A'))],
        ["Overall Eco Score", str(energy.get("Eco Score", "N/A")), wrap_text(energy.get("Energy Efficiency", "N/A"))],
        ["Power Stability Score", str(faults.get("Power Stability Score", "N/A")), wrap_text(faults.get("Electrical Health", "N/A"))],
        ["Fault Risk Level", str(faults.get("Risk Level", "N/A")), wrap_text(faults.get("Possible Appliance Risk", "N/A"))],
        ["Carbon Footprint", f"{sustainability.get('Carbon Footprint (kg CO2/month)', 'N/A')} kg CO2/mo", wrap_text(sustainability.get("Sustainability Level", "N/A"))],
        ["Home Sustainability Index", str(sustainability.get("Home Sustainability Index", "N/A")), wrap_text("Out of 100")]
    ]
    
    metrics_table = Table(metrics_data, colWidths=[150, 120, 250]) # Adjusted column widths slightly to give more room for text
    metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2c3e50")), 
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), 
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f8f9fa")), 
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('ALIGN', (0, 1), (0, -1), 'LEFT'), 
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE') # Vertically center the text for a cleaner look
    ]))
    story.append(metrics_table)

    # =========================================================
    # 4. FINANCIAL & SAVINGS PROJECTIONS TABLE
    # =========================================================
    story.append(Paragraph("3. Financial & Solar Projections", header_style))
    
    fin_data = [
        ["Estimated Monthly Savings", f"Rs {recommendation.get('Estimated Monthly Savings (₹)', '0')}"],
        ["Estimated Annual Savings", f"Rs {recommendation.get('Estimated Annual Savings (₹)', '0')}"],
        ["Solar Suitability Score", str(sustainability.get("Solar Suitability Score", "N/A"))],
        ["Solar Return on Investment", str(recommendation.get("Solar ROI", "N/A"))]
    ]
    
    fin_table = Table(fin_data, colWidths=[260, 260])
    fin_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#e8f8f5")), 
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#1abc9c")),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('PADDING', (0, 0), (-1, -1), 8)
    ]))
    story.append(fin_table)

    # =========================================================
    # 5. RECOMMENDATIONS & FUTURE IMPROVEMENTS
    # =========================================================
    story.append(Paragraph("4. AI Actionable Insights", header_style))
    
    # Top Recommendations
    story.append(Paragraph("<b>Top Recommendations:</b>", body_style))
    story.append(Spacer(1, 5))
    top_recs = ai_consultant.get("Top Recommendations", recommendation.get("Recommendations", []))
    if top_recs:
        for rec in top_recs:
            story.append(Paragraph(f"• {rec}", bullet_style))
    else:
        story.append(Paragraph("_No specific recommendations generated._", body_style))
        
    story.append(Spacer(1, 10))

    # Future Improvements
    story.append(Paragraph("<b>Future Improvements:</b>", body_style))
    story.append(Spacer(1, 5))
    future_imps = ai_consultant.get("Future Improvements", recommendation.get("Future Improvements", []))
    if future_imps:
        for imp in future_imps:
            story.append(Paragraph(f"• {imp}", bullet_style))
    else:
        story.append(Paragraph("_No future improvements listed._", body_style))

    # =========================================================
    # 6. SDGS SUPPORTED
    # =========================================================
    story.append(Paragraph("5. Sustainable Development Goals (SDGs)", header_style))
    sdgs = sustainability.get("SDGs Covered", [])
    if sdgs:
        for sdg in sdgs:
            story.append(Paragraph(f"🌱 {sdg}", bullet_style))
    else:
        story.append(Paragraph("_No SDGs mapped._", body_style))

    # =========================================================
    # 7. FOOTER & TEAM DETAILS
    # =========================================================
    story.append(Spacer(1, 30))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.lightgrey, spaceAfter=15))
    
    footer_style = ParagraphStyle(
        name="Footer", 
        parent=styles["Normal"], 
        alignment=TA_CENTER, 
        textColor=colors.HexColor("#7f8c8d"),
        fontSize=9,
        spaceAfter=3
    )
    
    story.append(Paragraph("<b>IBM SkillsBuild Academic Internship 2026</b>", footer_style))
    story.append(Paragraph("Team Name: Electro Archons", footer_style))
    story.append(Paragraph("Team Leader: Ashutosh Bhaskar Junare | Team Member: Nikhil Haridas Dhurve", footer_style))
    story.append(Paragraph("AI Multi-Agent Sustainable Energy Management System", footer_style))

    # =========================================================
    # BUILD PDF
    # =========================================================
    doc.build(story)
    
    return file_path