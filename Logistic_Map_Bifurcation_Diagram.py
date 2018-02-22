import matplotlib as plt

# Perturbation
eps = 0.01
# u is dependant variable
u = 0.0
# Perturbation in u
u = u + eps

# Plot r on x-axis
# Different values of r result in widely different behaviour
# As nonlinear dynamics, r represents combined rate for reproduction and starvation
r = 0.0
dr = 0.005

# Store x values in r_list
# Store y values in u_list
r_list = []
u_list = []

# Values of interest for parameter r are those in  interval [0,4]
while r < 4.0:
    # Disregard first 200 iterations to converge to equilibria
    for i in range(1,200):
        u = r*u*(1.0 - u)
    for i in range(1,500):
        u = r*u*(1.0 - u)
        r_list.append(r)
        u_list.append(u)
    r = r + dr
    u = u + eps

# Plot bifurcation diagram output
# This displays representation of connection between chaos and fractals
plt.pyplot.scatter(r_list, u_list, s=1, facecolor='0.1', lw = 0)
plt.pyplot.axis([1.0,4.0,0,1.0])
plt.pyplot.show()
