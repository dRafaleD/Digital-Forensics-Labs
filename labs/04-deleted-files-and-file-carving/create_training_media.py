#!/usr/bin/env python3
"""Create a harmless byte stream for file-carving practice."""

from pathlib import Path

out = Path("training_media.bin")

jpeg_like = (
    bytes.fromhex("FFD8FFE0")
    + b"JFIF\x00"
    + b"DF_LAB04_JPEG_PAYLOAD"
    + bytes.fromhex("FFD9")
)

png_like = (
    bytes.fromhex("89504E470D0A1A0A")
    + b"DF_LAB04_PNG_PAYLOAD"
    + bytes.fromhex("49454E44AE426082")
)

data = (
    b"UNALLOCATED_STYLE_PADDING_" * 8
    + jpeg_like
    + b"RANDOM_GAP_" * 12
    + png_like
    + b"TRAILING_PADDING_" * 8
)

out.write_bytes(data)
print(f"Created {out} ({len(data)} bytes)")
print("This is synthetic training data, not a real disk image.")
