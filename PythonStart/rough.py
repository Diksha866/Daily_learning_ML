my_list = [5,6,7, 2, 1]
# for i in my_list:
#   if i<3:
#     print("small")
#   else: 
#     print("large")    this is long way
for i in my_list:
  status = "small"  if i<3 else "large" # this is doing same work in small way suing lembda function
  print(f"{status}")
