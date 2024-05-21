def normal_greetings(date_string):
  return (f'''
    今天素 {date_string}! ᕙ(`▿´)ᕗ
    请务必吃好睡好,磨砺头脑,继续加油哦ww
  ''')

def birthday_greetings(person, days_before):
  assert type(days_before) == int
  assert 0 <= days_before and days_before <= 3

  return (f'''
    还有 {days_before} 天就素 {person} 宝宝的生日了˗ˋˏ♡ˎˊ˗
    记得早点去淘宝买个礼物哦ww
  ''')