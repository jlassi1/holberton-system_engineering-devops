#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
/**
 *infinite_while - program that creates 5 zombie processes.
 *
 *Return: 0
 */
int infinite_while(void)
{

	while (1)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		sleep(1);
	}
return (0);
}
/**
 *main - function main
 *
 *Return: 0
 */

int main(void)
{
	infinite_while();
return (0);
}
