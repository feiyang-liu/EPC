import torch

from epc.preview import preview_info, validate_logits


def main():
    logits = torch.randn(1, 32000)

    validate_logits(logits)

    info = preview_info()

    print("EPC preview smoke test")
    print("=" * 40)
    print(f"Method              : {info['method']}")
    print(f"Status              : {info['status']}")
    print(f"Full implementation : {info['full_implementation']}")
    print(f"Input shape         : {tuple(logits.shape)}")
    print("=" * 40)
    print("Smoke test passed.")


if __name__ == "__main__":
    main()
