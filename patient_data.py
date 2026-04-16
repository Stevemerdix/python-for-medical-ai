patients = []

def add_patient():
name = input("Enter patient name: ")
age = input("Enter age: ")
condition = input("Enter condition: ")

patient = {
"name": name,
"age": age,
"condition": condition
}

patients.append(patient)
print("Patient added successfully!")

def view_patients():
for p in patients:
print(p)

while True:
print("\n1. Add Patient\n2. View Patients\n3. Exit")
choice = input("Choose an option: ")

if choice == "1":
add_patient()
elif choice == "2":
view_patients()
elif choice == "3":
break
