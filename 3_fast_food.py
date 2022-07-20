from collections import deque

quantity = int(input())
orders = list(map(int, input().split()))
queue = deque(orders)
sum_of_served_food = 0
print(max(orders))
enough_quantity = True
while queue:
    if sum_of_served_food + queue[0] <= quantity:
        sum_of_served_food += queue.popleft()
    else:
        enough_quantity = False
        break
if enough_quantity:
    print("Orders complete")
else:
    left_orders = []
    while queue:
        left_orders.append(str(queue.popleft()))
    print(f"Orders left: {' '.join(left_orders)}")





#      if sum_of_served_food >= quantity:
#         print("Orders complete")
#         enough_quantity = True
#         break
# if not enough_quantity:
#     print(queue)







