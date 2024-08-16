Introduction
This Python script is designed to numerically solve a one-dimensional heat conduction problem using two different methods: the Forward-Time Central-Space (FTCS) method and the Crank-Nicolson method. Additionally, an exact solution is computed for comparison purposes. The heat conduction problem involves a one-dimensional rod with specified initial conditions and boundary conditions, and the temperature distribution along the rod is calculated over time.

Requirements
To run this script, you need to have the following installed:

Python (version 3.x)
NumPy
Matplotlib

Initial Setup:
1. Ensure that all required packages are installed in your Python environment.
2. Save the provided Python script with the name 210010039.py.
3. Make sure the script is in the same directory as the files FTCS_main.py, CN_main.py, and Exact.py, which contain the implementations of the FTCS method, Crank-Nicolson method, and exact solution computation, respectively.

Running the Script:
1. Open the Python script 210010039.py in your preferred Python environment or IDE.
2. Run the script.

Output:
The script will generate several plots illustrating the temperature distribution along the rod at different time intervals.
The plot also conatins a plot for unstable solution using FTCS wherein the time step used is 90 seconds which exceeds the stability threshold
It will also display plots showing the percentage error between the numerical solutions (FTCS and Crank-Nicolson) and the exact solution at different time intervals.

Notes:
The script uses specific values for constants such as thermal diffusivity (alpha), spatial step size (delta_x), and time step size (delta_t). These values can be adjusted according to the specific requirements of the problem.
It's essential to choose appropriate time step sizes to ensure stable and accurate numerical solutions. A time step size less than 78.9 seconds is recommended for stable results.
The provided scripts (FTCS_main.py, CN_main.py, and Exact.py) contain the implementations of the numerical methods and exact solution computation. Users can modify these files to customize the numerical methods or extend them for different problems.