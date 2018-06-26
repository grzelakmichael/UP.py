def func(a,b=[]):
    b.append(a)
    print(b)
func(1)
func(2)
func(2, [])
func(3)