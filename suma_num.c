#include <stdio.h>
#include <stdlib.h>


void suma_numeros(int numero_uno, int numero_dos){

    int suma = numero_uno+numero_dos;


    printf("La suma de los numeros es: %d", suma);
}


int main(){

    suma_numeros(5,8);

    return 0;
}