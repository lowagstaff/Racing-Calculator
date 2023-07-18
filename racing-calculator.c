/*
 ============================================================================
 Name        : task_06_final.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Racing Simulator
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

//Racing Simulator!

struct vehicle
{
	int year;
	char model[20];
	float size;
	int speed;
	float speed_60;
	struct vehicle *next;
};

void enter_info(struct vehicle *v)
{
	printf("\nEnter year: ");
	scanf("%d", &v->year);
	printf("Enter model (model only, no spaces): ");
	scanf("%s", v->model);
	printf("Enter engine size (i.e. 6.2): ");
	scanf("%g", &v->size);
	printf("Enter top speed (mph): ");
	scanf("%d", &v->speed);
	printf("Enter 0-60 (sec i.e. 2.5): ");
	scanf("%g", &v->speed_60);
}

void check_input(struct vehicle *v)
{
	char test[20];

	if (sizeof(v->model) != sizeof(test))
	{
		perror("Car input is incorrect\n");
	}
	else if (v->year <= 00 || v->year >= 3000)
	{
		perror("Year input is incorrect\n");
	}
	else if (v->size <= 0.1 || v->size >= 30)
	{
		perror("Engine size input is incorrect\n");
	}
	else if (v->speed <= 0 || v->speed >= 400)
	{
		perror("Speed input is incorrect\n");
	}
	else if (v->speed_60 <= 1.0)
	{
		perror("0-60 input is incorrect\n");
	}
}

void show_input(struct vehicle *v)
{
	printf("%d %s, %gL, top speed: %d MPH, 0-60: %g sec\n", v->year, v->model, v->size, v->speed, v->speed_60);
}

void racing_calculations(struct vehicle *v, struct vehicle *v2)
{
	int choice = 0;
	printf("\nChoose a race!\n");
	printf("1. Circuit\n");
	printf("2. Drag\n");
	printf("3. Sprint\n");
	printf("4. Time-Attack\n");
	printf("Type # from list to choose race: ");
	scanf("%d", &choice);

	switch(choice)
	{
	case 1:
		printf("\nYou chose: Circuit\n");
		if (v->speed > v2->speed)
		{
			printf("Winner:\n");
			show_input(v);
		}
		else if (v->speed < v2->speed)
		{
			printf("Winner:\n");
			show_input(v2);
		}
		else if (v->speed == v2->speed)
		{
			if (v->speed_60 < v2->speed_60)
			{
				printf("Winner:\n");
				show_input(v);
			}
			else if (v->speed_60 > v2->speed_60)
			{
				printf("Winner:\n");
				show_input(v2);
			}
			else if (v->speed_60 == v2->speed_60)
			{
				printf("It was a tie!\n");
			}
		}
		break;

	case 2:
		printf("\nYou chose: Drag\n");
		if (v->speed > v2->speed)
		{
			printf("Winner:\n");
			show_input(v);
		}
		else if (v->speed < v2->speed)
		{
			printf("Winner:\n");
			show_input(v2);
		}
		else if (v->speed == v2->speed)
		{
			printf("It was a tie!\n");
		}
		break;

	case 3:
		printf("\nYou chose: Sprint\n");
		if (v->speed > v2->speed || v->speed_60 < v2->speed_60)
		{
			printf("Winner:\n");
			show_input(v);
		}
		else if (v->speed < v2->speed || v->speed_60 > v2->speed_60)
		{
			printf("Winner:\n");
			show_input(v2);
		}
		else if (v->speed == v2->speed || v->speed_60 == v2->speed_60)
		{
			printf("It was a tie!\n");
		}
		break;

	case 4:
		printf("\nYou chose: Time-Attack\n");
		if (v->speed_60 < v2->speed_60)
		{
			printf("Winner:\n");
			show_input(v);
		}
		else if (v->speed_60 > v2->speed_60)
		{
			printf("Winner:\n");
			show_input(v2);
		}
		else if (v->speed_60 == v2->speed_60)
		{
			if (v->speed > v2->speed)
			{
				printf("Winner:\n");
				show_input(v);
			}
			else if (v->speed < v2->speed)
			{
				printf("Winner:\n");
				show_input(v2);
			}
			else if (v->speed == v2->speed)
			{
				printf("It was a tie!\n");
			}
		}
			break;

	default:
		perror("Please enter the correct #, the numbers are to the left of each race (i.e. 1)");
		break;
	}
}

int main(void)
{
	printf("Welcome to the racing simulator!\n");

	struct vehicle *v = malloc(sizeof(struct vehicle));
	v->next = NULL;
	enter_info(v);
	check_input(v);
	printf("\nVehicle 1:\n");
	show_input(v);

	struct vehicle *v2 = malloc(sizeof(struct vehicle));
	v2->next = NULL;
	enter_info(v2);
	check_input(v2);
	printf("\nVehicle 2:\n");
	show_input(v2);

	racing_calculations(v, v2);

	printf("Congratulations!\n");
	printf("Please come racing again!\n");
	while (1) {}
	return EXIT_SUCCESS;
}
