"""
Title: Estilo Estandar de Codificación PEP8
Autor: José Manuel Alvarado Balderrama
Date: 2024-08-20
Version: v1.0
"""

# Libraries that have been used
from Person import *
import time

class Timer:
    """
    This clase is a Context Manager that times how long 
    it takes to execute a block of code.
    """
    def __enter__(self):
        """
        This method saves the moment when it was initiated

        Returns:
            An instance of itself
        """
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        This method shows the time required to execute a block of code.

        Args:
            exc_type: 'exception type' of type exception
            exc_val: 'exception value' of type exception
            exc_tb: 'exception traceback' of type exception
        """
        end_time = time.time()
        print(f"Time taken: {end_time - self.start_time} seconds")

# Block of code
with Timer():
    # Creating an object of the class Person
    myself = Person('Manuel', 'Alvarado')
    myself.age = 20

    # Greeting using an object Person
    print(myself.greet())

    # Showing some attributes of this object
    print(myself)

print("Done!")