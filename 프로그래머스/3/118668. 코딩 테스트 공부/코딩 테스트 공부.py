from collections import deque
import heapq
def solution(alp, cop, problems):
    problems = [(0,0,1,0,1), (0,0,0,1,1)] + problems
    goal_alp = 0
    goal_cop = 0
    
    
    for itm in problems:
        goal_alp = max(goal_alp, itm[0])
        goal_cop = max(goal_cop, itm[1])
    skills = dict()
    skills[(alp, cop)] = 0
    
    
    hq = [(0, alp, cop)]
    ans = max(0, goal_cop - cop) + max(0, goal_alp - alp)

    while hq:
        cur_cost, cur_alp, cur_cop = heapq.heappop(hq)
        if skills[(cur_alp, cur_cop)] < cur_cost:
            continue
            
        for req_alp, req_cop, gain_alp, gain_cop, req_cost in problems:
            if req_alp <= cur_alp and req_cop <= cur_cop:
                next_cost, next_alp, next_cop = req_cost + cur_cost, cur_alp + gain_alp, cur_cop + gain_cop
                # 답 조건 되면 더 이상 안함
                if goal_cop <= next_cop and goal_alp <= next_alp:
                    ans = min(next_cost, ans)
                    continue
                # 더 풀어도 의미 없는 문제
                if (gain_cop == 0 and next_alp >= goal_alp) or (gain_alp == 0 and next_cop >= goal_cop) :
                    continue
                
                # 최악 보다 더 오래 걸리는 문제
                if ans <= next_cost:
                    continue
                
                # 처음 갖는 스펙
                if (next_alp, next_cop) not in skills:
                    skills[(next_alp, next_cop)] = next_cost
                    heapq.heappush(hq, (next_cost, next_alp, next_cop))
                # 갱신되는 스펙
                elif next_cost < skills[(next_alp, next_cop)]:
                    skills[(next_alp, next_cop)] = next_cost
                    heapq.heappush(hq, (next_cost, next_alp, next_cop))
    
    return ans
