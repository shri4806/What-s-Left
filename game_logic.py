# Game state for "What's Left"

game_state = {
    "day": 1,
    "balance": 10000
}

def next_day(state):
    state["day"] += 1
    return state
