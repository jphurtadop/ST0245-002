#----------------------------Ejercicio2---------------------------------#
def ArraySum(arr):
    result=0;
    for i in range(0,len(arr)):
        result=arr[i]+result
    print(result)
"""
T(n)=C1+C2*n+C3*n+C4
T(n)=n*(C2+C3)+C'-->Regla de las sumas
T(n)=n*C'---->Se quitan los productos
T(n)=O(n)
"""
#----------------------------Ejercicio1---------------------------------#
def ordenar(arr):
    for i in range(0,len(arr)): 
        j=i;
        while j > 0 &(arr[j-1]>arr[j]):
            temp=arr[j]
            arr[j]=arr[j-1]
            arr[j-1]=temp
            j=i-1
"""
T(n)=C1*n+n*C2+C3*n(n+1)/2+C4*n(n+1)/2+C5*n(n+1)/2+C6*n(n+1)/2+C7*n(n+1)/2
T(n)=(n(n+1)/2*)(C3+C4+C5+C6)+C'-->Regla de las sumas y producto
T(n)=(n^2+n)*1/2*C'---->Se quita la suma interna
T(n)=n^2+n---->Se quitan los productos y la suma interna
T(n)=O(n^2)
"""