class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }
        date_spt = date.split()
        day = date_spt[0][:-2]
        month = months[date_spt[1]]
        year = date_spt[2]
        formatted_date = f"{year}-{month}-{day.zfill(2)}"

        return formatted_date