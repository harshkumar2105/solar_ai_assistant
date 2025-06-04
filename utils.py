
from PIL import Image
import random

def analyze_image(image: Image.Image):
    # Simulated AI processing: In real implementation, call a vision API here
    rooftop_area_est = round(random.uniform(20.0, 60.0), 2)  # in sq meters
    panel_count = int(rooftop_area_est // 1.7)  # Assuming 1.7 sq.m per panel
    energy_output_kw = round(panel_count * 0.4, 2)  # each panel ~0.4 kW
    est_cost = panel_count * 25000  # Rs. 25,000 per panel estimate
    annual_savings = round(energy_output_kw * 1200 * 12, 2)  # 1200 units/kW/year, Rs. 12/unit
    roi_years = round(est_cost / annual_savings, 2)

    return {
        "Estimated Rooftop Area (sq.m)": rooftop_area_est,
        "Suggested Panel Count": panel_count,
        "Estimated Energy Output (kW)": energy_output_kw,
        "Estimated Installation Cost (INR)": est_cost,
        "Estimated Annual Savings (INR)": annual_savings,
        "Estimated Payback Period (years)": roi_years
    }
