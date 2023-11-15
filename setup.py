from setuptools import find_packages, setup

setup(
    name="setGPU",
    version="0.0.9",
    description="A small Python library that automatically sets CUDA_VISIBLE_DEVICES to the least-loaded GPU on multi-GPU systems.",
    author="Brandon Amos",
    author_email="datthinh1801@gmail.com",
    platforms=["any"],
    license="Public Domain",
    url="https://github.com/datthinh1801/setGPU",
    py_modules=["setGPU"],
    install_requires=["gpustat"],
)
