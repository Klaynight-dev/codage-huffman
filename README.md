# Huffman Coding

## Overview
This repository, named `codage-huffman`, provides a Python implementation of the Huffman coding algorithm. Huffman coding is a popular compression algorithm that assigns variable-length codes to input characters based on their frequencies, resulting in more efficient encoding for frequently occurring characters.

## Usage

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/Klaynight-dev/codage-huffman.git
cd codage-huffman
```

### Example
```python
from huffman import encoder_huffman, decoder_huffman

# Example text
text = "bonjour le monde"

# Encode the text using Huffman coding
encoded_text, huffman_codes = encoder_huffman(text)

# Decode the encoded text using Huffman codes
decoded_text = decoder_huffman(encoded_text, huffman_codes)

# Print results
print(f"Huffman Codes: {huffman_codes}")
print(f"Original Text: {text}")
print(f"Encoded Text: {encoded_text}")
print(f"Decoded Text: {decoded_text}")
```

### Output
```
Huffman Codes: {'b': '00', 'o': '01', 'n': '10', 'j': '110', 'u': '1110', 'r': '1111', ' ': '001', 'l': '1000', 'e': '1001', 'm': '101'}
Original Text: bonjour le monde
Encoded Text: 0001001110110111000111111000010100000101100111111110000100111110111100001111101000101101111001101011011100111000
Decoded Text: bonjour le monde
```

## Implementation Details

### `Noeud` Class
- Represents a node in the Huffman tree.
- Attributes:
  - `char` (str): The character associated with the node (None for internal nodes).
  - `freq` (int): The frequency of the character in the text.
  - `gauche` (Noeud): The left child node.
  - `droite` (Noeud): The right child node.
  - `identifiant` (int): Identifier of the node.

### `construire_arbre_huffman` Function
- Builds the Huffman tree for a given text.

### `encoder_huffman` Function
- Encodes a text using the Huffman algorithm.
- Returns the encoded text and a dictionary of Huffman codes.

### `decoder_huffman` Function
- Decodes an encoded text using Huffman codes.
- Returns the decoded text.

### `construire_codes_huffman` Function
- Builds a dictionary mapping characters to their Huffman codes.

## Author
- **GitHub:** [Klaynight-dev](https://github.com/Klaynight-dev)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
