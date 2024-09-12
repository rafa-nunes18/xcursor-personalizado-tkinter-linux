/* tkXcursor - Extensão para gerenciamento de cursores RGBA/animados   
 * para widgets Tkinter sob X.org  
 * Copyright (C) 2009 por Igor E. Novikov  
 *  
 * Versão 2.0.0 - 2024 Editado por Rafael A. Nunes  
 *   
 * Esta biblioteca é um software livre; você pode redistribuí-la e/ou  
 * modificá-la sob os termos da GNU Library General Public  
 * License, conforme publicado pela Free Software Foundation; seja  
 * a versão 2 da Licença, ou (a seu critério) qualquer versão posterior.  
 *  
 * Esta biblioteca é distribuída na esperança de que seja útil,  
 * mas SEM NENHUMA GARANTIA; sem mesmo a garantia implícita de  
 * COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM PROPÓSITO ESPECÍFICO. Veja a GNU  
 * Library General Public License para mais detalhes.  
 *  
 * Você deve ter recebido uma cópia da GNU Library General Public  
 * License junto com esta biblioteca; se não, escreva para a Free Software  
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  EUA  
 */ 
#include <X11/Xcursor/Xcursor.h>  
#include <X11/X.h>  
#include <tcl.h>  
#include <tk.h>  
#include <Python.h>  

// Função para verificar se ARGB é suportado  
static PyObject * tkXcursor_IsSupportedARGB(PyObject * self, PyObject * args) {  
    const char *tkwin_name;  
    PyObject *interpaddr;  
    Tcl_Interp *interp;  
    Tk_Window tkwin;  
    Display *display;  

    // Pareando os argumentos passados para a função  
    if (!PyArg_ParseTuple(args, "sO", &tkwin_name, &interpaddr))  
        return NULL;  

    interp = (Tcl_Interp *)PyLong_AsLong(interpaddr);  
    tkwin = Tk_NameToWindow(interp, tkwin_name, (ClientData)Tk_MainWindow(interp));  
    if (!tkwin) {  
        PyErr_SetString(PyExc_ValueError, Tcl_GetStringResult(interp));  
        return NULL;  
    }  

    display = Tk_Display(tkwin);  
    return PyLong_FromLong(XcursorSupportsARGB(display));  
}  

// Função para carregar um cursor a partir de um arquivo  
static PyObject * tkXcursor_FilenameLoadCursor(PyObject * self, PyObject * args) {  
    const char *filename;  
    const char *tkwin_name;  
    PyObject *interpaddr;  
    Tcl_Interp *interp;  
    Tk_Window tkwin;  
    Display *display;  

    // Pareando os argumentos passados para a função  
    if (!PyArg_ParseTuple(args, "sOs", &tkwin_name, &interpaddr, &filename))  
        return NULL;  

    interp = (Tcl_Interp *)PyLong_AsLong(interpaddr);  
    tkwin = Tk_NameToWindow(interp, tkwin_name, (ClientData)Tk_MainWindow(interp));  
    if (!tkwin) {  
        PyErr_SetString(PyExc_ValueError, Tcl_GetStringResult(interp));  
        return NULL;  
    }  

    display = Tk_Display(tkwin);  
    return PyLong_FromLong(XcursorFilenameLoadCursor(display, filename));  
}  

// Função para definir um cursor por ID  
static PyObject * tkXcursor_SetCursorByXID(PyObject * self, PyObject * args) {  
    const char *tkwin_name;  
    PyObject *interpaddr;  
    int cursor_id;  
    Tcl_Interp *interp;  
    Tk_Window tkwin;  
    Drawable drawable;  
    Display *display;  
    Cursor cursor;  

    // Pareando os argumentos passados para a função  
    if (!PyArg_ParseTuple(args, "sOi", &tkwin_name, &interpaddr, &cursor_id))  
        return NULL;  

    interp = (Tcl_Interp *)PyLong_AsLong(interpaddr);  
    cursor = (Cursor)cursor_id;  
    tkwin = Tk_NameToWindow(interp, tkwin_name, (ClientData)Tk_MainWindow(interp));  
    if (!tkwin) {  
        PyErr_SetString(PyExc_ValueError, Tcl_GetStringResult(interp));  
        return NULL;  
    }  

    drawable = Tk_WindowId(tkwin);  
    display = Tk_Display(tkwin);  
    XDefineCursor(display, drawable, cursor);  

    Py_INCREF(Py_None);  
    return Py_None;  
}  

// Definição dos métodos do módulo  
static PyMethodDef tkXcursor_methods[] = {  
    {"IsSupportedARGB", tkXcursor_IsSupportedARGB, METH_VARARGS, NULL},  
    {"FilenameLoadCursor", tkXcursor_FilenameLoadCursor, METH_VARARGS, NULL},  
    {"SetCursor", tkXcursor_SetCursorByXID, METH_VARARGS, NULL},  
    {NULL, NULL}  // Sentinel  
};  

// Definição do módulo  
static struct PyModuleDef tkXcursor_module = {  
    PyModuleDef_HEAD_INIT,  
    "_tkXcursor",          // Nome do módulo  
    "Module for Tkinter cursor support.",  // Documentação do módulo  
    -1,                   // Tamanho do estado do módulo  
    tkXcursor_methods     // Métodos do módulo  
};  

// Função de inicialização do módulo  
PyMODINIT_FUNC PyInit__tkXcursor(void) {  
    return PyModule_Create(&tkXcursor_module);  
}
