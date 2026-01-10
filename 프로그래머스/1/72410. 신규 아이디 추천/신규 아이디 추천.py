def solution(new_id):
    new_id = new_id.lower()

    allowed = set("abcdefghijklmnopqrstuvwxyz0123456789-_.")
    new_id = ''.join(c for c in new_id if c in allowed)

    result = []
    for c in new_id:
        if result and result[-1] == '.' and c == '.':
            continue
        result.append(c)
    new_id = ''.join(result)
    new_id = new_id.strip('.')

    if not new_id:
        new_id = 'a'
    new_id = new_id[:15]
    new_id = new_id.rstrip('.')
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id