company = ["exploitchip","jan Mohammad","Neamat"]
passwords = {"Neamat":0000,"exploitchip":1111,"Jan Mohammad":2222}

print(company[0],company[1])
password = int(input("Enter your pin : "))
def find_in_file(f):
  myfile = open("names.txt")
  Names = myfile.read()
  Names = Names.splitlines()
  if f in Names:
    return "that name is in the datasheet"
  else :
    return "the name is not in the datasheet"

if password in passwords.values():
  name = input("Enter name :")
  print(find_in_file(name))
else:
  print("Incorrect password!")
  print("This info can be accessed only by:")
  for key  in passwords.keys():
    print(key)
