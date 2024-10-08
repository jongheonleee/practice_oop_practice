def clip(text : str, max_len : 'int > 0' = 80) -> str :
  end = None

  if len(text) > max_len :
    space_before = text.rfind(' ', 0, max_len)
    if space_before >= 0 :
      end = space_before

    else :
      space_after = text.rfind(' ', max_len)
      if space_after >= 0 :
        end = space_after

  if end is None :
    end = len(text)

  return text[:end].rstrip()

# 어노테이션은 파이썬 인터프리터와 아무런 상관 없음
print(clip.__annotations__)