#!/usr/bin/env python

# This script generates the ability trees to be included directly in the manual tex file
# Trees are taken from and written to the trees/ subdirectory

import os
from ability_tree import *

def write_tex(tree_file, vert_spacing, horiz_spacing):
  scriptname = os.path.basename(os.path.realpath(__file__))
  trees_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"trees")
  tree = import_ability_tree(os.path.join(trees_dir,tree_file))
  f = open(os.path.join(trees_dir,tree_file+".tex"),'w')
  f.write("% THIS FILE WAS AUTOMATICALLY GENERATED BY "+scriptname+"\n\n")
  f.write(tree.tex(vert_spacing = vert_spacing, horiz_spacing = horiz_spacing))
  f.close()

def main():
  write_tex("example.tree", 0.85, [3,3.5,3])

if __name__=="__main__":
  main()
