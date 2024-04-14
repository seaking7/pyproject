import random

f = open("voca.txt", "r")
raw_data = f.read()
f.close()
# print(raw_data)
data_list = raw_data.split("\n")

while True:
    r_index = random.randrange(0, len(data_list))
    word = data_list[r_index]
    if len(word) <= 6:
        break

print(word)
