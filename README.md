# Drag-Polar Plot Generator
Generate drag-polar plots via XFOIL.

# Setup
1. Install Python at https://www.python.org/downloads/.
2. Download repository.
3. Open Terminal in repository folder.
4. Enter `pip install matplotlib`.
5. Enter `python main.py`.

# Usage
Run *main.py* via `python main.py` in Terminal.
`Airfoil:` will print.
Enter the particular airfoil on which to generate the drag-polar plot.
A tool to search airfoils is found here: http://airfoiltools.com/search/index.

After this, `Panels:` will print.
Enter the number of panels (integer) to place on the airfoil.
This input is equivalent to "PPAR"'s "N" command in XFOIL.
Then, `Iterations:` will print.
Enter the number of iterations (integer) to interpolate through when convergence fails.
Next, `Reynold's Number:` will print.
Enter the Reynold's number, found via multiplication of the fluid kinematic viscosity, the fluid flow velocity, and the characteristic length over which the fluid flows.
These inputs are equivalent to "OPER"'s "ITER" and "VISC" commands.

The next set of inputs are angle of attack parameters.
First, `Initial Angle of Attack:` will print.
Enter the angle of attack (degrees) to first simulate the drag coefficient and the lift coefficient.
Then, `Final Angle of Attack:` will print.
Enter the angle of attack (degrees) at which to end data generation.
Lastly, `Increment Angle of Attack:` will print.
Enter the angle of attack (degrees) step-size between the initial and final angles.
This input is equivalent to "PACC"'s "Aseq" command in XFOIL.

# Example
Entering the following inputs: `NACA0015` for `Airfoil:`, `160` for `Panels:`, `100` for `Iterations:`, `1e6` for `Reynold's Number:`, `0` for `Initial Angle of Attack:`, `90` for `Final Angle of Attack:`, and `1` for `Increment Angle of Attack:` results in *polar.dat*, *Figure_0.png*, and *Figure_1.png*.
*polar.dat* is XFOIL's simulated raw data.
*Figure_0.png* is a plot that displays the coefficient of lift and the coefficient of drag plotted against the angle of attack.
*Figure_1.png* is the drag-polar plot.
These figures are located in the repository.

# Errors
All errors are due to the user inputting incorrect values or XFOIL iterative failing.
To rectify your error, verify you are entering the correct values for each parameter or try entering different parameter values.

# Contact
For help, improvements, etc., feel free to contact **silveryystar** on Discord.
