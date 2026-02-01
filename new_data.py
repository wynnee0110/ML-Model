import pandas as pd

CSV_PATH = "data/data.csv"

while True:
    try:
        study_hours = int(input("Enter study hours: "))
        attendance = int(input("Enter attendance (%): "))
        prev_grade = int(input("Enter previous grade: "))
        sleep_hours = int(input("Enter sleep hours: "))
        practice = int(input("Enter practice hours: "))
        final_score = int(input("Enter final score: "))

        new_data = pd.DataFrame([{
            "study_hours": study_hours,
            "attendance": attendance,
            "prev_grade": prev_grade,
            "sleep_hours": sleep_hours,
            "practice": practice,
            "final_score": final_score
        }])

        new_data.to_csv(CSV_PATH, mode="a", header=False, index=False)

        print(" Row added. Enter next student.\n")

    except ValueError:
        print(" Invalid input. Please enter numeric values.\n")

    except KeyboardInterrupt:
        print("\n Data entry stopped.")
        break
