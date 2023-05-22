"""first_line = list(map(int, input().split()))
second_line = int(input())

sequence = [str(i) for i in range(len(first_line)) if first_line[i] == second_line]
if sequence:
    print(" ".join(sequence))
else:
    print("not found")




"""
sequence = (input("s").split())
x = input("a")

sc = [str(i) for i in range(len(sequence))if sequence[i] == x]
print(" ".join(sc) if sc else "not found")
