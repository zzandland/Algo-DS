
test: main.o
	+${MAKE} -C sorting
	g++ main.o quicksort.o -o test

main.o: main.cpp
	g++ -c main.cpp

clean:
	rm *.o test
