---
worktitle: Loop Design Patterns
---

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
* `str`
  * `+`: `''` or `""`
* `List`
  * `.append()`: `[]`
  
  
## Mathematical Calculation
	
	result = appropriate starting value
	while the calculation is not complete:
		update result by one step
  
  
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

	always = True
	while always and condition:
		if not property:
			always = False
			
## Check if a property is ever true

	ever = False
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
			
## Examples

	# Count instances from user inputs
	def count_short_words() -> int:
		count = 0
		finished = False
		while not finished:
			word = input("Enter a word: ")
			if len(word) == 0:
				finished = True
			elif len(word) <= 4:
				count += 1
				print(f"{word} is short!")
			else:
				print(f"{word} is long.")
		return count
		
	# Accumulate from sequence
	def reverse(s: str) -> str:
		opposite = '' 
		i = 0
		while i < len(s):
			opposite = s[i] + opposite
			i += 1
		return opposite
		
	# Accumulate from sequence
	def smallest_letter(s: str) -> str:
		smallest = s[0]
		i = 1
		while i < len(s):
			if s[i] < smallest:
				smallest = s[i]
			i += 1
		return smallest	

	# Computation
	# Count until a condition is met
	def logarithm(n: int, base: int) -> int:
		count = 0
		while n > 1:
			n //= base
			count += 1
		return count
		
	# Computation
	def power(base: int, exponent: int) -> int:
		product = 1
		while exponent > 0:
			product *= base
			exponent -= 1
		return product	
		
	# Traverse a sequence
	def prefixes(s: str):
		i = 0
		while i < len(s):
			print(s[:i+1])
			i += 1
			
	# Traverse a sequence
	def in_betweens(s: str, length: int):
		i = 0
		while i < len(s) - 1:
			print(s[i : i + length])
			i += 1
			
	# Filter a sequence
	def vowels_only(s: str) -> str:
		vowels = ''
		i = 0
		while i < len(s):
			if s[i] in 'aeiou':
				vowels += s[i]
			i += 1
		return vowels
		
	# Count instances from a sequence
	def vowel_count(s: str) -> int:
		count = 0
		i = 0
		while i < len(s):
			if s[i] in 'aeiou':
				count += 1
			i += 1
		return count
		
	# Filter a sequence
	def unique_items(items_sold: List[str]) -> List[str]:
		i = 0
		unique = []
		while i < len(items_sold):
			if items_sold[i] not in unique:
				unique.append(items_sold[i])
			i += 1
		return unique
		
	# Check if a property is true of some elements of a sequence
	def has_vowels(s: str) -> bool:
		ever = False
		i = 0
		while not ever and i < len(s):
			if s[i] in 'aeiou':
				ever = True
			i += 1
		return ever

	# Check if a property is true of all elements of a sequence
	def only_vowels(s: str) -> bool:
		always = True
		i = 0
		while always and i < len(s):
			if s[i] not in 'aeiou':
				always = False
			i += 1
		return always
