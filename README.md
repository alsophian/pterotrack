# pterotrack

Use discrete event simulation to plan your vacation!

## Usage

Pterotrack requires three arguments.  All date arguments should be specified as
ISO 8601 dates (YYYY-MM-DD).

    $ pterotrack <gain> <length> <end>

* `gain` is the amount of time off, in hours, you gain every pay period.
* `length` is the length of your pay period, in days
* `end` is when you want the simulation to end

Optional arguments are:
* `--start-date` to specify when the simulation should start (default is the
  current day)
* `--start-pto` (or `-s`) to specify how much time off you hold at simulation start
  (default is 0)
* `--accum-date` to specify the next time you accumulate time off (defaults to
  the value provided to `--start-date`, or the current date otherwise)

You can also plan vacations using the `--vacation-file` or `-v` option.  To use
this argument, create a comma-separated values file with two fields: date of
vacation, and number of hours spent that day.  For example, if I wanted to take
two weeks off from my Monday-to-Friday 9-5 job during June 2014, I'd write

    2014-06-09,8.0
    2014-06-10,8.0
    2014-06-11,8.0
    2014-06-12,8.0
    2014-06-13,8.0
    2014-06-16,8.0
    2014-06-17,8.0
    2014-06-18,8.0
    2014-06-19,8.0
    2014-06-20,8.0

Save that into a file, and I could budget with

    $ pterotrack --start-date 2014-05-31 -s 40 -v vacation.csv 4.0 14 2014-07-01

Comments, issues, and pull requests are welcome.  Pterotrack is licensed under
the terms of the Apache Public License 2.0 (see `LICENSE`).
