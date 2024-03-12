import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)  

    total_cost = 0
    while len(cables) > 1:
        # Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин тоді нам потрібно взяти дві найменші
        min1 = heapq.heappop(cables)
        min2 = heapq.heappop(cables)

        total_cost += min1 + min2
        heapq.heappush(cables, min1 + min2)
    return total_cost

# Код виконується і повертає мінімальну з можливих сум загальних витрат.
cables = [9, 3, 8, 14]
min_cost = min_cost_to_connect_cables(cables)
print("Мін витрати:", min_cost)
