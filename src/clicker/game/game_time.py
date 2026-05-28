import time
from .game_state import GameState


def time_elapsed(current_game: GameState) -> int:
    return int(time.monotonic() - current_game.started_at)

def manual_score_cooldown(current_game: GameState) -> int:
    return int(time.monotonic() - current_game.started_at)
