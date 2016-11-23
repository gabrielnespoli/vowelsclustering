import lib as lib
import sys


def main():
    args = sys.argv[1:]
    clustering = [lib.charfreq(f, args[-2]) for f in args[:-2]]
    k = int(args[-1])

    indices = lib.single_linkage(clustering,k)

    for l in indices:
        cluster = [args[:-2][e] for e in l if e is not None]
        if len(cluster) != 0:
            print(cluster)

if __name__ == "__main__":
    main()
