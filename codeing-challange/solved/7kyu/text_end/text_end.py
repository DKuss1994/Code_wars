def solution(text, ending):
    if ending in text[len(ending)*-1:]:
        return True
    return False