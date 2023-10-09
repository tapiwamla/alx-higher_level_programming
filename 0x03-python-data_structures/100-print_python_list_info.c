#include <Python.h>

/**
 * print_python_list_info - to print the basic info of a python list.
 * @p: a PyObject list.
 */
void print_python_list_info(PyObject *p)
{
/* Declare PyListObject pointer and PyObject pointer. */
int size, alloc, i;
PyObject *obj;

/* Check if p is a list. */
size = Py_SIZE(p);
alloc = ((PyListObject *)p)->allocated;

/* Print the basic info of the list. */
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);

/* Print the type of each element in the list. */
for (i = 0; i < size; i++)
{
printf("Element %d: ", i);

obj = PyList_GetItem(p, i);
printf("%s\n", Py_TYPE(obj)->tp_name);
}
}

