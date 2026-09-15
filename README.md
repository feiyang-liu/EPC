# EPC

Official repository for Evidence-Partitioned Calibration (EPC).

EPC is an inference-time calibration method for mitigating visual hallucinations in large vision-language models.

## Status

This repository currently provides a lightweight public preview of EPC.

A minimal interface, environment check, and smoke test are included. The current preview does not contain the complete EPC algorithm or benchmark evaluation pipeline.

The full implementation and reproduction code will be added after completion of the manuscript.

## Current Contents

- epc/preview.py: lightweight public preview utilities
- demo/environment_check.py: environment verification
- demo/smoke_test.py: basic interface smoke test
- requirements.txt: basic dependencies

## Quick Test

Environment check:

```bash
python demo/environment_check.py
```

Preview smoke test:

```bash
python demo/smoke_test.py
```

## Full Release

The complete EPC implementation, benchmark scripts, and reproduction instructions will be released in a later update.
