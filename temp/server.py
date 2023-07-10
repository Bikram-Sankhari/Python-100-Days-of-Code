import sys

# 👇️ User must press Ctrl + D (Unix) or Ctrl + Z (Windows) to exit

print('Press CTRL + D (Unix) or CTRL + Z (Windows) to exit')

user_input = sys.stdin.readlines()

# 👇️ get list of lines
print(user_input)

# 👇️ join the list items into a string
print(''.join(user_input))
