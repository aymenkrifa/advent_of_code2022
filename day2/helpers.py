from pandas import DataFrame, Series


def rock_paper_scissors(opp: Series, me: Series) -> str:
    """
    Generate the outcome of the game given both players' scors

    Parameters
    ----------
    opp : pandas.Series
        Opponent player's choice
    me : pandas.Series
        My choice

    Returns
    -------
    str
        Return the outcome of the game whether it's a draw, win or loss
    """

    if me == opp:
        return "draw"
    elif me == "rock":
        if opp == "scissors":
            return "win"
        else:
            return "loss"
    elif me == "paper":
        if opp == "rock":
            return "win"
        else:
            return "loss"
    elif me == "scissors":
        if opp == "paper":
            return "win"
        else:
            return "loss"


def me_choice(opp: Series, outcome: Series) -> str:
    """
    Generate my choice of the game given the opponent's choice
    and the outcome of the game.

    Parameters
    ----------
    opp : pandas.Series
        Opponent player's choice
    outcome : pandas.Series
        The outcome of the game

    Returns
    -------
    str
        Return my right choice, whether I have to choose rock, paper or scissors
    """

    if outcome == "draw":
        return opp
    if outcome == "win":
        if opp == "rock":
            return "paper"
        elif opp == "paper":
            return "scissors"
        else:
            return "rock"

    else:
        if opp == "rock":
            return "scissors"
        elif opp == "paper":
            return "rock"
        else:
            return "paper"


def calculate_score(df: DataFrame, scores: dict) -> int:
    """
    Calculate total final score

    Parameters
    ----------
    df : DataFrame
        The input data
    scores : dict
        Scores mapper

    Returns
    -------
    int
        The final total score
    """
    dataframe = df.copy()

    dataframe["win_lose_score"] = dataframe["outcome"].map(
        lambda x: scores["outcome"][x]
    )
    dataframe["choice_score"] = dataframe["me"].map(lambda x: scores["choice"][x])

    dataframe["total_score"] = dataframe["win_lose_score"] + dataframe["choice_score"]
    return dataframe["total_score"].sum()
