# this should take [project_name] 
# and refactor [barebones] to [projectname]

import os
import glob, re
import time

# this refactors project to project name
def refac(final_name):
  print("Refactoring to " + final_name + "...")
  # 3 cases: cwd, ./[foo]/* ../[cwd]/
  for filename in os.listdir(os.getcwd()):
    print(filename)
    print type(filename)
    # rename ./barebones/ to ./[final_name]/
    if filename == "barebones":
      os.rename(filename, final_name)
      print("renamed ./barebones to: ./" + final_name)
    else:
      pass
    # rename ./tests/barebones* ./tests/[final_name]*
    u_r_here = os.getcwd()
    if filename == "tests":
      go_here_now = os.path.join(u_r_here,filename)
      # this chdir to tests = go_here_now
      os.chdir(go_here_now)  
      for leaf_word in os.listdir(os.getcwd()):
        if "barebones" in leaf_word:
          leaf_word = os.path.join(go_here_now,leaf_word)
          new_name = final_name + "__init__.py"
          new_name = os.path.join(go_here_now,new_name)
          os.rename(leaf_word, new_name)
        os.chdir(u_r_here)
  # rename ../barebones/ ../[final_name]
  os.chdir(u_r_here)
  os.chdir('..')
  for root_name in os.listdir(os.getcwd()):
    if "barebones" in root_name:
      os.rename(root_name, final_name)
      os.chdir('%s') % final_name
      print("Files refactor complete. Please cd .. to find your new directory.")
      #os.listdir(os.getcwd())

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
  print("Here we need to check for files containing barebones") 

# this accepts user input for project name
def ref_to():
  print("This project name is: ")
  this_project=raw_input("> ")
  print("I got: '" + this_project + \
          "'  Is that right? [y/n]:")
  get_in(this_project)

ref_to()
