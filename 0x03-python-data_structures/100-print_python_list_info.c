#include <Python.h>
#include <stdio.h>


/**
 * print_python_list_info - Prints information about a Python list.
 * @p: PyObject pointer representing the Python list.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyObject *item;
	Py_ssize_t size, i;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
