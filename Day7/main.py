from functools import cmp_to_key

f = open("Day7/input", 'r')
lst = []
for line in f:
    word = line.rstrip("\n").split()
    word[1] = int(word[1])
    lst.append(word)
f.close()

# Part 1
order = "AKQJT98765432"

def get_hand_value(hand):
    cards = {}
    for c in hand:
        if c in cards: cards[c] += 1
        else: cards[c] = 1
    if 5 in cards.values(): return 7 # Five of a kind
    if 4 in cards.values(): return 6 # Four of a kind
    if 3 in cards.values() and 2 in cards.values(): return 5 # Full House
    if 3 in cards.values(): return 4 # Three of a kind
    if sum([value == 2 for value in cards.values()]) == 2: return 3 # Two pairs
    if 2 in cards.values(): return 2 # One pair
    if 1 in cards.values(): return 1 # High card
    return 0 # Only jokers for part 2

def compare_hands(one, two):
    if get_hand_value(one[0]) == get_hand_value(two[0]):
        for i in range(5):
            if order.index(one[0][i]) != order.index(two[0][i]):
                return order.index(one[0][i]) - order.index(two[0][i])
    return get_hand_value(two[0]) - get_hand_value(one[0])

def count_winnings(rule):
    sorted_lst = sorted(lst, key=cmp_to_key(rule))
    total_winnings = 0
    for i in range(len(sorted_lst)):
        total_winnings += sorted_lst[i][1]*(len(sorted_lst)-i)
    return total_winnings

print("The total winnings are", count_winnings(compare_hands))

# Part 2
new_order = "AKQT98765432J"

def get_hand_value_joker(hand):
    joker_count = hand.count("J")
    hand_value = get_hand_value(hand.replace("J", ""))
    for _ in range(joker_count):
        if hand_value in [2,3,4]: hand_value += 2
        else: hand_value += 1
    return hand_value

def compare_hands_joker(one, two):
    if get_hand_value_joker(one[0]) == get_hand_value_joker(two[0]):
        for i in range(5):
            if new_order.index(one[0][i]) != new_order.index(two[0][i]):
                return new_order.index(one[0][i]) - new_order.index(two[0][i])
    return get_hand_value_joker(two[0]) - get_hand_value_joker(one[0])

print("The total winnings with new joker rules are", count_winnings(compare_hands_joker))
