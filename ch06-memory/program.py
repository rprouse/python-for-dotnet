import memutil
from doomed import Doomed


def ref_counting():
    v1 = Doomed()
    v1_id = id(v1)
    print(f"Step 1: Ref count is {memutil.refs(v1_id)}")

    v2 = v1
    print(f"Step 2: Ref count is {memutil.refs(v1_id)}")

    v2 = None
    print(f"Step 3: Ref count is {memutil.refs(v1_id)}")

    v1 = None
    print(f"Step 4: Ref count is {memutil.refs(v1_id)}")

    print("End of method", flush=True)


def gcing():
    pass


def main():
    ref_counting()
    gcing()


if __name__ == '__main__':
    main()