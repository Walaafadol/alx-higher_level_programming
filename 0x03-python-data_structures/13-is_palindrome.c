#include "lists.h"

/**
 * is_palindrome - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}
/**
 * aux_palind - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * @end: double pointer to the linked list
 * Return: 1 if it is, 0 if not
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
{
		*head = (*head)->next;
			return (1);
}
		return (0);
}
