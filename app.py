from game_logic import game_state, next_day


print("Day:", game_state["day"])
print("Starting balance:", game_state["balance"])

next_day(game_state)
print("After moving to next day:", game_state["day"])

