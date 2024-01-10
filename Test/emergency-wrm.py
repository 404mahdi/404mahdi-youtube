class Patient:
    def __init__(self, id, name, age, bloodgroup, next=None, prev=None):
        self.id = id
        self.name = name
        self.age = age
        self.bloodgroup = bloodgroup
        self.next = next
        self.prev = prev
        

class WRM:
    patient_id = 1001
    def __init__(self):
        self.patients = Patient(None, None, None, None)
        self.patients.next = self.patients
        self.patients.prev = self.patients
        
    def RegisterPatient(self, name, age, bloodgroup):
        newPatient = Patient(WRM.patient_id, name, age, bloodgroup, self.patients, self.patients.prev)
        self.patients.prev.next = newPatient
        self.patients.prev = newPatient
        WRM.patient_id += 1
        print("Patient registered with id: ", newPatient.id)
        
    def ServePatient(self):
        if self.patients.next == self.patients:
            print("No patients to serve.")
        else:
            print("Serving patient id: ", self.patients.next.id)
            temp = self.patients.next
            self.patients.next = self.patients.next.next
            self.patients.next.prev = self.patients
            temp.next = None
            temp.prev = None
            
    def ShowPatient(self, id):
        current = self.patients.next
        while current != self.patients:
            if current.id == id:
                print("Patient id: ", current.id)
                print("Patient name: ", current.name)
                print("Patient age: ", current.age)
                print("Patient bloodgroup: ", current.bloodgroup)
                break
            if current.next == self.patients:
                print("Patient not found.")
            current = current.next
            
    def ShowAllPatients(self):
        current = self.patients.next
        while current != self.patients:
            print("Patient id: ", current.id)
            print("Patient name: ", current.name)
            print("Patient age: ", current.age)
            print("Patient bloodgroup: ", current.bloodgroup)
            current = current.next
            
    def CancelPatient(self, id):
        current = self.patients.next
        while current != self.patients:
            if current.id == id:
                print("Canceling Patient id: ", current.id)
                current.prev.next = current.next
                current.next.prev = current.prev
                current.next = None
                current.prev = None
                break
            if current.next == self.patients:
                print("Patient not found.")
            current = current.next
            
    def CancelAllPatients(self):
        
        self.patients.next = self.patients
        self.patients.prev = self.patients
        print("All patients canceled.")
        
    def CanDoctorGoHome(self):
        if self.patients.next == self.patients:
            print("Doctor can go home.")
        else:
            print("Doctor can't go home.")
            
    def ReverseTheLine(self):
        if self.patients.next == self.patients:
            print("No patients to reverse.")
        else:
            current = self.patients.next
            while current != self.patients:
                temp = current.next
                current.next = current.prev
                current.prev = temp
                current = current.prev
            temp = self.patients.next
            self.patients.next = self.patients.prev
            self.patients.prev = temp
            print("Line reversed.")
            
    def CountPatients(self):
        count = 0
        current = self.patients.next
        while current != self.patients:
            count += 1
            current = current.next
        print("Number of patients: ", count)
        
        

def main():
    wrm = WRM()
    while True:
        print("1. Register Patient")
        print("2. Serve Patient")
        print("3. Show Patient")
        print("4. Show All Patients")
        print("5. Cancel Patient")
        print("6. Cancel All Patients")
        print("7. Can Doctor Go Home")
        print("8. Reverse The Line")
        print("9. Count Patients")
        print("10. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            bloodgroup = input("Enter patient bloodgroup: ")
            wrm.RegisterPatient(name, age, bloodgroup)
        elif choice == 2:
            wrm.ServePatient()
        elif choice == 3:
            id = int(input("Enter patient id: "))
            wrm.ShowPatient(id)
        elif choice == 4:
            wrm.ShowAllPatients()
        elif choice == 5:
            id = int(input("Enter patient id: "))
            wrm.CancelPatient(id)
        elif choice == 6:
            wrm.CancelAllPatients()
        elif choice == 7:
            wrm.CanDoctorGoHome()
        elif choice == 8:
            wrm.ReverseTheLine()
        elif choice == 9:
            wrm.CountPatients()
        elif choice == 10:
            break
        else:
            print("Invalid choice.")
        print()
        
        
main()