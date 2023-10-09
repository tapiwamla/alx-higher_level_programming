#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - to reverse a singly linked list.
 * @head: points to the address of the first node.
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
listint_t *node = *head, *next, *prev = NULL;

while (node)
{
next = node->next;
node->next = prev;
prev = node;
node = next;
}

*head = prev;
return (*head);
}

/**
 * is_palindrome - to check if a singly linked list is a palindrome.
 * @head: points to the address of the first node.
 * Return: 1 if it is a palindrome, 0 if it is not.
 */
int is_palindrome(listint_t **head)
{
listint_t *temp;
listint_t *rev;
listint_t *mid;
size_t size = 0;
size_t i;

if (*head == NULL || (*head)->next == NULL)
{
return (1);
}

temp = *head;
while (temp)
{
size++;
temp = temp->next;
}

temp = *head;
for (i = 0; i < (size / 2) - 1; i++)
{
temp = temp->next;
}

if ((size % 2) == 0 && temp->n != temp->next->n)
{
return (0);
}

temp = temp->next->next;
rev = reverse_listint(&temp);
mid = rev;

temp = *head;
while (rev)
{
if (temp->n != rev->n)
{
return (0);
}
temp = temp->next;
rev = rev->next;
}
reverse_listint(&mid);

return (1);
}

