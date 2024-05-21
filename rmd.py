import argparse
import datetime
import os
import templ
import config

parser = argparse.ArgumentParser()

parser.add_argument(
  '-e',
  action='store_true',
  help='edit the config file'
)

args = parser.parse_args()

if args.e:
  os.system(config.editor + ' ' + config.config_file_name)
  exit(0)

print(templ.normal_greetings(str(datetime.date.today())))

str_anniversaries = [str(anniversary) for anniversary in config.anniversaries]
print(''.join(str_anniversaries))