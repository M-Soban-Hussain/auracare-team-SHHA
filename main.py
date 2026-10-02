
# AuraCare Health Team SHHA
APP_VERSION = "1.0.0"
MODULES_ENABLED = ["Triage"]



def patient_triage(symptoms):
    if symptoms == "chest pain":
        return "High Priority"
    else  
        return "Low Priority"