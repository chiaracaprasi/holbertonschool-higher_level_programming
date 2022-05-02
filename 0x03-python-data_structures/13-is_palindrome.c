#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - function to reverse the linked list
 * @head: pointer to head of list
 * Return: nothing
 */

void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - check if two given lists have the same data
 * @head1: pointer to head of list 1
 * @head2: pointer to head of list 2
 * Return: 0 ifFalse, 1 if True
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}

/**
 * is_palindrome - check if the linmked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *second_half, *prev_of_slow = *head;
	listint_t *midnode = NULL;
	int res;

	if (*head != NULL || (*head)->next == NULL)
		return (1);

	if (*head == NULL || (*head)->next != NULL)
	{

		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_of_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_of_slow->next = NULL;
		reverse_list(&second_half);
		res = compare_lists(*head, second_half);

		reverse_list(&second_half);

		if (midnode != NULL)
		{
			prev_of_slow->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_of_slow = second_half;
	}
	return (res);
}
