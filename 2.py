def faktorial_rekursive(n):

    if n == 0:
        return 1
    else:
        return n * faktorial_rekursive (n-1)
    
#Contoh penggunaan
bilangan = 5
hasil_faktorial = faktorial_rekursive(bilangan)
print("Faktorial dari", bilangan, "adalah", hasil_faktorial)