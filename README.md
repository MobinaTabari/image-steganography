
# Image Steganography Using LSB Techniques

## Project Overview

This undergraduate project focuses on the implementation and analysis of image steganography techniques using Python.

The primary objective is to investigate how secret information can be embedded into digital images and subsequently extracted using Least Significant Bit (LSB) substitution methods.

The project is being developed collaboratively using Jupyter Notebooks and GitHub.

## Algorithms

The project focuses on two algorithms:

### 1. Sequential 1-bit LSB Substitution

This technique embeds secret information by modifying the least significant bits of image data in a sequential order.

### 2. Random / PRNG-based LSB Substitution

This technique uses a Pseudorandom Number Generator (PRNG) to determine the positions used for embedding and extracting secret information.

## Project Components

The project consists of two main components:

**Embedding**
- Converting secret messages into binary data
- Selecting embedding positions
- Modifying image data to hide information
- Generating stego images

**Extraction**
- Reading stego images
- Retrieving embedded binary data
- Reconstructing the original message
- Supporting sequential and PRNG-based extraction

## Technologies

- Python
- Jupyter Notebook
- Visual Studio Code
- Pillow
- Git and GitHub

## Project Structure

```text
image-steganography/
├── notebooks/
│   └── 02_extraction.ipynb
├── README.md
├── .gitignore
└── LICENSE
```

The project structure will be expanded as development progresses.

## Development Status

**Status: In Progress**

Implementation, testing, integration, and documentation are ongoing.

## References

1. Fridrich, J. — *Steganography in Digital Media: Principles, Algorithms, and Applications.*
2. Provos, N., & Honeyman, P. — *Hide and Seek: An Introduction to Steganography.*
