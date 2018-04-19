.PHONY: run clean

run:
	python run.py

clean:
	rm -rf app/*.pyc app/__pycache__ log/*
