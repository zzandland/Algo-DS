test: 7_1.o DeckOfCards.o BlackJack.o
	g++ -o test 7_1.o DeckOfCards.o BlackJack.o

7_1.o: 7_1.cpp DeckOfCards.h BlackJack.o
	g++ -c 7_1.cpp

BlackJack.o: DeckOfCards.h BlackJack.h BlackJack.cpp
	g++ -c BlackJack.cpp

DeckOfCards.o: DeckOfCards.h DeckOfCards.cpp
	g++ -c DeckOfCards.cpp

clean:
	rm *.o test
