

.PHONY: run
run:
	python3 main.py

.PHONY: tests
test:
	python3 tests.py

.PHONY: clean
clean:	
	rm -rf output
