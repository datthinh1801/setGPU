import os
import gpustat
import random


def set_gpu():
    stats = gpustat.GPUStatCollection.new_query()
    ids = map(lambda gpu: int(gpu.entry["index"]), stats)
    ratios = map(
        lambda gpu: gpu.memory_free * int(gpu.power_limit - gpu.power_draw > 100),
        stats,
    )
    pairs = [(id_, ratio) for id_, ratio in zip(ids, ratios) if ratio > 0]
    random.shuffle(pairs)
    try:
        bestGPU = min(pairs, key=lambda x: x[1])[0]
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = str(bestGPU)
        print(f"export CUDA_VISIBLE_DEVICES={bestGPU}")
    except ValueError:
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = ""
        print(f"No GPU available")
