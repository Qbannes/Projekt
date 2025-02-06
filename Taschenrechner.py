# Taschenrechner in Python

def addiere(a, b):
    """Addiert zwei Zahlen"""
    return a + b

def subtrahiere(a, b):
    """Subtrahiert zwei Zahlen"""
    return a - b

def multipliziere(a, b):
    """Multipliziert zwei Zahlen"""
    return a * b

def dividiere(a, b):
    """Dividiert zwei Zahlen"""
    if b == 0:
        raise ValueError("Division durch Null nicht möglich")
    return a / b

def berechne(a, b, operator):
    """Berechnet eine einfache mathematische Operation"""
    if operator == "+":
        return addiere(a, b)
    elif operator == "-":
        return subtrahiere(a, b)
    elif operator == "*":
        return multipliziere(a, b)
    elif operator == "/":
        return dividiere(a, b)
    else:
        raise ValueError("Unbekannter Operator")

def main():
    print("Taschenrechner")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")
    print("5. Beenden")

    while True:
        choice = input("Wähle eine Option: ")
        if choice == "5":
            break
        elif choice in ["1", "2", "3", "4"]:
            a = float(input("Zahl 1: "))
            b = float(input("Zahl 2: "))
            operator = {
                "1": "+",
                "2": "-",
                "3": "*",
                "4": "/"
            }.get(choice)
            try:
                result = berechne(a, b, operator)
                print(f"Ergebnis: {result}")
            except ValueError as e:
                print(f"Fehler: {e}")
        else:
            print("Ungültige Option")

if __name__ == "__main__":
    main()