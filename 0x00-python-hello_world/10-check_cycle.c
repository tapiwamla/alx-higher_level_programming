#include "lists.h"

/**
 * check_cycle - to check if a singly linked list has a cycle in it.
 * @list: a pointer to the head of the linked list.
 * Return: 0 if there is no cycle, and 1 if there is.
 */
int check_cycle(listint_t *list)
{
listint_t *single_node;
listint_t *double_node;

/* Check for empty list or a list with a single node */
if (list == NULL || list->next == NULL)
{
return (0);
}

/**
 * Initialize the pointers to traverse the list.
 * single_node moves one node at a time.
 * double_node moves two nodes at a time.
 */

single_node = list;
double_node = list->next;

/* Traverse the list using single_node and double_node pointers */
while (double_node != NULL && double_node->next != NULL)
{
/* If the single_node and double_node meet at some point then there is a loop. */
if (single_node == double_node)
{
return (1);
}

/* Move the single node pointer one step. */
single_node = single_node->next;

/* Move the double node pointer one step. */
double_node = double_node->next->next;
}

/* If a loop exits, there is no cycle in the linked list. */
return (0);
}

