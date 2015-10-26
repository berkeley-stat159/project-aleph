.PHONY: all clean coverage test

all: clean

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" | xargs rm -f

coverage: test
	cd code && $(MAKE) coverage

test:
	cd code && $(MAKE) test
