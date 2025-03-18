from datetime import datetime, timedelta

def hospital_schedule_manager():
    department_names = ["Gynecologist", "Dermatrology"]
    patient_appointments = {}

    # Helper function for scheduling using CSP
    def schedule_appointments(department, doctors_present, online_patients_reported):
        max_patients_per_doctor = 45
        total_capacity = doctors_present * max_patients_per_doctor
        offline_patients = max(0, total_capacity - online_patients_reported)
        final_total_patients = online_patients_reported + offline_patients

        appointment_duration = timedelta(minutes=10)
        start_time = datetime.strptime("09:00", "%H:%M")
        lunch_start = datetime.strptime("13:00", "%H:%M")
        lunch_end = datetime.strptime("14:00", "%H:%M")

        doctor_schedule = {i: [] for i in range(1, doctors_present + 1)}
        patient_counter = 1

        for patient in range(1, final_total_patients + 1):
            consultant_room = (patient - 1) % doctors_present + 1
            doctor = consultant_room
            appointment_time = start_time + appointment_duration * ((patient - 1) // doctors_present)

            # Skip lunch break period
            if lunch_start <= appointment_time < lunch_end:
                appointment_time = lunch_end

            formatted_time = appointment_time.strftime("%H:%M")
            doctor_schedule[doctor].append((patient, formatted_time, consultant_room))
            patient_appointments[(department, patient)] = (formatted_time, consultant_room)

        return doctor_schedule, offline_patients, final_total_patients

    # Process departments
    for department in department_names:
        print(f"\nDepartment: {department}")

        # Input for doctors and online patients
        max_doctors = 6 if department == "Gynecologist" else 8
        doctors_present = int(input(f"Enter the number of doctors present (1-{max_doctors}): "))
        if not 1 <= doctors_present <= max_doctors:
            print(f"Invalid input. Doctors present should be between 1 and {max_doctors}.")
            return

        online_patients_reported = int(input("Enter the number of online appointment holders (0-45): "))
        if not 0 <= online_patients_reported <= 45:
            print("Invalid input. Online patients reported should be between 0 and 45.")
            return

        # Schedule appointments
        doctor_schedule, offline_patients, final_total_patients = schedule_appointments(department, doctors_present, online_patients_reported)

        # Display results
        print(f"Total online appointments: {online_patients_reported}")
        print(f"Total offline appointments scheduled: {offline_patients}")
        print(f"Final total patients: {final_total_patients}")
        print(f"Message to counter: GENERATE OFFLINE APPOINTMENT ONLY: {offline_patients}")

        # Display doctor schedules
        for doctor, appointments in doctor_schedule.items():
            print(f"\nDoctor {doctor}'s Schedule:")
            for patient, time, room in appointments:
                print(f"Patient {patient} - {time} in Consultant Room {room}")

    # Allow patients to check their appointment
    while True:
        department = input("\nEnter your department (Gynecologist or Dermatrology) to check your appointment: ")
        if department not in department_names:
            print("Invalid department. Please enter 'Gynecologist' or 'Dermatrology'.")
            continue

        try:
            appointment_number = int(input("Enter your appointment number: "))
        except ValueError:
            print("Invalid input. Please enter a valid appointment number.")
            continue

        if (department, appointment_number) in patient_appointments:
            appointment_time, room_number = patient_appointments[(department, appointment_number)]
            print(f"Your appointment time: {appointment_time} in Consultant Room {room_number}")
        else:
            print("Invalid appointment number. Please try again.")

        # Ask if the user wants to check another appointment
        check_another = input("Would you like to check another appointment? (y/n): ").lower()
        if check_another != 'y':
            break

# Call the function
hospital_schedule_manager()