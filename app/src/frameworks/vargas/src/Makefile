CC = g++
LIBS = -lm -pthread
CFLAGS = -Wall -c -fPIC -O3 -fomit-frame-pointer -ffast-math -DREENTRANT -std=c++0x
#CFLAGS = -Wall -c -fPIC -g -DREENTRANT -std=c++0x
PROGFLAGS = $(LIBS) -fPIC -O3 -fomit-frame-pointer -ffast-math -DREENTRANT
#PROGFLAGS = $(LIBS) -fPIC -g -DREENTRANT

EXE = getMetrics
OBJ = getMetrics.o

all: clean $(OBJ)
	$(CC) $(PROGFLAGS) $(OBJ) -o $(EXE)

getMetrics.o: getMetrics.h getMetrics.cpp
	$(CC) $(CFLAGS) getMetrics.cpp -o getMetrics.o

clean:
	rm -f .*.swp *~ $(OBJ) $(EXE)

backup:
	tar -cvzf backups/`date +%Y-%m-%d-%H.%M`.tar.gz *.h *.cpp Makefile 
