class Note:
    button: int
    def __init__(self, button: int) -> None:
        self.button = button

def compute_score(
        song: list[Note | None],
        player_inputs: list[Note | None]) -> int:
    score = 0
    for i in range(len(song)):
        song_note = song[i]
        player_note = player_inputs[i]
        if song_note is not None and player_note is not None and \
            song_note.button == player_note.button:
                score += 1
    return score

def main() -> None:
    song = [Note(1), Note(5), Note(5), None, Note(4), Note(3), None, Note(2)]
    
    player_inputs = [Note(1), None, Note(4), None, Note(4), Note(2),
            Note(2), Note(2)]

    score = compute_score(song, player_inputs)

    print(score)

if __name__ == '__main__':
    main()
