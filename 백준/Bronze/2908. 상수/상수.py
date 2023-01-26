n1,n2 = map(lambda x: reversed(str(x)) ,input().split())
print(max("".join(n1),"".join(n2)))