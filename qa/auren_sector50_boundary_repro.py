"""AUREN issue #133: deterministic floating-point sector boundary reproduction.

Usage:
    # Inside the AUREN checkout (requires pandas and engine package):
    python /path/to/auren_sector50_boundary.py

Expected: current AUREN code prints 35/Medium then 20/Low, though both
portfolios have exactly the same weights. This is a reproducer, NOT a
verified fix or a paid bounty award.
AI assistance was used in the analysis and script preparation.
"""
from __future__ import annotations

import pandas as pd

from engine.metrics import concentration, sector_exposure
from engine.score import risk_score

WEIGHTS_PCT = {"NVDA": 17, "MSFT": 28, "AAPL": 5, "AMD": 25, "TSM": 25}
ORDERS = [
    ("NVDA", "MSFT", "AAPL", "AMD", "TSM"),
    ("NVDA", "AAPL", "MSFT", "AMD", "TSM"),
]


def analyze(order: tuple[str, ...]) -> tuple[float, int, str]:
    weights = pd.Series({ticker: WEIGHTS_PCT[ticker] for ticker in order}, dtype=float)
    weights = weights / weights.sum()  # Same normalization used by AUREN's API.
    exposures = sector_exposure(weights)
    top_group = float(exposures["Big Tech"])
    score, level, _ = risk_score(
        conc=concentration(weights),
        vol=0.31,
        mdd=-0.10,
        pairs=[],
        sector_max=float(exposures.max()),
    )
    return top_group, score, level


if __name__ == "__main__":
    left, right = (analyze(order) for order in ORDERS)
    for order, result in zip(ORDERS, [left, right]):
        print(order, "Big Tech:", repr(result[0]), "score:", result[1], "level:", result[2])

    assert left == (0.5000000000000001, 35, "Medium"), left
    assert right == (0.5, 20, "Low"), right
    print("REPRODUCED: asset order changes strict >50% test despite identical weights.")
    print("EXPECTED AFTER FIX: both cases return (0.5, 20, 'Low').")
