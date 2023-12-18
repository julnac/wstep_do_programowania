def display_menu():
    print("MENU: ")
    print("1. Dodaj książkę")
    print("2. Usuń książkę")
    print("3. Modyfikuj książkę")
    print("4. Wyszukaj książkę")
    print("5. Wyświetl wszystkie książki")
    print("6. Wyjdź")


def add_book(database):
    author = input("Podaj autora: ")
    title = input("Podaj tytuł: ")
    publisher = input("Podaj wydawnictwo: ")
    year = input("Podaj rok wydania: ")

    database[title] = {"autor": author, "wydawnictwo": publisher, "rok_wydania": year}
    print(database)


def delete_book(database):
    print(database.keys())
    book_to_delete = input("Podaj Tytuł książki którą chcesz usunąć: ")

    if book_to_delete in database:
        database.pop(book_to_delete)
        print(f"Książka o tytule {book_to_delete} została usunięta.")
    else:
        print("nie ma takiej książki")
    print(database.keys())


def modify_book(database):
    print(database.keys())
    title = input("Aby zmodyfikowć książkę podaj jej tytuł: ")
    if title in database:
        author = input("Podaj nowego autora: ")
        publisher = input("Podaj nowe wydawnictwo: ")
        year = input("Podaj nowy rok wydania: ")

        database[title] = {"autor": author, "wydawnictwo": publisher, "rok_wydania": year}
        print("Książka zmodyfikowana.")
        print(database[title])
    else:
        print("Książka nie została znaleziona.")


def search_books(database):
    title = input("Podaj tytuł książki której szukasz: ")
    if title in database:
        print(database[title])
    else:
        print("Nie znaleziono książki")


def show_books(database):
    print(database)


if __name__ == "__main__":
    database = {}
    while True:
        display_menu()
        user_activity = input("Podaj liczbę z menu: ")
        if user_activity == '1':
            add_book(database)
        elif user_activity == '2':
            delete_book(database)
        elif user_activity == '3':
            modify_book(database)
        elif user_activity == '4':
            search_books(database)
        elif user_activity == '5':
            show_books(database)
        elif user_activity == '6':
            break
        else:
            print("Nieprawidłowy wybór.Spróbuj jeszcze raz.")
