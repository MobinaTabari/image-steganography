import numpy as np
import zlib
from PIL import Image


# V2 Header Configuration
MAGIC = b"STEG"
VERSION = 2

HEADER_SIZE = 14
HEADER_BITS = HEADER_SIZE * 8

SEQUENTIAL = 0
PRNG = 1


def prepare_image(image):
    """
    Convert image to RGB and return its pixel data.
    """
    image = image.convert("RGB")
    pixels = np.array(image, dtype=np.uint8)

    return pixels


def message_to_bytes(message):
    """
    Encode text as UTF-8 bytes.
    """
    return message.encode("utf-8")


def bytes_to_bits(data):
    """
    Convert bytes to bits using MSB-first order.
    """
    return ''.join(format(byte, '08b') for byte in data)


def message_to_bits(message):
    """
    Convert a text message to UTF-8 bits.
    """
    message_bytes = message_to_bytes(message)

    return bytes_to_bits(message_bytes)


def bits_to_bytes(bits):
    """
    Convert a bit string back to bytes.
    """
    if len(bits) % 8 != 0:
        raise ValueError("Bit length must be a multiple of 8.")

    if any(bit not in "01" for bit in bits):
        raise ValueError("Bits must contain only 0 and 1.")

    byte_values = []

    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        byte_value = int(byte, 2)
        byte_values.append(byte_value)

    return bytes(byte_values)


def create_header(payload_bytes, method):
    """
    Create the V2 header and return it as a 112-bit string.

    Header layout:
    Magic (4 bytes)
    Version (1 byte)
    Method (1 byte)
    Payload length (4 bytes, Big Endian)
    CRC32 (4 bytes, Big Endian)
    """

    if not isinstance(payload_bytes, bytes):
        raise TypeError("payload_bytes must be bytes.")

    if method not in (SEQUENTIAL, PRNG):
        raise ValueError("Invalid embedding method.")

    payload_length = len(payload_bytes)

    if payload_length > 0xFFFFFFFF:
        raise ValueError("Payload is too large.")

    crc32_value = zlib.crc32(payload_bytes) & 0xFFFFFFFF

    header = (
        MAGIC
        + bytes([VERSION, method])
        + payload_length.to_bytes(4, byteorder="big")
        + crc32_value.to_bytes(4, byteorder="big")
    )

    return bytes_to_bits(header)


def check_capacity(image_array, payload_bits):
    """
    Check whether the image has enough capacity
    for the V2 header and secret message.
    """

    total_channels = image_array.size
    required_bits = HEADER_BITS + len(payload_bits)

    if required_bits > total_channels:
        raise ValueError(
            f"Insufficient image capacity! "
            f"Required: {required_bits} bits, "
            f"Available: {total_channels} bits."
        )

    return total_channels - HEADER_BITS