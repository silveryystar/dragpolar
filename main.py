import os
import subprocess
import re
import matplotlib.pyplot as plt

if os.path.isfile("polar.dat") is True:
    os.remove("polar.dat")

airfoil = str(input("Airfoil: "))  # NACA0015

panels = int(input("Panels: "))  # 160
iterations = int(input("Iterations: "))  # 100
reynolds_number = float(input("Reynold's Number: "))  # 1e6

start_aoa = float(input("Initial Angle of Attack: "))  # 0
end_aoa = float(input("Final Angle of Attack: "))  # 90
increment_aoa = float(input("Increment Angle of Attack: "))  # 1

commands = [airfoil, "PPAR", f"N {panels}", "\r\n", "OPER", f"ITER {iterations}", f"VISC {reynolds_number}", "PACC",
            "polar.dat", "", f"Aseq {start_aoa} {end_aoa} {increment_aoa}", "\r\n", "QUIT"]
commands = '\n'.join(commands)

process = subprocess.Popen(['xfoil'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           text=True)
process.communicate(commands)

with open("polar.dat") as f:
    lines = f.readlines()

i = lines.index("  ------ -------- --------- --------- -------- -------- --------\n")

data = lines[i+1:]
data = [i.replace("\n", "") for i in data]
data = [re.sub(" +", ",", i) for i in data]
data = [i[1:] for i in data]
data = [list(map(float, i.split(','))) for i in data]

columns = list(zip(*data))
aoa, cl, cd, *_ = columns


# Figure 1
plt.scatter(aoa, cd, color="blue")
plt.scatter(aoa, cl, color="orange")

plt.plot(aoa, cd, color="blue", label="Drag Coefficient")
plt.plot(aoa, cl, color="orange", label="Lift Coefficient")

plt.title(f"{airfoil} Drag & Lift Coefficients versus Angle of Attack")
plt.xlabel("Angle of Attack (degrees)")
plt.ylabel("Drag & Lift Coefficient")

plt.legend()
plt.tight_layout()
plt.show()


# Figure 2
plt.scatter(cd, cl, c=aoa, cmap="rainbow")

plt.plot(cd, cl, color="black")

plt.colorbar(orientation="vertical", label="Angle of Attack (degrees)")

plt.title(f"{airfoil} Drag-Polar Plot")
plt.xlabel("Drag Coefficient")
plt.ylabel("Lift Coefficient")

plt.tight_layout()
plt.show()
