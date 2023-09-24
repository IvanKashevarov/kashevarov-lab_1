import time
start = time.time()
def resheto(array,n,i):
    if i*i<n:
        if array[i]!=0:
            j=i*i
            while j<=n:
                array[j]=0
                j+=i
        array = resheto(array, n, i+1)

    return array



if __name__ == '__main__':
    print("Введите количество цифр: ")
    while True:
        try:
            n = int(input())
            break
        except ValueError:
            print("Вы ввели не число. Повторите ввод")

    numbers = [i for i in range(n+1)]
    numbers = resheto(numbers,n,2)
    for i in numbers:
        if i!=0:
            print(i)
end = time.time()
print("time is", end-start)