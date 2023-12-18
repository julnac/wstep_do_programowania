def sum_numbers_from_file(file_path):
    try:
        total = 0
        with open(file_path, 'r') as file:
            for line in file:
                total += int(line)
        return total
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("The file contains non-numeric data.")


file_path = 'liczby.txt'
sum_of_numbers = sum_numbers_from_file(file_path)
if sum_of_numbers is not None:
    print(f"The sum of numbers is: {sum_of_numbers}")