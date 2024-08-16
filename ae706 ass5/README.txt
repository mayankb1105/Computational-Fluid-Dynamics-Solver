README for Stream Function Solver
This Python program calculates the stream function and velocity field for a specific two-dimensional flow using a finite difference method. The stream function satisfies the Laplace equation which is solved using an iterative numerical approach, specifically the Point Gauss Seidel Method.

Prerequisites
To run this code, ensure you have the following dependencies installed:

Python (recommended version 3.8 or above)
NumPy (for numerical operations)
Matplotlib (for plotting graphs and visualizations)

Files in the Repository
210010039.py: The main Python script containing the setup of the grid, initialization of parameters, and iterative solver for the stream function.
main3.py: The Python script containing the calculate function which performs the SOR iteration.

Usage
Ensure both main.py and main3.py are in the same directory.
Run main.py using a Python interpreter

This will execute the program, which performs the following:
Sets up a grid of points representing the spatial domain.
Initializes the stream function values at the boundaries.
Iteratively solves for the stream function over the domain using the calculate function defined in main3.py.
Calculates the x and y components of the velocity from the stream function.
Plots the results for the stream function and velocity components.

Output
The output includes several plots:

Contour map of the stream function.
Contour map of the x and y components of velocity.
Contour map of the total velocity magnitude.
Variation of the stream function along specific vertical lines.
Variation of velocity components along specific vertical lines.
Logarithm of the error versus iteration number plot to show convergence.
