import argparse
import psycopg2
import pyPdf
import PythonMagick
import tempfile
import contextlib
import os
import shutil

@contextlib.contextmanager
def make_temp_directory():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def main(argv=None):
    global load_tests

    parser = argparse.ArgumentParser()

    parser.add_argument('--database', type=str, default='png-testing')
    parser.add_argument('--user', type=str, default='qa')
    parser.add_argument('pdf_a', type=str)
    parser.add_argument('pdf_b', type=str) 

    args = parser.parse_args(argv)

    settings = vars(args)

    with make_temp_directory() as build_dir: 
        with psycopg2.connect(database=settings['database']) as con:
            with con.cursor() as cur:
                cur.execute("DROP TABLE IF EXISTS png_a")
                cur.execute("CREATE TABLE png_a (Page INT PRIMARY KEY, Data BYTEA)")
                pdf_im = pyPdf.PdfFileReader(file(settings['pdf_a'], "rb"))
                npage = pdf_im.getNumPages()
                for i in range(0,npage):
                    im = PythonMagick.Image(settings['pdf_a'] + "[{0}]".format(i))
                    png_path = os.path.join(build_dir,'file_out-' + str(i)+ '.png')
                    im.write(png_path)
                    with open(png_path,'r') as f:
                        img = f.read()
                        binary = psycopg2.Binary(img)
                        cur.execute("INSERT INTO png_a (Page, Data) VALUES (%s, %s)", (str(i),binary) )
                    os.remove(png_path)

                cur.execute("DROP TABLE IF EXISTS png_b")
                cur.execute("CREATE TABLE png_b (Page INT PRIMARY KEY, Data BYTEA)")
                pdf_im = pyPdf.PdfFileReader(file(settings['pdf_b'], "rb"))
                npage = pdf_im.getNumPages()
                for i in range(0,npage):
                    im = PythonMagick.Image(settings['pdf_b'] + "[{0}]".format(i))
                    png_path = os.path.join(build_dir,'file_out-' + str(i)+ '.png')
                    im.write(png_path)
                    with open(png_path,'r') as f:
                        img = f.read()
                        binary = psycopg2.Binary(img)
                        cur.execute("INSERT INTO png_b (Page, Data) VALUES (%s, %s)", (str(i),binary) )
                    os.remove(png_path)

if __name__ == "__main__":
    main() 
