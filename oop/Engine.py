class Engine:

    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        print("Engine started.")

    def stop(self):
        self.running = False
        print("Engine stopped.")