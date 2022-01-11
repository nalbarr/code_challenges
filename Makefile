.PHONY: env help all install clean clean-pyc clean-pyo
SRC_ROOT=src
SRC=$(SRC_ROOT)/hello/hellorepository.py \
	$(SRC_ROOT)/leet/problem9/solution.py
PYTHONPATH=$(SRC_ROOT)
TEST_ROOT=tests

help:
	@echo "make env"
	@echo "make install"
	@echo "make lint"
	@echo "make format"
	@echo "make test"

env:
	pipenv shell

install:
	pipenv install -r requirements.txt

build: clean
	pipenv install -e $(SRC_ROOT)

clean-pyc:
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "*.pyo" -exec rm -f {} +

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean: clean-pyc clean-build

lint:
	flake8 $(SRC)

format:
	black $(SRC)

# TODO: NA. Fix import issues
# test: clean build
# 	@echo $(PYTHONPATH); pytest tests/hello/test_hellorepository.py

test: clean build
	@echo $(PYTHONPATH); pytest tests/leet/problem9/test_problem9.py	

run: run_problem9

run_hello:
	python $(TEST_ROOT)/hello/hello.py

run_problem9:
	python $(TEST_ROOT)/leet/problem9/solution.py
