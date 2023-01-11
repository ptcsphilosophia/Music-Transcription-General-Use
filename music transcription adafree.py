
"""Dictionaries for duration and tone"""

duration_dict = {
    "Whole note": 1,
    "Half note": .5,
    "Quarter note": .25,
    "Eighth note": .125,
    "Sixteenth note": .0625,
    "Thirty-second note": .03125,
    }

tone_dict = {
    "Rest": 0,
    "C0": 16.35,
    "C#0": 17.32,
    "DFLAT0": 17.32,
    "D0": 18.35,
    "D#0": 19.45,
    "EFLAT0": 19.45,
    "E0": 20.60,
    "F0": 21.83,
    "F#0": 23.12,
    "GFLAT0": 23.12,
    "G0": 24.50,
    "G#0": 25.96,
    "AFLAT0": 25.96,
    "A0": 27.5,
    "A#0": 29.14,
    "BFLAT0": 29.14,
    "B0": 30.87,
    "C1": 32.70,
    "C#1": 34.65,
    "DFLAT1": 34.65,
    "D1": 36.71,
    "D#1": 38.89,
    "EFLAT1": 38.89,
    "E1": 41.20,
    "F1": 43.65,
    "F#1": 46.25,
    "GFLAT1": 46.25,
    "G1": 49.00,
    "G#1": 51.91,
    "A1": 55.00,
    "A#1": 58.27,
    "BFLAT1": 58.27,
    "B1": 61.74,
    "C2": 65.41,
    "C#2": 69.30,
    "DFLAT2": 69.30,
    "D2": 73.42,
    "D#2": 77.78,
    "EFLAT2": 77.78,
    "E2": 82.41,
    "F2": 87.31,
    "F#2": 92.50,
    "GFLAT2": 92.50,
    "G2": 98.00,
    "G#2": 103.83,
    "AFLAT2": 103.83,
    "A2": 110.00,
    "A#2": 110.00,
    "BFLAT2": 110.00,
    "B2": 123.47,
    "C3": 130.81,
    "C#3": 138.59,
    "DFLAT3": 138.59,
    "D3": 146.83,
    "D#3": 155.56,
    "EFLAT3": 155.56,
    "E3": 164.81,
    "F3": 174.61,
    "F#3": 185.00,
    "GFLAT3": 185.00,
    "G3": 196.00,
    "G#3": 207.65,
    "AFLAT3": 207.65,
    "A3": 220.00,
    "A#3": 233.08,
    "BFLAT3": 233.08,
    "B3": 246.94,
    "C4": 261.63,
    "C#4": 277.18,
    "DFLAT4": 277.18,
    "D4": 293.66,
    "D#4": 311.13,
    "EFLAT4": 311.13,
    "E4": 329.63,
    "F4": 349.23,
    "F#4": 369.99,
    "GFLAT4": 369.99,
    "G4": 392.00,
    "G#4": 415.30,
    "A4": 440.00,
    "A#4": 466.16,
    "BFLAT4": 466.16,
    "B4": 493.88,
    "C5": 523.25,
    "C#5": 554.37,
    "DFLAT5": 554.37,
    "D5": 587.33,
    "D#5": 622.25,
    "EFLAT5": 622.25,
    "E5": 659.25,
    "F5": 698.46,
    "F#5": 739.99,
    "GFLAT5": 739.99,
    "G5": 783.99,
    "G#5": 830.61,
    "AFLAT5": 830.61,
    "A5": 880.00,
    "A#5": 932.33,
    "BFLAT5": 932.33,
    "B5": 987.77,
    "C6": 1046.50,
    "C#6": 1108.73,
    "DFLAT6": 1108.73,
    "D6": 1174.66,
    "D#6": 1244.51,
    "EFLAT6": 1244.51,
    "E6": 1318.51,
    "F6": 1396.91,
    "F#6": 1479.98,
    "GFLAT6": 1479.98,
    "G6": 1567.98,
    "G#6": 1661.22,
    "AFLAT6": 1661.22,
    "A6": 1760.00,
    "A#6": 1864.66,
    "BFLAT6": 1864.66,
    "B6": 1975.53,
    "C7": 2093.00,
    "C#7": 2217.46,
    "DFLAT7": 2217.46,
    "D7": 2349.32,
    "D#7": 2489.02,
    "EFLAT7": 2489.02,
    "E7": 2637.02,
    "F7": 2793.83,
    "F#7": 2959.96,
    "GFLAT7": 2959.96,
    "G7": 3135.96,
    "G#7": 3322.44,
    "A7": 3520.00,
    "A#7": 3729.31,
    "BFLAT7": 3729.31,
    "B7": 3951.07,
    "C8": 4186.01,
    "C#8": 4434.92,
    "DFLAT8": 4434.92,
    "D8": 4698.63,
    "D#8": 4978.03,
    "EFLAT8": 4978.03,
    "E8": 5274.04,
    "F8": 5587.65,
    "F#8": 5919.91,
    "GFLAT8": 5919.91,
    "G8": 6271.93,
    "G#8": 6644.88,
    "AFLAT8": 6644.88,
    "A8": 7040.00,
    "A#8": 7458.62,
    "BFLAT8": 7458.62,
    "B8": 7902.13,
    }

""" Meat and potatoes function that initally calls the note_for_dict function 
that returns a usable string to be used for the frequency dictionary. 
When choosing the note length, two variables call two functions (duration and frequency) 
and these variables are appended to list as a pair for the final playback."""


def note_and_duration_menu(note, bpm):
    note_octave = note_for_dict(note)
    print(f"You have chosen {note_octave}.")
    while True:
        note_length_menu()
        try:
            note_length_user_selection = int(input(f"Please make select an note length for {note_octave}."))
        except ValueError:
            print("Please make a valid selection.")
        if note_length_user_selection == 7:
            print("Thank you.  We are returning to the note selection menu.")
            break
        elif note_length_user_selection == 1:
            print(f"You have selected Whole Note for {note_octave}.")
            whole_note_selection = duration_dict["Whole note"]
            print(whole_note_selection)
            note_frequency = note_to_frequency(note_octave)
            note_duration_var = duration(bpm, whole_note_selection)
            test_list.append((note_frequency, note_duration_var))
            print(test_list)
            break
        elif note_length_user_selection == 2:
            print(f"You have selected Half note for {note_octave}.")
            half_note_selection = duration_dict["Half note"]
            print(half_note_selection)
            note_frequency = note_to_frequency(note_octave)
            note_duration_var = duration(bpm, half_note_selection)
            test_list.append((note_frequency, note_duration_var))
            print(test_list)
            break
        elif note_length_user_selection == 3:
            print(f"You have selected Quarter note for {note_octave}.")
            quarter_note_selection = duration_dict["Quarter note"]
            print(quarter_note_selection)
            note_frequency = note_to_frequency(note_octave)
            note_duration_var = duration(bpm, quarter_note_selection)
            test_list.append((note_frequency, note_duration_var))
            print(test_list)
            break
        elif note_length_user_selection == 4:
            print(f"You have selected Eighth note for {note_octave}.")
            eighth_note_selection = duration_dict["Eighth note"]
            print(eighth_note_selection)
            note_frequency = note_to_frequency(note_octave)
            note_duration_var = duration(bpm, eighth_note_selection)
            test_list.append((note_frequency, note_duration_var))
            print(test_list)
            break
        elif note_length_user_selection == 5:
            print(f"You have selected Sixteenth note for {note_octave}.")
            sixteenth_note_selection = duration_dict["Sixteenth note"]
            print(sixteenth_note_selection)
            note_frequency = note_to_frequency(note_octave)
            note_duration_var = duration(bpm, sixteenth_note_selection)
            test_list.append((note_frequency, note_duration_var))
            print(test_list)
            break
        elif note_length_user_selection == 6:
            print(f"You have selected Thirty-second note for {note_octave}.")
            thirty_second_note_selection = duration_dict["Thirty-second note"]
            print(thirty_second_note_selection)
            note_frequency = note_to_frequency(note_octave)
            note_duration_var = duration(bpm, thirty_second_note_selection)
            test_list.append((note_frequency, note_duration_var))
            print(test_list)
            break


"""Main menu.  BPM must be chosen before writing music. Each note selection calls note_duration_menu.  Other selections
are self evident and call their respective functions."""


def menu():
    bpm = 0
    while True:
        print_menu()
        print("Please make a selection.")
        try:
            user_selection = int(input("What is your selection?"))
        except ValueError:
            print("Please enter a valid selection.")
            continue
        if user_selection == 7:
            print("Thank you for using the CS49 music transcription program.  Have a great day!")
            break
        elif user_selection == 1:
            bpm = int(input("What bpm would you like to use?"))
            print(f"You have chosen {bpm} beats per minute.")
        elif user_selection == 2:
            print("You have chosen to write music.")
            if bpm == 0:
                print("Please go set the bpm/tempo of the song.")
            else:
                while True:
                    note_menu()
                    try:
                        note_selection = int(input("Please make a selection."))
                    except ValueError:
                        print("Please make a valid choice.")
                        continue
                    if note_selection == 9:
                        print("Thank you.  Returning to main menu.")
                        break
                    elif note_selection == 1:
                        c = "C"
                        print(f"You have chosen {c}.")
                        note_and_duration_menu(c, bpm)
                    elif note_selection == 2:
                        d = "D"
                        print(f"You have chosen {d}.")
                        note_and_duration_menu(d, bpm)
                    elif note_selection == 3:
                        e = "E"
                        print(f"You have chosen {e}.")
                        note_and_duration_menu(e, bpm)
                    elif note_selection == 4:
                        f = "F"
                        print(f"You have chosen {f}.")
                        note_and_duration_menu(f, bpm)
                    elif note_selection == 5:
                        g = "G"
                        print(f"You have chosen {g}.")
                        note_and_duration_menu(g, bpm)
                    elif note_selection == 6:
                        a = "A"
                        print(f"You have chosen {a}.")
                        note_and_duration_menu(a, bpm)
                    elif note_selection == 7:
                        b = "B"
                        print(f"You have chosen {b}.")
                        note_and_duration_menu(b, bpm)
                    elif note_selection == 8:
                        rest = "Rest"
                        print(f"You have chosen {rest}.")
                        note_and_duration_menu(rest, bpm)
        elif user_selection == 3:
            display_list(test_list)
        elif user_selection == 4:
            print("Under testing. Unavailable")
        elif user_selection == 5:
            write_to_text(test_list)
        elif user_selection == 6:
            print("Under testing. Unavailable.")


"""Returns a note string that can be used as the key for the dictionary"""


def note_for_dict(note_type):
    if note_type == "Rest":
        note_to_freq = note_type
        return note_to_freq
    else:
        octave_var = octave_check()
        sharp_var = sharp_flat(note_type)
        note_to_freq = sharp_var + octave_var
        return note_to_freq


"""Prompts user to choose a valid octave for their note. """


def octave_check():
    octave_check_var = input("Please enter a valid octave (1-8).")
    while octave_check_var == "9":
        print("9 isn't a valid octave.")
        octave_check_var = input(f"Please choose a valid octave.")
    while not octave_check_var.isdigit():
        print("Please enter a valid number.")
        octave_check_var = input("Please choose a valid octave.")
    return octave_check_var


""" Prompts user to whether they want the note to be sharp or not. 
New Sharp/Flat function"""


def sharp_flat(sharp_check):
    non_sharps = ["B", "E"]
    non_flats = ["C", "F"]
    while True:
        sharp_flat_menu(sharp_check)
        try:
            sharp_flat_input = int(input(f"Note: {sharp_check}. Would You like {sharp_check} to be regular, sharp or flat?"))
        except ValueError:
            print("Integers only please")
        if sharp_flat_input == 1:
            print(f"You have chosen {sharp_check}")
            return sharp_check
        elif sharp_flat_input == 2:
            if sharp_check in non_flats:
                print("C and F don't have flats")
            else:
                sharp_check = sharp_check + "FLAT"
                print(f"You have chosen {sharp_check}")
                print(type(sharp_check))
                return sharp_check
        elif sharp_flat_input == 3:
            if sharp_check in non_sharps:
                print("B and E don't have sharps")
            else:
                sharp_check = sharp_check + "#"
                print(f"You have chosen {sharp_check}")
                print(type(sharp_check))
                return sharp_check


"""Old Sharp function"""


def sharp(note):
    sharps = ["C", "D", "F", "G", "A"]
    # while note in sharps:
    if note in sharps:
        # sharp_input = input(f"{note} Sharp? Y/N?")
        sharp_input = ""
        while not sharp_input == "Y" or "N":
            print("Please enter Y or N.")
            sharp_input = input(f"{note} Sharp? Y/N?")
            if sharp_input == "Y":
                note = note + "#"
                return note
            elif sharp_input == "N":
                return note
    else:
        return note


"""Print menus."""


def print_menu():
    print("1 - Set BPM/Tempo")
    print("2 - Write Music")
    print("3 - Display Notes/Duration Tuples in List")
    print("4 - Play Tones in List")
    print("5 - Write music to text file")
    print("6 - Play music from text file")
    print("7 - Quit")


def note_menu():
    print("Please make select a note.")
    print("1 - C")
    print("2 - D")
    print("3 - E")
    print("4 - F")
    print("5 - G")
    print("6 - A")
    print("7 - B")
    print("8 - Rest")
    print("9 - Go back")


def note_length_menu():
    print("1 - Whole note")
    print("2 - Half note")
    print("3 - Quarter note")
    print("4 - Eighth note")
    print("5 - Sixteenth note")
    print("6 - Thirty-second note")
    print("7 - Go back")


def sharp_flat_menu(note):
    print("Remember:  B/E don't have sharps and C/F don't have flats.")
    print(f"1 - {note}, no flat or sharp.")
    print(f"2 - {note} Flat")
    print(f"3 - {note} Sharp")


"""Duration and note to frequency functions."""


def duration(bpm: int, note_length):
    note_time_length = (240 / bpm) * note_length
    return note_time_length


def note_to_frequency(note: str):
    if note == "Rest":
        new_note = tone_dict[note]
        return new_note
    elif note.isupper():
        new_note = tone_dict[note]
        return new_note
    elif note.islower():
        note = note.upper()
        new_note = tone_dict[note]
        return new_note


"""Other menu option functions including display list, play notes in list, write to txt file and play from text file."""


def display_list(list_arg):
    print(f"Here is the music currently in the list. \n {list_arg}")
    for item in range(len(list_arg)):
        print(f"{item}: {list_arg[item]}")
    return list_arg


def write_to_text(list):
    with open(r'C:\Users\User\PycharmProjects\New_Text_Document.txt', 'w') as f:
        for line in list:
            f.write(f"{line}")
            f.write("\n")
        print(f"The note/duration pairs in {list} have been saved to text file.")


test_list = []


def main():
    menu()


if __name__ == '__main__':
    main()