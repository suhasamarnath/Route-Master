from capstone import Driver, Employee
from tabulate import tabulate

print("-" * 30)
print("Welcome to the Shuttle Service")


while True:
    print("_" * 30)
    choice = int(input("Select your option:\n\
		\t1. Bus Driver\n\
		\t2. Employee\n"))

    if choice == 1:
        driver_name = input("Name: ")
        while True:
            driver_phone = int(int(input("Phone Number: ")))
            if Driver.correct_phone(driver_phone) == False:
                break
            else:
                continue

        while True:
            bus_number = input("Bus number: ").replace(" ", "").upper()
            if Driver.correct_bus(bus_number) == False:
                break
            else:
                continue

        destination = input("Bus destination: ").upper()

        time = input("Departure time: ")
        seats = int(input("Seats available: "))
        Driver.list1.append(Driver(driver_name, driver_phone,
                                   bus_number, destination, time, seats))

    if choice == 2:
        employee_name = input("Name: ")

        while True:
            employee_phone = int(input("Enter Phone number: "))
            if Employee.correct_phone(employee_phone) == False:
                break
            else:
                continue

        employee_department = input("Department: ")
        department_id = input("Depatment id: ")
        print("Buses are travelling to the following destinations ( please enter destinations available in the list ): ")

        table = []
        for i in Driver.list1:
            if i.seats == 0:
                continue
            table.append([i.destination, i.driver_name,
                          i.driver_phone, i.bus_number, i.time, i.seats])
        print(tabulate(table, headers=["Destination", "Driver Name", "Driver PhNo",
                                       "Bus Number", "Time of Departure", " Seats Available"], tablefmt="psql"))

        while True:
            where_to = input("Enter Destination: ").upper()
            if Employee.correct_dest(where_to, employee_name, employee_phone, employee_department, department_id) == False:
                break
            else:
                continue

        print("Buses available: ")

        headers = ["Driver Name", "Bus No.",
                   "Time of Departure", "Seats available"]
        tables = []
        for obj in Driver.list1:
            if obj.destination == where_to:
                if obj.seats == 0:
                    continue
                tables.append(
                    [obj.driver_name, obj.bus_number, obj.time, obj.seats])
        print(tabulate(tables, headers=headers, tablefmt="psql"))
        print("\n")
        while True:
            busno = input("Enter the bus no. that you want to travel in: ").replace(
                " ", "").upper()
            if Employee.correct_bus(busno) == False:
                break
            else:
                continue

        for obj in Driver.list1:
            if obj.bus_number == busno:
                temp = obj
                while True:
                    seatsbooked = int(
                        input("Enter the seats you want to book: "))
                    if obj.seats_booking(obj, seatsbooked) == False:
                        break
                    else:
                        continue
                break

        Employee.display(temp, employee_name, employee_phone, employee_department, department_id, seatsbooked)
