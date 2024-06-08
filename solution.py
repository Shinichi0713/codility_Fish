# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 魚の動きのシミュレーション
def solution(A, B):
    # Implement your solution here
    C = [0 for i in range(len(B))]
    for i in range(len(B)):
        # meetするか確認
        if B[i]==0:
            C[i]=i-1
            if C[i] < 0:
                C[i] = 0
        else:
            C[i]=i+1
    while True:
        is_change = 0
        for i in range(len(B) - 1):
            if A[i] == 0 or A[i+1] == 0:
                continue
            if C[i] <= C[i+1]:
                if A[i] > A[i+1]:
                    A[i] = 0
                    C[i] += 1
                    is_change = 1
                else:
                    A[i+1] = 0
                    C[i] += -1
                    is_change = 1
        if is_change == 0:
            break
    num_alive = 0
    for i in range(len(A)):
        if A[i] > 0:
            num_alive += 1
    return num_alive
        