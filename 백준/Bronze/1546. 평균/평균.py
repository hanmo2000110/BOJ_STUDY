n = int(input())
l = list( map( int, input().split() ) )

m = max(l)
for i in range(len(l)) :
    l[i] = float(l[i] / m) * 100

print(sum(l)/n)
