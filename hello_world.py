import random

def random_saying():
    return random.sample( ['hi', 'look up', 'look down'], k = 2)

if __name__ == "__main__":
    print("Hello world!")
    print( random_saying() )
