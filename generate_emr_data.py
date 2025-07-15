import pandas as pd
import random
from faker import Faker

fake = Faker()

# -------- 1. Patient Records --------
def generate_patient_records(num_records=200):
    data = []
    for i in range(num_records):
        data.append({
            "PatientID": f"P{1000 + i}",
            "Name": fake.name(),
            "Age": random.randint(18, 90),
            "Gender": random.choice(["Male", "Female", "Other"]),
            "Provider": fake.name(),
            "AppointmentType": random.choice(["New", "Follow-up", "Annual", "Sick Visit"]),
            "VitalsEntered": random.choice(["Yes", "No"]),
            "CheckInTime": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M"),
            "CheckOutTime": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M"),
            "IssuesLogged": random.choice(["None", "Vitals entry delay", "System froze", "Missing templates", "Slow load time"])
        })
    return pd.DataFrame(data)

# -------- 2. Appointment Workflows --------
def generate_appointment_workflows(num_records=100):
    data = []
    for i in range(num_records):
        data.append({
            "AppointmentID": f"A{2000 + i}",
            "PatientID": f"P{1000 + random.randint(0, 199)}",
            "WorkflowStepsCompleted": random.choice(["All", "Vitals Skipped", "Vitals Delayed", "Provider Note Incomplete"]),
            "TimeToComplete": random.randint(8, 45),
            "ModulesUsed": random.choice(["Vitals, Notes, Billing", "Vitals only", "Notes only", "All Modules"]),
            "ErrorsEncountered": random.choice(["None", "Lag", "Missing fields", "Double entry"])
        })
    return pd.DataFrame(data)

# -------- 3. User Feedback --------
def generate_user_feedback(num_records=50):
    roles = ["Nurse", "Provider", "Admin", "MA", "Billing"]
    feedback = [
        "Vitals entry screen is slow",
        "Can’t find billing code template",
        "System crashes when saving notes",
        "Too many clicks to complete chart",
        "Training was insufficient",
        "Navigation is not intuitive",
        "Would like auto-populated templates",
        "No issues"
    ]
    data = []
    for i in range(num_records):
        data.append({
            "UserID": f"U{3000 + i}",
            "Role": random.choice(roles),
            "Department": random.choice(["Pediatrics", "Family Med", "Internal Med", "Cardiology"]),
            "Feedback": random.choice(feedback),
            "SatisfactionRating": random.randint(1, 5)
        })
    return pd.DataFrame(data)

# -------- Save All as CSVs --------
patient_df = generate_patient_records()
workflow_df = generate_appointment_workflows()
feedback_df = generate_user_feedback()

patient_df.to_csv("patient_records.csv", index=False)
workflow_df.to_csv("appointment_workflows.csv", index=False)
feedback_df.to_csv("user_feedback.csv", index=False)

print("✅ All CSV files generated successfully!")
