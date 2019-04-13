
test: main.o bit_func.o
	g++ main.o bit_func.o -o test

main.o: main.cpp bit_func.h
	g++ -c main.cpp

bit_func.o: bit_func.h
	g++ -c bit_func.cpp

clean:
	rm *.o test
