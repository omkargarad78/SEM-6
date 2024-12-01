print('Welcome to Hospital Disease Identification System')

# Counter to track the suspicion level of diseases
diseaseSuspicionCounter = 0
# Counter to track the severity of symptoms
severity = 0

# Variable to store the predicted disease
predictedDisease = None

# Flags to track specific symptoms
highFeverFlag = 0
coughFlag = 0
shortnessOfBreathFlag = 0

# List of questions related to symptoms
symptomQuestions = [
    'Do you have a high fever (above 101°F)?',
    'Are you experiencing coughing?',
    'Do you have shortness of breath or difficulty breathing?',
    'Do you experience chest pain or pressure?',
    'Are you feeling fatigued or experiencing weakness?',
    'Are you experiencing any gastrointestinal symptoms like nausea, vomiting, or diarrhea?',
    'Do you have muscle or body aches?',
    'Are you experiencing headaches?',
    'Do you have a sore throat?',
    'Are you experiencing loss of taste or smell?',
    'Have you been in close contact with someone diagnosed with a contagious disease?'
]

# Loop through the symptom questions and get user input
for i in range(len(symptomQuestions)):
    print(symptomQuestions[i])
    answer = input().lower()

    # Check if the answer indicates a positive symptom
    if answer == 'yes':
        diseaseSuspicionCounter += 1
        if i == 0:  # High fever
            severity += 2
            highFeverFlag = 1
        elif i == 1:  # Coughing
            severity += 1
            coughFlag = 1
        elif i == 2:  # Shortness of breath
            severity += 2
            shortnessOfBreathFlag = 1

# Determine potential disease based on the most severe symptom
if severity >= 8:
    predictedDisease = 'Pneumonia'
elif severity >= 6:
    predictedDisease = 'COVID-19'
elif severity >= 4:
    predictedDisease = 'Influenza (Flu)'
elif severity >= 3 and coughFlag == 1:
    predictedDisease = 'Bronchitis'
elif severity >= 2 and shortnessOfBreathFlag == 1:
    predictedDisease = 'Asthma'

# Print the predicted disease
if predictedDisease:
    print('Based on your symptoms, you may have', predictedDisease)
else:
    print('Your symptoms do not match any specific diseases.')

# Additional recommendations based on specific symptoms
print()
if highFeverFlag == 1:
    print("Please monitor your body temperature regularly and stay hydrated.")
if coughFlag == 1:
    print("Get plenty of rest and consider taking cough suppressants if the cough is severe.")
if shortnessOfBreathFlag == 1:
    print("If you are experiencing severe shortness of breath, seek medical attention immediately.")
