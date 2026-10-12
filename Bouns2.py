transmission = [
    [18, 0, 19, 8, -2, 17],
    [99, 23, 11, 8],
    [10, 4, 55, 23, 8]
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Task 1 - Remove the noise
cleaned = [
    [number for number in word if 4 <= number <= 29]
    for word in transmission
]


# Task 2 - Decode the words
decoded_words = [
    "".join([alphabet[number - 4] for number in word])
    for word in cleaned
]


# Task 3 - Reveal the message
secret_message = " ".join(decoded_words)


# Task 4 - Signal diagnostics
corrupted = [
    len(word) - len([number for number in word if 4 <= number <= 29])
    for word in transmission
]


print("Cleaned transmission:")
print(cleaned)

print("Decoded words:")
print(decoded_words)

print("Secret message:")
print(secret_message)

print("Corrupted values per word:")
print(corrupted)
