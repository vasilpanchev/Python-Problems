# 🖼️ Python Pattern Drawing Project

# Step 1: Display a menu to the user
print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get dimensions based on choice
if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
    rows = int(input("Enter the number of rows: "))
elif choice in [2, 5]:  # Patterns that need size
    size = int(input("Enter the size of the square/rectangle: "))

# Step 4: Generate the selected pattern
if choice == 1:  # Right-angled Triangle
    for i in range(1, rows + 1):
        print("*" * i)

elif choice == 2:  # Square with Hollow Center
    for i in range(1, size + 1):
        if i == 1 or i == size:
            print("*" * size)
        else:
            print("*", end='')
            print(" " * (size - 2), end='')
            print("*")

elif choice == 3:  # Diamond
    for i in range(1, int(rows / 2 + 2)):
        print(int(rows / 2 + 1 - i) * ' ', end='')
        print((i * 2 - 1) * '*')
    for i in range(int(rows / 2), 0, -1):
        print(int(rows / 2 + 1 - i) * ' ', end='')
        print((i * 2 - 1) * '*')

elif choice == 4:  # Left-angled Triangle
    for i in range(rows, 0, -1):
        print('*' * i)

elif choice == 5:  # Hollow Square
    for i in range(1, size + 1):
        if i == 1 or i == size:
            print("* " * size)
        else:
            print("*", end='')
            print(" " * (2 * (size - 1) - 1), end='')
            print("*")

elif choice == 6:  # Pyramid
    for i in range(1, rows + 1):
        print((rows - i) * ' ', end='')
        print((i * 2 - 1) * '*')

elif choice == 7:  # Reverse Pyramid
    for i in range(rows, 0, -1):
        print((rows - i) * ' ', end='')
        print((i * 2 - 1) * '*')

elif choice == 8:  # Rectangle with Hollow Center
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    for i in range(height):
        if i == 0 or i == height - 1:
            print("*" * width)
        else:
            print("*", end='')
            print(' ' * (width - 2), end='')
            print("*")

else:
    print("❌ Invalid choice! Please restart the program.")

# Step 5: Optional - Allow the user to restart or exit
