import sys
import numpy


def main():
    script = sys.argv[0]
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
            data = numpy.loadtxt(filename, delimiter=',')
            for m in data.mean(axis=1):
                print(m)
        except IOError as e:
            print("Could not read file: " + str(e))
    else:
        print('Usage: python ' + script + ' <filename>')

main()
