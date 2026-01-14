def solution(today, terms, privacies):
    def to_days(date):
        y, m, d = map(int, date.split('.'))
        return y * 12 * 28 + m * 28 + d
    today_days = to_days(today)
    term_dict = {}
    for term in terms:
        kind, months = term.split()
        term_dict[kind] = int(months) * 28
    answer = []
    for i, privacy in enumerate(privacies):
        date, kind = privacy.split()
        collected_day = to_days(date)
        expire_day = collected_day + term_dict[kind]
        if expire_day <= today_days:
            answer.append(i + 1)
    return answer