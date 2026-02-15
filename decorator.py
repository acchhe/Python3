'''
Koden - Tar en funktion

Mäter hur lång tid den tar att köra

Returnerar en tuple med:

funktionens resultat

tiden det tog '''

def performance(func): # Skapar en decorator. func är funktionen som ska “lindas in” (t.ex. add).
    import time # Importerar time här inne så att time alltid finns (och du slipper NameError i tester).
    import functools # Importerar functools för att kunna använda wraps.

    @functools.wraps(func) # Gör att wrapper-funktionen behåller originalfunktionens namn och info
    def wrapper(*args, **kwargs): # Det här är den nya funktionen som ersätter originalet.
        start_time = time.perf_counter() # Startar en högupplöst timer precis innan originalfunktionen körs.
        result = func(*args, **kwargs) # Kör originalfunktionen med exakt samma argument som wrappern fick, och sparar returvärdet i result.
        end_time = time.perf_counter() # Stoppar timern direkt efter att originalfunktionen är klar.
        elapsed_time = end_time - start_time # Räknar ut hur lång tid det tog (sekunder).
        return result, elapsed_time # Returnerar en tuple med: 1-originalfunktionens, 2-resultat tiden det tog

    return wrapper # Decoratorn returnerar wrapper-funktionen. Det är den som används istället för originalfunktionen.


@performance # Dekorerar add. Python gör i praktiken: add = performance(add).
def add(a, b):
    return a + b


# Test
sum_result, time_taken = add(1, 2) # Kallar add, men nu körs wrappern. Den returnerar (result, tid) som packas upp i två variabler.

print("Result:", sum_result) # Skriver ut resultatet (ska bli 3).
print("Time taken:", time_taken) # Skriver ut hur lång tid funktionen tog (väldigt litet tal).
