def max_rod_profit(prices, rod_len):
    best_profit = []   # best prices per length
    best_combo = []    # best cuts combo per length

    best_profit.append(0)    # length 0 profit = 0
    best_combo.append([])    # no cuts for length 0

    current_len = 1
    while current_len <= rod_len:
        local_best = 0
        chosen_cut = []
        cut_len = 1
        
        while cut_len <= current_len:
            if cut_len > len(prices):
                break
            # Calculate profit if cut of length cut_len is chosen
            profit = prices[cut_len - 1] + best_profit[current_len - cut_len]
            
            # Comparison process with details
            print(f"Comparing profit {profit} (cut length {cut_len}) with current best {local_best} for rod length {current_len}")
            
            if profit > local_best:
                print(f"-> New best profit found: {profit} with cut {cut_len}")
                local_best = profit
                chosen_cut = [cut_len] + best_combo[current_len - cut_len]
            cut_len += 1

        best_profit.append(local_best)
        best_combo.append(chosen_cut)
        current_len += 1

    # Return max profit and cuts for full rod length
    return best_profit[rod_len], best_combo[rod_len]

print("Max profit and cuts✂️:", max_rod_profit([1,5,8,9,10,17,17,20], 8))