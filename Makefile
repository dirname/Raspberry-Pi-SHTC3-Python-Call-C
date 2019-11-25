SHTC3:SHTC3.c
	gcc -shared -fPIC SHTC3.c -o SHTC3.so -lbcm2835 -lm
clean:
	rm SHTC3.so

