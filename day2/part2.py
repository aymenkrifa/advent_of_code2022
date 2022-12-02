import pandas as pd
from helpers import me_choice, calculate_score

df = pd.read_csv("input_data.txt", sep=" ", header=None, names=["opponent", "outcome"])

shape = {
    "opponent": {"A": "rock", "B": "paper", "C": "scissors"},
    "outcome": {"X": "lose", "Y": "draw", "Z": "win"},
}

scores = {
    "choice": {"rock": 1, "paper": 2, "scissors": 3},
    "outcome": {"lose": 0, "draw": 3, "win": 6},
}

for column in df.columns:
    df[column].replace(shape[column], inplace=True)

df["me"] = df.apply(lambda x: me_choice(x.opponent, x.outcome), axis=1)

print("Day 2 | Part 2 result:", calculate_score(df, scores))
