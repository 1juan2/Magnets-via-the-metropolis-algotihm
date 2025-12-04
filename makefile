.PHONY: all Functions Metropolis Graphs Deriva Analytics

all: Graphs

Functions:
	python Functions.py

Analytics: 
	python Analytic.py
	
deriva: 
	python deriv.py
	
Metropolis: Functions
	python Magnets_Metropolis.py

Graphs: Metropolis deriva
	python Graphs.py

