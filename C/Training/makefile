CC=gcc
# Using -Werror -Wall to make me write safer code
CFLAGS=-Werror -Wall

SRC=$(wildcard *.c)
EXE=$(patsubst %.c,%,$(SRC))

all:$(EXE)
# Compile
%: %.c
	$(CC) $(CFLAGS) $< -o compiled/$@
