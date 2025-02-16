# Sudoku Solver - Aplikacja webowa do rozwiązywania sudoku

## Opis projektu

Sudoku Solver to aplikacja webowa napisana w Pythonie z wykorzystaniem frameworka Flask oraz Google AI Studio API.  
Umożliwia użytkownikom rozwiązywanie sudoku na dwa sposoby:  

- **Wprowadzenie danych ręcznie**: Użytkownik może wpisać liczby do siatki sudoku bezpośrednio na stronie.  
- **Przesłanie obrazu**: Użytkownik może przesłać zdjęcie nierozwiązanego sudoku, a aplikacja automatycznie odczyta liczby i rozwiąże sudoku.  

Dodatkowo aplikacja oferuje:  

- **Rejestrację i logowanie użytkowników**  
- **Przechowywanie historii rozwiązań w bazie danych SQLite**  
- **Przeglądanie historii rozwiązań w formie tabel sudoku**  

---

## Funkcjonalności  

### 🔢 Rozwiązywanie sudoku  
- Wprowadź liczby ręcznie do siatki sudoku.  
- Prześlij zdjęcie sudoku, a aplikacja odczyta liczby i rozwiąże je.  

### 🔐 Rejestracja i logowanie  
- Użytkownicy mogą się zarejestrować i zalogować, aby korzystać z pełnej funkcjonalności.  

### 📜 Historia rozwiązań  
- Każde rozwiązane sudoku jest zapisywane w bazie danych.  
- Użytkownicy mogą przeglądać swoje poprzednie rozwiązania.  

### 🎨 Interfejs użytkownika  
- Prosty i intuicyjny interfejs webowy.  
- Tabele sudoku wyświetlane w czytelnej formie.  

---

## Wymagania systemowe  

- Python **3.8** lub nowszy  
- Biblioteki Pythonowe:  
  - Flask  
  - SQLite3  
  - Werkzeug (do obsługi haseł)  

---

## Użycie
### Strona główna
Przejdź do strony głównej, aby rozwiązać sudoku ręcznie lub przesłać obraz.

### Rejestracja i logowanie
Zarejestruj się, aby uzyskać dostęp do historii rozwiązań.
Zaloguj się, aby kontynuować.

### Rozwiązywanie sudoku
Wprowadź liczby do siatki sudoku i kliknij "Rozwiąż Sudoku".
Prześlij zdjęcie sudoku, a aplikacja rozwiąże je automatycznie.

### Historia rozwiązań
Przejdź do zakładki "Historia", aby zobaczyć swoje poprzednie rozwiązania.
