def normal_greetings(date_string):
  assert type(date_string) == str
  return (f'''
    今天素 {date_string}! ᕙ(`▿´)ᕗ
    请务必吃好睡好,磨砺头脑,继续加油哦ww
  ''')

def birthday_greetings(days_before, person):
  assert type(days_before) == int
  assert type(person) == str
  assert person != ''
  return (f'''
    以及！！还有{days_before}天就素{person}宝宝的生日啦˗ˋˏ♡ˎˊ˗
    记得早点去淘宝买个礼物！=͟͟͞͞ʕ•̫͡•ʔ 
  ''')

def festival_greetings(days_before, festival_name):
  assert type(days_before) == int
  assert type(festival_name) == str
  assert festival_name != ''
  return (f'''
    好快哦，{festival_name}就快到了！还有{days_before}天੭ ᐕ)੭*⁾⁾
  ''')