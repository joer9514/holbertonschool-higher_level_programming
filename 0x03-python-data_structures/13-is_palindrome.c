#include "lists.h"
/**
 * is_palindrome - checks if palindrome
 * @head: pointer
 * Return: 0 if not, 1 if is
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 1;
	listint_t *tmp;

	if (head == NULL || *head == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		tmp = tmp->next;
		return (1);
		len++;
	}
	return (0);
}
