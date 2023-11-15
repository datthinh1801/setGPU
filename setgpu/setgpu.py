import os
import gpustat
import random


def set_gpu():
    stats = gpustat.GPUStatCollection.new_query()
    ids = map(lambda gpu: int(gpu.entry["index"]), stats)
    ratios = map(
        lambda gpu: float(gpu.entry["memory.used"]) / float(gpu.entry["memory.total"]),
        stats,
    )
    pairs = list(zip(ids, ratios))
    random.shuffle(pairs)
    bestGPU = min(pairs, key=lambda x: x[1])[0]

    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = str(bestGPU)
    print(f"export CUDA_VISIBLE_DEVICES={bestGPU}")