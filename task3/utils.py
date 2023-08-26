def input_until_right(message="input a value: ", error_message="ERROR!", casting_type=str):
	"""
	Wrapper function for input, repeats the input until the appropriate datatype has been entered (users can exit via a Keyboard Interupt).
	
	Parameters
	----------
	* `message_value`: The prompt for the input.
	* `error_message`: The error message which is presented the input raises an error when casting the inputted value to `casting_type`.
	* `casting_type`: The data type which the inputted value is casted.
	"""
	while True:
		try:
			value = casting_type(input(message))
			break
		except KeyboardInterrupt: exit()
		except: 
			print(error_message)
			continue
	return value
			