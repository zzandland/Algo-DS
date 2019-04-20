test: 7_1.o DeckOfCards.o
	g++ -o test 7_1.o DeckOfCards.o

7_1.o: 7_1.cpp DeckOfCards.h
	g++ -c 7_1.cpp

DeckOfCards.o: DeckOfCards.h DeckOfCards.cpp
	g++ -c DeckOfCards.cpp

clean:
	rm *.o test
