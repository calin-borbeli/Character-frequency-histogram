from os import strerror

file_name = input("Enter the text file's name: ")
# create a dictionary to store the alphabet characters frequencies
frequency = {chr(ch): 0 for ch in range(ord("a"), ord("z") + 1)}
try:
    tf = open(file_name, "rt")
    ch = tf.read(1)  # read 1 character
    while ch != "":
        if ch.isalpha():
            frequency[ch.lower()] += 1  # transform to lower case and increment
        ch = tf.read(1)
    tf.close()
    wf = open(file_name + ".hist", "wt")
    # used a lambda to access the directory's elements and set reverse to get a valid order
    for char in sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True):
        if frequency[char] > 0:
            print(char, " -> ", frequency[char])
            wf.write(char + " -> " + str(frequency[char]) + "\n")
    wf.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
