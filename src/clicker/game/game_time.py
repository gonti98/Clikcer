import time

from .state import GameState


def time_elapsed(current_game: GameState) -> float:
    return float(time.monotonic() - current_game.started_at)
