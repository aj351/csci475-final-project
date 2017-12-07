2:
- Statistical databases are databases that allow queries of data on aggregate
  but not of individual data points. It seems safe enough - `select mean(income)
  from table` doesn't reveal the income of any individual. But the dangerous
  scenario occurs when an attacker is able to isolate the results from a single
  row, either by adding careful conditionals (such as "where"s) to the query, or
  by querying before and after the addition/removal of the target row.

- Discuss the two extremes of privacy and usability.
- Overview of DP.

9:
- Only industry implementations are from large companies.
- Apple uses it to collect data on iOS devices post iOS 10. Microsoft pioneered
  this research and hopefully is using it Cortana, etc.
- Many other companies have large statistical databases vulnerable to inference
  attacks
- Software engineers have big opportunity to implement in industry
- An open library to add DP functionality to a database would be very good in
  aiding adoption
