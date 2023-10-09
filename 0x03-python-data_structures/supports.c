#include "lists.h"

/**
 * print_listint - to print all the elements of a listint_t list.
 * @h: points to the first node.
 * Return: the number of nodes.
 */
size_t print_listint(const listint_t *h)
{
const listint_t *current;
unsigned int n; /* number of nodes */

/* Initialize current. */
current = h;
n = 0;

/* While current node is not NULL, iterate through the list. */
while (current != NULL)
{
printf("%i\n", current->n);
current = current->next;
n++;
}

return (n);
}

/**
 * add_nodeint_end - to add a new node at the end of a listint_t list.
 * @head: points to the first node.
 * @n: the integer to be added.
 * Return: the address of the new element, or NULL if it failed.
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
listint_t *new;
listint_t *current;

current = *head;

/* Allocate node. */
new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}

/* Put in the data. */
new->n = n;
new->next = NULL;

/* If the list is empty, make the new node the head. */
if (*head == NULL)
{
*head = new;
}

/* Else, traverse the list and insert the new node at the end. */
else
{
while (current->next != NULL)
{
current = current->next;
}

current->next = new;
}

return (new);
}

/**
 * free_listint - to free a listint_t list.
 * @head: a pointer to the first node.
 * Return: Void.
 */
void free_listint(listint_t *head)
{
listint_t *current;

/* While head is not null, iterate through the list. */
while (head != NULL)
{
current = head;
head = head->next;
free(current);
}
}

