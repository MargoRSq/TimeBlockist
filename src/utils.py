from src.config import DAY, HOUR, MINUTE
from src.exc import invalid_segm


def atof(s):
    try:
        if int(s):
            return (len(s))
    except:
        if not s:
            return 0
        return atof(s[:-1])

def count_secodns(segment: dict):
    match segment['segm']:
        case "d":
            return segment['num'] * DAY
        case "h":
            return segment['num'] * HOUR
        case "m":
            return segment['num'] * MINUTE
        case "s":
            return segment['num']
        case _:
            raise invalid_segm("Enter correct segment")

def fetch_segment(time_str: str):
    try:
        segm_index = atof(time_str)
        segm_str = time_str[:segm_index + 1]
        num = int(segm_str[:-1])
        segm = segm_str[-1:]
        return {"num": num, "segm": segm}
    except BaseException:
        print("Invalid input")
