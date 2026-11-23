message = "    Hello, World    "
print(f"Original text:{message}")

message = message.lstrip()  # lstrip() removes whitespace from the left side (beginning) of a string.
print(f"Left whitespace remove:{message}")

message = message.strip() # rstrip() removes whitespace from the right side (end) of a string.
print(f"Both whitespace remove:{message}")


message = message.rstrip() #  strip() removes whitespace from both sides of a string.
print(f"Right whitespace remove:{message}")