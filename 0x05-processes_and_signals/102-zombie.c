#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
/**
 *infinite_while - program that creates 5 zombie processes.
 *
 *Return: 0
 */
int infinite_while(void)
{

	while (1)
	{
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

pid_t pid;
	int i = 1;

	while (i <= 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
			exit(0);
		i++;
	}
	infinite_while();
return (0);
}
