import base64

choice = input("Choose (E)ncrypt or (D)ecrypt: ").upper()

if choice == "E":
    text = input("Enter file content: ")

    encoded = base64.b64encode(text.encode()).decode()

    print("\nProtected Content:")
    print(encoded)

elif choice == "D":
    text = input("Enter protected content: ")

    decoded = base64.b64decode(text.encode()).decode()

    print("\nRestored Content:")
    print(decoded)

else:
    print("Invalid Choice!")