d={'1': 'Tom', '2': 'R19EC000', '3': 'A', '4': '87xx74xx69', '5': '201'}
key = input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")
