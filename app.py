#Import Libraries
from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder
import numpy as np
import itertools
import pickle
import model # load model.py
app = Flask(__name__)
# render htmp page
@app.route('/')
def home():
    return render_template('multiple.html')

# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
    #arr = ['skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze'];
    input_features = [x for x in request.form.values()]
    #s1 = input_features[0]
    
    # printing result 
    #print ("List with only nth tuple element (i.e names) : " + str(res)) 

    #s1 = request.form
    #print(s1['Symptoms'][0])
    
    #print(s1['Symptoms'][1])
    s1 =  input_features[0]
    s2 =  input_features[1]
    s3 =  input_features[2]
    s4 =  input_features[3]
    s5 =  input_features[4] 
    #choices = [(str(x), str(x)) for  x in arr]
    # test if value was passed in (e.g. GET method), default value is 1
    #selected = request.args.get('choice')
    # application 'state' variable with default value and test
   # state = {'choice': selected}
    #s1="No"    
    # predict the price of house by calling model.py
    
    predicted_disease = model.predict_disease([s1,s2,s3,s4,s5])       
   # multiselect = request.form.getlist('select')
    print(predicted_disease)
    Dict = {'Fungal infection':'M1', 'Allergy':'M2', 'GERD':'M3', 'Chronic cholestasis':'M4',
       'Drug Reaction':'M5', 'Peptic ulcer diseae':'M6', 'AIDS':'M7', 'Diabetes ':'M8',
       'Gastroenteritis':'M9', 'Bronchial Asthma':'M10', 'Hypertension ':'M11', 'Migraine':'M12',
       'Cervical spondylosis':'M13', 'Paralysis (brain hemorrhage)':'M14', 'Jaundice':'M15',
       'Malaria':'M16', 'Chicken pox':'M17', 'Dengue':'M18', 'Typhoid':'M19', 'hepatitis A':'M20',
       'Hepatitis B':'M21', 'Hepatitis C':'M22', 'Hepatitis D':'M23', 'Hepatitis E':'M24',
       'Alcoholic hepatitis':'M25', 'Tuberculosis':'M26', 'Common Cold':'M27', 'Pneumonia':'M28',
       'Dimorphic hemmorhoids(piles)':'M29', 'Heart attack':'M30', 'Varicose veins':'M31',
       'Hypothyroidism':'M32', 'Hyperthyroidism':'M33', 'Hypoglycemia':'M34',
       'Osteoarthristis':'M35', 'Arthritis':'M36',
       '(vertigo) Paroymsal  Positional Vertigo':'M37', 'Acne':'M38',
       'Urinary tract infection':'M39', 'Psoriasis':'M40', 'Impetigo':'M41'}
    def get_values(k):
        for key, value in Dict.items():
             if k == key:
                 return value
     
        return "Recommended medicine not found"
    medicine = get_values(predicted_disease[0])
    # render the html page and show the output
    return render_template('multiple.html',predicted = 'Predicted Disease : {}'.format((predicted_disease[0])),medicine = 'Recommended medicine : {}'.format(medicine))

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080")
    
if __name__ == "__main__":
    app.run()
    app.config["CACHE_TYPE"] = "null"
    