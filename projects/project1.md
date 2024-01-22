---
layout: work
type: Project
num: 1
worktitle: Civic Assistance System
---

**Due Friday, February 23**
## Description

Many elements of our civic lives are governed by processes and
regulations. While they may be confusing and complicated, these
processes form a common way that we coordinate our interactions,
hopefully for the benefit of all. We can use our computing skills
to help facilitate a clear understanding of these processes.

For this project, you will create a program that interacts with a
user by asking questions. Follow-up questions depend upon the
previous questions asked. The questions and answers should guide
the user towards solving a concrete problem.

The content of the questions and answers should be related to a
citizen interacting with their government in some real-life civic
realm. You can ask the user for strings, integers, or floats. The
program must contain at least **six distinct questions** it can ask.
Every question after the first question might or might not be asked,
depending on the answers to previous questions.

Here is a list of potential interactions you might attempt to
simulate. This is by no means comprehensive and is meant as
inspiration for your program. You may choose one of these, or
one of your own, as long as you provide a citation in your code
to your connected real-world civic interaction.

* [Apply to be a U.S. Citizen](https://www.uscis.gov/citizenship/learners/apply-citizenship)
* [Voter Registration](https://www.usa.gov/register-to-vote)
* [How to Mail a Package](https://pe.usps.com/text/pub52/pub52c2_022.htm)
* [Register and Renew your Vehicle in Arkansas](https://www.dfa.arkansas.gov/motor-vehicle/vehicle-tag-renewal/)
* [Filing Taxes](https://www.irs.gov/pub/irs-pdf/i1040gi.pdf)
* [Permit applications for Conway, AR](http://cityofconway.org/pages/permits-inspections/)
* [Renovations in the Historic District of Gretna, LA](https://www.gretnala.com/wp-content/uploads/2017/10/1503007315_01128.pdf)
* [How to do Business with the U.S. Department of Transportation Pipeline and Hazardous Materials Safety Administration](https://www.phmsa.dot.gov/pipeline/special-permits-state-waivers/special-permits-and-state-waivers-overview)
* [The California Environmental Quality Act](http://resources.ca.gov/ceqa/flowchart/)

### Example

Here are two transcripts from an example system, to give you a sense as to what your program needs to be able to do.

#### Transcript 1
    Welcome to the DMV. Would you like to "register" or "renew" a vehicle?  register
    Has your vehicle been assessed this year?  no
    Please have your vehicle assessed and bring your stamped receipt from the county assessors's office.

#### Transcript 2
    Welcome to the DMV. Would you like to "register" or "renew" a vehicle?  register
    Has your vehicle been assessed this year?  yes
    Have you paid property taxes due for this vehicle?  yes
    What is the odometer reading? (please no commas)  1282
    What is the purchase price of the vehicle? (please no commas)  13234
    You will owe $860.21 in taxes. Will you be using "credit" or "cash"?  cash
    Was this a "new" or "used" purchase?  used
    Did you bring the title for the vehicle?  no
    Please return when you have the title with all signatures from the buyer and seller.

## Conditionals

Throughout the project, you should use conditionals (`if`, `elif`, `else`, as appropriate) to control
the flow. In general, you should ask the user a question and then determine what to do next depending
on their answer. In some cases, their answer will indicate that the program should stop. *However*,
this should be handled directly by the conditionals and the flow, not by resorting to any of
`quit()` or `exit()` or similar. Check with your instructor if you are not sure whether your
have followed this instruction correctly.

## Input/Output

To complete this program, you will need to learn about the `print` function, the `input` function, and type conversion functions.

### Output

The `print(str)` function instructs Python to display a string to the user.

Try it out with the code examples below. Notice how it is displaying
strings, but not with the normal '' around the text.

	print("Hello world!")

	x = 6
	if x > 5:
		print("High")
	else:
		print("Low")

	print("This is")
	print("a lot")
	print("of text")

If we want to print a string that includes information stored in variables, we can use a special type of string called a *format string* or *f-string*. When we preface the string with an *f*,  we can include whatever variables we want inside curly brackets, like so:

	x = 22
	y = 12.9
	print(f"My age is {x + 2} and I drink {y} glasses of water each day.")

### Input

The `input(str)` function instructs Python to show an input box, then wait for the user to type a string and hit <kbd>Enter</kbd>. The `str` parameter will be a prompt to tell the user what they should type. It then returns whatever the user typed as a str.

It will help to have an extra space at the end of your prompt string.

Try it out with the code below.

	name = input("What is your name? ")
	print(f"Hi, {name}!")

	animal = input("What is your favorite animal? ")
	if animal == "lemur":
		print("Mine too!")
	else:
		print(f"That's nice, I guess {animal}s are OK.")


**It is not necessary** to check that the user inputs the correct kind of answer. However, your instructions should make clear what answer(s) are expected. That is,
you should do something like:  "Are you a current Hendrix Student ('y' or 'n')?" It is okay if your code crashes if someone accidentally enters 'yes' -- you do not need to check for this.

### Type Conversion

The `input(str)` function will always return a `str`. Even if you type in a number. This can cause problems, as shown below.

	x = input("Type a number between 1 and 10. ")
	print(x + 3)

We can fix this with conversion functions. `int(str)` will take a `str` as a parameter, and return an `int`.

	x = input("Type a number between 1 and 10. ")
	y = int(x)
	print(y + 3)

Of course, the user could make a mistake and not enter an integer at all. For now, assume you have good users who always enter the correct type. Later, we will see how to fix this error.

If converting the result of a call to `input(str)`, you can usually do the conversion at the same time.

	x = int(input("Type a number between 1 and 10. "))
	if x > 5:
		print(f"{x} is too high.")
	else:
		print(f"{x} is too low.")

### Reflection

Along with your code, you should complete a short reflection on the following questions:
* Why did you choose the system you did?
* What did you learn about the system as a result of completing this assignment?
* How did this experience affect your understanding of the relationship between computing and society?

### Warning

Get started early! Pick an idea and run it by us. We are happy to help you think through the design of your program.

### Grading Criteria

* A **Level 1** project:
  * Follows the above guidelines for user input and output.
  * Asks six distinct questions.
  * No runtime errors for any expected user input.
  * No syntax errors.

* A **Level 2** project:
  * Meets all **Level 1** criteria.
  * Includes the Reflection described above.
  * No Pycharm style warnings -- exception: if your nested `if` statements cause a line to be too long, that is fine.
  * No grammatical or spelling errors.
  * No use of `quit()` or `exit()` -- the program flows and exits organically
  * The flow of the questions -- and response of the program -- makes sense in the context given.
  * Among the six or more questions, at least two distinct types of
    data (`str`, `int`, `float`) are requested. An example of
	meeting this criterion is having five questions that expect
	strings	and one question that expects an integer from the user.
  * For each question, directions to the user are clear as to what
    kind of input they should enter; for example: "Do you want 'y'
	or 'yes' for an affirmative?"
