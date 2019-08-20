#include <stdio.h>
#include <stdlib.h>
#include "../include/myarithmetic.h"
#define PARAMS 3

int main(int argc, char** argv) {

    if (argc != PARAMS) {
        printf("Inserte los parámetros correspondientes...\n");
        exit(0);
    }

    /* Parametros de entrada */
    int x = atoi(argv[1]);
    int y = atoi(argv[2]);

    /* Realiza operaciones */
    int sum_r = my_add(x, y);
    int res_r = my_sub(x, y);
    int mult_r = my_mult(x, y);
    int div_r = my_div(x, y);
    int sqrt_r = my_sqrt(x);

    /* Muestra resultados */
    printf("Suma: %d\n",  sum_r);
    printf("Resta: %d\n", res_r);
    printf("Multiplicacion: %d\n", mult_r);
    printf("Division: %d\n", div_r);
    printf("Raiz cuadrada del primer parametro: %d\n", sqrt_r);

    return 0;
}