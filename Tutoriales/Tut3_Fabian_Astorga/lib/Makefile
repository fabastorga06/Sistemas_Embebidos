SRC=myarithmetic
LIB=libmyarithmetic

STATIC=$(LIB).a
DYNAMIC=$(LIB).so
OBJ=$(SRC).o

CC=gcc
AR=ar rv
CFLAGS=-c -Wall
DFLAGS=ld -o

all: $(STATIC) $(DYNAMIC)

# static lib
$(STATIC): $(OBJ)
		$(AR) $(STATIC) $(OBJ)

# dynamic lib
$(DYNAMIC): $(OBJ)
		$(DFLAGS) $(DYNAMIC) $(OBJ) -shared


$(OBJ): $(SRC).c
		$(CC) $(CFLAGS) $(SRC).c
 

PHONY: clean
clean:
		rm $(STATIC) $(DYNAMIC) $(OBJ)