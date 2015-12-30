#m.space Standard imports
import copy
import itertools

# Scientific computing imports
import numpy
import matplotlib.pyplot as plt
import networkx
import pandas
import seaborn

class Person(object):
    """
    Person class, which encapsulates the entire behavior of a person.
    """
    
    def __init__(self, model, person_id, is_infected=False, condom_budget=1.0, prob_hookup=0.5):
        """
        Constructor for Person class.  By default,
          * not infected
          * will always buy condoms
          * will hookup 50% of the time
          
        Note that we must "link" the Person to their "parent" Model object.
        """
        # Set model link and ID
        self.model = model
        self.person_id = person_id
        
        # Set Person parameters.
        self.is_infected = is_infected
        self.condom_budget = condom_budget
        self.prob_hookup = prob_hookup
        
    def decide_condom(self):
        """
        Decide if we will use a condom.
        """
        if self.condom_budget >= (self.model.condom_cost - self.model.condom_subsidy):
            return True
        else:
            return False
    
    def decide_hookup(self):
        """
        Decide if we want to hookup with a potential partner.
        """
        if numpy.random.random() <= self.prob_hookup:
            return True
        else:
            return False
    
    def get_position(self):
        """
        Return position, calling through model.
        """
        return self.model.get_person_position(self.person_id)
    
    def get_neighbors(self):
        """
        Return neighbors, calling through model.
        """
        return self.model.get_person_neighbors(self.person_id)

    def __repr__(self):
        '''
        Return string representation.
        '''
        skip_none = True
        repr_string = type(self).__name__ + " ["
        except_list = "model"

        elements = [e for e in dir(self) if str(e) not in except_list]
        for e in elements:
            # Make sure we only display "public" fields; skip anything private (_*), that is a method/function, or that is a module.
            if not e.startswith("_") and eval('type(self.{0}).__name__'.format(e)) not in ['DataFrame', 'function', 'method', 'builtin_function_or_method', 'module', 'instancemethod']:
                    value = eval("self." + e)
                    if value != None and skip_none == True:
                        repr_string += "{0}={1}, ".format(e, value)

        # Clean up trailing space and comma.
        return repr_string.strip(" ").strip(",") + "]"


class Model(object):
    """
    Model class, which encapsulates the entire behavior of a single "run" in our HIV ABM.
    """
    
    def __init__(self, grid_size, num_people, min_subsidy=0.0, max_subsidy=1.0,
                     min_condom_budget=0.0, max_condom_budget=2.0,
                     condom_cost=1.0, min_prob_hookup=0.0, max_prob_hookup=1.0,
                    prob_transmit=0.9, prob_transmit_condom=0.1):
        """
        Class constructor.
        """
        # Set our model parameters; this is long but simple!
        self.grid_size = grid_size
        self.num_people =  num_people
        self.min_subsidy = min_subsidy
        self.max_subsidy = max_subsidy
        self.min_condom_budget = min_condom_budget
        self.max_condom_budget = max_condom_budget
        self.condom_cost = condom_cost
        self.min_prob_hookup = min_prob_hookup
        self.max_prob_hookup = max_prob_hookup
        self.prob_transmit = prob_transmit
        self.prob_transmit_condom = prob_transmit_condom
        
        # Set our state variables
        self.t = 0
        self.space = numpy.array((0,0))
        self.condom_subsidy = 0.0
        self.people = []
        self.num_interactions = 0
        self.num_interactions_condoms = 0
        self.num_infected = 0
        
        # Setup our history variables.
        self.history_space = []
        self.history_space_infected = []
        self.history_interactions = []
        self.history_num_infected = []
        self.history_num_interactions = []
        self.history_num_interactions_condoms = []
        
        # Call our setup methods to initialize space, people, and institution.
        self.setup_space()
        self.setup_people()
        self.setup_institution()
        
    def setup_space(self):
        """
        Method to setup our space.
        """
        # Initialize a space with a NaN's
        self.space = numpy.full((self.grid_size, self.grid_size), numpy.nan)
    
    def setup_people(self):
        """
        Method to setup our space.
        """
        
        # First, begin by creating all agents without placing them.
        for i in xrange(self.num_people):
            self.people.append(Person(model=self,
                                      person_id=i,
                                      is_infected=False,
                                      condom_budget=numpy.random.uniform(self.min_condom_budget, self.max_condom_budget),
                                      prob_hookup=numpy.random.uniform(self.min_prob_hookup, self.max_prob_hookup)))
        
        # Second, once created, place them into the space.
        for person in self.people:
            # Loop until unique
            is_occupied = True
            while is_occupied:
                # Sample location
                random_x = numpy.random.randint(0, self.grid_size)
                random_y = numpy.random.randint(0, self.grid_size)
                
                # Check if unique
                if numpy.isnan(self.space[random_x, random_y]):
                    is_occupied = False
                else:
                    is_occupied = True
            
            # Now place the person there by setting their ID.
            self.space[random_x, random_y] = person.person_id
            
        # Third, pick one person to be infected initially.
        random_infected = numpy.random.choice(range(self.num_people))
        self.people[random_infected].is_infected = True
        self.num_infected += 1

    def setup_institution(self):
        """
        Method to setup our space.
        """
        # Randomly sample a subsidy level
        self.condom_subsidy = numpy.random.uniform(self.min_subsidy, self.max_subsidy)
    
    def get_neighborhood(self, x, y, distance=1):
        """
        Get a Moore neighborhood of distance from (x, y).
        """
        neighbor_pos = [ ( x % self.grid_size, y % self.grid_size)
                                for x, y in itertools.product(xrange(x-distance, x+distance+1),
                                xrange(y-distance, y+distance+1))]
        return neighbor_pos
    
    def get_neighbors(self, x, y, distance=1):
        """
        Get any neighboring persons within distance from (x, y).
        """
        neighbor_pos = self.get_neighborhood(x, y, distance)
        neighbor_list = []
        for pos in neighbor_pos:
            # Skip identity
            if pos[0] == x and pos[1] == y:
                continue
                
            # Check if empty
            if not numpy.isnan(self.space[pos[0], pos[1]]):
                neighbor_list.append(int(self.space[pos[0], pos[1]]))
        
        return neighbor_list
    
    def get_person_position(self, person_id):
        """
        Get the position of a person based on their ID.
        """
        # Find the value that matches our ID in self.space, then reshape to a 2-element list.
        return numpy.reshape(numpy.where(self.space == person_id), (1, 2))[0].tolist()

    def get_person_neighbors(self, person_id, distance=1):
        """
        Get the position of a person based on their ID.
        """
        # Find the value that matches our ID in self.space, then reshape to a 2-element list.
        x, y = self.get_person_position(person_id)
        return self.get_neighbors(x, y, distance)   
    
    def move_person(self, person_id, x, y):
        """
        Move a person to a new (x, y) location.
        """
        
        # Get original
        original_position = self.get_person_position(person_id)
        
        # Check target location
        if not numpy.isnan(self.space[x, y]):
            raise ValueError("Unable to move person {0} to ({1}, {2}) since occupied.".format(person_id, x, y))
        
        # Otherwise, move by emptying and setting.
        self.space[original_position[0], original_position[1]] = numpy.nan
        self.space[x, y] = person_id
    
    def step_move(self):
        """
        Model step move function, which handles moving agents randomly around.
        """
        
        # Get a random order for the agents.
        random_order = range(self.num_people)
        numpy.random.shuffle(random_order)
        
        # Iterate in random order.
        for i in random_order:
            # Get current position
            x, y = self.get_person_position(i)
            
            # Move our agent between -1, 0, +1 in each dimension
            x_new = (x + numpy.random.randint(-1, 2)) % self.grid_size
            y_new = (y + numpy.random.randint(-1, 2)) % self.grid_size
            
            # Try to move them
            try:
                self.move_person(i, x_new, y_new)
            except ValueError:
                # Occupied, so fail.
                pass
    
    def step_interact(self):
        """
        "Interact" the agents by seeing if they will hookup and spread.
        """
        
        # Get a random order for the agents.
        random_order = range(self.num_people)
        numpy.random.shuffle(random_order)
        
        # Track which pairs we've tested.  Don't want to "interact" them twice w/in one step.
        seen_pairs = []
        
        # Iterate in random order.
        for i in random_order:
            # Get neighbors
            neighbors = self.get_person_neighbors(i)
            
            # Iterate over neighbors
            for neighbor in neighbors:
                # Check if we've already seen.
                a = min(i, neighbor)
                b = max(i, neighbor)
                if (a, b) not in seen_pairs:
                    seen_pairs.append((a, b))
                else:
                    continue
                
                # Check if hookup if not seen.
                hookup_a = self.people[a].decide_hookup()
                hookup_b = self.people[b].decide_hookup()
                if hookup_a and hookup_b:
                    # Hookup going to happen.  
                    self.num_interactions += 1
                                        
                    # Check now for condoms and use resulting rate.
                    if self.people[a].decide_condom() or self.people[b].decide_condom():
                        # Using a condom.
                        self.num_interactions_condoms += 1
                        use_condom = True
                        
                        if self.people[a].is_infected or self.people[b].is_infected:
                            is_transmission = numpy.random.random() <= self.prob_transmit_condom
                        else:
                            is_transmission = False
                    else:
                        # Not using a condom.
                        use_condom = False
                        if self.people[a].is_infected or self.people[b].is_infected:
                            is_transmission = numpy.random.random() <= self.prob_transmit
                        else:
                            is_transmission = False
                    
                    # Now infect.
                    self.history_interactions.append((self.t, a, b, use_condom, is_transmission))
                    if is_transmission:
                        self.people[a].is_infected = True
                        self.people[b].is_infected = True
    
    def get_num_infected(self):
        """
        Get the number of infected persons.
        """
        # Count
        infected = 0
        for person in self.people:
            if person.is_infected:
                infected += 1
                
        return infected
    
    def step(self):
        """
        Model step function.
        """
        
        # "Interact" agents.
        self.step_interact()
        
        # Move agents
        self.step_move()
        
        # Increment steps and track history.
        self.t += 1
        self.history_space.append(copy.deepcopy(self.space))
        self.history_space_infected.append(self.get_space_infected())
        self.num_infected = self.get_num_infected()
        self.history_num_infected.append(self.num_infected)
        self.history_num_interactions.append(self.num_interactions)
        self.history_num_interactions_condoms.append(self.num_interactions_condoms)

    def get_space_infected(self, t=None):
        """
        Return a projection of the space that shows which cells have an infected person.
        """
        if t == None:
            # Initialize empty
            infected_space = numpy.zeros_like(self.space)
            
            # Iterate over persons and set.
            for p in self.people:
                x, y = self.get_person_position(p.person_id)
                if p.is_infected:
                    infected_space[x, y] = +1
                else:
                    infected_space[x, y] = -1
            
            # Return
            return infected_space
        else:
            # Return historical step
            return self.history_space_infected[t]

    def __repr__(self):
        '''
        Return string representation.
        '''
        skip_none = True
        repr_string = type(self).__name__ + " ["

        elements = dir(self)
        for e in elements:
            # Make sure we only display "public" fields; skip anything private (_*), that is a method/function, or that is a module.
            e_type = eval('type(self.{0}).__name__'.format(e))
            if not e.startswith("_") and e_type not in ['DataFrame', 'function', 'method', 'builtin_function_or_method', 'module', 'instancemethod']:
                    value = eval("self." + e)
                    if value != None and skip_none == True:
                        if e_type in ['list', 'set', 'tuple']:
                            repr_string += "\n\n\t{0}={1},\n\n".format(e, value)
                        elif e_type in ['ndarray']:
                            repr_string += "\n\n\t{0}=\t\n{1},\n\n".format(e, value)
                        else:
                            repr_string += "{0}={1}, ".format(e, value)

        # Clean up trailing space and comma.
        return repr_string.strip(" ").strip(",") + "]"

