key = int(input())
lines = int(input())

message = []

for _ in range(lines):
    char = input()
    decrypted = chr(ord(char) + key)
    message.append(decrypted)

for letter in message:
    print(letter, end="")
