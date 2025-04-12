## Music Decryptor

Simplified version of [decrypt-mflac-frid](https://github.com/yllhwa/decrypt-mflac-frid)

Supports:
- Platform: Windows10/11
- App version: Latest QQMusic (2025.04.12)
- Format: *.mflac, *.mgg
 
## Usage
1. Launch QQMusic and download the music
2. run the following command
    ```bash
    pip install -r requirements.txt
    python decrypt-mflac-frida.py -i <input_dir> -o <output_dir>
    ```