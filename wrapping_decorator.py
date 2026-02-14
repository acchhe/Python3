🔹 1. Funktioner är “first-class objects” i Python

I Python kan funktioner:

sparas i variabler

skickas som argument

returneras från andra funktioner

Exempel:
def hälsa():
    print("Hej!")

say_hello = hälsa  # vi sparar funktionen i en variabel
say_hello()


Output:

Hej!


Detta är grunden för decorators.

🔹 2. Vad är Function Wrapping?

Function wrapping betyder att vi lägger en funktion inuti en annan funktion för att utöka eller ändra dess beteende.

Grundidé:
def wrapper(funktion):
    def ny_funktion():
        print("Innan funktionen körs")
        funktion()
        print("Efter funktionen körs")
    return ny_funktion


Användning:

def säg_hej():
    print("Hej världen!")

wrapped = wrapper(säg_hej)
wrapped()


Output:

Innan funktionen körs
Hej världen!
Efter funktionen körs


👉 Vi har alltså “lindat in” funktionen med extra beteende.

🔹 3. Vad är en Decorator?

En decorator är bara ett snyggare sätt att skriva function wrapping.

Istället för:

säg_hej = wrapper(säg_hej)


kan vi skriva:

@wrapper
def säg_hej():
    print("Hej världen!")


Det betyder exakt samma sak!

🔹 4. Viktigt: Hantera argument

Problemet: Vad händer om funktionen har argument?

Fel version:

def wrapper(funktion):
    def ny_funktion():
        funktion()
    return ny_funktion


Det funkar bara om funktionen inte har argument.

Rätt sätt: använd *args och **kwargs
def wrapper(funktion):
    def ny_funktion(*args, **kwargs):
        print("Funktionen startar")
        resultat = funktion(*args, **kwargs)
        print("Funktionen slutade")
        return resultat
    return ny_funktion


Exempel:

@wrapper
def addera(a, b):
    return a + b

print(addera(5, 3))


Output:

Funktionen startar
Funktionen slutade
8


👉 *args = alla positionella argument
👉 **kwargs = alla named arguments

🔹 5. Praktiska exempel
✅ Exempel 1: Loggning
def logga(funktion):
    def wrapper(*args, **kwargs):
        print(f"Kör {funktion.__name__}")
        return funktion(*args, **kwargs)
    return wrapper

@logga
def multiplicera(a, b):
    return a * b

print(multiplicera(4, 5))

✅ Exempel 2: Mäta tid
import time

def mät_tid(funktion):
    def wrapper(*args, **kwargs):
        start = time.time()
        resultat = funktion(*args, **kwargs)
        slut = time.time()
        print(f"Tid: {slut - start:.5f} sekunder")
        return resultat
    return wrapper

✅ Exempel 3: Behörighetskontroll
def kräver_admin(funktion):
    def wrapper(användare):
        if användare != "admin":
            print("Ingen behörighet!")
            return
        return funktion(användare)
    return wrapper

@kräver_admin
def radera_databas(användare):
    print("Databasen raderad!")

radera_databas("user")
radera_databas("admin")

🔹 6. Vad händer bakom kulisserna?

När du skriver:

@decorator
def min_funktion():
    pass


Python gör egentligen:

min_funktion = decorator(min_funktion)


Det är allt. Ingen magi 🧙‍♂️

🔹 7. Viktigt: functools.wraps

När vi använder decorators tappar funktionen sitt namn och docstring.

Exempel:

print(multiplicera.__name__)


Kan visa "wrapper" istället för "multiplicera".

Lösning:

from functools import wraps

def logga(funktion):
    @wraps(funktion)
    def wrapper(*args, **kwargs):
        return funktion(*args, **kwargs)
    return wrapper


Nu behåller funktionen sitt riktiga namn.

🔹 8. Decorators med argument

Ibland vill vi göra:

@repeat(3)
def hej():
    print("Hej")


Då behöver vi en decorator som returnerar en decorator.

def repeat(antal):
    def decorator(funktion):
        def wrapper(*args, **kwargs):
            for _ in range(antal):
                funktion(*args, **kwargs)
        return wrapper
    return decorator

🔹 9. Mental modell (Viktigt!)

Tänk så här:

Decorator
    ↓
Tar en funktion
    ↓
Returnerar en ny funktion
    ↓
Den nya funktionen kör extra kod + originalkoden

🔹 10. Sammanfattning

En decorator:

Tar en funktion som argument

Skapar en ny funktion

Returnerar den nya funktionen

Används med @

Standardstruktur:

from functools import wraps

def decorator(funktion):
    @wraps(funktion)
    def wrapper(*args, **kwargs):
        # kod före
        resultat = funktion(*args, **kwargs)
        # kod efter
        return resultat
    return wrapper
