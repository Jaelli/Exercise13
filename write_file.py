with open('pelican.txt', 'a') as File1:
    File1.write("A wonderful bird is the pelican,\n")
    File1.write("His bill holds more than his belican,\n")

Lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]

with open('pelican.txt', 'a') as File1:
    File1.writelines(Lines)

# \n is required so each line of text added goes onto a new line
