def max_rod_profit(prices, rod_len):

    best_profit = []   # here will be best prices
    best_combo = []    # here will be cuts

    # add dummy zero element for length 0, easier for index math
    best_profit.append(0)
    best_combo.append([])

    # now go step by step for each rod length
    current_len = 1
    while current_len <= rod_len:
        local_best = 0
        chosen_cut = []
        cut_len = 1
        
        while cut_len <= current_len:
            if cut_len > len(prices):
                break
            profit = prices[cut_len - 1] + best_profit[current_len - cut_len]
            if profit > local_best:
                local_best = profit
                chosen_cut = [cut_len] + best_combo[current_len - cut_len]
            cut_len = cut_len + 1

        best_profit.append(local_best)
        best_combo.append(chosen_cut)
        current_len = current_len + 1

    return best_profit[rod_len], best_combo[rod_len]

max_rod_profit([1,5,8,9,10,17,17,20], 8)