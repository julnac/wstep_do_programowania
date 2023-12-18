def select_lines_from_file(file_path, init_letter):
    try:
        chosen_lines = ""
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line[0] == init_letter:
                    chosen_lines += line
        return chosen_lines
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("The file contains non-alphabetic data.")


file_path = 'inwokacja.txt'
init_letter = "D"
init_letter_lines = select_lines_from_file(file_path, init_letter)
if init_letter_lines is not None:
    print(f"Lines that begin with {init_letter}:\n{init_letter_lines}")