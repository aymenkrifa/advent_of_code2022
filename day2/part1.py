import pandas as pd
from helpers import rock_paper_scissors, calculate_score

df = pd.read_csv("input_data.txt", sep=" ", header=None, names=["opponent", "me"])

shape = {
    "opponent": {"A": "rock", "B": "paper", "C": "scissors"},
    "me": {"X": "rock", "Y": "paper", "Z": "scissors"},
}

scores = {
    "choice": {"rock": 1, "paper": 2, "scissors": 3},
    "outcome": {"loss": 0, "draw": 3, "win": 6},
}

for column in df.columns:
    df[column].replace(shape[column], inplace=True)


df["outcome"] = df.apply(lambda x: rock_paper_scissors(x.opponent, x.me), axis=1)


print("Day 2 | Part 1 result:", calculate_score(df, scores))
