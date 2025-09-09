import sys
sys.path.append(r'C:\Users\user\Documents\python')

class Appointment:
    appointments = []
    id_num = 1

    @staticmethod
    def book_appointment(patient,doctor,date,time):
        for appt in Appointment.appointments:
            if appt['doctor'] == doctor and appt['date'] == date and appt['time'] == time:
                return 'Doctor not available'
                

        appointment_id = f'{Appointment.id_num:03}'
        Appointment.id_num += 1      
        new_appt = ( { 
                'id' : appointment_id,
                'patient' : patient,
                'doctor' : doctor,
                'date' : date,
                'time' : time,
                'status' : 'Scheduled'                                     
            })
        Appointment.appointments.append(new_appt)
            
        return (
        f"✅ Appointment booked!\n"
        f"Name: {new_appt['patient']} | ID: {new_appt['id']} | "
        f"Date: {new_appt['date']} | Time: {new_appt['time']} | "
        f"With: {new_appt['doctor']} | Status: {new_appt['status']}"
    )

    @staticmethod
    def view_appointment(name):
        result = [] 
        for appt in Appointment.appointments:
            if appt['patient'] == name or appt['doctor'] == name:
                result.append(f"ID: {appt['id']} | Date: {appt['date']} | Time: {appt['time']} | With: {appt['doctor']} | Status: {appt['status']}")
        if not result:
            return ["There are no pending appointments."]
        return result   

    @staticmethod
    def cancel_appointment(appointment_id,username):
        for appt in Appointment.appointments:
            if appt['id'] == appointment_id and appt['patient'] == username:
                appt['status'] = 'Cancelled'
                return 'Appointment Cancelled'
        return 'Appointment not found'                       