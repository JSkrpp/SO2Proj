# Systemy Operacyje 2 - Projekt 1

## Autor:
- Jakub Skorupa

## Temat zadania projektowego

Tematem zadania projektowego jest rozwiązanie problemu jedzących filozofów (Dining Philosophers problem).
Jest on jednym z najbardziej znanych problemów informatycznych związanych z dostępem do zasobów, synchronizacją wątków i rozwiązywaniem sekcji krytycznych.  

W problemie, wybrana ilość filozofów siedzi przy stole, przy którym znajduje się taka sama ilość widelców, jeden po ich lewej stronie oraz jeden po prawej.
Każdy z filozofów może wykonywać w danej jednostce czasu dokładnie jedno z trzech dostępnych mu działań: myślenie, bycie głodnym i jedzenie. W danym momencie
każdy z widelców może być trzymany przez dokładnie jednego filozofa. Aby filozof mógł jeść, potrzebuje mieć jednocześnie w ręce oba widelce znajdujące się po jego obu stronach

### Opis działań filozofów  
  -**Myślenie:**  Podczas tej czynności filozof nie chce brać do rąk żadnego z dostępnych dla niego widelców.  
  -**Głód:** Filozof sprawdza, czy widelce mu sąsiadujące są wolne. Następuje po okresie myślenia.  
  -**Jedzenie:** Filozof okupuje oba sąsiednie widelce, blokując dostęp do nich dla innych filozofów. Po zakończeniu filozof wraca do myślenia.  

### Problematyka z perspektywa programistycznej  

### Napotkane problemy i zastosowane rozwiązania

### Uruchamianie programu

### Podsumowanie
