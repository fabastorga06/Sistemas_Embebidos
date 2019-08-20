LDIR=lib/
SDIR=src/

all: calculadora

calculadora:
	make -C $(LDIR)
	make -C $(SDIR)

.PHONY: clean
clean:
	cd $(LDIR) && $(MAKE) clean
	cd $(SDIR) && $(MAKE) clean