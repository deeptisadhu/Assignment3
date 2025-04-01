# Assignment3
Task 1
Factorial Calculator Python Program

This program defines a function named factorial that calculates the factorial of a given non-negative integer. The factorial is computed using a loop, though you could also implement it with recursion. The program demonstrates the functionality by calling the function with a sample number and printing the result.

Table of Contents

Overview
Files
Requirements
Usage
Code Explanation
License
Author
Overview

The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. By definition, the factorial of 0 is 1.

This program includes:

A factorial function that calculates the factorial using a loop.
A demonstration call to factorial with a sample number.
Output of the calculated factorial printed to the console.
Files

factorial.py: The main Python script that contains the implementation of the factorial function and the demonstration code.
Requirements

Python 3.x: Ensure you have Python installed on your machine. You can download it from python.org.
Usage

Clone or Download the project to your local machine.
Open a Terminal (or Command Prompt) in the project directory.
Run the Program using the following command:
python factorial.py
View the Output in your terminal. It will display the factorial of the sample number provided in the script.
Code Explanation

factorial Function
Purpose: Calculate the factorial of a non-negative integer.
Input: A non-negative integer n.
Output: The factorial of n.
Implementation:
Loop Approach: Initialize a variable result to 1, and then iterate from 1 to n, multiplying the result by each number.
Base Case: The factorial of 0 is defined as 1.
Sample Usage
The script calls the factorial function with a sample number (e.g., 5) and prints the result. For example:

Calling factorial(5) computes 5 * 4 * 3 * 2 * 1, which equals 120.
Example Code

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using a loop.
    
    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.
    
    Returns:
    int: The factorial of n.
    """
    # Base case: 0! is defined as 1
    if n == 0:
        return 1

    result = 1
    # Calculate factorial using a loop from 1 to n
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    # Sample number to demonstrate the factorial function
    sample_number = 5
    result = factorial(sample_number)
    print(f"Factorial of {sample_number} is {result}")
License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

Task 2
Python Math Operations Program

Description

This Python program prompts the user to enter a number and then performs the following mathematical calculations using the math module:

Computes the square root of the number.

Calculates the natural logarithm (ln) of the number.

Finds the sine of the number (in radians).

The results are then displayed to the user.

Requirements

Python 3.x

Dependencies

This program requires the built-in Python math module, which is included with Python installations by default.

Usage

Run the script using a Python interpreter.

Enter a numerical value when prompted.

The program will compute and display the results.

Example Execution

Enter a number: 10
Square root: 3.1622776601683795
Natural Logarithm: 2.302585092994046
Sine: -0.5440211108893698

Error Handling

The program ensures that the natural logarithm function only operates on positive numbers.

If an invalid input (e.g., a non-numeric value) is provided, the program will handle it gracefully and prompt the user again.


