"""Reusable helpers for summarizing clinic systolic readings."""


def systolic_readings(encounters):
    """TODO: Returns the systolic blood pressures of every encounter stored in clinic_encounters.csv."""
    # TODO: collect the systolic value of every encounter into one list.
    
    readings_systolic = []
    for encounter in encounters:
        if not encounter:
            return None
        else:
            systolic = encounter["systolic"]
            readings_systolic.append(systolic)
    return readings_systolic
    pass


def mean_systolic(readings):
    """TODO: Returns the average systolic pressure for the Valid values stored in clinic_encounters.csv. 
    Also returns "None" for systolic pressures not collected."""
    # TODO: return None when there is nothing to average, then sum() / len().
    readings_systolic = []
    for reading in readings:
        if not reading:
            return None
        else:
            systolic = reading["systolic"]
            readings_systolic.append(systolic)
    return sum(readings_systolic) / len(readings_systolic)
    pass


def count_patients(encounters):
    """TODO: Collects only the number of distinct patient IDs in clinic_encounters.csv using a set."""
    # TODO: collect the patient IDs and keep only the distinct ones.
    ids = set()
    for encounter in encounters:
        ids.add(encounter["patient_id"])
    return ids
    pass


def patients_at_or_above(encounters, cutoff):
    """TODO: Returns only the patient IDs whose systolic pressure is above 130 mm Hg."""
    # TODO: keep each patient whose systolic reading is at or above cutoff.
    ids = []
    for encounter in encounters:
        if encounter["systolic"] > cutoff:
            ids.append(encounter["patient_id"])
    return ids
    pass
