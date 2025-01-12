from queue import Queue
import random

# Class for application 
class Application:
    def __init__(self, id):
        self.id = id

# Class for service centre
class Centre:
    def __init__(self):
        self.applications = Queue()

    # Function that generate application with random id
    def generate_request(self):
        id = random.randint(1, 10000000)
        self.applications.put(Application(id))

    def process_request(self):
        while not self.applications.empty():
            current_application: Application = self.applications.get()
            print(f"Serve aplication {current_application.id}")
        else:
            print("All applications were served, the queue is empty")
    
if __name__ == '__main__':
    # Create centre
    centre = Centre()
    print("Hello!")

    while True:

        user_input = input("If you wanna create new application press 'Enter'")

        if not user_input:
            # Create new applications
            for i in range(random.randrange(1, 10)):
                centre.generate_request() 
            
            # Process current applications
            centre.process_request()