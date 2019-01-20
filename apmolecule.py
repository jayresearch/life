#Constructing all possible macro molecules (apmolecule) from the basic Sugar, Phosphate, and Base
#
# Level of complexity of the molecule:

# Level 1: the single Molecule:
# {Type 1} 
# {Type 2}
# {Type 3}

# Level 2: Combination of any two molecules: 
#{Type 1 and Type 2}
#{Type 1 and Type 3}
#{Type 2 and Type 3}

# Level 3: Combination of any three molecules:
#{Type 1, Type 2 and Type 3}

#Usage: python apmolecule.py Input
#Input: type1.bid type1.bid type3.bid restriction.rl
#Output: output_file.bid
#
#--------------------------------------------------------------------------------------



import sys

try:

   type1_mole = sys.argv[1]
   type2_mole = sys.argv[2]
   type3_mole = sys.argv[3]
   rule_file = sys.argv[4]

except IndexError:
  
   print "Provide the input type1, type2, type3 and rule file \n"
   print "exiting...\n"
   exit()


type1_ptr = open(type1_mole, 'r') 
type2_ptr = open(type2_mole, 'r') 
type3_ptr = open(type3_mole, 'r')
rule_ptr = open("restriction.rl", 'r')
output_mole_ptr = open("output_file.bid", 'w+')

for line1 in type1_ptr:
    line1 = line1.strip(" ")
    if line1 != '' and line1 != '\n':
	if line1[0] != '#':
	   type1_mole = line1
           type1_num = type1_mole.strip('[''\n')
           type1_num = type1_num.strip(']')
           type1_mole_strip = type1_num 
           print "type1_mole_strip:" + type1_mole_strip 
	   type1_num = type1_num.split()[1]
           print "type1_mole at top" + type1_mole
	   for line2 in type2_ptr: 
               line2 = line2.strip(" ")
               if line2 != ''and line2 != '\n':
		   if line2[0] != '#':
		      type2_mole = line2
		      type2_num = type2_mole.strip('[' '\n')
		      type2_num = type2_num.strip(']')
                      type2_mole_strip = type2_num
                      print "type2_mole_strip:" + type1_mole_strip 
		      type2_num = type2_num.split()[1]
                      print "type2_mole:" + type2_mole
		      for rule in rule_ptr:                      
                          rule = rule.strip(" ")
                          print rule
                          if rule != '' or rule != '\n':
                              print "rule:" + rule[0]
                              print rule
			      if rule[0] != '#':
                                  print rule.split()
				  temp_rule = rule.split()
                                  print temp_rule
				  first_type = temp_rule[0]
				  yesno = temp_rule[1] 
				  second_type = temp_rule[2]

				  if type1_num == first_type  and type2_num == second_type and yesno == 'Y':
				     print "The yes (Y) rule found!" 
				     print "forming the new molecule..."
                                     temp1_mole = type1_mole_strip.split() 
                                     temp2_mole = type2_mole_strip.split()
                                     print "temp1_mole:: "
                                     print temp1_mole
                                     new_mole  = ''

                                     for i in range(3):
        		                 new_mole = new_mole + temp1_mole[i] + ' '

                                     for j in range(3):
        		                 new_mole = new_mole + temp1_mole[j+1] + ' '

                                     new_mole = '[' + new_mole.strip(' ') + ']'

				     output_mole_ptr.write(new_mole + '\n')
				     break

				  if type2_num == first_type  and type1_num == second_type and yesno == 'Y':
				     print "The yes (Y) rule found!"
				     print "forming the new molecule..."
                                     temp1_mole = type1_mole_strip.split() 
                                     temp2_mole = type2_mole_strip.split()
                                     new_mole  = ''

                                     for i in range(3):
        		                 new_mole = new_mole + temp1_mole[i] + ' '

                                     for j in range(3):
        		                 new_mole = new_mole + temp1_mole[j+1] + ' '

                                     new_mole = '[' + new_mole.strip(' ') + ']'

				     output_mole_ptr.write(new_mole + '\n')
				     break
		       #end of for rule....
	   #end of for line2...
#end of for line1...
          

