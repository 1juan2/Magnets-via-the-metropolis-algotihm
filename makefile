.PHONY: all Functions Metropolis Graphs

all: Graphs

Functions:
	python Functions.py

Metropolis: Functions
	python Magnets_Metropolis.py

Graphs: Metropolis
	python Graphs.py

