import numpy as np
import pandas as pd

limitless_multiVitamins = pd.DataFrame(
    {
        "Vitamin A": 1050,
        "Vitamin C": 90,
        "Vitamin D3": 25.0,
        "Vitamin E": 20.3,
        "Vitamin K": 60.0,
        "Vitamin B6": 2.0,
        "Vitamin B12": 6.0,
        "Vitamin B1 Thiamine": 1050.0,
        "Vitamin B2 Riboflavin": 1.3,
        "Niacin": 16.0,
        "Vitamin B9 Folic Acid": 200.0,
        "Biotin": 40.0,
        "Pantothenic Acid": 15.0,
        "Calcium": 210.0,
        "Iron": 8.0,
        "Phosphorus": 20.0,
        "Lodine": 150.0,
        "Magnesium": 100.0,
        "Zinc": 11.0,
        "Selenium": 100.0,
        "Copper": .9,
        "Manganese": 2.3,
        "Chromium": 35.0,
        "Molybdenum": 50.0,
        "Chloride": 72.0,
        "Potassium": 80.0,
        "Lycopene": 600.0,
    },
    index=["man_max"]
)
centrum_multiVitamins = pd.DataFrame(
    {
        "Vitamin A": 800.0,
        "Vitamin C": 80.0,
        "Vitamin D3": 10.0,
        "Vitamin E": 24.3,
        "Vitamin K": 30.0,
        "Vitamin B6": 2.1,
        "Vitamin B12": 3.0,
        "Vitamin B1 Thiamine": 1008.0,
        "Vitamin B2 Riboflavin": 2.1,
        "Niacin": 20.0,
        "Vitamin B9 Folic Acid": 200.0,
        "Biotin": 62.5,
        "Pantothenic Acid": 7.5,
        "Calcium": 200.0,
        "Iron": 3.75,
        "Phosphorus": 105.0,
        "Lodine": 100.0,
        "Magnesium": 120.0,
        "Zinc": 5.0,
        "Selenium": 30.0,
        "Copper": .5,
        "Manganese": 2.0,
        "Chromium": 40.0,
        "Molybdenum": 50.0,
        "Chloride": 0.0,
        "Potassium": 0.0,
        "Lycopene": 0.0,
    },

    index=["centrum_men"]
)

df = limitless_multiVitamins.append(centrum_multiVitamins)

df.loc['Diff Limitless - centrum'] = df.loc['man_max'] - df.loc['centrum_men']
# df.loc['Diff centrum - Limitless'] = df.loc['centrum_men'] - df.loc['man_max']
print(df.to_string())
