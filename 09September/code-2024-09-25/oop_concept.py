
# # Class

# class Vehicle:
#     # Class attributes
#     bmw = 'It is one of the most popular car brands.'
#     mercedes = 'It is another luxary car brand.'


#     # Instance methods
#     def start(self, key, horn):
#         self.key = key
#         self.horn = horn
#         accelerate = True
#         return f'Start the engine with {key}. Check the horn level {horn}.'
    

#     def drive(self):
#         speed = 120
#         return f'Drive the car using {self.key}.'
    

#     def stop(self):
#         brake = True
#         return f'Stop the car with horn {self.horn} db.'
    

#     def fuel(self):
#         tank_low = True
#         return 'Re-fill the tank.'

# vehicle_1 = Vehicle()

# # print(vehicle_1.bmw)

# print(vehicle_1.start('finger print', 20))

# print(vehicle_1.drive())

# print(vehicle_1.stop())

# print(vehicle_1.fuel())






# Class

class Vehicle:
    # Class attributes
    bmw = 'It is one of the most popular car brands.'
    mercedes = 'It is another luxary car brand.'


    # Instance methods
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print('This is init method and I am always called at the time of object creation.')
    

    def drive(self):
        speed = 120
        return f'Drive the car using {self.key}.'
    

    def stop(self):
        brake = True
        return f'Stop the car with horn {self.horn} db.'
    

    def fuel(self):
        tank_low = True
        return 'Re-fill the tank.'

vehicle_1 = Vehicle('BMW','X11')
# vehicle_2 = Vehicle('Tesla', 'Model 3')


# print(vehicle_1.bmw)




