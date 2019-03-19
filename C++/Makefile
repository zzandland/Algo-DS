
test: main.o
	+${MAKE} -C sorting
	g++ main.o heapsort.o -o test

main.o: main.cpp
	g++ -c main.cpp

clean:
	rm *.o test
