A = 'abcdeg'
B = 'hijklm'
C = 'ahbcdijklmeg'

A1 = 'aabcc'
B1 = 'dbbca'
C1 = 'aadbbcbcac'


# Below function fails at test case A1,B1,C1 though it passes for A,B,C
def find_interleaving(A, B, C):
    if (len(A) == 0):
        return B == C
    elif (len(B) == 0):
        return A == C
    else:
        if (len(C) == 0):
            return False

        if (C[0] == A[0]):
            return find_interleaving(A[1:], B, C[1:])
        elif (C[0] == B[0]):
            return find_interleaving(A, B[1:], C[1:])
        else:
            return False


# This function passes the both test cases A1,B1,C1 / A,B,C
def is_interleaving(A1, B1, C1):
    if (len(A) == 0):
        return B == C
    elif (len(B) == 0):
        return A == C
    else:
        if (len(C) == 0):
            return False

        if (C[0] == A[0] and C[0] == B[0]):
            return find_interleaving(A[1:], B, C[1:]) or find_interleaving(A, B[1:], C[1:])
        elif (C[0] == A[0]):
            return find_interleaving(A[1:], B, C[1:])
        elif (C[0] == B[0]):
            return find_interleaving(A, B[1:], C[1:])
        else:
            return False


print(find_interleaving(A, B, C))
print(is_interleaving(A, B, C))
print(find_interleaving(A1, B1, C1))
print(is_interleaving(A1, B1, C1))