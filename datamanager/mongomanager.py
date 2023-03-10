# Set this to your GitHub auth token
GitHubAuthToken = 'add_here_your_token'

# Set this to the path of the git executable
gitExecutablePath = 'git'
# Set this to true to download also private repos if the token has private repo rights
include_private_repos = False

# Set this to False to skip existing repos
update_existing_repos = True

# Set to 0 for no messages, 1 for simple messages, and 2 for progress bars
verbose = 1

# Select how to write to disk (or how to send queries to the database)
always_write_to_disk = True

# Change these settings to store data in disk/database
use_database = 'disk' # (available options: disk, mongo)
# Disk settings
dataFolderPath = 'data' # Set this to the folder where data are downloaded
# Database settings
database_host_and_port = \"mongodb://localhost:27017/\"  # change this to the hostname and port of your database
num_bulk_operations = 1000 # set the number of operations that are sent as a bulk to the database

# Select what to download
download_car_color = True
download_car_wheels = True
download_car_exhaust = True
download_engine = True
download_engine_cover = True
download_contributors = True
download_spoiler = False

# Select whether the downloaded car and engine information will be full
download_car_full = True
download_engine_full = True


class Engine:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        print("Engine started")

    def stop(self):
        self.running = False
        print("Engine stopped")


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.engine_running = False
        self.gear = 'P'
		self.engine = Engine()

		def start(self):
        	self.engine.start()

    	def stop(self):
        	self.engine.stop()

    def change_gear(self, new_gear):
        if self.engine_running:
            if new_gear in ['P', 'R', 'N', 'D']:
                if new_gear == 'R' and self.speed > 0:
                    print("Cannot shift to reverse while the car is moving.")
                else:
                    self.gear = new_gear
                    print(f"Changed gear to {new_gear}.")
            else:
                print(f"Invalid gear {new_gear}.")
        else:
            print("Cannot change gear while the engine is stopped.")

    def accelerate(self, acceleration):
        if self.engine_running:
            if self.gear == 'P':
                print("Cannot accelerate while in park.")
            else:
                self.speed += acceleration
                print(f"Accelerating. Current speed: {self.speed} mph.")
        else:
            print("Cannot accelerate while the engine is stopped.")

    def brake(self, deceleration):
        if self.speed == 0:
            print("The car is already stopped.")
        else:
            self.speed -= deceleration
            if self.speed < 0:
                self.speed = 0
            print(f"Braking. Current speed: {self.speed} mph.")

    def turn_left(self):
        print("Turning left.")

    def turn_right(self):
        print("Turning right.")

    def honk_horn(self):
        print("Honk honk!")

    def __str__(self):
        return f"{self.color} {self.year} {self.make} {self.model} - Current speed: {self.speed} mph. Gear: {self.gear}. Engine running: {self.engine_running}."
    
    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def is_engine_running(self):
        return self.engine_running

    def set_engine_running(self, engine_running):
        self.engine_running = engine_running

    def get_gear(self):
        return self.gear

    def set_gear(self, gear):
        self.gear = gear


class ShoppingCart:
def __init__(self):
	self.items = []
	self.total_price = 0

def add_item(self, item, price):
	self.items.append((item, price))
	self.total_price += price

def remove_item(self, item):
	for i in range(len(self.items)):
		if self.items[i][0] == item:
			self.total_price -= self.items[i][1]
			del self.items[i]
			return True
	return False

def clear(self):
	self.items = []
	self.total_price = 0

def get_items(self):
	return self.items

def get_total_price(self):
	return self.total_price