import sys
import compiler

if __name__=="__main__":

    if len(sys.argv)==1:
        files_names = ['first.txt', 'second.txt','parietal_lobe.txt']
    else:
        files_names = sys.argv[1:]

    compiler.compile(files_names, "out.md")
