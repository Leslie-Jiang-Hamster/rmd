import argparse
import templ
import config

parser = argparse.ArgumentParser()
parser.add_argument('-e', action='store_true', help='edit the config file')

parser.parse_args()

print(templ.greetings)