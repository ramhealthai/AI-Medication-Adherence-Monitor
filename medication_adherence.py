patients = {
    "John": 90,
    "Sarah": 65,
    "Michael": 40,
    "Emma": 85
}

print("Medication Adherence Monitoring System")
print("--------------------------------------")

for patient, adherence in patients.items():

    print("\nPatient:", patient)
    print("Adherence Rate:", adherence, "%")

    if adherence >= 80:
        print("Status: Good adherence")

    elif adherence >= 50:
        print("Status: Moderate adherence")

    else:
        print("Status: High risk of missed medication")
