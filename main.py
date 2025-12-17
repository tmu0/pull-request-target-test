import os

MERGE_COMMIT_SHA = os.environ.get('MERGE_COMMIT_SHA','not set')
GITHUB_PR_SHA = os.environ.get('GITHUB_PR_SHA','not set')


def main():
    print(f"MERGE_COMMIT_SHA = {MERGE_COMMIT_SHA}")
    print(f"GITHUB_PR_SHA = {GITHUB_PR_SHA}")
    print("internal pr")
    if GITHUB_PR_SHA != 'not set':
        with open(os.path.join(GITHUB_PR_SHA, 'README.md'), 'r') as readme:
            print(readme.read())


if __name__ == '__main__':
    main()
