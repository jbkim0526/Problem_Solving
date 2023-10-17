# https://www.acmicpc.net/problem/14889
import sys
from itertools import combinations
input = sys.stdin.readline

def init():
    """입력 처리 

    Returns:
        list: 능력치 graph 
    """
    totalnum = int(input())
    stat_graph = [list(map(int, input().split())) for _ in range(totalnum)]

    return [totalnum, stat_graph]


def run():
    totalnum, stat_graph = init()
    rows_sum = [sum(row) for row in stat_graph]
    cols_sum = [sum(col) for col in zip(*stat_graph)] #zip(*graph): graph의 각 열
    stat_per_member = [i+j for i, j in zip(rows_sum, cols_sum)] 
    total_stat = sum(rows_sum)
    
    min_score = total_stat
    for stat in combinations(stat_per_member, totalnum //2):
        val = abs(total_stat - sum(stat))
        if val < min_score:
            min_score = val
    print(min_score)         
    
run()