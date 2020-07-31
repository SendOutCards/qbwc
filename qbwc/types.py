from enum import Enum
from datetime import datetime

from typing_extensions import TypedDict


class DateMacro(Enum):
	all: str = 'All'
	today: str = 'Today'
	this_week: str = 'ThisWeek'
	this_week_to_date: str = 'ThisWeekToDate'
	this_month: str = 'ThisMonth'
	this_month_to_date: str = 'ThisMonthToDate'
	this_calendar_quarter: str = 'ThisCalendarQuarter'
	this_calendar_quarter_to_date: str = 'ThisCalendarQuarterToDate'
	this_fiscal_quarter: str = 'ThisFiscalQuarter'
	this_fiscal_quarter_to_date: str = 'ThisFiscalQuarterToDate'
	this_calendar_year: str = 'ThisCalendarYear'
	this_calendar_year_to_date: str = 'ThisCalendarYearToDate'
	this_fiscal_year: str = 'ThisFiscalYear'
	this_fiscal_year_to_date: str = 'ThisFiscalYearToDate'
	yesterday: str = 'Yesterday'
	last_week: str = 'LastWeek'
	last_week_to_date: str = 'LastWeekToDate'
	last_month: str = 'LastMonth'
	last_month_to_date: str = 'LastMonthToDate'
	last_calendar_quarter: str = 'LastCalendarQuarter'
	last_calendar_quarter_to_date: str = 'LastCalendarQuarterToDate'
	last_fiscal_quarter: str = 'LastFiscalQuarter'
	last_fiscal_quarter_to_date: str = 'LastFiscalQuarterToDate'
	last_calendar_year: str = 'LastCalendarYear'
	last_calendar_year_to_date: str = 'LastCalendarYearToDate'
	last_fiscal_year: str = 'LastFiscalYear'
	last_fiscal_year_to_date: str = 'LastFiscalYearToDate'
	next_week: str = 'NextWeek'
	next_four_weeks: str = 'NextFourWeeks'
	next_month: str = 'NextMonth'
	next_calendar_quarter: str = 'NextCalendarQuarter'
	next_calendar_year: str = 'NextCalendarYear'
	next_fiscal_quarter: str = 'NextFiscalQuarter'
	next_fiscal_year: str = 'NextFiscalYear'


class ModifiedDateRangeFilter(TypedDict):
	from_modified_date: datetime
	to_modified_date: datetime


class TxnDateRangeFilter(TypedDict):
	from_txn_date: datetime
	to_txn_date: datetime
	date_macro: DateMacro