#include<stdio.h>
/*comment Section*/
int main(void){

	int age;
	int number1;
	int mystery;

	printf("Enter you age\n");

	scanf("%d", &age);

	printf("Welcome Player one, Your age is %d\n", age);

	printf("Welcome to the guessing game\n");

	printf("Here are the rules\n 1. You guess a number and if it corresponds the the mystery number you win, Simple right?\n");

	printf("2. you only get one chance for now since you only have one life so be careful and have fun");
	printf("Enter your number\n");
	scanf("Enter your number: %d\n", &number1);

        if (number1 == mystery){
            printf("You Won\n");
        };

	return(0);
}
