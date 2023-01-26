# x = 1


# def func1():
#     x = 2

#     def func2():
#         nonlocal x
#         x = 3
#         print(x)

#     func2()
#     print(x)


# func1()
# print(x)

def func1():
    x = 10

    def func2():
        nonlocal x

        x = 20

    func2()
    print(x)

func1()
print(x)