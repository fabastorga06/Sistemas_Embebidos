BDIR=../bin/
LDIR=../lib/

CC=gcc
FLAGS=-o
CFLAGS=-I$(LDIR) -L$(LDIR)
SEXEC=staticlib
DEXEC=dynamiclib
SRC=calculadora.c
LIB=libmyarithmetic


all: static dynamic

# static
static: $(SRC)
		$(CC) $(FLAGS) $(BDIR)$(SEXEC) $(SRC) $(LDIR)$(LIB).a

# dynamic
dynamic:
		$(CC) $(FLAGS) $(BDIR)$(DEXEC) $(SRC) $(CFLAGS) -Bdynamic $(LDIR)$(LIB).so
		export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:pwd


.PHONY: clean
clean:
	rm -f $(BDIR)*lib