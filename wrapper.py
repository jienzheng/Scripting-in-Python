import subprocess

# Specify the full path to the MATLAB executable
# Adjust the path accordingly
matlab_executable = "/Applications/MATLAB_R2023b.app/bin/matlab"

# Set up MATLAB environment
matlab_process = subprocess.run([matlab_executable, "-batch", "run('task4.m');"], capture_output=True)

# Read values from 'data.txt'
with open('input.txt', 'r') as file:
 line = file.readline()
 input_array = [int(value) for value in line.split()]

# Converts the input_array from integer to string from map
# Using list() to return a list of strings
input_array = list(map(str, input_array))

# Compile the C program (assuming it's saved as task1.c)
subprocess.run(["gcc", "task1.c", "-o", "task1"])

# Run the compiled C program with the input array as arguments
process = subprocess.run(["./task1"] + input_array, capture_output=True, text=True)

# Store the output of the C program in a Python variable
output_variable = process.stdout.strip()

# Save the output_variable to a file
with open('c_output.txt', 'w') as f:
 f.write(output_variable)

### START OF HASKELL CODE ###
### START OF HASKELL CODE ###
### START OF HASKELL CODE ###

# Runs the Haskell code
subprocess.run(['ghc', 'task2.hs'])

# Opens a new textfile for Haskell program results
with open('haskell_output.txt', 'w') as f:
        f.write('')

# Run the compiled Haskell program with the input array as arguments
process = subprocess.run(["./task2"] + input_array, capture_output=True, text=True)

# Store the output of the Haskell program in a Python variable
output_variable = process.stdout.strip()

# Save the output_variable to a file
with open('haskell_output.txt', 'a') as f:
        f.write(output_variable)

### START OF PROLOG CODE ###
### START OF PROLOG CODE ###
### START OF PROLOG CODE ###

# Append “” to a an element in list
input_quotes = []
for i in input_array:
### https://stackoverflow.com/a/58957893 ###
    input_quotes.append(f"\"{i.rstrip()}\"")

# Opens a new textfile for Prolog program results
with open('prolog_output.txt', 'w') as f:
        f.write('')

# Makes all elements in list to be a string
prolog_input = "[" + ",".join(map(str, input_quotes)) + "]."

# Runs the prolog program
prolog = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'task3.pl'], input=prolog_input, capture_output=True, text=True)

# Gets the results from prolog program
plresult = prolog.stdout.strip()

# Replaces all “,” and “[” and “]” with “ ”
temp = plresult.replace("]", "")
no_bracket = temp.replace("[", "")
prolog_output = no_bracket.replace(",", " ")

# Saves output into the prolog textfile
with open('prolog_output.txt', 'a') as f:
    f.write(' ')
    f.write(prolog_output)

# Runs Matlab code to display all pictures of Mickey Mouse
matlab_process = subprocess.run([matlab_executable, "-batch", "run('task5.m'); pause(10);"], capture_output=True)

