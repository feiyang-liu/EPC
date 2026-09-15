import sys

import numpy as np
import torch
import transformers
from PIL import Image


def main():
    print("EPC public preview - environment check")
    print("=" * 45)

    print(f"Python       : {sys.version.split()[0]}")
    print(f"PyTorch      : {torch.__version__}")
    print(f"Transformers : {transformers.__version__}")
    print(f"NumPy        : {np.__version__}")
    print(f"Pillow       : {Image.__version__}")

    print(f"CUDA available: {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        print(f"CUDA device   : {torch.cuda.get_device_name(0)}")

    x = torch.tensor([1.0, 2.0, 3.0])
    assert torch.isfinite(x).all()

    print("=" * 45)
    print("Environment check passed.")


if __name__ == "__main__":
    main()
