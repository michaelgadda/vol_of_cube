class cube: 

	def vol_of_cube(a):
		
		if isinstance(a, str):
			return "The length of your edge can not be a string"
				
		elif isinstance(a, bool):
			return "The length of your edge can not be a boolean value"
		elif a < 0:
			less_than_0 = "The length needs to be greater than 0"
			return less_than_0
		
		volume = a * a * a 

		return volume