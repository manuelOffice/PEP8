"""
Title: Clase Persona
Autor: José Manuel Alvarado Balderrama
Date: 2024-08-20
Version: v1.0
"""

class Person:
    """
    This class provides the most common attributes and methods of a person.   
    """
    
    def __init__(self, fname: str, lname: str) -> None:
        """ 
        This method creates an instance of a Person [object].

        Args:
            fname: 'first name' of type string
            lname: 'last name' of type string

        Returns:
            There's not a return value
        """
        self.__age = None
        self.__fname = fname
        self.__lname = lname

    # Getter and Setter Methods

    @property
    def age(self) -> int:
        """ This method returns an integer value"""
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        """ This method recibes an integer value"""
        self.__age = age

    @property
    def fname(self) -> str:
        """ This method returns a string value"""
        return self.__fname
    
    @property
    def lname(self) -> str:
        """ This method returns a string value"""
        return self.__lname
    
    # Person class Methods
    
    def __str__(self) -> str:
        """
        This method makes the instantiated object printable.

        Returns:
            The most important attributes as a string.
        """
        full_name = "Full Name"
        age = "Age"
        return f"{full_name:<10}: {self.full_name()} \n{age:<10}: {self.age}"
    
    def full_name(self) -> str:
        """ This method returns a string value"""
        full_name = self.fname + " " + self.lname
        return full_name

    def greet(self, name: str = None) -> str:
        """Greets the user with a personalized message.

        Args:
            name: The name of the user to greet.

        Returns:
            A string containing the greeting message.
        """

        if name:
            return f"Hello, {name}. Nice to meet you!"
        else:
            return f"Hi, I'm {self.fname}!"
        
    def add_numbers(self, *args: int | float) -> int | float:
        """
        Add numbers together.

        Parameters:
            args (int or float): The numbers (in a tuple) to be added.

        Returns:
            int or float: The sum of the values.
        """
        result = 0
        for number in (args):
            result += number

        return result


if __name__== "__main__":
    # Creating an object of the class Person
    myself = Person('Manuel', 'Alvarado')

    #Llamada al metodo add_numbers()
    number = myself.add_numbers(20, 2, 5.2)
    print(f"Result = {number}")

    # Greeting using an object Person
    user_name = input("Enter your name: ")
    print(myself.greet(user_name))