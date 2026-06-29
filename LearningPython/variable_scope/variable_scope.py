# variable scope in python
# Local scope
# Global scope
# global keyword
# LEGB rule: Local -> Enclosing -> Global -> Built-in
def var_scope_demo3():
    q = 20
    print(q)
    def var_scope_demo4():
        q = 454
        print(q)
        def grand_child():
            q = 33
            print(q)
        grand_child()
    var_scope_demo4()
var_scope_demo3()
# note if there is no variable in any child/ grand child function then the output will be
# parent value
# here the var_scope_demo3 is parent function and demo4 is child so both will get printed
# also we can have multiple functions inside parent function and the variable can be
# accessible at any child or grand child function
# any built in keyword like print etc comes under built in highest level 
x =90
def var_scope_demo():
    # x = 899
    print(x)
def var_scope_demo2():
    print(x)
    # it will show error as the x has been assigned within the above boundaries
    # of that function
    # it will be local scope
var_scope_demo()
# here if we assign variable outside the function then it will be accessible to
# all functions meaning it is a global scope
# Also if the variable is within a function, and we write global_x then the variable will
# act as global scope called as global keyword