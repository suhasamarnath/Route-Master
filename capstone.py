from tabulate import tabulate
class Driver:

	list1 = []

	dest_list = []

	def __init__(self, driver_name, driver_phone, bus_number, destination, time, seats):
		self.driver_name = driver_name
		self.driver_phone = driver_phone
		self.bus_number = bus_number
		self.destination = destination
		self.time = time
		self.seats = seats

	def update(self, seats, seats_booked):
			self.seats = seats - seats_booked


	def correct_phone(phno):
		if len(str(phno)) == 10:
			if any(obj.driver_phone == phno for obj in Driver.list1):
				print("This phone number is already taken. Enter another one")
				return True
			else:
				return False
		else:
				print("Enter a valid phone number")

	def correct_bus(busno):
		if any(obj.bus_number == busno for obj in Driver.list1):
			print("This Bus Number already exists. Enter another number.")
			return True
		else:
			return False

	def seats_booking(self,obj,seatsbooked):
		self.obj = obj
		if (seatsbooked > obj.seats):
			print("You have booked too many seats. Please enter again.")
			return True
		else:
			obj.seats -= seatsbooked
			if obj.seats == 0:
				print("All seats in this bus have now been booked")				
			return False
		
				

class Employee:
	
	list2 = []

	def __init__(self, employee_name, employee_phone, employee_department, department_id, where_to):
		self.employee_name = employee_name
		self.employee_phone = employee_phone
		self.employee_department = employee_department
		self.department_id = department_id
		self.where_to = where_to

	def correct_phone(phno):
		if len(str(phno)) == 10:
			if any(obj.employee_phone == phno for obj in Employee.list2):
				print("This phone number is already taken. Enter another one")
				return True
			else:
				return False
		else:
				print("Enter a valid phone number")

	def correct_dest(dest,employee_name, employee_phone, employee_department, department_id):
		if any(obj.destination == dest for obj in Driver.list1):
			Employee.list2.append( Employee(employee_name, employee_phone, employee_department, department_id, dest))
			return False
		else:
			print("Enter a valid destination")
			return True

	def correct_bus(busno):
		if any(obj.bus_number == busno for obj in Driver.list1):
			return False
		else:
			print("Enter a valid bus Number")
			return True
			

	




