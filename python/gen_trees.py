#!/usr/bin/env python

# This script generates the ability trees to be included directly in the manual tex file
# Trees are taken from and written to the trees/ subdirectory

import os
from ability_tree import *

trees_to_write = ["example.tree"]

def write_tex(tree_file, vert_spacing, horiz_spacing):
  trees_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"trees")
  tree = import_ability_tree(os.path.join(trees_dir,tree_file))
  f = open(os.path.join(trees_dir,tree_file+".tex"),'w')
  f.write(tree.tex(vert_spacing = vert_spacing, horiz_spacing = horiz_spacing))
  f.close()

def main():
  for tree_file in trees_to_write:
    write_tex(tree_file, 0.85, [3,3.5,3])

if __name__=="__main__":
  main()
