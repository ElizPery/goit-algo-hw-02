from queue import Queue
import random
import time

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
            time.sleep(1)
        else:
            print("All applications were served, the queue is empty")
    
if __name__ == '__main__':
    # Create centre
    centre = Centre()
    print("Hello!")

    while True:

        user_input = input("If you wanna update and process new application press 'Enter'\nIf you wanna close the program write 'Exit'     >>>>>>>>>>     ")

        if not user_input:
            # Create new applications
            for i in range(random.randrange(1, 10)):
                centre.generate_request() 
            
            # Process current applications
            centre.process_request()
        elif user_input.lower().strip() == 'exit':
            print("Bye, see you!")
            break
        else:
            print("This command is not exist, please try again!")