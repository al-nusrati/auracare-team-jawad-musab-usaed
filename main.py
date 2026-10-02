# AuraCare Health System Core
APP_VERSION = "1.2.0"
MODULES_ENABLED = ["triage"]


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


def main():
    print(f"AuraCare v{APP_VERSION} running")


if __name__ == "__main__":
    main()