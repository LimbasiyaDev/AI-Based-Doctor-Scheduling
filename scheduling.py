# List of doctors and available shifts
doctors = ['Dr. John', 'Dr. Jack', 'Dr. Tom', 'Dr. Alexander']
shifts = [10, 22, 16, 8]

# Dictionary to store the schedule
schedule = {}

# Loop until all doctors are scheduled
while len(schedule) < len(doctors):
    # Display available doctors
    print("\nAvailable Doctors:")
    for i, doctor in enumerate(doctors):
        if doctor not in schedule:
            print(f"{i + 1}. {doctor}")

    # Get user input to select a doctor
    try:
        doctor_choice = int(input("\nChoose a doctor by number: ")) - 1
        if doctor_choice < 0 or doctor_choice >= len(doctors) or doctors[doctor_choice] in schedule:
            print("Invalid choice. Please try again.")
            continue
        doctor = doctors[doctor_choice]
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Display available shifts
    print("\nAvailable Shifts:")
    for shift in shifts:
        if shift not in schedule.values():
            print(f"- {shift} (24-hour format)")

    # Get user input to select a shift
    while True:
        try:
            shift_choice = int(input(f"Choose a shift for {doctor} (enter the number): "))
            if shift_choice not in shifts:
                print("Invalid shift. Please choose from the available shifts.")
                continue
            if shift_choice in schedule.values():
                print("This shift is already taken. Please choose another shift.")
                continue
            schedule[doctor] = shift_choice
            print(f"{doctor} has been assigned to shift {shift_choice}.")
            break
        except ValueError:
            print("Please enter a valid shift.")

# If all doctors are successfully assigned a shift, print the schedule
if len(schedule) == len(doctors):
    print("\nScheduling Successful!")
    for doctor, shift in schedule.items():
        print(f"{doctor}: Shift {shift}")
