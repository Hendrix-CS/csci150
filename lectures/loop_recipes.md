# Loop Design Patterns

## Receive input until we are finished

	# Input, Sentinel
	finished = False
	while not finished:
		response = input("Enter input: ")
		if response indicates we are finished:
			finished = True
		else:
			# Do other things with response
			
	# Input, Seeded
	response = seed value; loop condition will be true
	while response indicates we are not finished:
		response = input("Enter input: ")
		# Do other things with response
		
		
## Accumulation

	accumulator = identity value for operator and type
	while the loop keeps going:
		accumulator = accumulator [operator] value
		# Do other relevant things
		
Common types, operators, and identity elements:
* `int`
  * `+`: `0`
  * `*`: `1`
* `float`
  * `+`: `0.0`
  * `*`: `1.0`
* `bool`
  * `and`: `True`
  * `or`: `False`
* `str`
  * `+`: `''` or `""`
* `List`
  * `.append()`: `[]`
  
  
## Count until a condition is met

	count = 0
	while condition is not met:
		count += 1
		# other pertinent updates to variables
		

## Count instances of a property

	count = 0
	while condition is not met:
		if property is true:
			count += 1
		# other stuff
		
## Check if a property is always true

	always = true
	while always and condition:
		if not property:
			always = False
			
## Check if a property is ever true

	ever = false
	while not ever and condition:
		if property:
			ever = True
		
		
## Traverse a sequence

	i = 0
	while i < len(sequence):
		# Do something with sequence[i]
		i += 1
		
## Filter a sequence

	new_sequence = empty sequence
	i = 0
	while i < len(sequence):
		if property(sequence[i]):
			add sequence[i] to new_sequence
		i += 1


## Map a sequence

	new_sequence = empty sequence
	i = 0
	while i < len(sequence):
		add transform(sequence[i]) to new_sequence
		i += 1
		
		
## Some combinations

	# Accumulate from user inputs
	accumulator = identity element of type and operator
	finished = False
	while not finished:
		value = input("Enter value: ")
		if value indicates we're done:
			finished = True
		else:
			# Transform value to target type if needed
			accumulator = accumulator [operator] value

	# Accumulate from sequence
	accumulator = identity element of type and operator
	i = 0
	while i < len(sequence):
		accumulator = accumulator [operator] sequence[i]
		i += 1
		
	# Count instances from user inputs
	finished = False
	count = 0
	while not finished:
		response = input("Enter input: ")
		if response indicates we are finished:
			finished = True
		elif response matches our target property:
			count += 1
			
	# Count instances from a sequence
	count = 0
	i = 0
	while i < len(sequence):
		if sequence[i] matches our target property:
			count += 1
		i += 1
		
	# Check if a property is true of all elements of a sequence
	always = true
	i = 0
	while always and i < len(sequence):
		if sequence[i] does not match our property:
			always = False
		i += 1
		
	# Count until a condition is met from input
	finished = False
	count = 0
	while not finished:
		response = input("Enter input: ")
		if response indicates we are finished:
			finished = True
		else:
			count += 1

