import numpy as np
import matplotlib.pyplot as plt



def get_function_value(x1,x2):
    term1 = (x1**2+x2-11)**2 
    term2 = (x1+x2**2-7)**2
    f = term1 + term2
    return f

def initialize_positions(number_of_particles,n_dimensions,x_min,x_max,r):
    initial_particle_position = []
    for _ in range(number_of_particles):
        row=[]
        for _ in range(n_dimensions):
            r = np.random.rand()
            x = x_min + r*(x_max - x_min)
            row.append(x)
        initial_particle_position.append(row)
    return np.array(initial_particle_position)

def initialize_velocities(number_of_particles,n_dimensions,alpha,delta_t,x_min,x_max,V_max,r):
    initial_velocities = []
    for _ in range(number_of_particles):
        row=[]
        for _ in range(n_dimensions):
            r = np.random.rand()
            v = alpha/delta_t * (-(x_max-x_min)/2 + r*(x_max-x_min))
            row.append(v)
    initial_velocities.append(row)
    return np.clip(initial_velocities,-V_max,V_max)

# def evaluate_particle_swarm(particle_positions):
    number_of_particles = len(particle_positions)
    function_values = []
    swarm_best = particle_positions[0]
    particle_best = particle_positions

    for i in (range(number_of_particles)):
        
        function_value = get_function_value(particle_positions[0],particle_positions[1])
        function_values.append(function_value)
        if function_value > get_function_value(particle_best[0],particle_best[1]):
            particle_best[i] = particle_positions
        if function_value > get_function_value(swarm_best[0],swarm_best[1]):
            swarm_best[0] = particle_positions[0]
            swarm_best[1] = particle_positions[1]
    return np.array(swarm_best),np.array(particle_best)

def update_velocities(particle_positions, particle_velocities,
                       c1, c2, particle_best, swarm_best
                       , delta_t, w, V_max, q, r):

    swarm_best = [swarm_best for _ in range(len(particle_positions))]

    term1 = c1*r*((particle_best-particle_positions) / delta_t)
    term2 = c2*q*((swarm_best-particle_positions) / delta_t)

    particle_velocities = w*particle_velocities + term1 + term2
    return np.clip(particle_velocities,-V_max,V_max)

def update_positions(particle_positions,particle_velocities,delta_t):
    particle_positions += particle_velocities*delta_t
    return particle_positions


def plot_particles(plt, city_locations, color):
  x = []
  y = []
  for city_index in range(len(city_locations)):
    x.append(city_locations[city_index][0])
    y.append(city_locations[city_index][1])
  plt.scatter(x,y,color=color)

#############################################
# MAIN
############################################

number_of_particles = 40
n_dimensions = 2
x_min = -5
x_max = 5
delta_t = 1
c1 = 2
c2 = 2
alpha = 1
w = 1.4
beta = 0.9
v_max = 2
q = np.random.rand(number_of_particles,n_dimensions)
r = np.random.rand(number_of_particles,n_dimensions)

particle_positions = initialize_positions(number_of_particles,n_dimensions,x_min,x_max,r)
velocities = initialize_velocities(number_of_particles, n_dimensions, alpha, delta_t, x_min, x_max, v_max, r)

swarm_best = [np.random.randn(),np.random.rand()]
particle_best = particle_positions.copy()
best_x = []
best_fitness = []
for iteration in range(100):

    number_of_particles = len(particle_positions)
    function_values = []

    for particle, i in zip(particle_positions, range(number_of_particles)):
        function_value = get_function_value(particle[0],particle[1])
        function_values.append(function_value)
        if function_value < get_function_value(particle_best[i][0],particle_best[i][1]):
            particle_best[i] = particle
        if function_value < get_function_value(swarm_best[0],swarm_best[1]):
            swarm_best[0] = particle[0]
            swarm_best[1] = particle[1]
    
    min_func = min(function_values)
    best_fitness.append(min_func)
    i = best_fitness.index(min_func)
    best_x.append(swarm_best)
    if w > 0.4:
        w *= beta
    velocities = update_velocities(particle_positions, velocities,
                                    c1, c2, particle_best ,swarm_best ,
                                    delta_t, w, v_max, q, r) 
    particle_positions = update_positions(particle_positions,velocities,delta_t) 

    plt.cla()
    N = 100
    x1 = np.linspace(-5,5,N)
    x2 = np.linspace(-5,5,N)
    X1, X2 = np.meshgrid(x1,x2)

    Z = get_function_value(X1,X2)

    plt.contour(X1,X2,Z,[-1,1,10,20,30], extend='both')

    
    plot_particles(plt, particle_positions, 'red')
    plt.scatter(swarm_best[0],swarm_best[1],color='blue')
    plt.pause(0.1)
    plt.show()

    plt.ion()

    print(f"Iteration {iteration+1}/{100}, Best Position = {swarm_best},Best Fitness = {get_function_value(swarm_best[0],swarm_best[1])}")

mini_func = min(best_fitness)
best_fitness.append(mini_func)
i = best_fitness.index(mini_func)
sb = best_x[i]
print(f"Best overall position: {sb}, and best overall fitness: {mini_func}")


# Implementation of matplotlib function
# N = 100
# x1 = np.linspace(-5,5,N)
# x2 = np.linspace(-5,5,N)
# X1, X2 = np.meshgrid(x1,x2)

# Z = get_function_value(X1,X2)

# plt.contour(Z,[-1,1,10,20,30], extend='both')
# plt.title('matplotlib.pyplot.contourf() Example')
# plt.show()

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# fig = plt.figure(figsize=(10, 8))
# ax = plt.axes(projection='3d')
# ax.plot_surface(X1, X2, Z, cmap='cool', alpha=0.8)

# ax.set_title('3D Line Plot')
# plt.show()



