# Randomly generates a 6 x 6 list of assorted characters such that there are exactly two of each character

from random import sample
symbols =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@","!","%","&","/","(",")","=",";","^"]

first = sample(symbols, 18)
second = sample(first, len(first))
total = first + second
final_list = sample(total, len(total))

print(final_list[0], final_list[1], final_list[2], final_list[3], final_list[4], final_list[5])
print(final_list[6], final_list[7], final_list[8], final_list[9], final_list[10], final_list[11])
print(final_list[12], final_list[13], final_list[14], final_list[15], final_list[16], final_list[17])
print(final_list[18], final_list[19], final_list[20], final_list[21], final_list[22], final_list[23])
print(final_list[24], final_list[25], final_list[26], final_list[27], final_list[28], final_list[29])
print(final_list[30], final_list[31], final_list[32], final_list[33], final_list[34], final_list[35])
