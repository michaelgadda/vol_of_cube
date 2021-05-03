class fullname: 

	def first_plus_lastname(first_name, last_name):
		if first_name == '':
			return "You have forgot to enter your first name, please do so and try again"
		elif last_name == '':
			return "You have forgot to enter your last name, please do so and try again"
	
		
		fullname =  f"{first_name} {last_name}"
		
		for x in first_name: 
			if x.isalpha() == False: 
				non_alpha_error = "Your first contains a non alphabetic character, please remove it and try again!"
				return non_alpha_error 
		for z in last_name:
			if z.isalpha() == False: 
				l_non_alpha_error =  "Your last name contains a non alphabetic character, please remove it and try again!"
				return l_non_alpha_error
		return fullname