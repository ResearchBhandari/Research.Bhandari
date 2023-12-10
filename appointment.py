# Create a class to represent an Appointment
class Appointment:
    # Initialize the appointment with day of week and start time hour
    def __init__(self, day_of_week, start_time_hour):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour
    # Define getter methods to retrieve appointment information
    def get_client_name(self):
        return self.client_name

    def get_client_phone(self):
        return self.client_phone

    def get_appt_type(self):
        return self.appt_type

    def get_day_of_week(self):
        return self.day_of_week

    def get_start_time_hour(self):
        return self.start_time_hour

    def get_appt_type_desc(self):
        appt_types = {
            0: "Available",
            1: "Mens Cut",
            2: "Ladies Cut",
            3: "Mens Colouring",
            4: "Ladies Colouring"
        }
        return appt_types.get(self.appt_type, "Invalid Type")

    def get_end_time_hour(self):
        return self.start_time_hour + 1
    
    # Define setter methods to update appointment information
    def set_client_name(self, client_name):
        self.client_name = client_name

    def set_client_phone(self, client_phone):
        self.client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.appt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)

    def cancel(self):
        self.client_name = ""
        self.client_phone = ""
        self.appt_type = 0

    def format_record(self):
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day_of_week},{self.start_time_hour:02}"

    def __str__(self):
        return f"{self.client_name.ljust(20)} {self.client_phone.ljust(15)} {self.day_of_week.ljust(10)} {self.start_time_hour:02}:00 - {self.get_end_time_hour():02}:00 {self.get_appt_type_desc()}"
