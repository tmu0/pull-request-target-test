import os


def main():
    print(f"MERGE_COMMIT_SHA = {os.environ.get('MERGE_COMMIT_SHA','not set')}")


if __name__ == '__main__':
    main()
