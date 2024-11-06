import time

class Timer:
    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
    
    def get_duration(self):
        return self.end_time - self.start_time
