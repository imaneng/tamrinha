

def count_blue_cells(n, m):
    if n == 0 or m == 0:
        return 0
 
    if n == 2 and m == 2:
        return 2
 
    if n > m:
        if m == 1 and n % 3 == 1:
            return n//3 + 1
 
        return (n//3)*m + count_blue_cells(n-n//3*3, m)
 
    else:
        if n == 1 and m % 3 == 1:
            return m//3 + 1
 
        return (m//3)*n + count_blue_cells(m-m//3*3, n)
 
 

if __name__ == "__main__":
    tests = int(input())
    for _ in range(tests):
       a = int(input("tool ra vared konidd: ")) 
       b = int(input("arz ra vared konidd: "))
       print(count_blue_cells(a, b))