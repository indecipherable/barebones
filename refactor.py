# this should take [project_name] 
# and refactor [barebones] to [projectname]

import os

# this refactors project to project name
def refac(final_name):
  print("Refactoring to " + final_name + "...")
  for filename in os.listdir(os.getcwd()):
    print(filename)
    if filename == "barebones":
      os.rename("barebones", filename)
    else:
      pass

# this confirms user input for project name
def get_in(this_project_name):
  this_y_n = raw_input("> ")
  if this_y_n.lower() == 'y':
    print("OK, got 'y'")
    refac(this_project_name)
  elif this_y_n.lower() == 'n':
    print("OK, got 'n'")
    ref_to()
  else:
    print("Nope")
    print("Is " + this_project_name + " right? [y/n]:")
    get_in(this_project_name)

def do_next():
  print("Ok, next!!")

# this accepts user input for project name
def ref_to():
  print("This project name is: ")
  this_project=raw_input("> ")
  print("I got: '" + this_project + \
          "'  Is that right? [y/n]:")
  get_in(this_project)

ref_to()
