#!/usr/bin/env python

# This script generates the xp table to be included directly in the manual tex file

import os

# b = skill level base
# s = xp scale factor
# d = discount factor
b = 1.85
s = 50.0 / pow(b,-2)
d = 1.35/b

# Note that s is set so that the (3,3) position in the table has an xp cost of 50.
# Note that d is set to b'/b, where b' is a sort of modified base:
#  b' is the base you would see if you read diagonally down the table instead of straight down.
#  It represents how much harder it is, on average, to increase all children of a skill from a to a+1 vs from a-1 to a.

# a = attribute bonus
# c = current skill level
xp_cost = lambda a,c : int(round(s*pow(b,c)*pow(d,a+2)))

#list of current skill levels to put as rows of table:
clist = range(-4,4)

#list of attribute bonuses to put as columns table:
alist = map(lambda x:x/(2.0),range(-8,9))


colcolor = lambda color : ">{\\columncolor[HTML]{"+color+"}[\\tabcolsep][1.1\\tabcolsep]}"
blue = colcolor("67C4D8")
red  = colcolor("F67D75")
purp = colcolor("AFA1A7")


def main():
  scriptname = os.path.basename(os.path.realpath(__file__))

  f = open("xptable.tex", "w")
  f.write("% THIS FILE WAS AUTOMATICALLY GENERATED BY "+scriptname+"\n\n")
  f.write("\\setlength{\\minrowclearance}{6pt}\n")
  f.write("\\begin{tabular}{cr"+(len(alist)*'l')+"}\n")
  
  f.write("\\multicolumn{2}{"+purp+"c}{} & \\multicolumn{"+str(len(alist))+"}{"+blue+"c}{\\textbf{Attribute Bonus}} \\\\\n")
  f.write("\\noalign{\\vspace{-1pt}}\n")
  
  f.write("\\multicolumn{2}{"+purp+"c}{\multirow{-2}{*}{\\textbf{XP}}} &")
  for a in alist:
    f.write(" \\multicolumn{1}{"+blue+"r}{\\textbf{"+str(a)+"}} ")
    if a!=alist[-1]:
      f.write(" & ")
  f.write("\\\\ \\cline{3-"+str(2+len(alist))+"}\n")
  
  for c in clist:
    if c!=clist[-1]:
      f.write(" \\multicolumn{1}{"+red+"r}{} & ")
    else:
      f.write("\\multicolumn{1}{"+red+"l}{")
      f.write("\\multirow{-"+str(len(clist))+"}{*}{")
      f.write("\\rotatebox[origin=c]{90}{\\textbf{Current Skill Level}}")
      f.write("}} & ")
    f.write(" \\multicolumn{1}{"+red+"r|}{\\textbf{"+str(c)+"}} & ")
    for a in alist:
      f.write(" \\multicolumn{1}{r|}{"+str(xp_cost(a,c))+"} ")
      if a!=alist[-1]:
        f.write(" & ")
    f.write("\\\\ \\cline{3-"+str(2+len(alist))+"}\n")
    f.write("\\noalign{\\vspace{-1pt}}\n")
  
  f.write("\\end{tabular}\n")
  f.close()

  f = open("xp_start_multiplier.tex", "w")
  f.write("% THIS FILE WAS AUTOMATICALLY GENERATED BY "+scriptname+"\n")
  f.write(str(xp_cost(-2,-2)))
  f.close()

  f = open("base.tex", "w")
  f.write("% THIS FILE WAS AUTOMATICALLY GENERATED BY "+scriptname+"\n")
  f.write(str(b))
  f.close()


if __name__ == "__main__":
  main()
