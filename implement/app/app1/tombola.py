import abc

class Tombola(abc.ABC) :
  @abc.abstractmethod
  def load(self, iterable):
    """iterable의 항목들을 추가함"""

  @abc.abstractmethod
  def pick(self):
    """
    - 무작위로 항목을 하나 제거하고 반환
    - 객체가 비어 있을 때 이 메서드를 실행하면 LookupError 발생
    """

  def loaded(self):
    """최소 한 개의 항목이 있으면 True, 없으면 False를 반환함"""
    return bool(self.inspect())

  def inspect(self):
    """현재 안에 있는 항목들로 구성된 정렬된 튜플을 반환함"""
    items = []

    while True :
      try :
        items.append(self.pick())
      except LookupError :
        break

    self.load(items)
    return tuple(sorted(items))

