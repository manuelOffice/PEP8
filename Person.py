"""
Title:PEP 8 Compliance
"""

def add_numbers(a, b):
    """
    Add two numbers together.

    Parameters:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.

    Returns:
        int or float: The sum of the two input values.
    """
    result = a + b
    return result

def greet(name):
    """Greets the user with a personalized message.

    Args:
        name: The name of the user to greet.

    Returns:
        A string containing the greeting message.
    """

    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, world!"


if __name__== "__main__":
    #Llamada al metodo add_numbers()
    number = add_numbers(20,2)
    print(number)
    user_name = input("Enter your name: ")
    greeting = greet(user_name)
    print(greeting)