import itertools


distances = [
    [0, 1, 2],
    [1, 0, 3],
    [2, 3, 0]
]

def tsp(distances):
    # 全ての都市の順列を生成
    permutations = itertools.permutations(range(len(distances)))

    min_distance = float('inf')
    best_route = None

    for permutation in permutations:
        # 順列の始点と終点をつなげる
        route = permutation + (permutation[0],)
        # 総距離を計算
        total_distance = sum(distances[route[i]][route[i+1]] for i in range(len(distances)))

        # 最短距離を更新
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = permutation

    return best_route, min_distance


print(tsp(distances))