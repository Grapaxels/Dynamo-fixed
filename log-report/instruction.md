There is an Apache-style access log at `/app/access.log`. Parse it and write a JSON report to `/app/report.json`.

Success criteria:

1. `/app/report.json` is a valid JSON object containing exactly these keys and value types: `total_requests` as an integer, `unique_ips` as an integer, and `top_path` as a string.
2. `total_requests` is the number of non-empty log entries in `/app/access.log`.
3. `unique_ips` is the number of distinct client IP addresses, using the first whitespace-separated field of each non-empty log entry.
4. `top_path` is the request path with the highest request count, using the path from each quoted HTTP request line.
