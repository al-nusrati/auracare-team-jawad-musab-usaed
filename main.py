APP_VERSION = "1.1.0"
MODULES_ENABLED = ["triage"]


def triage_patient(name, heart_rate, temperature):
    """Assign a triage level based on patient vitals."""
    if heart_rate > 120 or temperature > 39.5:
        level = "CRITICAL"
    elif heart_rate > 100 or temperature > 38.0:
        level = "URGENT"
    else:
        level = "STABLE"
    return {"patient": name, "level": level}
    
# Doctor Schedule Lookup
DOCTOR_SCHEDULE = {
    "Dr. Smith": ["Mon", "Wed", "Fri"],
    "Dr. Patel": ["Tue", "Thu"],
    "Dr. Lee": ["Mon", "Tue", "Thu", "Fri"],
    "Dr. Garcia": ["Wed", "Fri"],
}

def get_doctor_schedule(doctor_name):
    """Return the available days for a given doctor."""
    schedule = DOCTOR_SCHEDULE.get(doctor_name)
    if schedule:
        return f"{doctor_name} is available on: {', '.join(schedule)}"
    return f"No schedule found for {doctor_name}."

def list_all_schedules():
    """Print the full schedule for all doctors."""
    for doctor, days in DOCTOR_SCHEDULE.items():
        print(f"{doctor}: {', '.join(days)}")

if __name__ == "__main__":
    print(f"AuraCare v{APP_VERSION} running")
    print(get_doctor_schedule("Dr. Smith"))
    list_all_schedules()
    
