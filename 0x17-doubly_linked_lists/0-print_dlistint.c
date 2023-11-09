#include <stdio.h>
#include "lists.h"

/**
 *print_dlistint - check the code
 *@h:aparemeter
 *Return: Always EXIT_SUCCESS.
 */
size_t print_dlistint(const dlistint_t *h)
{
size_t i = 0;
if (h != NULL)
{
printf("%d\n", h->n);
h = h->next;
i++
}
return (i);
