import json

class TrendReport:
    def __init__(self, report, is_trend, has_diff_within_range, status):
        self.report = report
        self.is_trend = is_trend
        self.has_diff_within_range = has_diff_within_range
        self.status = status

    def to_dict(self):
        return {
            "report": self.report,
            "is_trend": self.is_trend,
            "has_diff_within_range": self.has_diff_within_range,
            "status": self.status
        }

def can_be_safe_by_removing_one_level(report):
    numbers = list(map(int, report.split()))
    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i+1:]
        if (is_increasing(modified_numbers) or is_decreasing(modified_numbers)) and has_difference_within_range(modified_numbers):
            return ' '.join(map(str, modified_numbers))
    return None

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

        if not (is_trend and has_diff_within_range):
            modified_report = can_be_safe_by_removing_one_level(report)
            if modified_report:
                numbers = list(map(int, modified_report.split()))
                is_trend = is_increasing(numbers) or is_decreasing(numbers)
                has_diff_within_range = has_difference_within_range(numbers)

        status = "Safe" if is_trend and has_diff_within_range else "Unsafe"
        trend_reports.append(TrendReport(report, is_trend, has_diff_within_range, status))
    return trend_reports

with open('input.txt') as file:
    content = file.readlines()
    reports = [x.strip() for x in content]

trend_reports = detect_trend_reports(reports)

# Print the JSON output
safe_reports_count = sum(1 for trend_report in trend_reports if trend_report.is_trend and trend_report.has_diff_within_range)
print(json.dumps({"reactor_reports": [trend_report.to_dict() for trend_report in trend_reports]}, indent=4))
print(json.dumps({"total_trends_with_diff": safe_reports_count}, indent=4))