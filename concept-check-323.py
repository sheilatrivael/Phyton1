#Typical values
check.expect("Test 1", swap_two("banana", 2, 5), "baaann")

#Small and large values
check.expect("small", swap_two("ab", 0, 1), "ba")
check.expect("large", swap_two("incomprehensibilities", 0, 20), "sncomprehensibilitiei")
check.expect("large swap", swap_two("a" * 1000, 100, 999), "a" * 1000)

#Boundary values and 
check.expect("first and last", swap_two("banana", 0, 5), "aananb")
check.expect("first", swap_two("banana", 0, 0), "banana")
check.expect("last", swap_two("banana", 5, 5), "banana")

#Special cases
check.expect("same letter", swap_two("banana", 1, 3), "banana")
check.expect("same letter", swap_two("banana", 3, 3), "banana")
check.expect("pos1 larger", swap_two("banana", 5, 2), "baaann")

#Relationship between parameters
check.expect("same spot", swap_two("banana", 1, 1), "banana")
