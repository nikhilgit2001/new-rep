# # import math

# # class Circle:
# #     # Constructor to initialize the Circle object with x, y, and r values.
# #     def __init__(self, x, y, r):
# #         self.x = x
# #         self.y = y
# #         self.r = r

# #     # Method to compute the circumference of the circle.
# #     def circumference(self):
# #         # Circumference formula: 2 * pi * r
# #         return 2 * math.pi * self.r

# #     # Method to compute the area of the circle.
# #     def area(self):
# #         # Area formula: pi * r^2
# #         return math.pi * self.r**2

# # # Example usage:
# # # Create a Circle object with center at (0, 0) and radius 5.
# # circle1 = Circle(0, 0, 5)

# # # Calculate and print the circumference and area.
# # print(f"Circumference: {circle1.circumference()}")
# # print(f"Area: {circle1.area()}")



# # def calculate_string_length(input_string):
# #     count = 0
# #     for char in input_string:
# #         count += 1
# #     return count

# # # Example usage:
# # user_input = input("Enter a string: ")
# # length = calculate_string_length(user_input)
# # print(f"The length of the string is: {length}")
# # ######################################################

# # def find_longest_word(words):
# #     # Check if the list is empty
# #     if not words:
# #         return None, 0  # Return None and 0 if the list is empty

# #     longest_word = words[0]
# #     max_length = len(longest_word)

# #     for word in words:
# #         current_length = len(word)
# #         if current_length > max_length:
# #             longest_word = word
# #             max_length = current_length

# #     return longest_word, max_length

# # # Example usage:
# # word_list = ["apple", "banana", "kiwi", "grapefruit", "pear", "orange"]

# # longest_word, length_of_longest_word = find_longest_word(word_list)

# # if longest_word is not None:
# #     print(f"The longest word is '{longest_word}' with a length of {length_of_longest_word} characters.")
# # else:
# #     print("The word list is empty.")
# # # ######################################################



# # import math

# # class Point:
# #     # Constructor to initialize the Point object with x and y coordinates.
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y

# #     # Method to calculate the distance between two points.
# #     def distance(self, other_point):
# #         # Calculate the differences in x and y coordinates.
# #         x_diff = other_point.x - self.x
# #         y_diff = other_point.y - self.y

# #         # Use the distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
# #         distance_result = math.sqrt(x_diff**2 + y_diff**2)

# #         return distance_result

# # # Example usage:
# # # Create two Point objects.
# # point1 = Point(1, 2)
# # point2 = Point(4, 6)

# # # Calculate the distance between the two points using the distance method.
# # distance_between_points = point1.distance(point2)

# # # Print the result.
# # print(f"The distance between the two points is: {distance_between_points}")


# # # ######################################################



# # import math

# # class Circle:
# #     # Constructor to initialize the Circle object with x, y, and r values.
# #     def __init__(self, x, y, r):
# #         self.x = x
# #         self.y = y
# #         self.r = r

# #     # Method to compute the circumference of the circle.
# #     def circumference(self):
# #         # Circumference formula: 2 * pi * r
# #         return 2 * math.pi * self.r

# #     # Method to compute the area of the circle.
# #     def area(self):
# #         # Area formula: pi * r^2
# #         return math.pi * self.r**2

# # # Example usage:
# # # Create a Circle object with center at (0, 0) and radius 5.
# # circle1 = Circle(0, 0, 5)

# # # Calculate and print the circumference and area.
# # print(f"Circumference: {circle1.circumference()}")
# # print(f"Area: {circle1.area()}")

# # # ######################################################


# class Stack:
#     def __init__(self):
#         # Initialize an empty list to represent the stack.
#         self.items = []

#     def push(self, item):
#         # Add the item to the end of the list (top of the stack).
#         self.items.append(item)

#     def pop(self):
#         # Check if the stack is empty before attempting to pop.
#         if not self.is_empty():
#             # Remove and return the item from the end of the list (top of the stack).
#             return self.items.pop()
#         else:
#             print("Stack is empty. Cannot pop.")

#     def head(self):
#         # Check if the stack is empty before attempting to get the head.
#         if not self.is_empty():
#             # Return the item at the end of the list (top of the stack) without removing it.
#             return self.items[-1]
#         else:
#             print("Stack is empty. No head.")

#     def is_empty(self):
#         # Check if the stack is empty.
#         return len(self.items) == 0

#     def size(self):
#         # Return the number of elements in the stack.
#         return len(self.items)

# # Example usage:
# stack = Stack()

# # Push elements onto the stack.
# stack.push(1)
# stack.push(2)
# stack.push(3)

# # Print the stack size and head.
# print(f"Stack size: {stack.size()}")
# print(f"Head of the stack: {stack.head()}")

# # Pop elements from the stack.
# popped_item = stack.pop()
# print(f"Popped item: {popped_item}")

# # Print the updated stack size and head.
# print(f"Stack size after pop: {stack.size()}")
# print(f"Head of the stack after pop: {stack.head()}")



# # # ######################################################



import math

class Circle:
    # Constructor to initialize the Circle object with x, y, and r values.
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    # Method to compute the circumference of the circle.
    def circumference(self):
        # Circumference formula: 2 * pi * r
        return 2 * math.pi * self.r

    # Method to compute the area of the circle.
    def area(self):
        # Area formula: pi * r^2
        return math.pi * self.r**2

# Example usage:
# Create a Circle object with center at (0, 0) and radius 5.
circle1 = Circle(0, 0, 5)

# Calculate and print the circumference and area.
print(f"Circumference: {circle1.circumference()}")
print(f"Area: {circle1.area()}")
