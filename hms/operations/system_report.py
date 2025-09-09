import sys
sys.path.append(r'C:\Users\user\Documents\python')
import authentication as auth3
import operations.appointment as app

class SystemReport:
    @staticmethod
    def generate_report():
        total_users = len(auth3.USERS)
        roles = {'doctor': 0, 'patient': 0, 'admin': 0}
        for user in auth3.USERS.values():
            role = user.get('role')
            if role in roles:
                roles[role] += 1

        total_appointments = len(app.Appointment.appointments)
        status_counts = {'Scheduled': 0, 'Completed': 0, 'Cancelled': 0}

        for appt in app.Appointment.appointments:
            status = appt.get('status', 'Scheduled')
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1

        print("\n📊 SYSTEM REPORT")
        print("-" * 40)
        print(f"Total Users: {total_users}")
        print(f"  Doctors: {roles['doctor']}")
        print(f"  Patients: {roles['patient']}")
        print(f"  Admins: {roles['admin']}")
        print()
        print(f"Total Appointments: {total_appointments}")
        for status, count in status_counts.items():
            print(f"  {status}: {count}")
        print("-" * 40)

