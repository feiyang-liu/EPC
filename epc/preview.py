import torch


def validate_logits(logits: torch.Tensor) -> None:
    """Validate tensor inputs used by the EPC public preview."""

    if not isinstance(logits, torch.Tensor):
        raise TypeError("logits must be a torch.Tensor")

    if logits.ndim < 2:
        raise ValueError("logits must have at least two dimensions")

    if not torch.isfinite(logits).all():
        raise ValueError("logits contain non-finite values")


def preview_info():
    """Return basic information about the current public preview."""

    return {
        "method": "EPC",
        "status": "public preview",
        "full_implementation": False,
    }
