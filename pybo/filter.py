def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'.encode('unicode-escape').decode()):
    return value.strftime(fmt).encode().decode('unicode-escape')