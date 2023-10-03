#include "lists.h"

/**
 * insert_node - to insert a number into a sorted singly linked list.
 * @head: to point to the head of the list.
 * @number: the number to insert.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
/* Declare a node and a new node. */
listint_t *node = *head;
listint_t *new;

/* Create a new node. */
new = malloc(sizeof(listint_t));

/* If malloc fails, return NULL. */
if (new == NULL)
{
return (NULL);
}

/* Set the value of the new node. */
new->n = number;

/* If the head is NULL or the number is less than the head, insert at the head. */
if (node == NULL || node->n >= number)
{
new->next = node;
*head = new;
return (new);
}

/* Traverse the list to find the correct position to insert the new node. */
while (node && node->next && node->next->n < number)
{
node = node->next;
}

/* Insert the new node. */
new->next = node->next;
node->next = new;

return (new);
}

