from game_logic import (
    game_state,
    day1_choice,
    day2_choice,
    day3_choice,
    day4_choice,
    day5_choice,
    day6_choice,
    day7_ending,
    next_day
)

# -------- DAY 1 --------
game_state = day1_choice(game_state, 1)
next_day(game_state)

# -------- DAY 2 --------
game_state = day2_choice(game_state, 3)
next_day(game_state)

# -------- DAY 3 --------
game_state = day3_choice(game_state, 2)
next_day(game_state)

# -------- DAY 4 --------
game_state = day4_choice(game_state, 1)
next_day(game_state)

# -------- DAY 5 --------
game_state = day5_choice(game_state, 1)
next_day(game_state)

# -------- DAY 6 --------
game_state = day6_choice(game_state, 1)
next_day(game_state)

# -------- DAY 7 --------
ending = day7_ending(game_state)

print("\n--- WEEK COMPLETE ---")
print("Final Balance:", game_state["balance"])
print("Ending:")
print(ending)





