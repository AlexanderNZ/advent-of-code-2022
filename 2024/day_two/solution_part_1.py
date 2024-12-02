from pprint import pprint

class TrendReport:
    def __init__(self, report, is_trend, has_diff_within_range, status):
        self.report = report
        self.is_trend = is_trend
        self.has_diff_within_range = has_diff_within_range
        self.status = status

    def __repr__(self):
        return f"TrendReport(report={self.report}, is_trend={self.is_trend}, has_diff_within_range={self.has_diff_within_range}, status={self.status})"

def has_difference_within_range(numbers, min_diff=1, max_diff=3):
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < min_diff or diff > max_diff:
            return False
    return True

def is_increasing(report):
    return all(report[i] < report[i + 1] for i in range(len(report) - 1))

def is_decreasing(report):
    return all(report[i] > report[i + 1] for i in range(len(report) - 1))

def detect_trend_reports(input_reports):
    trend_reports = []
    for report in input_reports:
        numbers = list(map(int, report.split()))
        is_trend = is_increasing(numbers) or is_decreasing(numbers)
        has_diff_within_range = has_difference_within_range(numbers)
        status = "Safe" if is_trend and has_diff_within_range else "Unsafe"
        trend_reports.append(TrendReport(report, is_trend, has_diff_within_range, status))
    return trend_reports

with open('input.txt') as file:
    content = file.readlines()
    reports = [x.strip() for x in content]

trend_reports = detect_trend_reports(reports)
pprint(trend_reports)

total_trends_with_diff = sum(1 for trend_report in trend_reports if trend_report.is_trend and trend_report.has_diff_within_range)
pprint(total_trends_with_diff)