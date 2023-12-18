def create_file(file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        print("Wisz 'end' aby zakończyć wprowadzanie słów.")
        while True:
            word = input("Dodaj słowo: ")
            if word == 'end':
                break
            file.write(word + '\n')


def count_letters(file_path, letter):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            count += line.count(letter)
    return count


file_path = input("Podaj nazwę pliku, który chcesz stworzyć: ") + '.txt'
create_file(file_path)
letter = input("Której litery występowanie chcesz policzyć?: ")
print(f"Liczba wystąpień litery '{letter}' w pliku: {count_letters(file_path, letter)}")