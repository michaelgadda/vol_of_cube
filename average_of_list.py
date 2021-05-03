
class list_: 

	def average_of_list(arr: list): 
		length = len(arr)
		total = 0 
		for i in arr: 
			if isinstance(i, str): 
				string_error = "Please enter a list of ONLY numbers!"
				return string_error
			elif isinstance(i, bool):
				boolean_error = "Please enter a list of ONLY numbers!"
				return boolean_error
			else:	
				total += i 

		try: 
			average = total/length 
		
		except ZeroDivisionError:
			ZDE = "Please enter more than 0 elements"
			return ZDE
		
		return average
