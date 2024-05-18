#  else keyword can be used with the for and while loops
# The else block appears after the body of the loop. 
# The statements in the else block will be executed after all iterations are completed. 
# The program exits the loop only after the else block is executed.

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")