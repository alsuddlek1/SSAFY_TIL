## powerset

def backtrac(a,k,input):
    global  MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a,k)
    else:
        k += 1
        ncadidates = construct_candidates(a,k,input, c)
        for i  in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def construct_candidates(a,k,input,c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
backtrac(a,0,3)