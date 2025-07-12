import pretty_midi

def sequence_to_midi(seq, filename="fibonacci.mid"):
    midi = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano

    start_time = 0
    for num in seq:
        pitch = 60 + (num % 24)  # C4 = 60, 두 옥타브 범위
        duration = 0.5  # 고정된 길이
        note = pretty_midi.Note(
            velocity=100,
            pitch=pitch,
            start=start_time,
            end=start_time + duration
        )
        piano.notes.append(note)
        start_time += duration

    midi.instruments.append(piano)
    midi.write(filename)
    return filename
