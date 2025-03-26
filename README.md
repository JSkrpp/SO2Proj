# Systemy Operacyje 2 - Projekt 1

## Autor:
- Jakub Skorupa

## Temat zadania projektowego

Tematem zadania projektowego jest rozwiązanie problemu jedzących filozofów (Dining Philosophers problem).
Jest on jednym z najbardziej znanych problemów informatycznych związanych z dostępem do zasobów, synchronizacją wątków i rozwiązywaniem sekcji krytycznych.  

W problemie, wybrana ilość filozofów siedzi przy stole, przy którym znajduje się taka sama ilość widelców, jeden po ich lewej stronie oraz jeden po prawej.
Każdy z filozofów może wykonywać w danej jednostce czasu dokładnie jedno z trzech dostępnych mu działań: myślenie, bycie głodnym i jedzenie. W danym momencie
każdy z widelców może być trzymany przez dokładnie jednego filozofa. Aby filozof mógł jeść, potrzebuje mieć jednocześnie w ręce oba widelce znajdujące się po jego obu stronach

### Opisczynności filozofów  
  -**Myślenie:**  Podczas tej czynności filozof nie chce brać do rąk żadnego z dostępnych dla niego widelców.  
  -**Głód:** Filozof sprawdza, czy widelce mu sąsiadujące są wolne. Następuje po okresie myślenia.  
  -**Jedzenie:** Filozof okupuje oba sąsiednie widelce, blokując dostęp do nich dla innych filozofów. Po zakończeniu filozof wraca do myślenia.  

### Problematyka z perspektywy programistycznej  
Podczas implementacji rozwiązania problemu jedzących filozofów głównym zadaniem jest skuteczne zapobieganie zjawisku zakleszczenia   
(ang. *deadlock*), czyli sytuacji, w której dwa wątki (tutaj filozofowie), czekają nawzajem na wykonanie przez nie pewnej czynności korzystającej ze współdzielonej sekcji kodu aplikacji. 
Następnym problemem jest sekcja krytyczna i synchronizacja wątków z wzięciem tej sekcji pod uwagę. Sekcja krytyczna jest elementem kodu, który występuje tylko jednokrotnie w aplikacji wielowątkowej, 
a co za tym idzie, może być wykorzystywana tylko przez jeden wątek na raz. Istotą poprawnego rozwiązania problemu jest zapewnienie, że każdy z uruchomionych w aplikacji wątków jest w stanie przeprowadzać zamierzone działanie
w sposób płynny i sprawny.

### Napotkane problemy i zastosowane rozwiązania
  -**Synchronizacja działań wątków: ** W celu zapobiegania sytuacji, w której dwa wątki jednocześnie "kłóca się" o dostęp do widelców, wprowadzona została zmienna boolean *lock*, będaca częścią klasy *DiningPhilosopher*. 
  Uruchamiana jest jedna instancja obiektu tej klasy, więc niezależnie od ilości wątków tylko jeden z nich może w tym samym czasie mieć dostęp do widelców.  
  -**Zakleszczanie: ** Pierwszą metodą zapobieganiu zakleszczaniu była implementacja systemu brania widelców przez filozofów w taki sposób, gdzia rozpoczącie jedzenia jest jednoznaczne z wzięciem obu widelców jednocześnie.
  Okazało się jednak to niewystarczającym rozwiązaniem, gdyż dochodziło do sytuacji, w której filozofowie oczekiwali na widelce przez nieskończony czas. Do stanu głodu, zostały dodane małe opóźnienia rzędu 1ms, które wyeliminowały występowanie tego problemu.
  Dodatkową optymalizacją pod tym względem jest także wprowadzenie losowości w czasach jedzenia i myślenia. Zmnijeszyło to znacznie ilość wystąpien sytuacji, w których dwa wątki chcą w tym samym momencie uzyskać dostęp do widelców.  

### Uruchamianie programu

### Podsumowanie
