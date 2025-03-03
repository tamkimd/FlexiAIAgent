from .base import BaseTool
import datetime
from typing import Optional


class TimeQueryTool(BaseTool):
    """This tool queries a past date based on the current time. You must use this tool for any questions related to time.
    - Input: Optional negative integer parameters:
        - `date`: negative integer or zero (number of days to go back).
        - `month`:negative integer or zero (number of months to go back).
        - `year`:negative integer or zero (number of years to go back).
        ex: {"date": -1, "month": -1, "year": -1}

    - Output: A string representing the past date and time. If no parameters are provided, the tool returns the current date.
    """

    def execute(
        self, date: Optional[int] = 0, month: Optional[int] = 0, year: Optional[int] = 0
    ) -> str:
        if date > 0 or month > 0 or year > 0:
            raise ValueError(
                "All parameters must be negative or zero to query past time."
            )

        now = datetime.datetime.now().date()

        if date == 0 and month == 0 and year == 0:
            return f"This is the current date: {now}"

        new_year = now.year + year
        new_month = now.month + month
        while new_month <= 0:
            new_year -= 1
            new_month += 12

        try:
            new_date = now.replace(year=new_year, month=new_month)
        except ValueError:
            new_date = now.replace(year=new_year, month=new_month, day=28)

        new_date = new_date + datetime.timedelta(days=date)

        input_description = f"past {abs(year)} year(s) " if year else ""
        input_description += f"{abs(month)} month(s) " if month else ""
        input_description += f"{abs(date)} day(s)" if date else ""
        input_description = input_description.strip()

        return f"This is the past date ({input_description} ago): {new_date}"
