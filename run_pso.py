import numpy as np


def get_function_value(x1,x2):
    term1 = (x1**2+x2-11)**2 + (x1+x2**2-7)
    term2 = (x1+x2**2-7)**2
    f = term1 + term2
    return f

def initialize_positions(number_of_particles,n,x_min,x_max):
    initial_particle_position = []
    for _ in range(number_of_particles):
        row=[]
        for _ in range(n):
            r = np.random.rand()
            x = x_min + r*(x_max - x_min)
            row.append(x)
        initial_particle_position.append(row)
    return np.array(initial_particle_position)

def initialize_velocities(number_of_particles,n,alpha,delta_t,x_min,x_max):
    initial_velocities = []
    for _ in range(number_of_particles):
        row=[]
        for _ in range(n):
            r = np.random.rand()
            v = alpha/delta_t * (-(x_max-x_min)/2 + r*(x_max-x_min))
            row.append(v)
    initial_velocities.append(row)
    return np.array(initial_velocities)

def evaluate_particle_swarm(partical_positions):
    number_of_particles = len(partical_positions)
    function_values = []
    x_sb = []
    x_pb = [[] for _ in range(number_of_particles) ]
    for particle_position, i in zip(partical_positions,range(number_of_particles)):
        function_value = get_function_value(particle_position[0],particle_position[1])
        function_values.append(function_value)
        if function_value > get_function_value(x_pb[i][0],x_pb[i][1]):
            x_pb[i] = particle_position
        if function_value > get_function_value(x_sb[i][0],x_sb[i][1]):
            x_sb[0] = particle_position[0]
            x_sb[1] = particle_position[1]
    return np.array(x_sb),np.array(x_pb)

def update_velocities(particle_positions,particle_velocities,c1,c2,x_pb,x_sb,delta_t,w):
    q = np.random.rand()
    r = np.random.rand()

    term1 = c1*q*((x_pb-particle_positions) / delta_t)
    term2 = c2*r*((x_sb-particle_positions) / delta_t)

    particle_velocities = w*particle_velocities + term1 + term2
    
    return particle_velocities

def update_positions(particle_positions,particle_velocities,delta_t):
    particle_positions += particle_velocities*delta_t
    return particle_positions




while ():
  path_collection = []
  path_length_collection = []
  for ant_index in range(number_of_ants):  
    # Generate paths:
    path = generate_path(pheromone_levels, visibility, alpha, beta) # Uncomment after writing the function
    path_length = get_path_length(path, city_locations) # Uncomment after writing the function
    if (path_length < minimum_path_length):
      minimum_path_length = path_length
      print(minimum_path_length)
      # To do: Add code for plotting here

      # print(delta_pheromone_levels)
      # print(pheromone_levels)
    path_collection.append(path)
    path_length_collection.append(path_length)

  # Update pheromone levels:
  delta_pheromone_levels = compute_delta_pheromone_levels(path_collection,path_length_collection) # Uncomment after writing the function
  pheromone_levels = update_pheromone_levels(pheromone_levels, delta_pheromone_levels, rho) #

def plot():
    pass
        

X = initialize_positions(4,2,-5,5)

print(X)