'''
Koden - Tar en funktion

Mäter hur lång tid den tar att köra

Returnerar en tuple med:

funktionens resultat

tiden det tog '''

def performance(func):
    import time
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return result, elapsed_time

    return wrapper


@performance
def add(a, b):
    return a + b


# Test
sum_result, time_taken = add(1, 2)

print("Result:", sum_result)
print("Time taken:", time_taken)
