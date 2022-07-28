import pandas as pd

def calculate_bmi(wt_kg, ht_cm):
    return wt_kg/((ht_cm/100)**2)

def category_risk(x):
    bmi = x
    if bmi <= 18.4:  
        bmi_cat = 'underweight'
        health_risk = 'Malnutrition risk '
    elif bmi <= 24.9:  
        bmi_cat = 'Normal weight'
        health_risk = 'Low risk '
    elif bmi <= 29.9:  
        bmi_cat = 'Overweight'
        health_risk = 'Enhanced risk'
    elif bmi <= 34.9:
        bmi_cat = 'Moderately obese'
        health_risk = 'Medium risk '
    elif bmi <= 39.9:
        bmi_cat = 'Severely obese'
        health_risk = 'High risk'
    else:  
        bmi_cat = 'Very severely obese'
        health_risk = 'Very high risk'
    return bmi_cat, health_risk


patients = pd.read_json('patients.json')

#Calculate BMI
patients['BMI Range (Kg/m2)'] = calculate_bmi(patients['WeightKg'], patients['HeightCm'])

#Calculate BMI Category and Health Risk
cat_risk = patients['BMI Range (Kg/m2)'].apply(category_risk)
patients[['BMI Category', 'Health risk ']] = pd.DataFrame(cat_risk.tolist(), index=patients.index)

print(patients)

n_overwt = len(patients[patients['BMI Category'] == 'Overweight'])
print('Number of Overweight patients = ', n_overwt)

