odd_numbers = [11, 13, 15, 17, 19]
even_numbers = [12, 14, 16, 18, 20]
print("Odd Numbers List: ", odd_numbers)
print("Even Numbers List: ", even_numbers)

odd_numbers.extend(even_numbers)
merged_list = odd_numbers

print("Merged List: ", merged_list)

new_mergedlist = [i * 2 for i in merged_list]
print(new_mergedlist)
for i in new_mergedlist:
  print("Data Type of {} value:".format(i))
  print(type(i))
