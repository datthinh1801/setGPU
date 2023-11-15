# setGPU

A small Python library that automatically sets `CUDA_VISIBLE_DEVICES`
to the least-loaded GPU on multi-GPU systems and can be used by:

Putting `import setgpu` before any import
   that will use a GPU like Torch, TensorFlow, or JAX.

# Installation

```
pip install git+https://github.com/datthinh1801/setGPU.git
```

# Dependencies

+ [Jongwook Choi's](https://wook.kr) [gpustat](https://github.com/wookayin/gpustat) library (`pip install gpustat`)

# Licensing

This code is in the public domain.
