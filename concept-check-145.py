#the check module is automatically imported for this question
#Typical values
check.expect("Example 1", in_interval(1,5,3), 1) #given
check.expect("Example 2", in_interval(1,5,7), 0) #val above end

#Small and large values
check.expect("Small typical values", in_interval(0,8,4), 1) #given
check.expect("Small values", in_interval(0,7,0), 1) #given 
check.expect("Large values pass", in_interval(10**6,10**8,10**7), 1) #given
check.expect("Large values fail", in_interval(10**6,10**8,10**10), 0) #given

#Boundary values and relationship between parameters
check.expect("Val equal start", in_interval(2,9,2), 1) #given
check.expect("Val equal end", in_interval(2,9,9), 1) #given
check.expect("All equal and z", in_interval(0, 0, 0), 1) #added
check.expect("Test 13", in_interval(6, 6, 6), 1) #not required

#Special cases
check.expect("Val below start", in_interval(3,5,1), 0) #added
check.expect("Val above end", in_interval(3,5,7), 0) #added, not required