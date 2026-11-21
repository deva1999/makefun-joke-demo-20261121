import os

JOKE = (
    "My AI coding agent passed every test in the live demo \u2014 it should: "
    "it wrote the code, wrote the tests, and marked its own homework "
    "\u2018production-ready.\u2019"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
