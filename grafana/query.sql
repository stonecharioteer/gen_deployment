SELECT
  DATE(DATE_SUB(closed_on, INTERVAL DAYOFMONTH(closed_on) - 1 DAY)) AS time,
  COUNT(DISTINCT issue_id) as value,
  "Late" as metric
FROM redmine_issues_summary WHERE closed_on is not null and $__timeFilter(closed_on) and
assignee_name in($a_name) and 
assignee_groups in($a_groups) and 
priority in($prior) and 
top_parent_project_name in($top_parent) and 
tracker in($track) and 
project_name in($proj_name) and 
status in($stat) and closed_on_time = "Late"
group by closed_month_lbl
ORDER BY closed_on


