import argparse
from log_hello_cli import sapa

def main():
    parser = argparse.ArgumentParser(description="Program sapaan sederhana.")
    parser.add_argument("--nama", type=str, required=True, help="Nama kamu")
    args = parser.parse_args()

    print(sapa(args.nama))

if __name__ == "__main__":
    main()