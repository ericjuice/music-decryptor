## Music Decryptor

Just batch decrypt the vip songs downloaded by QQMusic.
You should have vip privilege to download songs.

Simplified version of [decrypt-mflac-frida](https://github.com/yllhwa/decrypt-mflac-frida)

Supports:
- Platform: Windows10/11
- App version: Latest QQMusic (2025.04.12)
- Format: *.mflac, *.mgg
 
## Usage
1. Launch QQMusic and download the music
2. run the following command
    ```bash
    pip install -r requirements.txt
    python main.py -i <input_dir> -o <output_dir>
    ```

## Warning
This tool is only for educational purposes and is not intended for commercial use.
