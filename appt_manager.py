# appt_manager.py
from appointment import Appointment
# Create a function to initialize a weekly calendar
def create_weekly_calendar():
    calendar = []
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    for day in days_of_week:
        for hour in range(9, 17):
            appointment = Appointment(day, hour)
            calendar.append(appointment)
    
    return calendar
# Create a function to find an appointment based on the day and start hour
def find_appointment_by_time(appointment_list, day, start_hour):
    for appointment in appointment_list:
        if appointment.get_day_of_week() == day and appointment.get_start_time_hour() == start_hour:
            return appointment
    return None
# Create a function to load previously scheduled appointments from a file
def load_scheduled_appointments(appointment_list):
    while True:
        filename = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").lower()
        if filename == 'y':
            filename = input("Enter appointment filename: ")
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        data = line.strip().split(',')
                        day, start_hour, client_name, client_phone, appt_type = data
                        appointment = find_appointment_by_time(appointment_list, day, int(start_hour))
                        if appointment:
                            appointment.schedule(client_name, client_phone, int(appt_type))
                print(f"{len(lines)} previously scheduled appointments have been loaded")
                break
            except FileNotFoundError:
                print("File not found. Re-enter appointment filename.")
        elif filename == 'n':
            break
        else:
            print("Invalid input. Enter 'Y' for Yes or 'N' for No.")

# Create a function to print the main menu
def print_menu():
    print("Jojo's Hair Salon Appointment Manager")
    print("=====================================")
    print(" 1) Schedule an appointment")
    print(" 2) Find appointment by name")
    print(" 3) Print calendar for a specific day")
    print(" 4) Cancel an appointment")
    print(" 9) Exit the system")
    choice = input("Enter your selection: ")

    if choice == '1':
        print("\n** Schedule an appointment **")

    return choice

# Create a function to show appointments for a specific name
def show_appointments_by_name(appointment_list, client_name):
    matching_appointments = [appointment for appointment in appointment_list if client_name.lower() in appointment.get_client_name().lower()]
    
    if not matching_appointments:
        print(f"No appointments found for {client_name.capitalize()}")
        return

    print("\n** Find appointment by name **")
    print("Client Name          | Phone Number     | Day       | Start | End   | Type")
    
    for appointment in matching_appointments:
        print(f"{appointment.get_client_name():<20} | {appointment.get_client_phone():<16} | {appointment.get_day_of_week():<9} | "
              f"{appointment.get_start_time_hour():02}:00 | {appointment.get_end_time_hour():02}:00 | {appointment.get_appt_type_desc()}")

# Create a function to show appointments for a specific day

def show_appointments_by_day(appointment_list, day):
    matching_appointments = [appointment for appointment in appointment_list if appointment.get_day_of_week().lower() == day.lower()]

    if not matching_appointments:
        print(f"No appointments for {day.capitalize()}")
        return

    print("\nAppointments for", day.capitalize())
    print("Client Name          | Phone Number     | Day       | Start | End   | Type")
    for appointment in matching_appointments:
        print(f"{appointment.get_client_name():<20} | {appointment.get_client_phone():<16} | {appointment.get_day_of_week():<9} | "
              f"{appointment.get_start_time_hour():02}:00 | {appointment.get_end_time_hour():02}:00 | {appointment.get_appt_type_desc()}")

# Create a function to save scheduled appointments to a file
def save_scheduled_appointments(appointment_list):
    filename = input("Enter appointment filename: ")
    try:
        with open(filename, 'w') as file:
            for appointment in appointment_list:
                if appointment.get_appt_type() != 0:
                    file.write(appointment.format_record() + '\n')
    except FileExistsError:
        print("File already exists.")

# Create the main function to run the appointment manager system
def main():
    print("Starting the Appointment Manager System")
    weekly_calendar = create_weekly_calendar()
    load_scheduled_appointments(weekly_calendar)

    while True:
        choice = print_menu()

        if choice == '1':
            day = input("What day: ")
            start_hour = int(input("Enter start hour (24 hour clock): "))
            appointment = find_appointment_by_time(weekly_calendar, day, start_hour)

            if appointment:
                client_name = input("Client Name: ")
                client_phone = input("Client Phone: ")

                print("Type of Appointments:")
                print("0. Available")
                print("1. Mens Cut $50")
                print("2. Ladies Cut $80")
                print("3. Mens Colouring $50")
                print("4. Ladies Colouring $120")

                appt_type = int(input("Select Type of Appointment (0-4): "))
                if 0 <= appt_type <= 4:
                    appointment.schedule(client_name, client_phone, appt_type)
                   
                   
                    print(f"OK, {client_name}'s appointment is scheduled!")
                else:
                    print("Invalid appointment type. Appointment not scheduled.")

            else:
                print("Invalid day or hour. Appointment not scheduled.")
        elif choice == '2':
            client_name = input("Enter Client Name: ")
            show_appointments_by_name(weekly_calendar, client_name)

        elif choice == '3':
            day = input("Enter day of week: ")
            show_appointments_by_day(weekly_calendar, day)

        elif choice == '4':
            day = input("What day: ")
            start_hour = int(input("Enter start hour (24 hour clock): "))
            appointment = find_appointment_by_time(weekly_calendar, day, start_hour)

            if appointment and appointment.get_appt_type() != 0:
                appointment.cancel()
                print(f"Appointment: {day} {start_hour:02}:00 - {appointment.get_end_time_hour():02}:00 for {appointment.get_client_name()} has been cancelled!")
            else:
                print("That time slot isn't booked and doesn't need to be cancelled")

        elif choice == '9':
            save = input("Would you like to save all scheduled appointments to a file (Y/N)? ").lower()
            if save == 'y':
                save_filename = input("Enter appointment filename: ")
                save_scheduled_appointments(weekly_calendar, save_filename)
                count_saved_appointments = len([appt for appt in weekly_calendar if appt.get_appt_type() != 0])
                print(f"{count_saved_appointments} scheduled appointments have been successfully saved")
            print("Good Bye!")
            break


if __name__ == "__main__":
    main()
