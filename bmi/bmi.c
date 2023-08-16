#include <stdio.h>

int flag(int param1, int param2) {
    int a = param1;
    int b = param2;

    a /= 4;
    a += 40;
    a -= 2;
    a /= 10;

    a = b * a;
    b = b * a;
    a = b << (a * b);

    int c = a & b;
    c = (c ^ a) | b;

    printf("%f, %f\n", a, b);
    printf("%f, %f\n", c, c);

    return a * c;   
}

int main() {
    int w0 = 42;
    int w1 = 69;
    double f1 = flag(w0, w1);
    double f2 = flag(w1, w0); 

    double result = f1 + f2;
    printf("An attempt was made - %f\n", result);

    return 0;
}