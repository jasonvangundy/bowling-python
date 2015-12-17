from robber import expect
from src import bowling


def test_first_roll_records_roll1_in_first_frame():
    game = bowling.Game()
    game.roll(3)
    expect(game.build_score()).to.eq(3)
    expect(game.frames).to.have.length(1)


def test_second_roll_records_roll2_in_first_frame():
    game = bowling.Game()
    game.roll(3)
    game.roll(5)
    expect(game.build_score()).to.eq(8)
    expect(game.frames).to.have.length(1)


def test_frame_is_complete_after_strike():
    game = bowling.Game()
    game.roll(10)
    game.roll(1)
    expect(game.frames).to.have.length(2)


def test_scores_multiple_frames_without_marks():
    game = bowling.Game()
    game.roll(5)
    game.roll(3)
    game.roll(2)
    game.roll(1)
    expect(game.build_score()).to.eq((5 + 3) + (2 + 1))


def test_scores_strike_from_previous_frame():
    game = bowling.Game()
    game.roll(10)
    game.roll(1)
    expect(game.build_score()).to.eq((10 + 1) + 1)


def test_scores_multiple_strikes_in_a_row():
    game = bowling.Game()
    game.roll(10)
    game.roll(10)
    game.roll(10)
    expect(game.build_score()).to.eq((10 + 10 + 10) + (10 + 10) + 10)


def test_strike_in_first_frame_scores_10():
    game = bowling.Game()
    game.roll(10)
    game.roll(0)
    expect(game.build_score()).to.eq((10 + 0) + 0)
    expect(game.frames).to.have.length(2)


def test_scores_spare_from_previous_frame():
    game = bowling.Game()
    game.roll(9)
    game.roll(1)
    game.roll(4)
    game.roll(3)
    expect(game.build_score()).to.eq((9 + 1 + 4) + (4 + 3))


def test_scores_game():
    game = bowling.Game()
    for i in range(1, 21):
        game.roll(4)

    expect(game.build_score()).to.eq(4 * 20)


def test_scores_final_frame_with_spare():
    game = bowling.Game()
    for i in range(0,18):
        game.roll(4)

    game.roll(9)
    game.roll(1)
    game.roll(5)
    expect(game.build_score()).to.eq((4 * 18) + (9 + 1) + 5)


def test_scores_final_frame_with_strike_and_non_marks():
    game = bowling.Game()
    for i in range(0, 18):
        game.roll(4)

    game.roll(10)
    game.roll(1)
    game.roll(1)
    expect(game.build_score()).to.eq((4 * 18) + (10 + 1 + 1))


def test_scores_final_frame_with_strikeout():
    game = bowling.Game()
    for i in range(0,18):
        game.roll(4)

    game.roll(10)
    game.roll(10)
    game.roll(10)
    expect(game.build_score()).to.eq(102)


def test_scores_perfect_game():
    game = bowling.Game()
    for i in range(0, 20):
        game.roll(10)

    expect(game.build_score()).to.eq(300)
