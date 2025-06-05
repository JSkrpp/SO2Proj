# Systemy Operacyje 2 - Projekt 2

## Autorzy:
- Jakub Skorupa
- Mikołaj Lipiński

## Temat zadania projektowego    

Zadanie polega na zaprojektowaniu i implementacji wielowątkowego serwera czatowego, umożliwiającego komunikację pomiędzy wieloma użytkownikami w czasie rzeczywistym. Projekt powinien uwzględniać obsługę wielu wątków w celu efektywnego zarządzania połączeniami oraz przesyłaniem wiadomości.

### Implementacja serwera i klientów za pomocą wątków.     

Aplikacja została napisana w języku Python. Do komunikacji serwer-klient zastosowana została biblioteka *socket*, umożliwiająca proste postawienie serwera na adresie localhost (127.0.0.1). Każdy z klientów uruchamiany jest jako nowy wątek,
a ich synchronizacją zajmuje się Lock z biblioteki *threading*. Dodatkowo serwer obsługuje równoczesne przesyłanie wiadomości między wieloma użytkownikami, zapewniając spójność danych. Mechanizmy synchronizacji eliminują ryzyko kolizji w dostępie do wspólnych zasobów.

### Opis problemu programistycznego    

Głównym problemem rozwiązywanym w zadaniu projektowym jest synchronizacja wątków w aplikacji sieciowej. Brak lub niepoprawna implementacja mechanizmów synchronizacji może powodować błędne wyświetlanie wiadomości w 
skrajnych przypadkach, np. gdy dwóch klientów wysyła w idealnie tym samym czasie wiadomości, może nastąpić sytuacja, w której wiadomości nachodzą się na siebie na interfejsie użytkownika. Wprowadzona w tym celu blokada
w metodzie *broadcast_message* zapewnia, że serwer wysyła do klientów maks. jedną wiadomośc w tym samym czasie. Blokada zapobiega także problemom związanym z jednoczesymi próbami połączenia się z aplikacją.

### Dodatkowe ulepszenia    
Jako, że porjekt wykonywaliśmy w grupie dwuosobowej zdecydowaliśmy się na dodatkowe ulepszenia aplikacji. Głównym ulepszeniem było wprowadzenie prostego interfewjsu użytkownika z kilkoma dodatkami:  
  - Kolory uczetników czatu
  - Timestampy wiadomości
  - Możliwość czyszczenia czatu
  - Możliwość rozłączenia z czatu za pomoca wiadomości "bye"  

### Uruchamianie programu
  Uruchomienie programu przebiega w dwóch krokach, w pierwszej kolejności uruchamiamy serwer a następnie aplikacje klienta       
  -**Linux:**    
  Uruchamianie serwera:
  - `./server_linux.sh`

  Uruchamianie klienta:
  - `./client_linux.sh`

  **Uwaga:** Skrypty uruhamiające aplikacje na systemach linux mogą nie mieć wymaganych uprawnień, w takim przypadku należy je dodać za pomocą komendy:    
  `chmod +x server_linux.sh`    
  `chmod +x client_linux.sh`
