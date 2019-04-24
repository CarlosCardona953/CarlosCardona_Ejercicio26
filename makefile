all: rgk_001.dat rgk_01.dat rgk_1.dat rgk_001.png rgk_01.png rgk_1.png

%.png: %.dat grafica.py
	python grafica.py
    
%.dat: CarlosCardona_Ejercicio26.x
	./CarlosCardona_Ejercicio26.x 

CarlosCardona_Ejercicio26.x: CarlosCardona_Ejercicio26.cpp
	g++ CarlosCardona_Ejercicio26.cpp -o CarlosCardona_Ejercicio26.x

clean:
	rm -rf *.x *.dat *.png