#!/usr/bin/env python3
"""Radio Car Simulation"""
# std imports
import sys
from time import sleep

# local
import blessed

term = blessed.Terminal()


class Grid:
    '''A class to handle the game board grid with W x H cells
    
    Attributes
    ----------
    self.height: int 
        Stores number of rows in the grid.
    self.width: int
        Stores number of columns in the grid
    '''
    
    cells = []
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
        
        self.cells = [[term.on_darkolivegreen(' ') for w in range(width)] for h in range(height)]
        
                

    def print_grid(self):
        '''Function to print the room/gameboard/grid in the console'''
        print()
        for i in range(self.height):
            index = 0
            tmp = ''
            for j in range(2 * self.width + 1):
                if j % 2 == 0:
                    tmp += '|'
                else:
                    tmp += self.cells[i][index]
                    index += 1
            print(term.darkkhaki('  -------'))
            print(term.darkkhaki(str(self.height - i - 1)) + '| ' + term.darkkhaki(tmp))
        print()
    
    def update_grid(self, car):
        '''Function to update the grid with new position of the radio car.
        Calls print_grid when grid cells have been updated.'''
        grid_y = car.loc[0]
        grid_x = car.loc[1]
        
        self.cells[grid_y][grid_x] = term.on_cyan(' ')
        
        self.print_grid()


class RadioCar:
    '''A class to handle the radio car
    Holds information about movement, orientation
    
    Attributes
    ----------
    self.loc: list
        Stores the grid location of the car
    self.orientation: string
        Stores the direction the car is facing (N,E,S,W)
    self.path: list
        Stores the steps of the path (F, B, L, R)'''
        
    def __init__(self, loc, orientation):
        self.loc = loc
        self.orientation = orientation
        self.path = None
        
    def forward(self, grid):
        '''Function to move the radio car forward.
        Forward movement is dictated by where the car is heading.
        Calls update_grid when location is incremented.'''
        if self.orientation.lower() == 's' and self.loc[0] < (grid.height - 1):     # -1 to compensate for 0 indexing
            self.loc[0] += 1
            grid.update_grid(self)
            sleep(0.5)
        elif self.orientation.lower() == 'e' and self.loc[1] < (grid.width - 1):
            self.loc[1] += 1
            grid.update_grid(self)
            sleep(0.5)
        elif self.orientation.lower() == 'n' and self.loc[0] > 0:
            self.loc[0] -= 1
            grid.update_grid(self)
            sleep(0.5)
        elif self.orientation.lower() == 'w' and self.loc[1] > 0:
            self.loc[1] -= 1
            grid.update_grid(self)
            sleep(0.5)
        else:
            sys.exit(term.on_red('Car crashed into the wall. Simulation over'))

    def backward(self, grid):
        '''Function to move the radio car backward.
        Backward movement is dictated by where the car is heading.
        Calls update_grid when location is incremented.'''
        if self.orientation.lower() == 's' and self.loc[0] < (grid.height - 1):
            self.loc[0] -= 1
            grid.update_grid(self)
            sleep(0.5)
        elif self.orientation.lower() == 'e' and self.loc[1] < (grid.width - 1):
            self.loc[1] -= 1
            grid.update_grid(self)
            sleep(0.5)
        elif self.orientation.lower() == 'n' and self.loc[0] > 0:
            self.loc[0] += 1
            grid.update_grid(self)
            sleep(0.5)
        elif self.orientation.lower() == 'w' and self.loc[1] > 0:
            self.loc[1] += 1
            grid.update_grid(self)
            sleep(0.5)
        else:
            sys.exit(term.on_red('Car crashed into the wall. Simulation over'))

    def right(self):
        '''Function to change the cars heading when given 'Right' command.
        Does not need to update grid.'''
        if self.orientation.lower() == 's':
            self.orientation = 'w'
            return
        elif self.orientation.lower() == 'e':
            self.orientation = 's'
            return
        elif self.orientation.lower() == 'n':
            self.orientation = 'e'
            return
        elif self.orientation.lower() == 'w':
            self.orientation = 'n'
            return
        else:
            sys.exit(term.on_red('Something went wrong in the right turn. Simulation over'))

    def left(self):
        '''Function to change cars heading when given 'Left' command.
        Does not need to update grid'''
        if self.orientation.lower() == 's':
            self.orientation = 'e'
            return
        elif self.orientation.lower() == 'e':
            self.orientation = 'n'
            return
        elif self.orientation.lower() == 'n':
            self.orientation = 'w'
            return
        elif self.orientation.lower() == 'w':
            self.orientation = 's'
            return
        else:
            sys.exit(term.on_red('Something went wrong in the right turn. Simulation over'))


class Game:
    '''Wrapper class for entire game
    Member functions for each logical step of the simulation:
        Initialize grid
        Initialize radio car
        Input path
        Functions for to verify that the inputs are correct
        and to handle errors otherwise.
    
    Attributes
    ----------
    self.grid: Grid
        Stores the Grid object for the simulation.
    self.car: RadioCar
        Stores the RadioCar object for the simulation.
        '''
    
    def __init__(self):
        print(term.darkkhaki('/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/'))
        print(term.darkkhaki('--------Welcome to the Radio Car Simulator!------------'))
        print(term.darkkhaki('/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/'))
    
        self.grid = None
        self.car = None
        
    def verify_dimensions(self, dimensions):
        '''Function to verify that the dimensions are given correctly.
        Only two positive integers are allowed.
        Throws error and returns empty list if arguments are not
        integers, negative integers, or too many arguments.
        Returns list of grid dimensions if correct.'''
        
        int_dims = []
        if len(dimensions) == 2:
            for dim in dimensions:
                try:
                    int_dims.append(int(dim))
                except:
                    print('\n\n\n')
                    print(term.on_red('Dimensions must be integers!'))
                    print('\n\n\n')
                    return []
                    
            if int_dims[0] < 0 or int_dims[1] < 0:
                print('\n\n\n')
                print(term.on_red('Integers must be positive!'))
                print('\n\n\n')
                return []
            
            return int_dims
        
        elif len(dimensions) > 2:
            print('\n\n\n')
            print(term.on_red('Too many arguments! Only input two numbers.'))
            print('\n\n\n')
            return []
        else:
            print('\n\n\n')
            print(term.on_red('Too few arguments! Must input two numbers.'))
            print('\n\n\n')
            return []
        
    def verify_car(self, input):
        '''Function to verify inputs for car's location and heading.
        Throws error if there are too many/few arguments, the first two
        arguments are not positive integers inside the grid bounds, or
        the last argument is not one of (N, E, S, W) letters.
        Returns list of start position and heading if correct, otherwise
        empyt list.'''
        
        int_pos = []
        orientation = ''
        if len(input) == 3:
            i = 0
            for element in input:
                if i < 2:
                    try:
                        if int(element) > (self.grid.height or self.grid.width):
                           print('\n\n\n')
                           print(term.on_red('Start index out of range!'))
                           print('\n\n\n')
                           return []
                        elif int(element) < 0:
                            print('\n\n\n')
                            print(term.on_red('Start index out of range!'))
                            print('\n\n\n')
                            return []
                        int_pos.append(int(element))
                        i += 1
                    except:
                        print('\n\n\n')
                        print(term.on_red('Invalid input! First two arguments must be numbers.'))
                        print('\n\n\n')
                        return []
            
                elif isinstance(element, str) and i == 2:
                    if element.lower() not in ('n', 's', 'e', 'w'):
                        print('\n\n\n')
                        print(term.on_red('Invalid orientation! Must be N, E, S, W'))
                        print('\n\n\n')
                        return []
                    orientation = element
                    
                else:
                    print('\n\n\n')
                    print(term.on_red('Invalid input! Must be on form (height width orientation)'))
                    print('\n\n\n')
                    return []
                
        elif len(input) > 3:
            print(term.on_red('Too many arguments! Input one number and a letter.'))
            return []
        else:
            print(term.on_red('Too few arguments!'))
            return []
        
        int_pos.append(orientation)
        return int_pos
    
    def verify_path(self, path):
        '''Function to verify the path inputs.
        Only letters, not integers, allowed.
        Must be one of (F, B, R, L).
        Returns list of path commands if correct, empty
        list otherwise.'''
        
        verified_path = []
        for step in path:
            try:
                number = int(step)
                print(term.on_red('{} is a number! Only (F, B, R, L) allowed.'.format(number)))
                return []
            except:
                if step.lower() not in ('f', 'b', 'l', 'r'):
                    print(term.on_red('Invalid input! Only (F, B, R, L) allowed.'))
                    return []
                else:
                    verified_path.append(step)
        
        return verified_path
    
    def initialize_grid(self):
        '''Function to initialize self.grid by taking in user input, 
        verifying it is correct, and creates a Grid object with the 
        specified dimensions.'''
        
        print(term.black_on_darkkhaki('Enter dimensions of grid (height width)'))
        dims = input()
        print('\n')
        dims = self.verify_dimensions(dims.split())
        if len(dims) == 0:
            sys.exit(term.on_red('ERROR! Exiting simulation.'))
        
        self.grid  = Grid(dims[0], dims[1])
        self.grid.print_grid()
        
    def initialize_car(self):
        '''Function to initialize self.car by taking in user input,
        verifying it is correct, and creates a RadioCar object with
        the specified starting position and heading.'''
        
        print(term.black_on_darkkhaki('Enter starting position and orientation (x y (N S E W))'))
        car_args = input()
        print('\n')
        car_args = self.verify_car(car_args.split())
        if len(car_args) == 0:
            sys.exit(term.on_red('ERROR! Exiting simulation.'))
        location = car_args[0:2]
        location[0] = int(self.grid.height) - location[0] - 1
        
        self.car = RadioCar(location, car_args[2])
        self.grid.update_grid(self.car)        
        
    def input_path(self):
        '''Function to collect the path commands from user input,
        verifying it is correct, and sets the path to the car's attribute.'''
        
        print(term.black_on_darkkhaki('Enter radio car\'s path (expressed in F (forward), B (backward), L (left), R (right))'))
        path = input()
        print('\n')
        path = self.verify_path(path.split())
        if len(path) == 0:
            sys.exit(term.on_red('ERROR! Exiting simulation.'))
                
        self.car.path = path
    
    def execute_path(self):
        '''Function to execute the given path commands.
        Goes throught the car's path list and calls functions for each command.'''
        car = self.car
        grid = self.grid
        for step in car.path:
            if step.lower() == 'f':
                car.forward(grid)
            elif step.lower() == 'b':
                car.backward(grid)
            elif step.lower() == 'r':
                car.right()
            elif step.lower() == 'l':
                car.left()
            else:
                sys.exit(term.on_red('Something went wrong when executing the path! Simulation over.'))
        
        
def main():
    
    
    g = Game()
    g.initialize_grid()
    g.initialize_car()
    g.input_path()
    g.execute_path()
    
    print()
    success_msg = 'Car finished successfully!'
    final_msg = 'Position of car is ({}, {}), heading {}.'.format((g.grid.height - g.car.loc[0] - 1), g.car.loc[1], g.car.orientation.upper())
    line = '-' * (term.width)
    s_space = ' ' * (term.width - len(success_msg))
    f_space = ' ' * (term.width - len(final_msg))
   
    print()
    print(line)
    print(term.on_green(success_msg) + term.on_green(s_space))
    print(term.on_green(final_msg) + term.on_green(f_space))
    print(line)
    

    
    
    
if __name__=="__main__":
    main()
