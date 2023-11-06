#include "python.h"
#include <object.h>
#include <listobject.h>
/**
*print_python_list_info - program
*Return:0
*@p:parameter
*/
void print_python_list_info(PyObject *p)
{
int i, size, aloc;
PyObject *obj;
size = PY_SIZE(p);
aloc = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", aloc);
for (i = 0; i < size; i++)
{
printf("Elemen %d: ", i);
obj = PyList_Getitem(p, i);
printf("%s\n", Py_TYPE(obj)->tp_name);
}
