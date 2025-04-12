import frida
import os
import hashlib
import argparse
import logging


def run_decrypt(input_dir, output_dir):
    if not os.path.exists(input_dir):
        logging.error(f"Input directory: {input_dir} does not exist.")
        return

    # get abs path
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)

    # hook
    session = frida.attach("QQMusic.exe")

    # load script
    script = session.create_script(open("hook_qq_music.js", "r", encoding="utf-8").read())
    script.load()

    if not os.path.exists(output_dir):
        logging.info(f"Creating output directory: {output_dir}")
        os.makedirs(output_dir)

    # for each file
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.splitext(file)
            
            # only mflac and mgg
            if file_path[-1] in [".mflac", ".mgg"]:
                logging.info(f"Decrypting {file}")
                
                # rename
                file_path = list(file_path)
                file_path[-1] = file_path[-1].replace("mflac", "flac").replace("mgg", "ogg")
                
                # check if file exists
                output_file_path = os.path.join(output_dir, "".join(file_path))
                if os.path.exists(output_file_path):
                    logging.info(f"File {output_file_path} exists, skipping...")
                    continue

                tmp_file_path = hashlib.md5(file.encode()).hexdigest()
                tmp_file_path = os.path.join(output_dir, tmp_file_path)
                tmp_file_path = os.path.abspath(tmp_file_path)
                
                # invoke script
                data = script.exports_sync.decrypt(os.path.join(root, file), tmp_file_path)
                
                # rename
                os.rename(tmp_file_path, output_file_path)
                logging.info(f"Decrypt success: {output_file_path}")

    session.detach()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True, help="Please input input directory")
    parser.add_argument("-o", "--output", type=str, required=True, help="Please input output directory")
    args = parser.parse_args()
    run_decrypt(args.input, args.output)