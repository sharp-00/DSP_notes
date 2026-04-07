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

**10-03-26**

## Matplotlib
    - figure
    - plots
    - axes
        - relative plot positions in figure
        - left margin, right margin, width, height eg. --> ax_cmp = fig.add_axes([0.3, 0.35, 0.5, 0.5])
    - twin axes


# rainfall
    - 8X8 plot 
        - heatmap in the middle, right to it, the average rainfall, colorbar on left, and at the bottom --
    - pcolormesh
    -         

**11-03-26**

## Visual Hierarchy

    - various factors guide the viewers eye 
            -size, location, color
                    -eg.--> tree in a FOREST and TREE in a forest 

# VH in matplotlib 
    - some parameters: 
        - linestyle(ls), linewidth(lw)
        - opacity(alpha)
        - different colors (in accordance with Gestalt principles) eg.--> red(important), grey(not important)
        - zorder (layers--> above and below, similar to layers in photoshop?)
        - Location (top-left and center)
 

## **24-3-26**

## Performance Evaluation and Improvement - Computational Complexity

# Computational Problem
        Input --> Information provided to the problem solver.
        Output --> The solution that satisfies to the problem's requirements.
    Output is the solution to the problem, it is what the problem solver needs to do to solve the problem.

# Data Structure
    A systematic way of --
    organising(access), managing, storing data

# Algorithm
    A finite sequence of computational steps that takes an input and produces output in execution of steps in finite time.

    Main Characterstics
    - Finite sequence of steps
    - Unambiguous comoputational steps
    - Execution stops after finite time in desired output

    # **Aspects of Algorithm**
        - Design
        - Correctness (Verification) --> as long as input is correct, the algorithm should always give correct answer
        - Efficiency (**This is what we will be doing**)
            - Time (Operations, I/O - Multiple levels) --> time spend on operation, fetching data from machine/disk/cloud (I/O)
                        time takes to fetch --> machine<disk<<cloud
        - Communication (size and number of messages, Initial delay
        - Space complexity
        
    Algorithm efficiency challenges
        - Input space is very large in most cases, while testing we use finite sized samples from the space
        - Computer speeds have been changing (different computers with different speeds)
        - Variation in programming language and even Operating System
        - Variation in transaltion from high level language to machine language
        - resource sharing on a computer may affect execution time (many processes(application) running at the same time)

    How do we solve these?
        - Fix model of computation --???
        - Fix basic set of instructions
        - Complexity (efficiency) as a function of the size of input
                    f(n) number of basic steps for input size = n



    Find minimum  value, (have to look, not enough in slides)

        if for loop takes n times
        then while loop will take n + 1 times
        for  i = 0 to n-1
                --> n times
        while i <= n-1
                --> n+1 times (it will fail at the last one)



**25-03-26**

Time Complexiity: A * n + B  where n=j-i+1
    Idea -->  Consider leading term, ignore constants
    Is it okay to use only the leading term?
    Suppose we have two algorithm
    Algorithm A  Time complexity-> n * logn
    Algotirtm B  Time complexity --> n^2  

    c(nlogn)   and   c`(n^2)

    now give benefit to algo B
    big constant for algo A and small for algoB
    c = 100 and c`=1

It is not always true that one algorithm is better than the other, we can always find a value n_0 where the other algorithm is better

## Asymptotic Complexity
        Upper Bound (O) - Big-O
            -> f(n)=O(g(n))    --->    0<=f(n)<=c* g(n)
    O is the set       
    here = does not mean equals to, it means f(n) is a member of O(g(n))
            eg,--> 20n = O(n^2)
            This is for algorithm, need no more effort than O(maximum)
        Lower Bound - big omega
            --> This is for problem, not for algorithm, minimum effort required to solve the problem        

        Tight Bound(theta(0))
    
        





**30-03-26**

    Bashscripts
        ls -lt for recently modified file and ls -lt | head -n 2 to print only that         
        head can print the top 10 lines, can change the NUM using head -5    
    - ls | wc -l  to print the number of files in a directory
    - ls -l | tail +2 | wc -l
    
    - how many unique customers in online-retail.csv
        - how many lines? --> wc -l <filename> or cat <filename> | wc -l

    - cut -d ',' -f8 <filename> |tail -n +2 | sort | uniq -u | wc -l

    - cut -d ',' -f1 <filename> |tail -n +2 | sort |uniq| wc -l

    - cat filename | grep -c 'whatever you want to search' (-c is for count)

    - to append >>






**NEED NOTES**









 





**07-04-2026**

### Performance Analysis

  #  basic timing
        
        - ex_time.py

        - ex_profile.py
                - run --> the columns by the library cProfile --> ncalls, tottime, percall, cumtime(-_~), percall(for cumtime), filename


 ## Sorting Algorithms
    
  # Quick Sort

    - 
