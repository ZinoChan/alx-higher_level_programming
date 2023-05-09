#include "lists.h"

/**
 * insert_node - add node to list
 * @head: head
 * @number: where to add
 * Return: adss or null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *previous;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n < number)
		{
			previous = current;
			current = current->next;
		}

		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}
