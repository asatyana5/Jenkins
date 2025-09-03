import sys

def main():
    print("❌ Test Failed (forced failure for Jenkins test)!")
    sys.exit(0)   # non-zero exit code → Jenkins marks build as failed

if __name__ == "__main__":
    main()
