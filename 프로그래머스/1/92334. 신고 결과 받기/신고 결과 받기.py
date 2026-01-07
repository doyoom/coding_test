def solution(id_list, report, k):
    answer = []
    report = set(report)
    reported_count = {user: 0 for user in id_list}
    report_map = {user: [] for user in id_list}
    for r in report:
        reporter, reported = r.split()
        reported_count[reported] += 1
        report_map[reporter].append(reported)
    banned = set()
    for user in reported_count:
        if reported_count[user] >= k:
            banned.add(user)
    for user in id_list:
        count = 0
        for target in report_map[user]:
            if target in banned:
                count += 1
        answer.append(count)
    return answer