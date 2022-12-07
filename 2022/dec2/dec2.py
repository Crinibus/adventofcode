import pathlib
from dataclasses import dataclass

move_score = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}


class Move:
    def __init__(self, letter) -> None:
        self.move = letter
        self.move_score = move_score.get(self.move)


    @staticmethod
    def fight(elf_move: "Move", player_move: "Move") -> "PlayerResult":
        winning_moves = {
            "A": "Y",
            "B": "Z",
            "C": "X",
            "Y": "A",
            "Z": "B",
            "X": "C",
        }

        player_winning_move = winning_moves.get(elf_move.move)

        is_draw = elf_move.move_score == player_move.move_score
        player_won = player_move.move == player_winning_move
        player_fight_score = 6 if player_won else 3 if is_draw else 0

        return PlayerResult(is_draw, player_won, player_move, player_fight_score)


@dataclass
class PlayerResult:
    is_draw: bool
    player_won: bool
    player_move: Move
    player_fight_score: int


def get_input() -> list[str]:
    root_path = pathlib.Path(__file__).parent.absolute()

    with open(f"{root_path}/input.txt", "r") as input_file:
        input_raw = input_file.readlines()

    return [line.strip() for line in input_raw]


def get_fights(input_data: list[str]) -> tuple[tuple[Move, Move]]:
    fights: list[tuple[Move, Move]] = []

    for line in input_data:
        elf_move, my_move = line.split(" ")
        fight = (Move(elf_move), Move(my_move))
        fights.append(fight)

    return fights


def get_answer_part_1(input_data):
    fights = get_fights(input_data)

    result_scores: list[int] = []

    for fight in fights:
        elf_move = fight[0]
        player_move = fight[1]

        result = Move.fight(elf_move, player_move)
        # print(f"{result.is_draw=}")
        # print(f"{result.player_won=}")
        # print(f"{result.player_fight_score=}")
        # print(f"{result.player_move.move_score=}")
        # print(f"Score={result.player_fight_score + result.player_move.move_score}")

        score = result.player_move.move_score + result.player_fight_score
        result_scores.append(score)

    return sum(result_scores)


def get_answer_part_2(input_data):
    pass


def main():
    input_data = get_input()

    answer1 = get_answer_part_1(input_data)
    answer2 = get_answer_part_2(input_data)

    print(f"Part 1 answer: {answer1}")
    print(f"Part 2 answer: {answer2}")


if __name__ == "__main__":
    main()
