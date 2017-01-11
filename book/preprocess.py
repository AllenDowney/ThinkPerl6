import sys

from Filist import Filist

def main(name, filename, *argv):
    # print the contents of the given file
    ft = Filist(filename)
    ft.move_indexterms()
    ft.sub_lines(r'section\*', r'section')
    ft.sub_lines(r'\\begin{code}', r'\\begin{verbatim}plasTeXjava')
    ft.sub_lines(r'\\end{code}', r'\\end{verbatim}')
    ft.sub_lines(r'\\begin{stdout}', r'\\begin{verbatim}')
    ft.sub_lines(r'\\end{stdout}', r'\\end{verbatim}')
    ft.sub_lines(r'Chapter~\\ref', r'~\\ref')
    ft.sub_lines(r'Section~\\ref', r'~\\ref')
    ft.sub_lines(r'Subsection~\\ref', r'~\\ref')
    ft.sub_lines(r'Figure~\\ref', r'~\\ref')
    ft.sub_lines(r'Exercise~\\ref', r'~\\ref')
    ft.sub_lines(r'\\java{\\%', r'\\java{%')
    ft.sub_lines(r'\[fontshape=up\]', r'')
    ft.sub_lines(r'\(p.~\\pageref\{[^\}]*\}\)', r'')
    print ft

if __name__ == '__main__':
    main(*sys.argv)
