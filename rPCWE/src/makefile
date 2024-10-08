ifeq ($(shell uname -s), Darwin)
	CC = clang
else
	CC = gcc
	CFLAGS += -pthread -lm
endif

CFLAGS += -O2 -std=c99 

all: rpcwe.c
	${CC} rpcwe.c ${CFLAGS} -o rpcwe
clean: 
	rm rpcwe
