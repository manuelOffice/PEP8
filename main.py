""" Liberia time forma de importar una liberia """
import time

class Timer:
    #
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print(f"Time taken: {end_time - self.start_time} seconds")

with Timer():
    # Code to be timed goes here
    pass