import argparse
import logging
from log_hello_cli import sapa
logging.basicConfig(filename='log.txt', level=logging.INFO)
def main():
    parser = argparse.ArgumentParser(description="Program sapaan sederhana.")
    parser.add_argument("--nama", type=str, required=True, help="Nama kamu")
    args = parser.parse_args()

    try:
        pesan = sapa(args.nama)
        logging.info(f'program dijakankan oleh {args.nama}')
        print(pesan)
    except Exception as e:
        logging.error(f'ERRO : {e}')
        print('maaf terjadi kesalahan')

if __name__ == "__main__":
    main()