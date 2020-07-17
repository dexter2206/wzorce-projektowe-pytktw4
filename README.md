# Zadania
1. Fabryka abstrakcyjna

   1. Zamodelujemy tworzenie aplikacji, w której możemy zmieniać styl (theme).

      - Główny obiekt aplikacji ma możliwoś tworzenia elementów interfejsu:
      - Pasek narzędzi (toolbar)
      - Przycisków (button)
      - Głównego okna (Window)

      - Chcemy uniezależnić typ tworzonych elementów od wybranego theme'u.
      - Możliwość dodania nowych theme'ów bez konieczności modyfikowania głównej klasy aplikacji

      Zaprojektuj hierarchię klas rozwiązującą powyższy problem. Użyj wzorca fabryki abstrakcyjnej.

   2. Na zajęciach z algorytmów mówiliśmy o Odwrotnej Notacji Polskiej (RPN). Napisaliśmy też funkcję,
      która obliczała wartość wyrażenia zadanego w RPN.

      Funkcja obliczająca wyrażenie zadane w RPN przyjmowała jako argument listę złożoną z:
      - Liczb
      - Operatorów

      Przeważnie jednak, wyrażenie zostanie odczytane z łańcucha znaków. Jak więc skonwertować je
      do takiej listy?

      Załóżmy, że łańcuch znaków zawiera elementy oddzielone pojedynczą spacją (np. "5.5 3.1 +").
      Wystarczy więc:

      - podzielić łańcuch w miejscach gdzie pojawia się spacja.
      - dla każðego elementu w powstałej liście:
        - Jeżeli element jest pojedynczym znakiem i nie jest cyfrom, to jest operatorem.
	- W przeciwnym razie jest to liczba.

      Gdzie tu miejse na fabrykę? Otóż istnieje kilka typów liczbowych: float, int, decimal.
      Cel: napisz funkcję konwertującą napis do listy oczekiwanej przez `evaluate_rpn`, używającą
      zadanej fabryki do tworzenia liczb.

2. Budowniczy

   URLe które wpisujemy w pasku przeglądarki zawierają kilka składników.

   ```text
   http://example.com:80
   ```
   - http to nazwa protokołu
   - example.com to adres witryny
   - 80 to port na którym komunikujemy się ze stroną

   Oczywiście, nie zawsze wpisujemy wszystkie te składniki. Jeśli tego nie zrobimy, to część z nich
   przyjmuje domyślne wartości.

   Na przykład domyślnym protokołem jest http, a domyślnym portem dla tego protokołu jest port 80.
   W związku z tym wpisując w pasku adresu "www.example.com", pełny adres to "http://www.example.com:80".

   Zadanie: napisać klasę przechowującą wszystkie komponenty URLa. Umożliwić jej skonstruowanie
   tak, żeby podanie adresu było konieczne, ale podanie portu i protokołu: nie.

   Zrealizować to zadanie używając opcjonalnych parametrów.

   Opcjoalnie: zrealizować to w "obiektowej" wersji i porównać wygodę użycia jednego i drugiego rozwiązania.

3. Adapter

   Napisaliśmy aplikację, któ©a potrafi wykonywać pewne operacje sieciowe.
   W tym celu wykorzystuje obiekty (klientów) implementujących następujący protokół.

   ```python
   class Client(Protocol):

       def __init__(self, address, port):
           pass
           
       def connect():
	         pass

	     def send(message: str):
	         pass
	     
	     def disconnect():
	         pass

   ```

   Klasa korzystająca z klienta wygląda tak:

   ```python
   class MessageSender:

       def __init__(self, client: Client):
           self.client = client
           
       def send_message(self, messages: Iterable[str]):
           self.client.connect()
           for message in messages:
               self.client.send(message)
           self.client.disconnect()
    ```
    
    Jakiś czas później trafiliśmy na klienta, który implementuje interesującą nas funkcjonalność. Niestety, jego interfejs jest niezgodny z naszą aplikacją i wygląda tak:
    
    ```python
    class TCPClient:
    
        def __init__(self, host: str): # host to napis postaci adres:port
            pass
            
        def open_connection():
            pass
            
        def write(data: bytes):
            pass
            
        def close_connection():
            pass
    ```
    Naszym zadaniem jest napisanie adapter do klasy `TCPClient` tak, aby możliwe było jej użycie w naszej aplikacji.
    
4. Dekorator

   1. Czasem możemy być zainteresowani historią wywołania jakiejś funkcji. Napisać dekorator `history` który umożliwi zapisanie i odczytanie z jakimi parametrami funkcja została wywołana.
   
     Przykład użycia:
     
     ```python
     
     @history
     def greet(who, greeting="Hello"):
         print(f"{greeting}, {who}!")
         
     print(greet("Konrad"))
     print(greet("Ania", "Good morning"))
     print(greet("Olek", greeting="Good afternoon"))
     
     print(greet.history) # Powinno wypisać historię wywołania naszej funkcji.
     ```
   2. Możemy dekorować również klasy. Napisać następujące dekoratory:
   
      - Dekorator `log_access` który zaloguje dostęp do każdego atrybutu obiektu udekorowanej klasy.
      - (Trochę trudniejsze) Dekorator `immutable` który sprawi że udekorowana klasa będzie niemutowalna (przynajmniej pozornie).
      
5. Łańcuch odpowiedzialności.

   W tym przykładzie zaimplementujemy symulację programu służącego do skalowania plików w różnych formatach graficznych.
   
   - Powiedzmy, że nasza aplikacja służy do skalowania obrazu w róznych formatach (png, jpg, gif, bmp...).
   - Skalowaniem obrazu każdego formatu zajmuje się osobna klasa.
   
   Zamodelować funkcjonowanie takiego programu, używając łańcucha odpowiedzialności.
   - Każðy element łańcucha pozwala na skalowanie jednego typu obrazu.
   - Ważne! Jeśli jeden element łańcucha przetworzy obraz, to przetwarzanie powinno się przerwać.
   - Co z obsługą błędu? Co jeśli żaden element łańcucha nie potrafił poradzić sobie z danym obrazem?
   
6. Iterator

   Jako ćwiczenie w tworeniu iteratorów, spróbuj napisać następujące wersje wbudowanych iteratorów:
   
   - `enumerate`
   - `zip`
