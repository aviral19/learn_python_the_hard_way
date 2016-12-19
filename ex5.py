my_name = 'Aviral Bajpai'
my_age = 18
my_height = 175 #cm
my_weight = 69 #kg
my_eyes = "Black"
my_teeth = 'white'
my_hair = "Black"

print "Let's talk about %s." % my_name
print "He's %d cm tall" % my_height
print "He's %d kilograms heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

#this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age+my_height+my_weight)

height_in_inch =  my_height/2.54
weight_pounds =  2.2*my_weight

print "He's %d inches tall" %height_in_inch
print "He's %d pounds heavy." %weight_pounds
