# AuraCare Health System Core
APP_VERSION = "2.2.0"
MODULES_ENABLED = ["triage", "schedule"]

# Doctor Schedule Lookup Data
DOCTOR_SCHEDULE = {
    "Dr. Smith": ["Mon", "Wed", "Fri"],
    "Dr. Patel": ["Tue", "Thu"],
    "Dr. Lee": ["Mon", "Tue", "Thu", "Fri"],
    "Dr. Garcia": ["Wed", "Fri"],
}

DOCTOR_TIMINGS = {
    101: ["09:00 AM - 01:00 PM", "03:00 PM - 06:00 PM"],
    102: ["10:00 AM - 02:00 PM"],
}


def triage_patient(name, heart_rate, temperature):
    """Assign a triage level based on patient vitals."""
    if heart_rate <= 0 or temperature <= 0:
        raise ValueError("Invalid vitals")
    if heart_rate > 120 or temperature > 39.5:
        level = "CRITICAL"
    elif heart_rate > 100 or temperature > 38.0:
        level = "URGENT"
    else:
        level = "STABLE"
    return {"patient": name, "level": level}


def get_doctor_schedule(doctor_name):
    """Return the available days for a given doctor name."""
    schedule = DOCTOR_SCHEDULE.get(doctor_name)
    if schedule:
        return f"{doctor_name} is available on: {', '.join(schedule)}"
    return f"No schedule found for {doctor_name}."


def list_all_schedules():
    """Print the full schedule for all doctors."""
    for doctor, days in DOCTOR_SCHEDULE.items():
        print(f"{doctor}: {', '.join(days)}")


def get_doctor_schedule_by_id(doctor_id):
    """Retrieve schedule timings for a given doctor ID."""
    return DOCTOR_TIMINGS.get(doctor_id, "No schedule found for this doctor.")


if __name__ == "__main__":
    print(f"AuraCare v{APP_VERSION} running")
    print(get_doctor_schedule("Dr. Smith"))
    print(get_doctor_schedule_by_id(101))
    list_all_schedules()