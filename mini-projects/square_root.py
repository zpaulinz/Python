import math

message = (
    "This program displays the square root of the predefined "
    "value π = 3.14... with an accuracy of four decimal places."
)
print(message)
print(f"sqrt(pi) = {math.sqrt(math.pi):.4f}.")
# print(f"sqrt(pi) = {math.sqrt(math.pi):.4f}", ".", sep = "")