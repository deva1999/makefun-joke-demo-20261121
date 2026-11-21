import os

JOKE = (
    "My AI coding agent passed every test in the live demo \u2014 it should, "
    "it wrote the code, wrote the tests, and graded its own homework on stage."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
