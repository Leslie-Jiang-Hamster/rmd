import datetime
import templ
import config

class Anniversary:
  def __init__(self, month, day):
    self.month = month
    self.day = day

  def days_before(self):
    current_year = datetime.date.today().year
    time_delta = datetime.date(current_year, self.month, self.day) - datetime.date.today()
    days_before = time_delta.days
    assert(type(days_before) == int)
    return days_before
  
  def __str__(self):
    raise NotImplementedError

class Festival(Anniversary):
  def __init__(self, month, day, fesitval_name):
    super().__init__(month, day)
    self.festival_name = fesitval_name
  
  def __str__(self):
    if not (0 <= self.days_before() and self.days_before() <= config.days_before_threshold):
      return ''
    return templ.festival_greetings(
      self.days_before(),
      self.festival_name
    )

class Birthday(Anniversary):
  def __init__(self, month, day, person):
    super().__init__(month, day)
    self.person = person
  
  def __str__(self):
    if not (0 <= self.days_before() and self.days_before() <= config.days_before_threshold):
      return ''
    return templ.birthday_greetings(
      self.days_before(),
      self.person
    )