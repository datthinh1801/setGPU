from setuptools import find_packages, setup

setup(
    name="setgpu",
    version="0.1.2",
    description="A small Python library that automatically sets CUDA_VISIBLE_DEVICES to the least-loaded GPU on multi-GPU systems.",
    author="datthinh1801",
    author_email="datthinh1801@gmail.com",
    platforms=["any"],
    license="Public Domain",
    url="https://github.com/datthinh1801/setGPU",
    py_modules=["setgpu"],
    install_requires=["gpustat"],
    packages=find_packages(),
)
