import sys

def read_in():
    print("Output from Python")
    print("First name: " + sys.argv[1])
    print("Last name: " + sys.argv[2])
    #Since our input would only be having one line, parse our JSON data from that
    return "hello"
if __name__ == '__main__':
    read_in()
