#Fibonacci
fib_list = [1, 1]
entrada = input("Quantes vegades vols guardar fibonacci?: ")
def fib(n):
    while len(fib_list) != n:
        fib_list.append(fib_list[-1] + fib_list[-2])

fib(int(entrada))

x = open("fibonacci.txt", "a") 
x.write(str(fib_list))
x.close()

print("Operació finalitzada!")