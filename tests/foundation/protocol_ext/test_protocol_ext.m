// Based on: https://pyobjc.readthedocs.io/en/latest/notes/using-nsxpcinterface.html#a-template-extension

#define Py_LIMITED_API 0x030A0000
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#import <Cocoa/Cocoa.h>

@protocol TestProtocol
-(void)doSomething:(NSString*)name withReply:(void (^)(NSObject*))completion;
@end

static PyMethodDef mod_methods[] = {
    { }
};

static struct PyModuleDef module_def = {
     PyModuleDef_HEAD_INIT,
     "test_protocol_ext",
     NULL,
     0,
     mod_methods,
     NULL,
     NULL,
     NULL,
     NULL};

PyObject* __attribute__((__visibility__("default")))
PyInit_test_protocol_ext(void)
{
    // Have to reference the protocol somewhere so that it gets included in the
    // binary.
    (void)@protocol(TestProtocol);

    return PyModule_Create(&module_def);
}
