# Based on: pyobjc.readthedocs.io/en/latest/notes/using-nsxpcinterface.html#a-template-extension

from setuptools import Extension, setup

setup(
    name="test-protocol-ext",
    version="0.1",
    ext_modules=[
        Extension(
            "test_protocol_ext",
            ["test_protocol_ext.m"],
            extra_link_args=["-framework", "Cocoa"],
            py_limited_api=True,
        )
    ],
)
