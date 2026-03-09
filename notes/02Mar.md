### Errors and Exceptions

- Syntax Errors : detected before execution
		raised by the interprator
		
- Runtime errors(exceptions) : occur during execution

egs :	
	ZeroDivisionError
	TypeError
	KeyError

	Syntax	
		try:
			x = int(input())
			print(10/x)
		except ZeroDivisionError:
			print("Division by zero!")
		except ValueError:
			print("Inva;id input")

	files in class folder
		1_basic.py
		1_el_fi.py
			try, except, else, finally
try, except, finally	
	finally will always be executed if present
	Statements execute sequentially
	if an exception occurs:
	CHECK SLIDES

	Why use finally?

Raising Exceptions:
		eg: 3_withdraw.py
			check super()

## pytest

	eg. - test_library.py and library.py		
		--Homework --> triangle.py


---SKIPPED CLASS


**09-03-26**

## **Data Visualization**

# Why is it important??
    - helps in informing decisions
    - easy to see patterns in data not visible in textual/tabular format
        - collapse a third dimension using colors, sizes, etc.
    - form hypotheses about the data (trends, cycles, etc.)

# Where can it go wrong?
    - when axis limits are inconsistent with intent
        - eg. -> absolute and percantage change, height difference etc.
    - if axis and data series labels are inconsistent / wrong / missing
    - if "size" of markers on plot are not defined prop to volume
    - if plot elements are inconsistent with the Gestalt Principles
                #Gestalt Principle
                            - Gestalt principles explain how the human mind organizes visual information and stimuli into patterns. 
                            - Grouping individual elements into a unified whole helps us digest what we see more easily.
    - colormaps (sequential / divergent) should be consistent with data range
    - color(map) choice is incompatible with forms of color blindness
        - check for different types of color blindness
        - make perceptually uniform sequential colormap --> even in greyscale you can see the gradient
        - AVOID RAINBOW COLORMAP
    - if line plots are not justified (i.e. underlying data is not continuous)
        - eg. temperature - continuous, can use line plots
    
