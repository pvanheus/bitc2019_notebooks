import sys
import numpy


def main():
    script = sys.argv[0]
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
            data = numpy.loadtxt(filename, delimiter=',')
        except IOError as e:
            print("Could not read file: " + str(e))
            sys.exit(1) # exit with an error code
        for m in data.mean(axis=1):
            print(m)

    else:
        print('Usage: python ' + script + ' <filename>')

if __name__ == '__main__':
    main()
