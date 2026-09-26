def function_a():
    print("a_before")
    function_b()
    print("a_after")
def function_b():
    print("b_before")
    function_c()
    print("b_after")
def function_c():
    print("c")
function_a()