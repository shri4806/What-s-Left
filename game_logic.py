# Game state for "What's Left"
from events import get_event
game_state = {
    "day": 1,
    "balance": 10000,

     # memory flags
    "discipline": 0,
    "comfort": 0,
    "responsibility": 0,
    "risk": 0,
    "ambition": 0
}

def next_day(state):
    state["day"] += 1
    return state

def apply_event(state):
    event, change = get_event()
    state["balance"] += change
    return event, change, state

def day1_choice(state, choice):
    """
    Day 1 choices:
    1 -> Basic Living
    2 -> Comfortable Start
    3 -> Small Treat
    """

    if choice == 1:
        # Basic Living
        state["balance"] -= 800
        state["discipline"] += 1

    elif choice == 2:
        # Comfortable Start
        state["balance"] -= 1200
        state["comfort"] += 1

    elif choice == 3:
        # Small Treat
        state["balance"] -= 1500
        state["comfort"] += 1
        state["discipline"] -= 1

    return state

def day2_choice(state, choice):
    """
    Day 2 choices:
    1 -> Hold Back
    2 -> Normal Day
    3 -> Convenience Wins
    """

    if choice == 1:
        # Hold Back
        state["balance"] -= 700
        state["discipline"] += 1
        state["risk"] += 1  # frustration builds if repeated

    elif choice == 2:
        # Normal Day
        state["balance"] -= 1000

    elif choice == 3:
        # Convenience Wins
        state["balance"] -= 1300
        state["comfort"] += 1

    return state

def day3_choice(state, choice):
    """
    Day 3 choices:
    1 -> Delay obligation
    2 -> Handle properly
    3 -> Overpay for peace
    """

    if choice == 1:
        # Delay obligation
        state["balance"] -= 900
        state["risk"] += 2  # postponing responsibility is risky

    elif choice == 2:
        # Handle properly
        state["balance"] -= 1400
        state["responsibility"] += 1

    elif choice == 3:
        # Overpay for peace
        state["balance"] -= 1800
        state["responsibility"] += 1
        state["risk"] -= 1  # clears future stress slightly

    return state

def day4_choice(state, choice):
    """
    Day 4 choices:
    1 -> Ignore the issue
    2 -> Fix it normally
    3 -> Preventive action
    """

    if choice == 1:
        # Ignore the issue
        state["balance"] -= 600
        state["risk"] += 2  # this WILL come back later

    elif choice == 2:
        # Fix it normally
        state["balance"] -= 1100
        state["responsibility"] += 1

    elif choice == 3:
        # Preventive action
        state["balance"] -= 1600
        state["responsibility"] += 1
        state["risk"] -= 1  # reduces future escalation

    return state

def day5_choice(state, choice):
    """
    Day 5 choices:
    1 -> Take opportunity (ambition)
    2 -> Play it safe
    3 -> Prepare for uncertainty
    """

    if choice == 1:
        # Career / opportunity event
        state["balance"] -= 1200
        state["ambition"] += 1
        state["risk"] += 1  # lower buffer increases pressure

    elif choice == 2:
        # Play it safe
        state["balance"] -= 800
        state["discipline"] += 1

    elif choice == 3:
        # Prepare for uncertainty
        state["balance"] -= 1000
        state["responsibility"] += 1
        state["risk"] -= 1  # cushions future impact

    return state

def day6_choice(state, choice):
    """
    Day 6 choices:
    1 -> Bare minimum response
    2 -> Responsible handling
    3 -> Eliminate the risk
    """

    # base costs
    if choice == 1:
        state["balance"] -= 700
        state["risk"] += 2

    elif choice == 2:
        state["balance"] -= 1100
        state["responsibility"] += 1

    elif choice == 3:
        state["balance"] -= 1500
        state["responsibility"] += 1
        state["risk"] -= 2

    # consequence of accumulated risk
    if state["risk"] >= 4:
        # problem escalates
        state["balance"] -= 800

    return state

def day7_ending(state):
    """
    Determines the ending based on the week's decisions.
    """

    balance = state["balance"]
    risk = state["risk"]
    responsibility = state["responsibility"]
    ambition = state["ambition"]
    discipline = state["discipline"]
    comfort = state["comfort"]

    # Ending logic
    if balance <= 0:
        return "You made it through the week, but completely drained your buffer."

    if risk >= 4 and responsibility <= 1:
        return "Things piled up. You spent the week reacting instead of preparing."

    if ambition >= 1 and balance < 2000:
        return "You chased growth knowing it would cost you. The week was heavy, but meaningful."

    if discipline >= 2 and comfort <= 1:
        return "You stayed careful and controlled. You survived without unnecessary damage."



