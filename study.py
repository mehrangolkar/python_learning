def Greet(name):
   print(f"Hello {name}")
   print(f"How are you doing {name} ?")

def Greeting_with(name,location):
    print(f"Hello {name} you live in {location} .")

Greet("Mehran Golkar")
print("=========================")
Greeting_with("Mehran Golkar", "Tehran IR")
print("=========================")
Greeting_with(location="Tehran", name="Mehran Golkar")