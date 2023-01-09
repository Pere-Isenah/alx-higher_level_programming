#include "lists.h"
#include <stddef.h>

int is_palindrome(listint_t **head) {
  if (head == NULL || *head == NULL) {
    return 1;
  }

  listint_t *current = *head;
  int length = 0;
  while (current != NULL) {
    current = current->next;
    length++;
  }

  current = *head;
  int values[length];
  int i = 0;
  while (current != NULL) {
    values[i] = current->n;
    current = current->next;
    i++;
  }

  int start = 0;
  int end = length - 1;
  while (start < end) {
    if (values[start] != values[end]) {
      return 0;
    }
    start++;
    end--;
  }

  return 1;
}
