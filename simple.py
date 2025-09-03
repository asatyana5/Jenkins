import random
import sys

def main():
    # Randomly decide pass or fail
    result = random.choice([True, False])

    if result:
        print("✅ Test Passed")
        sys.exit(0)  # exit code 0 = success
    else:
        print("❌ Test Failed")
        sys.exit(1)  # exit code 1 = failure

if __name__ == "__main__":
    main()
