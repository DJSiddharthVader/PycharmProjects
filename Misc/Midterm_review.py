
def answer_phone(hour,is_weekday,is_mom):
    if is_mom is True:
        return "answer"
    else:
        if is_weekday is True:
            if hour >=7 and hour <= 21:
                return "answer"
            else:
                return "don't answer"
        else:
            if hour >= 10 and hour <= 23.99:
                return "answer"
            else:
                return "don't answer"
