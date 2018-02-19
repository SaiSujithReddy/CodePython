
#https://www.interviewcake.com/question/python/reverse-words
message = 'find you will pain only go you recordings security the into if'


stack = []
for x in message.split(" "):
    stack.append(x)
while stack:
    print(stack.pop(), end=" ")

print()
x = message.split(" ")
print(" ".join(reversed(x)))

print(" ".join(reversed(message.split(" "))))


