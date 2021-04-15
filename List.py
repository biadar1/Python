#Oryginał Bartosz Białczak
from typing import Any
class Node:
    value: Any
    next: 'Node'

    def __init__(self, val_1: Any, next_: 'Node'): #tworzymy obiekt self.value i wskaźnik self.next
        self.value=val_1 
        self.next=next_

class LinkedList:
    head: Node
    tail: Node

    def __init__(self): #tworzymy obiekty self.head i self.tail
        self.head = None
        self.tail = None

    def push(self, val: Any):
        new = Node(val, self.head) #nowy obiekt typu Node wskazujący na self.head
        self.head = new #nasz nowy obiekt staje się teraz początkiem listy
        if self.tail == None: #jeśli za pomocą tej funkcji tworzymy pierwszy obiekt w liście, ten obiekt staje się self.tail
            self.tail = self.head

    def append(self, val: Any):
        new = Node(val, None) #nowy obiekt wskazujący na None
        if self.tail == None: #jeśli nie mieliśmy "ogona", nowy obiekt staje się ogonem
            self.tail = new
        else:
             self.tail.next = new #jeśli mieliśmy już "ogon" to zamieniamy go na nowy obiekt
             self.tail = new
        if self.head == None: #jeśli za pomocą tej funkcji tworzymy pierwszy obiekt w liście, ten obiekt staje się self.head
            self.head = self.tail

    def node(self, at: int) -> Node:
        i=0 #dodajemy wewnętrzny licznik
        if self.head == None: #jeśli lista jest pusta to przerywamy funkcję i wyświetlamy odpowiednią informację
            print('Lista jest pusta')
            return
        helper = self.head #tworzymy pomocniczy obiekt
        while i < at: #szukamy docelowego Node w miejscu At
            if helper == None: #jeśli użytkownik próbuje wyświetlić Node który nie istnieje w liście, przerywamy pętlę
                print('Nie ma takiego elementu listy')
                break
            helper = helper.next #przechodzimy przez kolejne Node listy
            i += 1 
        return helper

    def insert(self, value_: Any, after: Node):
        if self.head == None: #jeśli lista jest pusta to przerywamy funkcję i wyświetlamy odpowiednią informację
            print('Lista jest pusta')
            return 
        helper = self.head #tworzymy pomocniczy obiekt
        while helper != after: #szukamy Node docelowego (after)
            helper = helper.next #przechodzimy przez kolejne Node listy
        new = Node(value_, helper.next) #tworzymy nowy obiekt Node wskazujący na Node następny po after
        helper.next = new #"łączymy" naszą listę z nowym obiektem
        if helper == self.tail: #jeśli miejsce docelowe jest ogonem (czyli jeśli za pomocą tej funkcji dodajemy nowy ostatni Node)
            self.tail = Node(value_,None) #przypisujemy nowy element jako nowy "ogon" ze wskaźnikiem None

    def pop(self) -> Any:
        if self.head == None: #jeśli lista jest pusta to przerywamy funkcję i wyświetlamy odpowiednią informację
            print('Lista jest pusta')
            return 
        if self.head.next == None: #jeśli następny element listy jest pusty to przypisujemy nowy "ogon"
            self.tail = self.head
        pop_ = self.head #tworzymy nowy obiekt który zapisze pierwszy element listy
        self.head = self.head.next #usuwamy pierwszy element z listy
        return pop_.value #zwracamy wartość usuniętego elementu
        
    def remove_last(self) -> Any:
        if self.head == None: #jeśli lista jest pusta to przerywamy funkcję i wyświetlamy odpowiednią informację
            print('Lista jest pusta')
            return 
        helper = self.head #tworzymy pomocniczy obiekt
        if helper.next == None: #jeśli w liście jest tylko 1 element, usuwamy go i zwracamy jego wartość
            self.head = None
            return helper.value
        while helper.next.next != None: #jeśli w liście jest >1 elementów, to szukamy elementu 3ciego od końca (bo 3ci jest = None)
            helper = helper.next
        remove_last_ = helper.next #tworzymy obiekt który zapisze usuwany element
        helper.next = None #usuwamy ostatni element
        self.tail = helper #przypisujemy "ogon" do aktualnie ostatniego elementu listy
        return remove_last_.value #wypisujemy wartość usuniętego elementu

    def remove(self, after: Node):
        if self.head == None:  #jeśli lista jest pusta to przerywamy funkcję i wyświetlamy odpowiednią informację
            print('Lista jest pusta')
            return 
        helper = self.head #tworzymy pomocniczy obiekt
        while helper != after: #szukamy Node docelowego (after)
            helper = helper.next
        if helper.next == None: #jeśli próbujemy usunąc element którego nie ma to zakańczamy funkcję
            return
        helper.next = helper.next.next #usuwamy element po elemencie after
    
    def __str__(self) -> str:
        if self.head == None: #jeśli lista jest pusta to przerywamy funkcję i wyświetlamy odpowiednią informację
            print('Lista jest pusta')
            return 
        helper = self.head #tworzymy pomocniczy obiekt
        myList = str(helper.value) #tworzymy nasz wyjściowy string i przypisujemy mu początkowy element listy jako string
        while helper.next != None: #"przechodzimy" przez kolejne elementy listy
            helper = helper.next
            myList +=' -> '+str(helper.value) #dopisujemy do wyjściowego stringa kolejne elementy listy
        return myList #zwracamy wypełniony string wyjściowy

    def __len__(self) -> int:
        i = 0 #tworzymy wewnętrzny licznik
        helper = self.head #tworzymy pomocniczy obiekt
        while helper != None: #"przechodzimy" przez kolejne elementy listy
            helper = helper.next
            i+=1 #zwiększamy licznik o 1 za każdym razem jak "przejdziemy" przez element listy
        return i #zwracamy licznik

class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList() #tworzymy obiekt self._storage (który automatycznie jest pusty ze względu na LinkedList().__init__ )

    def push(self, element: Any):
        self._storage.append(element) #wykorzystujemy funkcję append() klasy LinkedList() do dodania elementu na "szczycie" stosu

    def pop(self) -> Any:
        return self._storage.remove_last() #wykorzystujemy funkcję remove_last() klasy LinkedList() do zwrócenia wartości i usunięcia elementu na "szczycie" stosu 

    def __str__(self) -> str:
        if self._storage.head == None: #jeśli stos jest pusty to przerywamy funkcję i wyświetlamy odpowiednią informację
            print('Stos jest pusty')
            return 
        tempStack = self._storage #tworzymy pomocniczy obiekt typu Stack()
        myStack = str(tempStack.pop()) #tworzymy string wyjściowy i przypisujemy mu, jako string, element ze "szczytu" stosu za pomocą funkcji pop() z klasy Stack()
        helper = self._storage.head #tworzymy pomocniczy obiekt
        while helper != None: #"przechodzimy" przez kolejne elementy stosu
            myStack +='\n' + str(tempStack.pop()) #dopisujemy do wyjściowego stringa kolejne elementy stosu
            helper = helper.next
        return myStack #zwracamy wypełniony string wyjściowy

    def __len__(self) -> int: 
        i = 0 #tworzymy wewnętrzny licznik
        helper = self._storage.head #tworzymy pomocniczy obiekt
        while helper != None: #"przechodzimy" przez kolejne elementy stosu
            helper = helper.next
            i+=1 #zwiększamy licznik o 1 za każdym razem jak "przejdziemy" przez element stosu
        return i #zwracamy licznik

class Queue:
    _storage: LinkedList

    def __init__(self): #tworzymy obiekt self._storage (który automatycznie jest pusty ze względu na LinkedList().__init__ )
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.head.value #zwracamy wartość pierwszego elementu kolejki

    def enqueue(self, element: Any):
        self._storage.append(element) #wykorzystujemy funkcję append() klasy LinkedList() do dodania elementu na końcu kolejki

    def dequeue(self) -> Any:
        return self._storage.pop() #wykorzystujemy funkcję pop() klasy LinkedList() do zwrócenia wartości i usunięcia pierwszego elementu kolejki

    def __str__(self) -> str:
        if self._storage.head == None: #jeśli kolejka jest pusta to przerywamy funkcję i wyświetlamy odpowiednią informację
            print('Kolejka jest pusta')
            return 
        helper = self._storage.head #tworzymy pomocniczy obiekt
        myQueue = str(helper.value) #tworzymy string wyjściowy i przypisujemy mu, jako string, pierwszy element kolejki
        while helper.next != None: #"przechodzimy" przez kolejne elementy kolejki
            helper = helper.next
            myQueue +=', '+str(helper.value) #dopisujemy do wyjściowego stringa kolejne elementy kolejki
        return myQueue #zwracamy wypełniony string wyjściowy
        
    def __len__(self) -> int:
        i = 0 #tworzymy wewnętrzny licznik
        helper = self._storage.head #tworzymy pomocniczy obiekt
        while helper != None: #"przechodzimy" przez kolejne elementy kolejki
            helper = helper.next
            i+=1 #zwiększamy licznik o 1 za każdym razem jak "przejdziemy" przez element kolejki
        return i #zwracamy licznik

list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2