CC=gcc
# Using -Werror -Wall to make me write safer code
CFLAGS=-Werror -Wall

SRC=$(shell ls progs/*.c)
EXE=$(patsubst progs/%.c,%,$(SRC))

all:$(EXE)
# Compile
%: progs/%.c
	$(CC) $< -o $@ $(CFLAGS)
