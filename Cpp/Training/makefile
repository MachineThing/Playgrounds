CC=g++
# Using -Werror -Wall to make me write safer code
CFLAGS=-Werror -Wall

SRC=$(shell ls progs/*.cpp)
EXE=$(patsubst progs/%.cpp,%,$(SRC))

all:$(EXE)
# Compile
%: progs/%.cpp
	$(CC) $< -o $@ $(CFLAGS)
