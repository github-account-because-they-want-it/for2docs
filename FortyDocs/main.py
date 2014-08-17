'''
Created on Aug 11, 2014
@author: Mohammed Hamdy
'''
from __future__ import print_function, division
from lib.dbmaker import ModelFiller
from lib.docmaker import HTMLDocMaker
import time
NOISY = True

def main(sourceDirectory, destinationDirectory):
  mf = ModelFiller(sourceDirectory)
  if NOISY:
    print("Phase #1: Parsing source files into database")
    t = time.time()
  #mf.fillModel()
  if NOISY:
    print("Phase #1: Finished <parsed {:d} files in {:.2f} minutes>".format(mf.fileCount(), (time.time()-t) / 60))
    print()
    print("Phase #2: Generating documentation")
    
  dm = HTMLDocMaker(destinationDirectory)
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
  args = parser.parse_args()
  if not args.source_directory or not args.destination_directory:
    # look for a config
    if os.path.exists(config_file_name):
      config_parser = ConfigParser.ConfigParser()
      config_parser.read(config_file_name)
      source_directory = config_parser.get("Directories", "source_directory")
      destination_directory = config_parser.get("Directories", "destination_directory")
      main(source_directory, destination_directory)
    else:
      parser.print_help()
  else:
    source_directory = args.source_directory
    destination_directory = args.destination_directory
    config_parser = ConfigParser.ConfigParser()
    config_parser.add_section("Directories")
    config_parser.set("Directories", "source_directory", source_directory)
    config_parser.set("Directories", "destination_directory", destination_directory)
    with open(config_file_name, "wb") as conf:
      config_parser.write(conf)
    main(source_directory, destination_directory)