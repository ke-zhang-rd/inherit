import argparse


parser = argparse.ArgumentParser(description='Process a string.')
parser.add_argument('s', type=str, help='string for construct class')
args = parser.parse_args()


class Constructor:

    def __init__(self, s):
        self.s = s
        self.name_list = None
        self.f = open("src.py", "w")

    def check_legal(self):
        return True

    def output(self):
        if not self.check_legal():
            return False

        self.names = self.s.split('(')
        self.writer(f'{self.names[-1]}', '')
        for c, p in zip(self.names[-2::-1], self.names[:0:-1]):
            self.writer(f'{c}({p})', '')

    def writer(self, class_line, paras_line):
        body = f"class {class_line}:\n" +\
               "\n" +\
               "    def __init__(self):\n" +\
               "        pass\n" +\
               "\n\n"
        self.f.write(body)
        

def main():
    c = Constructor(args.s)
    c.output()


if __name__ == '__main__':
    main()
