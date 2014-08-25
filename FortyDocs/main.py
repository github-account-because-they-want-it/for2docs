'''
Created on Aug 11, 2014
@author: Mohammed Hamdy
'''
from __future__ import print_function, division
from lib.dbmaker import ModelFiller
from lib.docmaker import HTMLDocMaker
import time
NOISY = True

def main(sourceDirectory, destinationDirectory, docTitle, defines):
  #mf = ModelFiller(sourceDirectory, defines)
  if NOISY:
    print("Phase #1: Parsing source files into database")
    t = time.time()
  #mf.fillModel()
  if NOISY:
    #print("Phase #1: Finished <parsed {:d} files in {:.2f} minutes>".format(mf.fileCount(), (time.time()-t) / 60))
    print()
    print("Phase #2: Generating documentation")
    
  dm = HTMLDocMaker(destinationDirectory, docTitle)
  dm.makeDocs()
  if NOISY:
    print("Phase #2: Finished")
    print("Done")

if __name__ == "__main__":
  import argparse, ConfigParser, os
  config_file_name = os.path.join(os.path.dirname(__file__), "last_args.txt")
  parser = argparse.ArgumentParser()
  parser.add_argument("-s", "--source_directory", help="The directory in which to search for Fortran files, recursively")
  parser.add_argument("-d", "--destination_directory", help="The directory in which documentation will be generated")
  parser.add_argument("-t", "--doc_title", default="Fortran Documentation", help="The title used in the documentation tab and index link")
  parser.add_argument('--define', nargs='+', default=[])
  args = parser.parse_args()
  if not args.source_directory or not args.destination_directory:
    # look for a config
    if os.path.exists(config_file_name):
      config_parser = ConfigParser.ConfigParser()
      config_parser.read(config_file_name)
      source_directory = config_parser.get("Directories", "source_directory")
      destination_directory = config_parser.get("Directories", "destination_directory")
      documentation_title = config_parser.get("Other", "documentation_title")
      defines = config_parser.get("Other", "conditional_defines")
      main(source_directory, destination_directory, documentation_title, defines)
    else:
      parser.print_help()
  else:
    source_directory = args.source_directory
    destination_directory = args.destination_directory
    documentation_title = args.doc_title
    conditional_defines = args.define
    config_parser = ConfigParser.ConfigParser()
    config_parser.add_section("Directories")
    config_parser.set("Directories", "source_directory", source_directory)
    config_parser.set("Directories", "destination_directory", destination_directory)
    config_parser.add_section("Other")
    config_parser.set("Other", "documentation_title", documentation_title)
    config_parser.set("Other", "conditional_defines", conditional_defines)
    with open(config_file_name, "wb") as conf:
      config_parser.write(conf)
    main(source_directory, destination_directory, args.doc_title, conditional_defines)