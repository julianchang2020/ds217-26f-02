#!/usr/bin/env python3
"""Summarize one week of clinic encounters and save the two report files."""

from pathlib import Path

from vitals_tools import (
    count_patients,
    mean_systolic,
    patients_at_or_above,
    systolic_readings,
)


DATA_PATH = Path("data") / "clinic_encounters.csv"
OUTPUT_DIR = Path("output")


def read_encounters(data_path):
    """TODO: A usable encounter row should have three comma-separated fields: patient_id, visit_date, and systolic.
    The third field "systolic" should be an integer (able to be read by int()) and should be between 60 and 250 mm Hg.

    Give back two values: the list of usable encounters, and how many data
    rows you skipped. `main()` unpacks them the way the lecture unpacks a
    tuple, with two names on the left of the `=`.
    """
    # TODO: read the rows and skip the header line.
    # TODO: count every other data row as skipped, the blank line included,
            #       and print one line per skipped row so you can see what dropped out.
    # TODO: keep a row only when it has three fields, int() can read the
        #       systolic field, and the reading is plausible.
    with open(data_path, "r") as file: 
        rows = file.readlines()

    encounters = []
    skipped_encounter = []

    for row in rows[1:]:
        # Evaluates if row is blank.
        if not row.strip():
            print("Skipping a blank row")
            skipped_encounter.append(row)
            continue
        fields = row.strip().split(",")

        # Evaluates if row can be split into 3 fields.
        if len(fields) != 3:
            print(f"Skipping a row with {len(fields)} fields: {row.strip()})")
            skipped_encounter.append(row)
            continue
        patient_id, visit_date, systolic = fields

        # Evaluates if "systolic" is an integer and is within range; otherwise, the usable rows are saved into a dictionary called "encounters".
        try:
            systolic = int(systolic)
        except ValueError as error:
            print(f"Skipping {patient_id}: {error}")
            skipped_encounter.append(row)
        else:
            if (systolic < 60):
                print(f"Skipping {patient_id}: systolic pressure below 60 mmHg")
                skipped_encounter.append(row)
            elif (systolic > 250):
                print(f"Skipping {patient_id}: systolic pressure above 250 mmHg")
                skipped_encounter.append(row)
            else:
                encounters.append({"patient_id": patient_id, "visit_date": visit_date, "systolic": systolic}) 
        count_usable = len(encounters)
        skipped = len(skipped_encounter)
    # TODO: end with `return encounters, skipped`.
    return encounters, skipped
    pass


def main():
    """TODO: describe the two artifacts this writes."""
    encounters, skipped = read_encounters(DATA_PATH)

    # TODO: build the six report lines and write them to output/vitals_report.txt.
    # TODO: read the file back and print it, so you can see what was saved.
    # TODO: choose your follow-up cutoff, then write output/followup_list.txt
    #       with the Cutoff line, the Reason line, and one patient ID per line.
    
    #print(len(encounters))
    #print(skipped)
    #print(len(count_patients(encounters)))
    #print(mean_systolic(encounters))
    #print(max(systolic_readings(encounters)))
    #print(min(systolic_readings(encounters)))

    # Creates "output/vitals_report.txt" file with the six required report lines.
    OUTPUT_DIR.mkdir(exist_ok = True)
    vitals_path = OUTPUT_DIR / "vitals_report.txt"

    results = [f"Usable encounters: {len(encounters)}\n", f"Skipped rows: {skipped}\n", f"Patients seen: {len(count_patients(encounters))}\n", 
              f"Mean systolic: {mean_systolic(encounters)} mmHg\n", f"Highest systolic: {max(systolic_readings(encounters))} mmHg\n", 
              f"Lowest systolic: {min(systolic_readings(encounters))} mmHg"]
    
    with open(vitals_path, "w") as file:
        for result in results:
            file.write(result)

    # Creates "output/followup_list.txt" file with the specified cutoff value below.
    cutoff = 130
    above_cutoff = patients_at_or_above(encounters, cutoff)
    reason = "I am choosing 130 mmHg as my cutoff as it is the recommended cutoff point for reporting Stage 1 Hypertension by the American Heart Association."

    followup = OUTPUT_DIR / "followup_list.txt"

    with open(followup, "w") as file:
        file.write(f"Cutoff: {cutoff} mmHg\n")
        file.write(f"Reason: {reason}\n")
        for i in above_cutoff:
            file.write(f"{i}\n")


if __name__ == "__main__":
    main()
