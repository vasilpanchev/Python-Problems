string = input()
string = string.lower()
keywords = ["fish", "sand", "water", "sun"]

count = sum(string.count(word) for word in keywords)

print(count)