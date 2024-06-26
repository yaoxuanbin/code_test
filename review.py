# Review 1

def add_to_list(value, my_list=[]):

    my_list.append(value)

    return my_list

 

# Review 2

def format_greeting(name, age):

    #need use f in order to use variable
    return f"Hello, my name is {name} and I am {age} years old."

 

# Review 3

class Counter:

    def __init__(self):
        self.count = 0
        

    def increment(self):
        self.count += 1
 

    def get_count(self):

        return self.count

 

# Review 4

import threading

 

class SafeCounter:

    def __init__(self):

        self.count = 0

 

    def increment(self):

        self.count += 1

 

    def worker(counter):

        for _ in range(1000):

            counter.increment()

     

    counter = SafeCounter()

    threads = []

    for _ in range(10):

        t = threading.Thread(target=worker, args=(counter,))

        t.start()

        threads.append(t)

     

    for t in threads:

        t.join()

 

# Review 5

def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            counts[item] =+ 1

        else:

            counts[item] = 1

    return counts


if __name__ == "__main__":
    print('#add_to_list')
    my_list=[1]
    my_list=add_to_list(2,my_list)
    my_list=add_to_list(3,my_list)
    print(my_list)
    print('#format_greeting')
    print(format_greeting('peter',20))
    print('#counter')
    counter=Counter()
    counter.increment()
    counter.increment()
    print(counter.get_count())
    
    