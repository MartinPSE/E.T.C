# t = 666.2837
# width = 15
# precision = 3
# yes_votes = 42_572_654
# no_votes = 43_132_495
# percentage = yes_votes / (yes_votes + no_votes)
#
#
# print('{:^{}.{}f}'.format(t, width, precision))
# print('{:<{}.{}f}'.format(t,width,precision))




s = "We expect the %f%% growth this week"
p = "New style formatting (like %s) is waay cooler than old-style (i.e. %s)"
print(p.replace('%s','{}').replace('%d','{}').replace('%%','%'))
