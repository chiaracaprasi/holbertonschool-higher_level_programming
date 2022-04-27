#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to list
 * @number: nu,ber to insert
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new, *tmp;

	if (head == NULL)
		return (NULL);

	/* create new node with number as value n and next is NULL */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	/* if number is less than n in 1st node make new node the head node */
	if (*head != NULL && (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
		{
		while (current != NULL && current->n < number)
		{
			tmp = current;
			current = current->next;
		}
		tmp->next = new;
		new->next = current;
	}
	return (new);
}
