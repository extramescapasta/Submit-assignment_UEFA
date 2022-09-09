# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer1 = "Ruud Gullit"
scorer2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = (scorer1 +" "+ str(goal_0)) +", "+ (scorer2 +" "+ str(goal_1)) 
print(scorers)
report = f'{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute'
print(report)
player = scorer2
print(player)
first_name = player[0:5]
print(first_name)
last_name = player[6:16]
print(last_name)
last_name_len = len(player[6:16])
print(last_name_len) 
name_short = (first_name[0])+". "+(last_name)
print(name_short)
chant = (((first_name + "! ") [:7]) * len(first_name)) [:34]
print(chant)
good_chant = chant[5] !=" " 
print(good_chant)