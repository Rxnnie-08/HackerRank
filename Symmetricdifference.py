M = int(input())
m_input = input()
N = int(input())
n_input = input()
m_list = list(map(int,m_input.split(" ")))
n_list = list(map(int,n_input.split(" ")))
m_set = set(m_list)
n_set = set(n_list)
answer = m_set^n_set
answer_new = sorted(answer)
for i in answer_new:
    print(i)