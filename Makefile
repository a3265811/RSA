CC = python3

i:
	$(CC) RSA.py -i
r:
	$(CC) RSA.py
clean:
	rm -rf report.txt
