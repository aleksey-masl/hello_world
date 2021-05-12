def func_outer():
    x = 2
    print(x)
    def func_inner():
        #nonlocal x
        x = 6
        print(x)
    func_inner()
func_outer()
