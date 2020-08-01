from enum import Enum
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Optional, List, Union
from typing_extensions import TypedDict

IDTYPE = str
STRTYPE = str
DATETIMETYPE = datetime
DATETYPE = datetime
TIMEINTERVALTYPE = timedelta
BOOLTYPE = bool
GUIDTYPE = str
AMTTYPE = Decimal
FLOATTYPE = Decimal
PRICETYPE = Decimal
INTTYPE = int
QUANTYPE = int
PERCENTTYPE = Decimal


class BillableStatus(Enum):
    Billable = "Billable"
    NotBillable = "NotBillable"
    HasBeenBilled = "HasBeenBilled"


class DataExtType(Enum):
    AMTTYPE = "AMTTYPE"
    DATETIMETYPE = "DATETIMETYPE"
    INTTYPE = "INTTYPE"
    PERCENTTYPE = "PERCENTTYPE"
    PRICETYPE = "PRICETYPE"
    QUANTYPE = "QUANTYPE"
    STR1024TYPE = "STR1024TYPE"
    STR255TYPE = "STR255TYPE"


class ActiveStatus(Enum):
    ActiveOnly = "ActiveOnly"
    InactiveOnly = "InactiveOnly"
    All = "All"


class MatchCriterion(Enum):
    StartsWith = "StartsWith"
    Contains = "Contains"
    EndsWith = "EndsWith"


class DeliveryPolicy(Enum):
    DeliverAlways = "DeliverAlways"
    DeliverOnlyIfRunning = "DeliverOnlyIfRunning"


class CompanyFileEventOperation(Enum):
    Close = "Close"
    Open = "Open"


class SpecialItemType(Enum):
    FinanceCharge = "FinanceCharge"
    ReimbursableExpenseGroup = "ReimbursableExpenseGroup"
    ReimbursableExpenseSubtotal = "ReimbursableExpenseSubtotal"


class SerialNumberAddedOrRemoved(Enum):
    Added = "Added"
    Removed = "Removed"


class ListDataExtType(Enum):
    Account = "Account"
    Customer = "Customer"
    Employee = "Employee"
    Item = "Item"
    OtherName = "OtherName"
    Vendor = "Vendor"


class TxnDataExtType(Enum):
    ARRefundCreditCard = "ARRefundCreditCard"
    Bill = "Bill"
    BillPaymentCheck = "BillPaymentCheck"
    BillPaymentCreditCard = "BillPaymentCreditCard"
    BuildAssembly = "BuildAssembly"
    Charge = "Charge"
    Check = "Check"
    CreditCardCharge = "CreditCardCharge"
    CreditCardCredit = "CreditCardCredit"
    CreditMemo = "CreditMemo"
    Deposit = "Deposit"
    Estimate = "Estimate"
    InventoryAdjustment = "InventoryAdjustment"
    Invoice = "Invoice"
    ItemReceipt = "ItemReceipt"
    JournalEntry = "JournalEntry"
    PurchaseOrder = "PurchaseOrder"
    ReceivePayment = "ReceivePayment"
    SalesOrder = "SalesOrder"
    SalesReceipt = "SalesReceipt"
    SalesTaxPaymentCheck = "SalesTaxPaymentCheck"
    VendorCredit = "VendorCredit"


class OtherDataExtType(Enum):
    Company = "Company"


class SalesTaxCountry(Enum):
    Australia = "Australia"
    Canada = "Canada"
    UK = "UK"
    US = "US"


class JobStatus(Enum):
    Awarded = "Awarded"
    Closed = "Closed"
    InProgress = "InProgress"
    _None = "_None"
    NotAwarded = "NotAwarded"
    Pending = "Pending"


class PreferredDeliveryMethod(Enum):
    _None = "_None"
    Email = "Email"
    Fax = "Fax"


class FirstMonthFiscalYear(Enum):
    January = "January"
    February = "February"
    March = "March"
    April = "April"
    May = "May"
    June = "June"
    July = "July"
    August = "August"
    September = "September"
    October = "October"
    November = "November"
    December = "December"


class FirstMonthIncomeTaxYear(Enum):
    January = "January"
    February = "February"
    March = "March"
    April = "April"
    May = "May"
    June = "June"
    July = "July"
    August = "August"
    September = "September"
    October = "October"
    November = "November"
    December = "December"


class TaxForm(Enum):
    Form1040 = "Form1040"
    Form1065 = "Form1065"
    Form1120 = "Form1120"
    Form1120S = "Form1120S"
    Form990 = "Form990"
    Form990PF = "Form990PF"
    Form990T = "Form990T"
    OtherOrNone = "OtherOrNone"


class ServiceStatus(Enum):
    Active = "Active"
    Expired = "Expired"
    Never = "Never"
    Pending = "Pending"
    Suspended = "Suspended"
    Terminated = "Terminated"
    Trial = "Trial"


class ClearedStatus(Enum):
    Cleared = "Cleared"
    NotCleared = "NotCleared"
    Pending = "Pending"


class AcquiredAs(Enum):
    New = "New"
    Old = "Old"


class DateMacro(Enum):
    All = "All"
    Today = "Today"
    ThisWeek = "ThisWeek"
    ThisWeekToDate = "ThisWeekToDate"
    ThisMonth = "ThisMonth"
    ThisMonthToDate = "ThisMonthToDate"
    ThisCalendarQuarter = "ThisCalendarQuarter"
    ThisCalendarQuarterToDate = "ThisCalendarQuarterToDate"
    ThisFiscalQuarter = "ThisFiscalQuarter"
    ThisFiscalQuarterToDate = "ThisFiscalQuarterToDate"
    ThisCalendarYear = "ThisCalendarYear"
    ThisCalendarYearToDate = "ThisCalendarYearToDate"
    ThisFiscalYear = "ThisFiscalYear"
    ThisFiscalYearToDate = "ThisFiscalYearToDate"
    Yesterday = "Yesterday"
    LastWeek = "LastWeek"
    LastWeekToDate = "LastWeekToDate"
    LastMonth = "LastMonth"
    LastMonthToDate = "LastMonthToDate"
    LastCalendarQuarter = "LastCalendarQuarter"
    LastCalendarQuarterToDate = "LastCalendarQuarterToDate"
    LastFiscalQuarter = "LastFiscalQuarter"
    LastFiscalQuarterToDate = "LastFiscalQuarterToDate"
    LastCalendarYear = "LastCalendarYear"
    LastCalendarYearToDate = "LastCalendarYearToDate"
    LastFiscalYear = "LastFiscalYear"
    LastFiscalYearToDate = "LastFiscalYearToDate"
    NextWeek = "NextWeek"
    NextFourWeeks = "NextFourWeeks"
    NextMonth = "NextMonth"
    NextCalendarQuarter = "NextCalendarQuarter"
    NextCalendarYear = "NextCalendarYear"
    NextFiscalQuarter = "NextFiscalQuarter"
    NextFiscalYear = "NextFiscalYear"


class TxnType(Enum):
    ARRefundCreditCard = "ARRefundCreditCard"
    Bill = "Bill"
    BillPaymentCheck = "BillPaymentCheck"
    BillPaymentCreditCard = "BillPaymentCreditCard"
    BuildAssembly = "BuildAssembly"
    Charge = "Charge"
    Check = "Check"
    CreditCardCharge = "CreditCardCharge"
    CreditCardCredit = "CreditCardCredit"
    CreditMemo = "CreditMemo"
    Deposit = "Deposit"
    Estimate = "Estimate"
    InventoryAdjustment = "InventoryAdjustment"
    Invoice = "Invoice"
    ItemReceipt = "ItemReceipt"
    JournalEntry = "JournalEntry"
    LiabilityAdjustment = "LiabilityAdjustment"
    Paycheck = "Paycheck"
    PayrollLiabilityCheck = "PayrollLiabilityCheck"
    PurchaseOrder = "PurchaseOrder"
    ReceivePayment = "ReceivePayment"
    SalesOrder = "SalesOrder"
    SalesReceipt = "SalesReceipt"
    SalesTaxPaymentCheck = "SalesTaxPaymentCheck"
    Transfer = "Transfer"
    VendorCredit = "VendorCredit"
    YTDAdjustment = "YTDAdjustment"


class LinkType(Enum):
    AMTTYPE = "AMTTYPE"
    QUANTYPE = "QUANTYPE"


class PendingStatus(Enum):
    All = "All"
    PendingOnly = "PendingOnly"
    NotPendingOnly = "NotPendingOnly"


class ItemTypeFilter(Enum):
    AllExceptFixedAsset = "AllExceptFixedAsset"
    Assembly = "Assembly"
    Discount = "Discount"
    FixedAsset = "FixedAsset"
    Inventory = "Inventory"
    InventoryAndAssembly = "InventoryAndAssembly"
    NonInventory = "NonInventory"
    OtherCharge = "OtherCharge"
    Payment = "Payment"
    Sales = "Sales"
    SalesTax = "SalesTax"
    Service = "Service"


class AddToMenu(Enum):
    File = "File"
    Company = "Company"
    Customers = "Customers"
    Vendors = "Vendors"
    Employees = "Employees"
    Banking = "Banking"


class VisibleIf(Enum):
    AccountantCopyExists = "AccountantCopyExists"
    AssemblyItemsEnabled = "AssemblyItemsEnabled"
    ClassesEnabled = "ClassesEnabled"
    EstimatesEnabled = "EstimatesEnabled"
    HasCustomers = "HasCustomers"
    HasVendors = "HasVendors"
    InventoryEnabled = "InventoryEnabled"
    IsAccountantCopy = "IsAccountantCopy"
    MultiUserMode = "MultiUserMode"
    PayrollEnabled = "PayrollEnabled"
    PriceLevelsEnabled = "PriceLevelsEnabled"
    SalesOrdersEnabled = "SalesOrdersEnabled"
    SalesTaxEnabled = "SalesTaxEnabled"
    TimeTrackingEnabled = "TimeTrackingEnabled"


class VisibleIfNot(Enum):
    AccountantCopyExists = "AccountantCopyExists"
    AssemblyItemsEnabled = "AssemblyItemsEnabled"
    ClassesEnabled = "ClassesEnabled"
    EstimatesEnabled = "EstimatesEnabled"
    HasCustomers = "HasCustomers"
    HasVendors = "HasVendors"
    InventoryEnabled = "InventoryEnabled"
    IsAccountantCopy = "IsAccountantCopy"
    MultiUserMode = "MultiUserMode"
    PayrollEnabled = "PayrollEnabled"
    PriceLevelsEnabled = "PriceLevelsEnabled"
    SalesOrdersEnabled = "SalesOrdersEnabled"
    SalesTaxEnabled = "SalesTaxEnabled"
    TimeTrackingEnabled = "TimeTrackingEnabled"


class EnabledIf(Enum):
    AccountantCopyExists = "AccountantCopyExists"
    AssemblyItemsEnabled = "AssemblyItemsEnabled"
    ClassesEnabled = "ClassesEnabled"
    EstimatesEnabled = "EstimatesEnabled"
    HasCustomers = "HasCustomers"
    HasVendors = "HasVendors"
    InventoryEnabled = "InventoryEnabled"
    IsAccountantCopy = "IsAccountantCopy"
    MultiUserMode = "MultiUserMode"
    PayrollEnabled = "PayrollEnabled"
    PriceLevelsEnabled = "PriceLevelsEnabled"
    SalesOrdersEnabled = "SalesOrdersEnabled"
    SalesTaxEnabled = "SalesTaxEnabled"
    TimeTrackingEnabled = "TimeTrackingEnabled"


class EnabledIfNot(Enum):
    AccountantCopyExists = "AccountantCopyExists"
    AssemblyItemsEnabled = "AssemblyItemsEnabled"
    ClassesEnabled = "ClassesEnabled"
    EstimatesEnabled = "EstimatesEnabled"
    HasCustomers = "HasCustomers"
    HasVendors = "HasVendors"
    InventoryEnabled = "InventoryEnabled"
    IsAccountantCopy = "IsAccountantCopy"
    MultiUserMode = "MultiUserMode"
    PayrollEnabled = "PayrollEnabled"
    PriceLevelsEnabled = "PriceLevelsEnabled"
    SalesOrdersEnabled = "SalesOrdersEnabled"
    SalesTaxEnabled = "SalesTaxEnabled"
    TimeTrackingEnabled = "TimeTrackingEnabled"


class TxnDelType(Enum):
    ARRefundCreditCard = "ARRefundCreditCard"
    Bill = "Bill"
    BillPaymentCheck = "BillPaymentCheck"
    BillPaymentCreditCard = "BillPaymentCreditCard"
    BuildAssembly = "BuildAssembly"
    Charge = "Charge"
    Check = "Check"
    CreditCardCharge = "CreditCardCharge"
    CreditCardCredit = "CreditCardCredit"
    CreditMemo = "CreditMemo"
    Deposit = "Deposit"
    Estimate = "Estimate"
    InventoryAdjustment = "InventoryAdjustment"
    Invoice = "Invoice"
    ItemReceipt = "ItemReceipt"
    JournalEntry = "JournalEntry"
    PayrollLiabilityAdjustment = "PayrollLiabilityAdjustment"
    PayrollPriorPayment = "PayrollPriorPayment"
    PayrollYearToDateAdjustment = "PayrollYearToDateAdjustment"
    PurchaseOrder = "PurchaseOrder"
    ReceivePayment = "ReceivePayment"
    SalesOrder = "SalesOrder"
    SalesReceipt = "SalesReceipt"
    SalesTaxPaymentCheck = "SalesTaxPaymentCheck"
    TimeTracking = "TimeTracking"
    TransferInventory = "TransferInventory"
    VehicleMileage = "VehicleMileage"
    VendorCredit = "VendorCredit"


class ListDelType(Enum):
    Account = "Account"
    BillingRate = "BillingRate"
    Class = "Class"
    Currency = "Currency"
    Customer = "Customer"
    CustomerMsg = "CustomerMsg"
    CustomerType = "CustomerType"
    DateDrivenTerms = "DateDrivenTerms"
    Employee = "Employee"
    InventorySite = "InventorySite"
    ItemDiscount = "ItemDiscount"
    ItemFixedAsset = "ItemFixedAsset"
    ItemGroup = "ItemGroup"
    ItemInventory = "ItemInventory"
    ItemInventoryAssembly = "ItemInventoryAssembly"
    ItemNonInventory = "ItemNonInventory"
    ItemOtherCharge = "ItemOtherCharge"
    ItemPayment = "ItemPayment"
    ItemSalesTax = "ItemSalesTax"
    ItemSalesTaxGroup = "ItemSalesTaxGroup"
    ItemService = "ItemService"
    ItemSubtotal = "ItemSubtotal"
    JobType = "JobType"
    OtherName = "OtherName"
    PaymentMethod = "PaymentMethod"
    PayrollItemNonWage = "PayrollItemNonWage"
    PayrollItemWage = "PayrollItemWage"
    PriceLevel = "PriceLevel"
    SalesRep = "SalesRep"
    SalesTaxCode = "SalesTaxCode"
    ShipMethod = "ShipMethod"
    StandardTerms = "StandardTerms"
    ToDo = "ToDo"
    UnitOfMeasureSet = "UnitOfMeasureSet"
    Vehicle = "Vehicle"
    Vendor = "Vendor"
    VendorType = "VendorType"
    WorkersCompCode = "WorkersCompCode"


class TxnDisplayModType(Enum):
    Bill = "Bill"
    BillPaymentCheck = "BillPaymentCheck"
    BillPaymentCreditCard = "BillPaymentCreditCard"
    BuildAssembly = "BuildAssembly"
    Charge = "Charge"
    Check = "Check"
    CreditCardCharge = "CreditCardCharge"
    CreditCardCredit = "CreditCardCredit"
    CreditMemo = "CreditMemo"
    Deposit = "Deposit"
    Estimate = "Estimate"
    InventoryAdjustment = "InventoryAdjustment"
    Invoice = "Invoice"
    ItemReceipt = "ItemReceipt"
    JournalEntry = "JournalEntry"
    PurchaseOrder = "PurchaseOrder"
    ReceivePayment = "ReceivePayment"
    SalesOrder = "SalesOrder"
    SalesReceipt = "SalesReceipt"
    SalesTaxPaymentCheck = "SalesTaxPaymentCheck"
    VendorCredit = "VendorCredit"


class MappingCategory(Enum):
    BOX1 = "BOX1"
    BOX2 = "BOX2"
    BOX3 = "BOX3"
    BOX4 = "BOX4"
    BOX5 = "BOX5"
    BOX6 = "BOX6"
    BOX7 = "BOX7"
    BOX8 = "BOX8"
    BOX9 = "BOX9"
    BOX10 = "BOX10"
    BOX13 = "BOX13"
    BOX14 = "BOX14"


class DoneStatus(Enum):
    NotDoneOnly = "NotDoneOnly"
    DoneOnly = "DoneOnly"
    All = "All"


class Type(Enum):
    Task = "Task"
    Call = "Call"
    Fax = "Fax"
    Email = "Email"
    Meeting = "Meeting"
    Appointment = "Appointment"


class Priority(Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"


class SubscriptionType(Enum):
    Data = "Data"
    UI = "UI"
    UIExtension = "UIExtension"


class EntityTypeFilter(Enum):
    Customer = "Customer"
    Employee = "Employee"
    OtherName = "OtherName"
    Vendor = "Vendor"


class AccountTypeFilter(Enum):
    AccountsPayable = "AccountsPayable"
    AccountsReceivable = "AccountsReceivable"
    AllowedFor1099 = "AllowedFor1099"
    APAndSalesTax = "APAndSalesTax"
    APOrCreditCard = "APOrCreditCard"
    ARAndAP = "ARAndAP"
    Asset = "Asset"
    BalanceSheet = "BalanceSheet"
    Bank = "Bank"
    BankAndARAndAPAndUF = "BankAndARAndAPAndUF"
    BankAndUF = "BankAndUF"
    CostOfSales = "CostOfSales"
    CreditCard = "CreditCard"
    CurrentAsset = "CurrentAsset"
    CurrentAssetAndExpense = "CurrentAssetAndExpense"
    CurrentLiability = "CurrentLiability"
    Equity = "Equity"
    EquityAndIncomeAndExpense = "EquityAndIncomeAndExpense"
    ExpenseAndOtherExpense = "ExpenseAndOtherExpense"
    FixedAsset = "FixedAsset"
    IncomeAndExpense = "IncomeAndExpense"
    IncomeAndOtherIncome = "IncomeAndOtherIncome"
    Liability = "Liability"
    LiabilityAndEquity = "LiabilityAndEquity"
    LongTermLiability = "LongTermLiability"
    NonPosting = "NonPosting"
    OrdinaryExpense = "OrdinaryExpense"
    OrdinaryIncome = "OrdinaryIncome"
    OrdinaryIncomeAndCOGS = "OrdinaryIncomeAndCOGS"
    OrdinaryIncomeAndExpense = "OrdinaryIncomeAndExpense"
    OtherAsset = "OtherAsset"
    OtherCurrentAsset = "OtherCurrentAsset"
    OtherCurrentLiability = "OtherCurrentLiability"
    OtherExpense = "OtherExpense"
    OtherIncome = "OtherIncome"
    OtherIncomeOrExpense = "OtherIncomeOrExpense"


class TxnTypeFilter(Enum):
    All = "All"
    ARRefundCreditCard = "ARRefundCreditCard"
    Bill = "Bill"
    BillPaymentCheck = "BillPaymentCheck"
    BillPaymentCreditCard = "BillPaymentCreditCard"
    BuildAssembly = "BuildAssembly"
    Charge = "Charge"
    Check = "Check"
    CreditCardCharge = "CreditCardCharge"
    CreditCardCredit = "CreditCardCredit"
    CreditMemo = "CreditMemo"
    Deposit = "Deposit"
    Estimate = "Estimate"
    InventoryAdjustment = "InventoryAdjustment"
    Invoice = "Invoice"
    ItemReceipt = "ItemReceipt"
    JournalEntry = "JournalEntry"
    LiabilityAdjustment = "LiabilityAdjustment"
    Paycheck = "Paycheck"
    PayrollLiabilityCheck = "PayrollLiabilityCheck"
    PurchaseOrder = "PurchaseOrder"
    ReceivePayment = "ReceivePayment"
    SalesOrder = "SalesOrder"
    SalesReceipt = "SalesReceipt"
    SalesTaxPaymentCheck = "SalesTaxPaymentCheck"
    Transfer = "Transfer"
    VendorCredit = "VendorCredit"
    YTDAdjustment = "YTDAdjustment"


class TransactionDetailLevelFilter(Enum):
    All = "All"
    SummaryOnly = "SummaryOnly"
    AllExceptSummary = "AllExceptSummary"


class TransactionPostingStatusFilter(Enum):
    Either = "Either"
    NonPosting = "NonPosting"
    Posting = "Posting"


class TransactionPaidStatusFilter(Enum):
    Either = "Either"
    Closed = "Closed"
    Open = "Open"


class OptionForPriceRuleConflict(Enum):
    Zero = "Zero"
    BasePrice = "BasePrice"


class QBFileMode(Enum):
    MultiUser = "MultiUser"
    SingleUser = "SingleUser"


class LineType(Enum):
    ECPurchases = "ECPurchases"
    ECSales = "ECSales"
    Purchases = "Purchases"
    Sales = "Sales"
    SubTotal = "SubTotal"
    TaxOnPurchases = "TaxOnPurchases"
    TaxOnSales = "TaxOnSales"
    Total = "Total"


class ListMergeType(Enum):
    Account = "Account"
    Class = "Class"
    Customer = "Customer"
    ItemDiscount = "ItemDiscount"
    ItemGroup = "ItemGroup"
    ItemInventory = "ItemInventory"
    ItemNonInventory = "ItemNonInventory"
    ItemOtherCharge = "ItemOtherCharge"
    ItemPayment = "ItemPayment"
    ItemSalesTax = "ItemSalesTax"
    ItemSalesTaxGroup = "ItemSalesTaxGroup"
    ItemService = "ItemService"
    ItemSubtotal = "ItemSubtotal"
    Vendor = "Vendor"


class AdjustRelativeTo(Enum):
    StandardPrice = "StandardPrice"
    Cost = "Cost"
    CurrentCustomPrice = "CurrentCustomPrice"


class PriceLevelType(Enum):
    FixedPercentage = "FixedPercentage"
    PerItem = "PerItem"


class CustomDetailReportType(Enum):
    CustomTxnDetail = "CustomTxnDetail"


class ReportDateMacro(Enum):
    All = "All"
    Today = "Today"
    ThisWeek = "ThisWeek"
    ThisWeekToDate = "ThisWeekToDate"
    ThisMonth = "ThisMonth"
    ThisMonthToDate = "ThisMonthToDate"
    ThisQuarter = "ThisQuarter"
    ThisQuarterToDate = "ThisQuarterToDate"
    ThisYear = "ThisYear"
    ThisYearToDate = "ThisYearToDate"
    Yesterday = "Yesterday"
    LastWeek = "LastWeek"
    LastWeekToDate = "LastWeekToDate"
    LastMonth = "LastMonth"
    LastMonthToDate = "LastMonthToDate"
    LastQuarter = "LastQuarter"
    LastQuarterToDate = "LastQuarterToDate"
    LastYear = "LastYear"
    LastYearToDate = "LastYearToDate"
    NextWeek = "NextWeek"
    NextFourWeeks = "NextFourWeeks"
    NextMonth = "NextMonth"
    NextQuarter = "NextQuarter"
    NextYear = "NextYear"


class ReportModifiedDateRangeMacro(Enum):
    All = "All"
    Today = "Today"
    ThisWeek = "ThisWeek"
    ThisWeekToDate = "ThisWeekToDate"
    ThisMonth = "ThisMonth"
    ThisMonthToDate = "ThisMonthToDate"
    ThisQuarter = "ThisQuarter"
    ThisQuarterToDate = "ThisQuarterToDate"
    ThisYear = "ThisYear"
    ThisYearToDate = "ThisYearToDate"
    Yesterday = "Yesterday"
    LastWeek = "LastWeek"
    LastWeekToDate = "LastWeekToDate"
    LastMonth = "LastMonth"
    LastMonthToDate = "LastMonthToDate"
    LastQuarter = "LastQuarter"
    LastQuarterToDate = "LastQuarterToDate"
    LastYear = "LastYear"
    LastYearToDate = "LastYearToDate"
    NextWeek = "NextWeek"
    NextFourWeeks = "NextFourWeeks"
    NextMonth = "NextMonth"
    NextQuarter = "NextQuarter"
    NextYear = "NextYear"


class ReportDetailLevelFilter(Enum):
    All = "All"
    AllExceptSummary = "AllExceptSummary"
    SummaryOnly = "SummaryOnly"


class ReportPostingStatusFilter(Enum):
    Either = "Either"
    NonPosting = "NonPosting"
    Posting = "Posting"


class SummarizeRowsBy(Enum):
    Account = "Account"
    BalanceSheet = "BalanceSheet"
    Class = "Class"
    Customer = "Customer"
    CustomerType = "CustomerType"
    Day = "Day"
    Employee = "Employee"
    FourWeek = "FourWeek"
    HalfMonth = "HalfMonth"
    IncomeStatement = "IncomeStatement"
    ItemDetail = "ItemDetail"
    ItemType = "ItemType"
    Month = "Month"
    Payee = "Payee"
    PaymentMethod = "PaymentMethod"
    PayrollItemDetail = "PayrollItemDetail"
    PayrollYtdDetail = "PayrollYtdDetail"
    Quarter = "Quarter"
    SalesRep = "SalesRep"
    SalesTaxCode = "SalesTaxCode"
    ShipMethod = "ShipMethod"
    TaxLine = "TaxLine"
    Terms = "Terms"
    TotalOnly = "TotalOnly"
    TwoWeek = "TwoWeek"
    Vendor = "Vendor"
    VendorType = "VendorType"
    Week = "Week"
    Year = "Year"


class IncludeColumn(Enum):
    Account = "Account"
    Aging = "Aging"
    Amount = "Amount"
    AmountDifference = "AmountDifference"
    AverageCost = "AverageCost"
    BilledDate = "BilledDate"
    BillingStatus = "BillingStatus"
    CalculatedAmount = "CalculatedAmount"
    Class = "Class"
    ClearedStatus = "ClearedStatus"
    CostPrice = "CostPrice"
    Credit = "Credit"
    Currency = "Currency"
    Date = "Date"
    Debit = "Debit"
    DeliveryDate = "DeliveryDate"
    DueDate = "DueDate"
    EstimateActive = "EstimateActive"
    ExchangeRate = "ExchangeRate"
    FOB = "FOB"
    IncomeSubjectToTax = "IncomeSubjectToTax"
    Invoiced = "Invoiced"
    Item = "Item"
    ItemDesc = "ItemDesc"
    LastModifiedBy = "LastModifiedBy"
    LatestOrPriorState = "LatestOrPriorState"
    Memo = "Memo"
    ModifiedTime = "ModifiedTime"
    Name = "Name"
    NameAccountNumber = "NameAccountNumber"
    NameAddress = "NameAddress"
    NameCity = "NameCity"
    NameContact = "NameContact"
    NameEmail = "NameEmail"
    NameFax = "NameFax"
    NamePhone = "NamePhone"
    NameState = "NameState"
    NameZip = "NameZip"
    OpenBalance = "OpenBalance"
    OriginalAmount = "OriginalAmount"
    PaidAmount = "PaidAmount"
    PaidStatus = "PaidStatus"
    PaidThroughDate = "PaidThroughDate"
    PaymentMethod = "PaymentMethod"
    PayrollItem = "PayrollItem"
    PONumber = "PONumber"
    PrintStatus = "PrintStatus"
    ProgressAmount = "ProgressAmount"
    ProgressPercent = "ProgressPercent"
    Quantity = "Quantity"
    QuantityAvailable = "QuantityAvailable"
    QuantityOnHand = "QuantityOnHand"
    QuantityOnSalesOrder = "QuantityOnSalesOrder"
    ReceivedQuantity = "ReceivedQuantity"
    RefNumber = "RefNumber"
    RunningBalance = "RunningBalance"
    SalesRep = "SalesRep"
    SalesTaxCode = "SalesTaxCode"
    SerialOrLotNumber = "SerialOrLotNumber"
    ShipDate = "ShipDate"
    ShipMethod = "ShipMethod"
    SourceName = "SourceName"
    SplitAccount = "SplitAccount"
    SSNOrTaxID = "SSNOrTaxID"
    TaxLine = "TaxLine"
    TaxTableVersion = "TaxTableVersion"
    Terms = "Terms"
    TxnID = "TxnID"
    TxnNumber = "TxnNumber"
    TxnType = "TxnType"
    UnitPrice = "UnitPrice"
    UserEdit = "UserEdit"
    ValueOnHand = "ValueOnHand"
    WageBase = "WageBase"
    WageBaseTips = "WageBaseTips"


class IncludeAccounts(Enum):
    All = "All"
    InUse = "InUse"


class ReportOpenBalanceAsOf(Enum):
    ReportEndDate = "ReportEndDate"
    Today = "Today"


class ReportBasis(Enum):
    Accrual = "Accrual"
    Cash = "Cash"
    _None = "_None"


class ColType(Enum):
    Account = "Account"
    Addr1 = "Addr1"
    Addr2 = "Addr2"
    Addr3 = "Addr3"
    Addr4 = "Addr4"
    Addr5 = "Addr5"
    Aging = "Aging"
    Amount = "Amount"
    AmountDifference = "AmountDifference"
    AverageCost = "AverageCost"
    BilledDate = "BilledDate"
    BillingStatus = "BillingStatus"
    Blank = "Blank"
    CalculatedAmount = "CalculatedAmount"
    Class = "Class"
    ClearedStatus = "ClearedStatus"
    CostPrice = "CostPrice"
    CreateDate = "CreateDate"
    Credit = "Credit"
    CustomField = "CustomField"
    Date = "Date"
    Debit = "Debit"
    DeliveryDate = "DeliveryDate"
    DueDate = "DueDate"
    Duration = "Duration"
    EarliestReceiptDate = "EarliestReceiptDate"
    EstimateActive = "EstimateActive"
    FOB = "FOB"
    IncomeSubjectToTax = "IncomeSubjectToTax"
    Invoiced = "Invoiced"
    IsAdjustment = "IsAdjustment"
    Item = "Item"
    ItemDesc = "ItemDesc"
    ItemVendor = "ItemVendor"
    Label = "Label"
    LastModifiedBy = "LastModifiedBy"
    LatestOrPriorState = "LatestOrPriorState"
    Memo = "Memo"
    ModifiedTime = "ModifiedTime"
    Name = "Name"
    NameAccountNumber = "NameAccountNumber"
    NameAddress = "NameAddress"
    NameCity = "NameCity"
    NameContact = "NameContact"
    NameEmail = "NameEmail"
    NameFax = "NameFax"
    NamePhone = "NamePhone"
    NameState = "NameState"
    NameZip = "NameZip"
    OpenBalance = "OpenBalance"
    OriginalAmount = "OriginalAmount"
    PaidAmount = "PaidAmount"
    PaidStatus = "PaidStatus"
    PaidThroughDate = "PaidThroughDate"
    PaymentMethod = "PaymentMethod"
    PayrollItem = "PayrollItem"
    Percent = "Percent"
    PercentChange = "PercentChange"
    PercentOfTotalRetail = "PercentOfTotalRetail"
    PercentOfTotalValue = "PercentOfTotalValue"
    PhysicalCount = "PhysicalCount"
    PONumber = "PONumber"
    PrintStatus = "PrintStatus"
    ProgressAmount = "ProgressAmount"
    ProgressPercent = "ProgressPercent"
    Quantity = "Quantity"
    QuantityAvailable = "QuantityAvailable"
    QuantityOnHand = "QuantityOnHand"
    QuantityOnOrder = "QuantityOnOrder"
    QuantityOnPendingBuild = "QuantityOnPendingBuild"
    QuantityOnSalesOrder = "QuantityOnSalesOrder"
    ReceivedQuantity = "ReceivedQuantity"
    RefNumber = "RefNumber"
    ReorderPoint = "ReorderPoint"
    RetailValueOnHand = "RetailValueOnHand"
    RunningBalance = "RunningBalance"
    SalesPerWeek = "SalesPerWeek"
    SalesRep = "SalesRep"
    SalesTaxCode = "SalesTaxCode"
    ShipDate = "ShipDate"
    ShipMethod = "ShipMethod"
    ShipToAddr1 = "ShipToAddr1"
    ShipToAddr2 = "ShipToAddr2"
    ShipToAddr3 = "ShipToAddr3"
    ShipToAddr4 = "ShipToAddr4"
    ShipToAddr5 = "ShipToAddr5"
    SONumber = "SONumber"
    SourceName = "SourceName"
    SplitAccount = "SplitAccount"
    SSNOrTaxID = "SSNOrTaxID"
    SuggestedReorder = "SuggestedReorder"
    TaxLine = "TaxLine"
    TaxTableVersion = "TaxTableVersion"
    Terms = "Terms"
    Total = "Total"
    TxnID = "TxnID"
    TxnNumber = "TxnNumber"
    TxnType = "TxnType"
    UnitPrice = "UnitPrice"
    UserEdit = "UserEdit"
    ValueOnHand = "ValueOnHand"
    WageBase = "WageBase"
    WageBaseTips = "WageBaseTips"


class UnitOfMeasureType(Enum):
    Area = "Area"
    Count = "Count"
    Length = "Length"
    Other = "Other"
    Time = "Time"
    Volume = "Volume"
    Weight = "Weight"


class UnitUsedFor(Enum):
    Purchase = "Purchase"
    Sales = "Sales"
    Shipping = "Shipping"


class TransactionMode(Enum):
    CardNotPresent = "CardNotPresent"
    CardPresent = "CardPresent"


class CreditCardTxnType(Enum):
    Authorization = "Authorization"
    Capture = "Capture"
    Charge = "Charge"
    Refund = "Refund"
    VoiceAuthorization = "VoiceAuthorization"


class AVSStreet(Enum):
    Pass = "Pass"
    Fail = "Fail"
    NotAvailable = "NotAvailable"


class AVSZip(Enum):
    Pass = "Pass"
    Fail = "Fail"
    NotAvailable = "NotAvailable"


class CardSecurityCodeMatch(Enum):
    Pass = "Pass"
    Fail = "Fail"
    NotAvailable = "NotAvailable"


class PaymentStatus(Enum):
    Unknown = "Unknown"
    Completed = "Completed"


class Status(Enum):
    Hot = "Hot"
    Warm = "Warm"
    Cold = "Cold"


class ThousandSeparator(Enum):
    Comma = "Comma"
    Period = "Period"
    Space = "Space"
    Apostrophe = "Apostrophe"


class ThousandSeparatorGrouping(Enum):
    XX_XXX_XXX = "XX_XXX_XXX"
    X_XX_XX_XXX = "X_XX_XX_XXX"


class DecimalPlaces(Enum):
    _0 = "_0"
    _2 = "_2"


class DecimalSeparator(Enum):
    Period = "Period"
    Comma = "Comma"


class ReportingPeriod(Enum):
    Monthly = "Monthly"
    Quarterly = "Quarterly"


class AssignToObject(Enum):
    Account = "Account"
    ARRefundCreditCard = "ARRefundCreditCard"
    Bill = "Bill"
    BillPaymentCheck = "BillPaymentCheck"
    BillPaymentCreditCard = "BillPaymentCreditCard"
    BuildAssembly = "BuildAssembly"
    Charge = "Charge"
    Check = "Check"
    Company = "Company"
    CreditCardCharge = "CreditCardCharge"
    CreditCardCredit = "CreditCardCredit"
    CreditMemo = "CreditMemo"
    Customer = "Customer"
    Deposit = "Deposit"
    Employee = "Employee"
    Estimate = "Estimate"
    InventoryAdjustment = "InventoryAdjustment"
    Invoice = "Invoice"
    Item = "Item"
    ItemReceipt = "ItemReceipt"
    JournalEntry = "JournalEntry"
    OtherName = "OtherName"
    PurchaseOrder = "PurchaseOrder"
    ReceivePayment = "ReceivePayment"
    SalesOrder = "SalesOrder"
    SalesReceipt = "SalesReceipt"
    SalesTaxPaymentCheck = "SalesTaxPaymentCheck"
    Vendor = "Vendor"
    VendorCredit = "VendorCredit"


class AssignClassesTo(Enum):
    _None = "_None"
    Accounts = "Accounts"
    Items = "Items"
    Names = "Names"


class CalculateChargesFrom(Enum):
    DueDate = "DueDate"
    InvoiceOrBilledDate = "InvoiceOrBilledDate"


class AgingReportBasis(Enum):
    AgeFromDueDate = "AgeFromDueDate"
    AgeFromTransactionDate = "AgeFromTransactionDate"


class SummaryReportBasis(Enum):
    Accrual = "Accrual"
    Cash = "Cash"


class PaySalesTax(Enum):
    Monthly = "Monthly"
    Quarterly = "Quarterly"
    Annually = "Annually"


class FirstDayOfWeek(Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    Sunday = "Sunday"


class IsTrackingSerialOrLotNumber(Enum):
    _None = "_None"
    SerialNumber = "SerialNumber"
    LotNumber = "LotNumber"


class GeneralSummaryReportType(Enum):
    BalanceSheetByClass = "BalanceSheetByClass"
    BalanceSheetPrevYearComp = "BalanceSheetPrevYearComp"
    BalanceSheetStandard = "BalanceSheetStandard"
    BalanceSheetSummary = "BalanceSheetSummary"
    CustomerBalanceSummary = "CustomerBalanceSummary"
    ExpenseByVendorSummary = "ExpenseByVendorSummary"
    IncomeByCustomerSummary = "IncomeByCustomerSummary"
    InventoryStockStatusByItem = "InventoryStockStatusByItem"
    InventoryStockStatusByVendor = "InventoryStockStatusByVendor"
    IncomeTaxSummary = "IncomeTaxSummary"
    InventoryValuationSummary = "InventoryValuationSummary"
    InventoryValuationSummaryBySite = "InventoryValuationSummaryBySite"
    LotNumberInStockBySite = "LotNumberInStockBySite"
    PhysicalInventoryWorksheet = "PhysicalInventoryWorksheet"
    ProfitAndLossByClass = "ProfitAndLossByClass"
    ProfitAndLossByJob = "ProfitAndLossByJob"
    ProfitAndLossPrevYearComp = "ProfitAndLossPrevYearComp"
    ProfitAndLossStandard = "ProfitAndLossStandard"
    ProfitAndLossYTDComp = "ProfitAndLossYTDComp"
    PurchaseByItemSummary = "PurchaseByItemSummary"
    PurchaseByVendorSummary = "PurchaseByVendorSummary"
    SalesByCustomerSummary = "SalesByCustomerSummary"
    SalesByItemSummary = "SalesByItemSummary"
    SalesByRepSummary = "SalesByRepSummary"
    SalesTaxLiability = "SalesTaxLiability"
    SalesTaxRevenueSummary = "SalesTaxRevenueSummary"
    SerialNumberInStockBySite = "SerialNumberInStockBySite"
    TrialBalance = "TrialBalance"
    VendorBalanceSummary = "VendorBalanceSummary"


class SummarizeColumnsBy(Enum):
    Account = "Account"
    BalanceSheet = "BalanceSheet"
    Class = "Class"
    Customer = "Customer"
    CustomerType = "CustomerType"
    Day = "Day"
    Employee = "Employee"
    FourWeek = "FourWeek"
    HalfMonth = "HalfMonth"
    IncomeStatement = "IncomeStatement"
    ItemDetail = "ItemDetail"
    ItemType = "ItemType"
    Month = "Month"
    Payee = "Payee"
    PaymentMethod = "PaymentMethod"
    PayrollItemDetail = "PayrollItemDetail"
    PayrollYtdDetail = "PayrollYtdDetail"
    Quarter = "Quarter"
    SalesRep = "SalesRep"
    SalesTaxCode = "SalesTaxCode"
    ShipMethod = "ShipMethod"
    Terms = "Terms"
    TotalOnly = "TotalOnly"
    TwoWeek = "TwoWeek"
    Vendor = "Vendor"
    VendorType = "VendorType"
    Week = "Week"
    Year = "Year"


class ReportCalendar(Enum):
    CalendarYear = "CalendarYear"
    FiscalYear = "FiscalYear"
    TaxYear = "TaxYear"


class ReturnRows(Enum):
    ActiveOnly = "ActiveOnly"
    NonZero = "NonZero"
    All = "All"


class ReturnColumns(Enum):
    ActiveOnly = "ActiveOnly"
    NonZero = "NonZero"
    All = "All"


class PaymentMethodType(Enum):
    AmericanExpress = "AmericanExpress"
    Cash = "Cash"
    Check = "Check"
    DebitCard = "DebitCard"
    Discover = "Discover"
    ECheck = "ECheck"
    GiftCard = "GiftCard"
    MasterCard = "MasterCard"
    Other = "Other"
    OtherCreditCard = "OtherCreditCard"
    Visa = "Visa"


class ListDisplayAddType(Enum):
    Account = "Account"
    Customer = "Customer"
    Employee = "Employee"
    Item = "Item"
    OtherName = "OtherName"
    Vendor = "Vendor"


class AccountType(Enum):
    AccountsPayable = "AccountsPayable"
    AccountsReceivable = "AccountsReceivable"
    Bank = "Bank"
    CostOfGoodsSold = "CostOfGoodsSold"
    CreditCard = "CreditCard"
    Equity = "Equity"
    Expense = "Expense"
    FixedAsset = "FixedAsset"
    Income = "Income"
    LongTermLiability = "LongTermLiability"
    NonPosting = "NonPosting"
    OtherAsset = "OtherAsset"
    OtherCurrentAsset = "OtherCurrentAsset"
    OtherCurrentLiability = "OtherCurrentLiability"
    OtherExpense = "OtherExpense"
    OtherIncome = "OtherIncome"


class SpecialAccountType(Enum):
    AccountsPayable = "AccountsPayable"
    AccountsReceivable = "AccountsReceivable"
    CondenseItemAdjustmentExpenses = "CondenseItemAdjustmentExpenses"
    CostOfGoodsSold = "CostOfGoodsSold"
    DirectDepositLiabilities = "DirectDepositLiabilities"
    Estimates = "Estimates"
    ExchangeGainLoss = "ExchangeGainLoss"
    InventoryAssets = "InventoryAssets"
    ItemReceiptAccount = "ItemReceiptAccount"
    OpeningBalanceEquity = "OpeningBalanceEquity"
    PayrollExpenses = "PayrollExpenses"
    PayrollLiabilities = "PayrollLiabilities"
    PettyCash = "PettyCash"
    PurchaseOrders = "PurchaseOrders"
    ReconciliationDifferences = "ReconciliationDifferences"
    RetainedEarnings = "RetainedEarnings"
    SalesOrders = "SalesOrders"
    SalesTaxPayable = "SalesTaxPayable"
    UncategorizedExpenses = "UncategorizedExpenses"
    UncategorizedIncome = "UncategorizedIncome"
    UndepositedFunds = "UndepositedFunds"


class CashFlowClassification(Enum):
    _None = "_None"
    Operating = "Operating"
    Investing = "Investing"
    Financing = "Financing"
    NotApplicable = "NotApplicable"


class TrackLostEvents(Enum):
    All = "All"
    _None = "_None"


class ListEventType(Enum):
    Account = "Account"
    Class = "Class"
    Customer = "Customer"
    CustomerMsg = "CustomerMsg"
    CustomerType = "CustomerType"
    DateDrivenTerms = "DateDrivenTerms"
    Employee = "Employee"
    ItemDiscount = "ItemDiscount"
    ItemFixedAsset = "ItemFixedAsset"
    ItemGroup = "ItemGroup"
    ItemInventory = "ItemInventory"
    ItemInventoryAssembly = "ItemInventoryAssembly"
    ItemNonInventory = "ItemNonInventory"
    ItemOtherCharge = "ItemOtherCharge"
    ItemPayment = "ItemPayment"
    ItemSalesTax = "ItemSalesTax"
    ItemSalesTaxGroup = "ItemSalesTaxGroup"
    ItemService = "ItemService"
    ItemSubtotal = "ItemSubtotal"
    JobType = "JobType"
    OtherName = "OtherName"
    PaymentMethod = "PaymentMethod"
    PriceLevel = "PriceLevel"
    SalesRep = "SalesRep"
    SalesTaxCode = "SalesTaxCode"
    ShipMethod = "ShipMethod"
    StandardTerms = "StandardTerms"
    ToDo = "ToDo"
    Vendor = "Vendor"
    VendorType = "VendorType"


class ListEventOperation(Enum):
    Add = "Add"
    Modify = "Modify"
    Delete = "Delete"
    Merge = "Merge"


class TxnEventType(Enum):
    ARRefundCreditCard = "ARRefundCreditCard"
    Bill = "Bill"
    BillPaymentCheck = "BillPaymentCheck"
    BillPaymentCreditCard = "BillPaymentCreditCard"
    Charge = "Charge"
    Check = "Check"
    CreditCardCharge = "CreditCardCharge"
    CreditCardCredit = "CreditCardCredit"
    CreditMemo = "CreditMemo"
    Deposit = "Deposit"
    Estimate = "Estimate"
    InventoryAdjustment = "InventoryAdjustment"
    Invoice = "Invoice"
    ItemReceipt = "ItemReceipt"
    JournalEntry = "JournalEntry"
    PurchaseOrder = "PurchaseOrder"
    ReceivePayment = "ReceivePayment"
    SalesOrder = "SalesOrder"
    SalesReceipt = "SalesReceipt"
    SalesTaxPaymentCheck = "SalesTaxPaymentCheck"
    TimeTracking = "TimeTracking"
    VendorCredit = "VendorCredit"


class TxnEventOperation(Enum):
    Add = "Add"
    Modify = "Modify"
    Delete = "Delete"


class Relation(Enum):
    Spouse = "Spouse"
    Partner = "Partner"
    Mother = "Mother"
    Father = "Father"
    Sister = "Sister"
    Brother = "Brother"
    Son = "Son"
    Daughter = "Daughter"
    Friend = "Friend"
    Other = "Other"


class EmployeeType(Enum):
    Officer = "Officer"
    Owner = "Owner"
    Regular = "Regular"
    Statutory = "Statutory"


class PartOrFullTime(Enum):
    PartTime = "PartTime"
    FullTime = "FullTime"


class Exempt(Enum):
    Exempt = "Exempt"
    NonExempt = "NonExempt"


class KeyEmployee(Enum):
    Yes = "Yes"
    No = "No"


class Gender(Enum):
    Male = "Male"
    Female = "Female"


class USCitizen(Enum):
    Yes = "Yes"
    No = "No"


class Ethnicity(Enum):
    AmericianIndian = "AmericianIndian"
    Asian = "Asian"
    Black = "Black"
    Hawaiian = "Hawaiian"
    Hispanic = "Hispanic"
    White = "White"
    TwoOrMoreRaces = "TwoOrMoreRaces"


class Disabled(Enum):
    Yes = "Yes"
    No = "No"


class OnFile(Enum):
    Yes = "Yes"
    No = "No"


class USVeteran(Enum):
    Yes = "Yes"
    No = "No"


class MilitaryStatus(Enum):
    Active = "Active"
    Reserve = "Reserve"


class PayPeriod(Enum):
    Daily = "Daily"
    Weekly = "Weekly"
    Biweekly = "Biweekly"
    Semimonthly = "Semimonthly"
    Monthly = "Monthly"
    Quarterly = "Quarterly"
    Yearly = "Yearly"


class UseTimeDataToCreatePaychecks(Enum):
    NotSet = "NotSet"
    UseTimeData = "UseTimeData"
    DoNotUseTimeData = "DoNotUseTimeData"


class AccrualPeriod(Enum):
    BeginningOfYear = "BeginningOfYear"
    EveryHourOnPaycheck = "EveryHourOnPaycheck"
    EveryPaycheck = "EveryPaycheck"


class ListType(Enum):
    Account = "Account"
    Class = "Class"
    Customer = "Customer"
    CustomerMsg = "CustomerMsg"
    CustomerType = "CustomerType"
    DateDrivenTerms = "DateDrivenTerms"
    Employee = "Employee"
    ItemDiscount = "ItemDiscount"
    ItemFixedAsset = "ItemFixedAsset"
    ItemGroup = "ItemGroup"
    ItemInventory = "ItemInventory"
    ItemInventoryAssembly = "ItemInventoryAssembly"
    ItemNonInventory = "ItemNonInventory"
    ItemOtherCharge = "ItemOtherCharge"
    ItemPayment = "ItemPayment"
    ItemSalesTax = "ItemSalesTax"
    ItemSalesTaxGroup = "ItemSalesTaxGroup"
    ItemService = "ItemService"
    ItemSubtotal = "ItemSubtotal"
    JobType = "JobType"
    OtherName = "OtherName"
    PaymentMethod = "PaymentMethod"
    PriceLevel = "PriceLevel"
    SalesRep = "SalesRep"
    SalesTaxCode = "SalesTaxCode"
    ShipMethod = "ShipMethod"
    StandardTerms = "StandardTerms"
    ToDo = "ToDo"
    Vendor = "Vendor"
    VendorType = "VendorType"


class TemplateType(Enum):
    BuildAssembly = "BuildAssembly"
    CreditMemo = "CreditMemo"
    Estimate = "Estimate"
    Invoice = "Invoice"
    PurchaseOrder = "PurchaseOrder"
    SalesOrder = "SalesOrder"
    SalesReceipt = "SalesReceipt"


class WageType(Enum):
    Bonus = "Bonus"
    Commission = "Commission"
    HourlyOvertime = "HourlyOvertime"
    HourlyRegular = "HourlyRegular"
    HourlySick = "HourlySick"
    HourlyVacation = "HourlyVacation"
    SalaryRegular = "SalaryRegular"
    SalarySick = "SalarySick"
    SalaryVacation = "SalaryVacation"


class PayrollDetailReportType(Enum):
    EmployeeStateTaxesDetail = "EmployeeStateTaxesDetail"
    PayrollItemDetail = "PayrollItemDetail"
    PayrollReviewDetail = "PayrollReviewDetail"
    PayrollTransactionDetail = "PayrollTransactionDetail"
    PayrollTransactionsByPayee = "PayrollTransactionsByPayee"


class PaidStatus(Enum):
    All = "All"
    PaidOnly = "PaidOnly"
    NotPaidOnly = "NotPaidOnly"


class BillingRateType(Enum):
    FixedRate = "FixedRate"
    PerItem = "PerItem"


class BudgetSummaryReportType(Enum):
    BalanceSheetBudgetOverview = "BalanceSheetBudgetOverview"
    BalanceSheetBudgetVsActual = "BalanceSheetBudgetVsActual"
    ProfitAndLossBudgetOverview = "ProfitAndLossBudgetOverview"
    ProfitAndLossBudgetPerformance = "ProfitAndLossBudgetPerformance"
    ProfitAndLossBudgetVsActual = "ProfitAndLossBudgetVsActual"


class BudgetCriterion(Enum):
    Accounts = "Accounts"
    AccountsAndClasses = "AccountsAndClasses"
    AccountsAndCustomers = "AccountsAndCustomers"


class SummarizeBudgetColumnsBy(Enum):
    Class = "Class"
    Customer = "Customer"
    Date = "Date"


class SummarizeBudgetRowsBy(Enum):
    Account = "Account"
    Class = "Class"
    Customer = "Customer"


class JournalLineType(Enum):
    Debit = "Debit"
    Credit = "Credit"


class PayrollSummaryReportType(Enum):
    EmployeeEarningsSummary = "EmployeeEarningsSummary"
    PayrollLiabilityBalances = "PayrollLiabilityBalances"
    PayrollSummary = "PayrollSummary"


class AdjustBillingRateRelativeTo(Enum):
    StandardRate = "StandardRate"
    CurrentCustomRate = "CurrentCustomRate"


class Operator(Enum):
    LessThan = "LessThan"
    LessThanEqual = "LessThanEqual"
    Equal = "Equal"
    GreaterThan = "GreaterThan"
    GreaterThanEqual = "GreaterThanEqual"


class TxnDisplayAddType(Enum):
    Bill = "Bill"
    BillPayment = "BillPayment"
    BuildAssembly = "BuildAssembly"
    Charge = "Charge"
    Check = "Check"
    CreditCardCharge = "CreditCardCharge"
    CreditCardCredit = "CreditCardCredit"
    CreditMemo = "CreditMemo"
    Deposit = "Deposit"
    Estimate = "Estimate"
    InventoryAdjustment = "InventoryAdjustment"
    Invoice = "Invoice"
    ItemReceipt = "ItemReceipt"
    JournalEntry = "JournalEntry"
    PurchaseOrder = "PurchaseOrder"
    ReceivePayment = "ReceivePayment"
    SalesOrder = "SalesOrder"
    SalesReceipt = "SalesReceipt"
    SalesTaxPaymentCheck = "SalesTaxPaymentCheck"
    VendorCredit = "VendorCredit"


class CustomSummaryReportType(Enum):
    CustomSummary = "CustomSummary"


class TimeReportType(Enum):
    TimeByItem = "TimeByItem"
    TimeByJobDetail = "TimeByJobDetail"
    TimeByJobSummary = "TimeByJobSummary"
    TimeByName = "TimeByName"


class NonWageType(Enum):
    Addition = "Addition"
    CompanyContribution = "CompanyContribution"
    Deduction = "Deduction"
    DirectDeposit = "DirectDeposit"
    Tax = "Tax"


class RemoveFromObject(Enum):
    Account = "Account"
    ARRefundCreditCard = "ARRefundCreditCard"
    Bill = "Bill"
    BillPaymentCheck = "BillPaymentCheck"
    BillPaymentCreditCard = "BillPaymentCreditCard"
    BuildAssembly = "BuildAssembly"
    Charge = "Charge"
    Check = "Check"
    Company = "Company"
    CreditCardCharge = "CreditCardCharge"
    CreditCardCredit = "CreditCardCredit"
    CreditMemo = "CreditMemo"
    Customer = "Customer"
    Deposit = "Deposit"
    Employee = "Employee"
    Estimate = "Estimate"
    InventoryAdjustment = "InventoryAdjustment"
    Invoice = "Invoice"
    Item = "Item"
    ItemReceipt = "ItemReceipt"
    JournalEntry = "JournalEntry"
    OtherName = "OtherName"
    PurchaseOrder = "PurchaseOrder"
    ReceivePayment = "ReceivePayment"
    SalesOrder = "SalesOrder"
    SalesReceipt = "SalesReceipt"
    SalesTaxPaymentCheck = "SalesTaxPaymentCheck"
    Vendor = "Vendor"
    VendorCredit = "VendorCredit"


class GeneralDetailReportType(Enum):
    _1099Detail = "_1099Detail"
    AuditTrail = "AuditTrail"
    BalanceSheetDetail = "BalanceSheetDetail"
    CheckDetail = "CheckDetail"
    CustomerBalanceDetail = "CustomerBalanceDetail"
    DepositDetail = "DepositDetail"
    EstimatesByJob = "EstimatesByJob"
    ExpenseByVendorDetail = "ExpenseByVendorDetail"
    GeneralLedger = "GeneralLedger"
    IncomeByCustomerDetail = "IncomeByCustomerDetail"
    IncomeTaxDetail = "IncomeTaxDetail"
    InventoryValuationDetail = "InventoryValuationDetail"
    JobProgressInvoicesVsEstimates = "JobProgressInvoicesVsEstimates"
    Journal = "Journal"
    MissingChecks = "MissingChecks"
    OpenInvoices = "OpenInvoices"
    OpenPOs = "OpenPOs"
    OpenPOsByJob = "OpenPOsByJob"
    OpenSalesOrderByCustomer = "OpenSalesOrderByCustomer"
    OpenSalesOrderByItem = "OpenSalesOrderByItem"
    PendingSales = "PendingSales"
    ProfitAndLossDetail = "ProfitAndLossDetail"
    PurchaseByItemDetail = "PurchaseByItemDetail"
    PurchaseByVendorDetail = "PurchaseByVendorDetail"
    SalesByCustomerDetail = "SalesByCustomerDetail"
    SalesByItemDetail = "SalesByItemDetail"
    SalesByRepDetail = "SalesByRepDetail"
    TxnDetailByAccount = "TxnDetailByAccount"
    TxnListByCustomer = "TxnListByCustomer"
    TxnListByDate = "TxnListByDate"
    TxnListByVendor = "TxnListByVendor"
    UnpaidBillsDetail = "UnpaidBillsDetail"
    UnbilledCostsByJob = "UnbilledCostsByJob"
    VendorBalanceDetail = "VendorBalanceDetail"


class AgingReportType(Enum):
    APAgingDetail = "APAgingDetail"
    APAgingSummary = "APAgingSummary"
    ARAgingDetail = "ARAgingDetail"
    ARAgingSummary = "ARAgingSummary"
    CollectionsReport = "CollectionsReport"


class ReportAgingAsOf(Enum):
    ReportEndDate = "ReportEndDate"
    Today = "Today"


class TxnVoidType(Enum):
    ARRefundCreditCard = "ARRefundCreditCard"
    Bill = "Bill"
    BillPaymentCheck = "BillPaymentCheck"
    BillPaymentCreditCard = "BillPaymentCreditCard"
    Charge = "Charge"
    Check = "Check"
    CreditCardCharge = "CreditCardCharge"
    CreditCardCredit = "CreditCardCredit"
    CreditMemo = "CreditMemo"
    Deposit = "Deposit"
    InventoryAdjustment = "InventoryAdjustment"
    Invoice = "Invoice"
    ItemReceipt = "ItemReceipt"
    JournalEntry = "JournalEntry"
    SalesReceipt = "SalesReceipt"
    VendorCredit = "VendorCredit"


class ListDisplayModType(Enum):
    Account = "Account"
    Customer = "Customer"
    Employee = "Employee"
    Item = "Item"
    OtherName = "OtherName"
    Vendor = "Vendor"


class JobReportType(Enum):
    ItemEstimatesVsActuals = "ItemEstimatesVsActuals"
    ItemProfitability = "ItemProfitability"
    JobEstimatesVsActualsDetail = "JobEstimatesVsActualsDetail"
    JobEstimatesVsActualsSummary = "JobEstimatesVsActualsSummary"
    JobProfitabilityDetail = "JobProfitabilityDetail"
    JobProfitabilitySummary = "JobProfitabilitySummary"


class CustomerMsgAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE


class CustomerMsgAddRq(TypedDict, total=False):
    CustomerMsgAdd: CustomerMsgAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CustomerMsgRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE


class ErrorRecovery(TypedDict, total=False):
    ListID: IDTYPE
    OwnerID: GUIDTYPE
    TxnID: IDTYPE
    TxnNumber: INTTYPE
    EditSequence: STRTYPE
    ExternalGUID: GUIDTYPE


class CustomerMsgAddRs(TypedDict, total=False):
    CustomerMsgRet: CustomerMsgRet
    ErrorRecovery: ErrorRecovery


class BarCode(TypedDict, total=False):
    BarCodeValue: STRTYPE
    AssignEvenIfUsed: BOOLTYPE
    AllowOverride: BOOLTYPE


class ItemSubtotalAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ItemDesc: STRTYPE
    ExternalGUID: GUIDTYPE


class ItemSubtotalAddRq(TypedDict, total=False):
    ItemSubtotalAdd: ItemSubtotalAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class DataExtRet(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtName: STRTYPE
    DataExtType: DataExtType
    DataExtValue: STRTYPE


class ItemSubtotalRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ItemDesc: STRTYPE
    SpecialItemType: SpecialItemType
    ExternalGUID: GUIDTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemSubtotalAddRs(TypedDict, total=False):
    ItemSubtotalRet: ItemSubtotalRet
    ErrorRecovery: ErrorRecovery


class BankAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class Address(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE
    City: STRTYPE
    State: STRTYPE
    PostalCode: STRTYPE
    Country: STRTYPE
    Note: STRTYPE


class SalesTaxPaymentCheckMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    TxnDate: DATETYPE
    BankAccountRef: BankAccountRef
    IsToBePrinted: BOOLTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    Address: Address


class SalesTaxPaymentCheckModRq(TypedDict, total=False):
    SalesTaxPaymentCheckMod: SalesTaxPaymentCheckMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class PayeeEntityRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class AddressBlock(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE


class ItemSalesTaxRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SalesTaxPaymentCheckLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemSalesTaxRef: ItemSalesTaxRef
    Amount: AMTTYPE


class SalesTaxPaymentCheckRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    PayeeEntityRef: PayeeEntityRef
    TxnDate: DATETYPE
    BankAccountRef: BankAccountRef
    Amount: AMTTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    Address: Address
    AddressBlock: AddressBlock
    IsToBePrinted: BOOLTYPE
    ExternalGUID: GUIDTYPE
    SalesTaxPaymentCheckLineRet: Union[SalesTaxPaymentCheckLineRet, List[SalesTaxPaymentCheckLineRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class SalesTaxPaymentCheckModRs(TypedDict, total=False):
    SalesTaxPaymentCheckRet: SalesTaxPaymentCheckRet
    ErrorRecovery: ErrorRecovery


class EntityRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class CustomerRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ItemServiceRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ClassRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class PayrollItemWageRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class TimeTrackingMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    TxnDate: DATETYPE
    EntityRef: EntityRef
    CustomerRef: CustomerRef
    ItemServiceRef: ItemServiceRef
    Duration: TIMEINTERVALTYPE
    ClassRef: ClassRef
    PayrollItemWageRef: PayrollItemWageRef
    Notes: STRTYPE
    BillableStatus: BillableStatus


class TimeTrackingModRq(TypedDict, total=False):
    TimeTrackingMod: TimeTrackingMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TimeTrackingRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    TxnDate: DATETYPE
    EntityRef: EntityRef
    CustomerRef: CustomerRef
    ItemServiceRef: ItemServiceRef
    Duration: TIMEINTERVALTYPE
    ClassRef: ClassRef
    PayrollItemWageRef: PayrollItemWageRef
    Notes: STRTYPE
    BillableStatus: BillableStatus
    ExternalGUID: GUIDTYPE
    IsBillable: BOOLTYPE
    IsBilled: BOOLTYPE


class TimeTrackingModRs(TypedDict, total=False):
    TimeTrackingRet: TimeTrackingRet
    ErrorRecovery: ErrorRecovery


class ItemRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class InventorySiteRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class InventorySiteLocationRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class OverrideUOMSetRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ARAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class OverrideItemAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ChargeMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    CustomerRef: CustomerRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    ItemRef: ItemRef
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    OptionForPriceRuleConflict: OptionForPriceRuleConflict
    Amount: AMTTYPE
    Desc: STRTYPE
    ARAccountRef: ARAccountRef
    ClassRef: ClassRef
    BilledDate: DATETYPE
    DueDate: DATETYPE
    OverrideItemAccountRef: OverrideItemAccountRef


class ChargeModRq(TypedDict, total=False):
    ChargeMod: ChargeMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class LinkedTxn(TypedDict, total=False):
    TxnID: IDTYPE
    TxnType: TxnType
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    LinkType: LinkType
    Amount: AMTTYPE


class ChargeRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    CustomerRef: CustomerRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    ItemRef: ItemRef
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    Amount: AMTTYPE
    BalanceRemaining: AMTTYPE
    Desc: STRTYPE
    ARAccountRef: ARAccountRef
    ClassRef: ClassRef
    BilledDate: DATETYPE
    DueDate: DATETYPE
    IsPaid: BOOLTYPE
    ExternalGUID: GUIDTYPE
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ChargeModRs(TypedDict, total=False):
    ChargeRet: ChargeRet
    ErrorRecovery: ErrorRecovery


class AdditionalContactRef(TypedDict, total=False):
    ContactName: STRTYPE
    ContactValue: STRTYPE


class VendorRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ShipToEntityRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class TemplateRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class VendorAddress(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE
    City: STRTYPE
    State: STRTYPE
    PostalCode: STRTYPE
    Country: STRTYPE
    Note: STRTYPE


class ShipAddress(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE
    City: STRTYPE
    State: STRTYPE
    PostalCode: STRTYPE
    Country: STRTYPE
    Note: STRTYPE


class TermsRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ShipMethodRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SalesTaxCodeRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class PurchaseOrderLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    ManufacturerPartNumber: STRTYPE
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    InventorySiteLocationRef: InventorySiteLocationRef
    CustomerRef: CustomerRef
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    IsManuallyClosed: BOOLTYPE
    OverrideItemAccountRef: OverrideItemAccountRef
    Other1: STRTYPE
    Other2: STRTYPE


class ItemGroupRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class PurchaseOrderLineGroupMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    PurchaseOrderLineMod: Union[PurchaseOrderLineMod, List[PurchaseOrderLineMod]]


class PurchaseOrderMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    VendorRef: VendorRef
    ClassRef: ClassRef
    InventorySiteRef: InventorySiteRef
    ShipToEntityRef: ShipToEntityRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    VendorAddress: VendorAddress
    ShipAddress: ShipAddress
    TermsRef: TermsRef
    DueDate: DATETYPE
    ExpectedDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    FOB: STRTYPE
    IsManuallyClosed: BOOLTYPE
    Memo: STRTYPE
    VendorMsg: STRTYPE
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    Other1: STRTYPE
    Other2: STRTYPE
    ExchangeRate: FLOATTYPE
    PurchaseOrderLineMod: PurchaseOrderLineMod
    PurchaseOrderLineGroupMod: PurchaseOrderLineGroupMod


class PurchaseOrderModRq(TypedDict, total=False):
    PurchaseOrderMod: PurchaseOrderMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class VendorAddressBlock(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE


class ShipAddressBlock(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE


class CurrencyRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class PurchaseOrderLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    ManufacturerPartNumber: STRTYPE
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    InventorySiteLocationRef: InventorySiteLocationRef
    CustomerRef: CustomerRef
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ReceivedQuantity: QUANTYPE
    UnbilledQuantity: QUANTYPE
    IsBilled: BOOLTYPE
    IsManuallyClosed: BOOLTYPE
    Other1: STRTYPE
    Other2: STRTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class PurchaseOrderLineGroupRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    IsPrintItemsInGroup: BOOLTYPE
    TotalAmount: AMTTYPE
    PurchaseOrderLineRet: Union[PurchaseOrderLineRet, List[PurchaseOrderLineRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class PurchaseOrderRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    VendorRef: VendorRef
    ClassRef: ClassRef
    InventorySiteRef: InventorySiteRef
    ShipToEntityRef: ShipToEntityRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    VendorAddress: VendorAddress
    VendorAddressBlock: VendorAddressBlock
    ShipAddress: ShipAddress
    ShipAddressBlock: ShipAddressBlock
    TermsRef: TermsRef
    DueDate: DATETYPE
    ExpectedDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    FOB: STRTYPE
    TotalAmount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    TotalAmountInHomeCurrency: AMTTYPE
    IsManuallyClosed: BOOLTYPE
    IsFullyReceived: BOOLTYPE
    Memo: STRTYPE
    VendorMsg: STRTYPE
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    Other1: STRTYPE
    Other2: STRTYPE
    ExternalGUID: GUIDTYPE
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]
    PurchaseOrderLineRet: PurchaseOrderLineRet
    PurchaseOrderLineGroupRet: PurchaseOrderLineGroupRet
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class PurchaseOrderModRs(TypedDict, total=False):
    PurchaseOrderRet: PurchaseOrderRet
    ErrorRecovery: ErrorRecovery


class ModifiedDateRangeFilter(TypedDict, total=False):
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE


class TxnDateRangeFilter(TypedDict, total=False):
    FromTxnDate: DATETYPE
    ToTxnDate: DATETYPE
    DateMacro: DateMacro


class EntityFilter(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class AccountFilter(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class RefNumberFilter(TypedDict, total=False):
    MatchCriterion: MatchCriterion
    RefNumber: STRTYPE


class RefNumberRangeFilter(TypedDict, total=False):
    FromRefNumber: STRTYPE
    ToRefNumber: STRTYPE


class CurrencyFilter(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]


class ItemReceiptQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeLinkedTxns: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class APAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class LiabilityAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class AccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SalesRepRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ExpenseLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    AccountRef: AccountRef
    Amount: AMTTYPE
    Memo: STRTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    SalesTaxCodeRef: SalesTaxCodeRef
    BillableStatus: BillableStatus
    SalesRepRef: SalesRepRef
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Cost: PRICETYPE
    Amount: AMTTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    SalesTaxCodeRef: SalesTaxCodeRef
    BillableStatus: BillableStatus
    SalesRepRef: SalesRepRef
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class DataExt(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtName: STRTYPE
    DataExtValue: STRTYPE


class ItemGroupLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    TotalAmount: AMTTYPE
    ItemLineRet: Union[ItemLineRet, List[ItemLineRet]]
    DataExt: Union[DataExt, List[DataExt]]


class ItemReceiptRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    VendorRef: VendorRef
    APAccountRef: APAccountRef
    LiabilityAccountRef: LiabilityAccountRef
    TxnDate: DATETYPE
    TotalAmount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    TotalAmountInHomeCurrency: AMTTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExternalGUID: GUIDTYPE
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]
    ExpenseLineRet: Union[ExpenseLineRet, List[ExpenseLineRet]]
    ItemLineRet: ItemLineRet
    ItemGroupLineRet: ItemGroupLineRet
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemReceiptQueryRs(TypedDict, total=False):
    ItemReceiptRet: Union[ItemReceiptRet, List[ItemReceiptRet]]


class TransferFromAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class TransferToAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class TransferAdd(TypedDict, total=False):
    TxnDate: DATETYPE
    TransferFromAccountRef: TransferFromAccountRef
    TransferToAccountRef: TransferToAccountRef
    ClassRef: ClassRef
    Amount: AMTTYPE
    Memo: STRTYPE


class TransferAddRq(TypedDict, total=False):
    TransferAdd: TransferAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TransferRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    TxnDate: DATETYPE
    TransferFromAccountRef: TransferFromAccountRef
    FromAccountBalance: AMTTYPE
    TransferToAccountRef: TransferToAccountRef
    ToAccountBalance: AMTTYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    Memo: STRTYPE


class TransferAddRs(TypedDict, total=False):
    TransferRet: TransferRet


class TimeTrackingEntityFilter(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]


class TimeTrackingQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    TimeTrackingEntityFilter: TimeTrackingEntityFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TimeTrackingQueryRs(TypedDict, total=False):
    TimeTrackingRet: Union[TimeTrackingRet, List[TimeTrackingRet]]


class ParentRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class UnitOfMeasureSetRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class IncomeAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class PurchaseTaxCodeRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class COGSAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class PrefVendorRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class AssetAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ItemInventoryMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    ManufacturerPartNumber: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    ForceUOMChange: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesDesc: STRTYPE
    SalesPrice: PRICETYPE
    IncomeAccountRef: IncomeAccountRef
    ApplyIncomeAccountRefToExistingTxns: BOOLTYPE
    PurchaseDesc: STRTYPE
    PurchaseCost: PRICETYPE
    PurchaseTaxCodeRef: PurchaseTaxCodeRef
    COGSAccountRef: COGSAccountRef
    ApplyCOGSAccountRefToExistingTxns: BOOLTYPE
    PrefVendorRef: PrefVendorRef
    AssetAccountRef: AssetAccountRef
    ReorderPoint: QUANTYPE
    Max: QUANTYPE


class ItemInventoryModRq(TypedDict, total=False):
    ItemInventoryMod: ItemInventoryMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemInventoryRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    Sublevel: INTTYPE
    ManufacturerPartNumber: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesDesc: STRTYPE
    SalesPrice: PRICETYPE
    IncomeAccountRef: IncomeAccountRef
    PurchaseDesc: STRTYPE
    PurchaseCost: PRICETYPE
    PurchaseTaxCodeRef: PurchaseTaxCodeRef
    COGSAccountRef: COGSAccountRef
    PrefVendorRef: PrefVendorRef
    AssetAccountRef: AssetAccountRef
    ReorderPoint: QUANTYPE
    Max: QUANTYPE
    QuantityOnHand: QUANTYPE
    AverageCost: PRICETYPE
    QuantityOnOrder: QUANTYPE
    QuantityOnSalesOrder: QUANTYPE
    ExternalGUID: GUIDTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemInventoryModRs(TypedDict, total=False):
    ItemInventoryRet: ItemInventoryRet
    ErrorRecovery: ErrorRecovery


class BuildAssemblyMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    QuantityToBuild: QUANTYPE
    MarkPendingIfRequired: BOOLTYPE
    RemovePending: BOOLTYPE


class BuildAssemblyModRq(TypedDict, total=False):
    BuildAssemblyMod: BuildAssemblyMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemInventoryAssemblyRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ComponentItemLineRet(TypedDict, total=False):
    ItemRef: ItemRef
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    Desc: STRTYPE
    QuantityOnHand: QUANTYPE
    QuantityNeeded: QUANTYPE


class BuildAssemblyRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    ItemInventoryAssemblyRef: ItemInventoryAssemblyRef
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsPending: BOOLTYPE
    QuantityToBuild: QUANTYPE
    QuantityCanBuild: QUANTYPE
    QuantityOnHand: QUANTYPE
    QuantityOnSalesOrder: QUANTYPE
    ExternalGUID: GUIDTYPE
    ComponentItemLineRet: Union[ComponentItemLineRet, List[ComponentItemLineRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class BuildAssemblyModRs(TypedDict, total=False):
    BuildAssemblyRet: BuildAssemblyRet
    ErrorRecovery: ErrorRecovery


class ReportPeriod(TypedDict, total=False):
    FromReportDate: DATETYPE
    ToReportDate: DATETYPE


class ReportAccountFilter(TypedDict, total=False):
    AccountTypeFilter: AccountTypeFilter
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class ReportEntityFilter(TypedDict, total=False):
    EntityTypeFilter: EntityTypeFilter
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class ReportItemFilter(TypedDict, total=False):
    ItemTypeFilter: ItemTypeFilter
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class ReportClassFilter(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class ReportTxnTypeFilter(TypedDict, total=False):
    TxnTypeFilter: Union[TxnTypeFilter, List[TxnTypeFilter]]


class ReportModifiedDateRangeFilter(TypedDict, total=False):
    FromReportModifiedDate: DATETYPE
    ToReportModifiedDate: DATETYPE


class GeneralDetailReportQueryRq(TypedDict, total=False):
    GeneralDetailReportType: GeneralDetailReportType
    DisplayReport: BOOLTYPE
    ReportPeriod: ReportPeriod
    ReportDateMacro: ReportDateMacro
    ReportAccountFilter: ReportAccountFilter
    ReportEntityFilter: ReportEntityFilter
    ReportItemFilter: ReportItemFilter
    ReportClassFilter: ReportClassFilter
    ReportTxnTypeFilter: ReportTxnTypeFilter
    ReportModifiedDateRangeFilter: ReportModifiedDateRangeFilter
    ReportModifiedDateRangeMacro: ReportModifiedDateRangeMacro
    ReportDetailLevelFilter: ReportDetailLevelFilter
    ReportPostingStatusFilter: ReportPostingStatusFilter
    SummarizeRowsBy: SummarizeRowsBy
    IncludeColumn: Union[IncludeColumn, List[IncludeColumn]]
    IncludeAccounts: IncludeAccounts
    ReportOpenBalanceAsOf: ReportOpenBalanceAsOf
    ReportBasis: ReportBasis


class DeletedDateRangeFilter(TypedDict, total=False):
    FromDeletedDate: DATETIMETYPE
    ToDeletedDate: DATETIMETYPE


class ListDeletedQueryRq(TypedDict, total=False):
    ListDelType: Union[ListDelType, List[ListDelType]]
    DeletedDateRangeFilter: DeletedDateRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ListDeletedRet(TypedDict, total=False):
    ListDelType: ListDelType
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeDeleted: DATETIMETYPE
    FullName: STRTYPE


class ListDeletedQueryRs(TypedDict, total=False):
    ListDeletedRet: Union[ListDeletedRet, List[ListDeletedRet]]


class EmployeeRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class LeadRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ToDoAdd(TypedDict, total=False):
    Notes: STRTYPE
    IsActive: BOOLTYPE
    Type: Type
    Priority: Priority
    CustomerRef: CustomerRef
    EmployeeRef: EmployeeRef
    LeadRef: LeadRef
    VendorRef: VendorRef
    IsDone: BOOLTYPE
    ReminderDate: DATETYPE
    ReminderTime: TIMEINTERVALTYPE


class ToDoAddRq(TypedDict, total=False):
    ToDoAdd: ToDoAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ToDoRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Notes: STRTYPE
    IsActive: BOOLTYPE
    Type: Type
    Priority: Priority
    CustomerRef: CustomerRef
    EmployeeRef: EmployeeRef
    LeadRef: LeadRef
    VendorRef: VendorRef
    IsDone: BOOLTYPE
    ReminderDate: DATETYPE
    ReminderTime: TIMEINTERVALTYPE


class ToDoAddRs(TypedDict, total=False):
    ToDoRet: ToDoRet
    ErrorRecovery: ErrorRecovery


class ReceivePaymentQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class PaymentMethodRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class DepositToAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class CreditCardTxnInputInfo(TypedDict, total=False):
    CreditCardNumber: STRTYPE
    ExpirationMonth: INTTYPE
    ExpirationYear: INTTYPE
    NameOnCard: STRTYPE
    CreditCardAddress: STRTYPE
    CreditCardPostalCode: STRTYPE
    CommercialCardCode: STRTYPE
    TransactionMode: TransactionMode
    CreditCardTxnType: CreditCardTxnType


class CreditCardTxnResultInfo(TypedDict, total=False):
    ResultCode: INTTYPE
    ResultMessage: STRTYPE
    CreditCardTransID: STRTYPE
    MerchantAccountNumber: STRTYPE
    AuthorizationCode: STRTYPE
    AVSStreet: AVSStreet
    AVSZip: AVSZip
    CardSecurityCodeMatch: CardSecurityCodeMatch
    ReconBatchID: STRTYPE
    PaymentGroupingCode: INTTYPE
    PaymentStatus: PaymentStatus
    TxnAuthorizationTime: DATETIMETYPE
    TxnAuthorizationStamp: INTTYPE
    ClientTransID: STRTYPE


class CreditCardTxnInfo(TypedDict, total=False):
    CreditCardTxnInputInfo: CreditCardTxnInputInfo
    CreditCardTxnResultInfo: CreditCardTxnResultInfo


class DiscountAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class DiscountClassRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class AppliedToTxnRet(TypedDict, total=False):
    TxnID: IDTYPE
    TxnType: TxnType
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BalanceRemaining: AMTTYPE
    Amount: AMTTYPE
    DiscountAmount: AMTTYPE
    DiscountAccountRef: DiscountAccountRef
    DiscountClassRef: DiscountClassRef
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]


class ReceivePaymentRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    CustomerRef: CustomerRef
    ARAccountRef: ARAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    TotalAmount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    TotalAmountInHomeCurrency: AMTTYPE
    PaymentMethodRef: PaymentMethodRef
    Memo: STRTYPE
    DepositToAccountRef: DepositToAccountRef
    CreditCardTxnInfo: CreditCardTxnInfo
    UnusedPayment: AMTTYPE
    UnusedCredits: AMTTYPE
    ExternalGUID: GUIDTYPE
    AppliedToTxnRet: Union[AppliedToTxnRet, List[AppliedToTxnRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ReceivePaymentQueryRs(TypedDict, total=False):
    ReceivePaymentRet: Union[ReceivePaymentRet, List[ReceivePaymentRet]]


class PreferencesQueryRq(TypedDict, total=False):
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class AccountingPreferences(TypedDict, total=False):
    IsUsingAccountNumbers: BOOLTYPE
    IsRequiringAccounts: BOOLTYPE
    IsUsingClassTracking: BOOLTYPE
    AssignClassesTo: AssignClassesTo
    IsUsingAuditTrail: BOOLTYPE
    IsAssigningJournalEntryNumbers: BOOLTYPE
    ClosingDate: DATETYPE


class FinanceChargeAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class FinanceChargePreferences(TypedDict, total=False):
    AnnualInterestRate: PERCENTTYPE
    MinFinanceCharge: AMTTYPE
    GracePeriod: INTTYPE
    FinanceChargeAccountRef: FinanceChargeAccountRef
    IsAssessingForOverdueCharges: BOOLTYPE
    CalculateChargesFrom: CalculateChargesFrom
    IsMarkedToBePrinted: BOOLTYPE


class JobsAndEstimatesPreferences(TypedDict, total=False):
    IsUsingEstimates: BOOLTYPE
    IsUsingProgressInvoicing: BOOLTYPE
    IsPrintingItemsWithZeroAmounts: BOOLTYPE


class HomeCurrencyRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class MultiCurrencyPreferences(TypedDict, total=False):
    IsMultiCurrencyOn: BOOLTYPE
    HomeCurrencyRef: HomeCurrencyRef


class MultiLocationInventoryPreferences(TypedDict, total=False):
    IsMultiLocationInventoryAvailable: BOOLTYPE
    IsMultiLocationInventoryEnabled: BOOLTYPE


class DefaultDiscountAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class PurchasesAndVendorsPreferences(TypedDict, total=False):
    IsUsingInventory: BOOLTYPE
    DaysBillsAreDue: INTTYPE
    IsAutomaticallyUsingDiscounts: BOOLTYPE
    DefaultDiscountAccountRef: DefaultDiscountAccountRef


class ReportsPreferences(TypedDict, total=False):
    AgingReportBasis: AgingReportBasis
    SummaryReportBasis: SummaryReportBasis


class DefaultShipMethodRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class PriceLevels(TypedDict, total=False):
    IsUsingPriceLevels: BOOLTYPE
    IsRoundingSalesPriceUp: BOOLTYPE


class SalesAndCustomersPreferences(TypedDict, total=False):
    DefaultShipMethodRef: DefaultShipMethodRef
    DefaultFOB: STRTYPE
    DefaultMarkup: PERCENTTYPE
    IsTrackingReimbursedExpensesAsIncome: BOOLTYPE
    IsAutoApplyingPayments: BOOLTYPE
    PriceLevels: PriceLevels


class DefaultItemSalesTaxRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class DefaultTaxableSalesTaxCodeRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class DefaultNonTaxableSalesTaxCodeRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SalesTaxPreferences(TypedDict, total=False):
    DefaultItemSalesTaxRef: DefaultItemSalesTaxRef
    PaySalesTax: PaySalesTax
    DefaultTaxableSalesTaxCodeRef: DefaultTaxableSalesTaxCodeRef
    DefaultNonTaxableSalesTaxCodeRef: DefaultNonTaxableSalesTaxCodeRef
    IsUsingVendorTaxCode: BOOLTYPE
    IsUsingCustomerTaxCode: BOOLTYPE
    IsUsingAmountsIncludeTax: BOOLTYPE


class TimeTrackingPreferences(TypedDict, total=False):
    FirstDayOfWeek: FirstDayOfWeek


class CurrentAppAccessRights(TypedDict, total=False):
    IsAutomaticLoginAllowed: BOOLTYPE
    AutomaticLoginUserName: STRTYPE
    IsPersonalDataAccessAllowed: BOOLTYPE


class ItemsAndInventoryPreferences(TypedDict, total=False):
    EnhancedInventoryReceivingEnabled: BOOLTYPE
    IsTrackingSerialOrLotNumber: IsTrackingSerialOrLotNumber
    isTrackingOnSalesTransactionsEnabled: BOOLTYPE
    isTrackingOnPurchaseTransactionsEnabled: BOOLTYPE
    isTrackingOnInventoryAdjustmentEnabled: BOOLTYPE
    isTrackingOnBuildAssemblyEnabled: BOOLTYPE
    FIFOEnabled: BOOLTYPE
    FIFOEffectiveDate: DATETYPE
    IsRSBEnabled: BOOLTYPE
    IsBarcodeEnabled: BOOLTYPE


class PreferencesRet(TypedDict, total=False):
    AccountingPreferences: AccountingPreferences
    FinanceChargePreferences: FinanceChargePreferences
    JobsAndEstimatesPreferences: JobsAndEstimatesPreferences
    MultiCurrencyPreferences: MultiCurrencyPreferences
    MultiLocationInventoryPreferences: MultiLocationInventoryPreferences
    PurchasesAndVendorsPreferences: PurchasesAndVendorsPreferences
    ReportsPreferences: ReportsPreferences
    SalesAndCustomersPreferences: SalesAndCustomersPreferences
    SalesTaxPreferences: SalesTaxPreferences
    TimeTrackingPreferences: TimeTrackingPreferences
    CurrentAppAccessRights: CurrentAppAccessRights
    ItemsAndInventoryPreferences: ItemsAndInventoryPreferences


class PreferencesQueryRs(TypedDict, total=False):
    PreferencesRet: PreferencesRet


class ClassAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef


class ClassAddRq(TypedDict, total=False):
    ClassAdd: ClassAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ClassRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef
    Sublevel: INTTYPE


class ClassAddRs(TypedDict, total=False):
    ClassRet: ClassRet
    ErrorRecovery: ErrorRecovery


class DataExtDefAdd(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtName: STRTYPE
    DataExtType: DataExtType
    AssignToObject: Union[AssignToObject, List[AssignToObject]]
    DataExtListRequire: BOOLTYPE
    DataExtTxnRequire: BOOLTYPE
    DataExtFormatString: STRTYPE


class DataExtDefAddRq(TypedDict, total=False):
    DataExtDefAdd: DataExtDefAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class DataExtDefRet(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtID: INTTYPE
    DataExtName: STRTYPE
    DataExtType: DataExtType
    AssignToObject: Union[AssignToObject, List[AssignToObject]]
    DataExtListRequire: BOOLTYPE
    DataExtTxnRequire: BOOLTYPE
    DataExtFormatString: STRTYPE


class DataExtDefAddRs(TypedDict, total=False):
    DataExtDefRet: DataExtDefRet
    ErrorRecovery: ErrorRecovery


class OtherNameAddress(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE
    City: STRTYPE
    State: STRTYPE
    PostalCode: STRTYPE
    Country: STRTYPE
    Note: STRTYPE


class OtherNameAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    CompanyName: STRTYPE
    Salutation: STRTYPE
    FirstName: STRTYPE
    MiddleName: STRTYPE
    LastName: STRTYPE
    OtherNameAddress: OtherNameAddress
    Phone: STRTYPE
    AltPhone: STRTYPE
    Fax: STRTYPE
    Email: STRTYPE
    Contact: STRTYPE
    AltContact: STRTYPE
    AccountNumber: STRTYPE
    Notes: STRTYPE
    ExternalGUID: GUIDTYPE


class OtherNameAddRq(TypedDict, total=False):
    OtherNameAdd: OtherNameAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class OtherNameAddressBlock(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE


class OtherNameRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    CompanyName: STRTYPE
    Salutation: STRTYPE
    FirstName: STRTYPE
    MiddleName: STRTYPE
    LastName: STRTYPE
    OtherNameAddress: OtherNameAddress
    OtherNameAddressBlock: OtherNameAddressBlock
    Phone: STRTYPE
    AltPhone: STRTYPE
    Fax: STRTYPE
    Email: STRTYPE
    Contact: STRTYPE
    AltContact: STRTYPE
    AccountNumber: STRTYPE
    Notes: STRTYPE
    ExternalGUID: GUIDTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class OtherNameAddRs(TypedDict, total=False):
    OtherNameRet: OtherNameRet
    ErrorRecovery: ErrorRecovery


class ReceivePaymentToDepositQueryRq(TypedDict, total=False):
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ReceivePaymentToDepositRet(TypedDict, total=False):
    TxnID: IDTYPE
    TxnLineID: IDTYPE
    TxnType: TxnType
    CustomerRef: CustomerRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Amount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    AmountInHomeCurrency: AMTTYPE


class ReceivePaymentToDepositQueryRs(TypedDict, total=False):
    ReceivePaymentToDepositRet: Union[ReceivePaymentToDepositRet, List[ReceivePaymentToDepositRet]]


class NameFilter(TypedDict, total=False):
    MatchCriterion: MatchCriterion
    Name: STRTYPE


class NameRangeFilter(TypedDict, total=False):
    FromName: STRTYPE
    ToName: STRTYPE


class UnitOfMeasureSetQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BaseUnit(TypedDict, total=False):
    Name: STRTYPE
    Abbreviation: STRTYPE


class RelatedUnit(TypedDict, total=False):
    Name: STRTYPE
    Abbreviation: STRTYPE
    ConversionRatio: PRICETYPE


class DefaultUnit(TypedDict, total=False):
    UnitUsedFor: UnitUsedFor
    Unit: STRTYPE


class UnitOfMeasureSetRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    UnitOfMeasureType: UnitOfMeasureType
    BaseUnit: BaseUnit
    RelatedUnit: Union[RelatedUnit, List[RelatedUnit]]
    DefaultUnit: Union[DefaultUnit, List[DefaultUnit]]


class UnitOfMeasureSetQueryRs(TypedDict, total=False):
    UnitOfMeasureSetRet: Union[UnitOfMeasureSetRet, List[UnitOfMeasureSetRet]]


class DataExtDefQueryRq(TypedDict, total=False):
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]
    AssignToObject: Union[AssignToObject, List[AssignToObject]]
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class DataExtDefQueryRs(TypedDict, total=False):
    DataExtDefRet: Union[DataExtDefRet, List[DataExtDefRet]]


class BillAddress(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE
    City: STRTYPE
    State: STRTYPE
    PostalCode: STRTYPE
    Country: STRTYPE
    Note: STRTYPE


class CustomerMsgRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class CustomerSalesTaxCodeRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class PriceLevelRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SalesOrderLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    PriceLevelRef: PriceLevelRef
    ClassRef: ClassRef
    Amount: AMTTYPE
    OptionForPriceRuleConflict: OptionForPriceRuleConflict
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    IsManuallyClosed: BOOLTYPE
    Other1: STRTYPE
    Other2: STRTYPE


class SalesOrderLineGroupMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    SalesOrderLineMod: Union[SalesOrderLineMod, List[SalesOrderLineMod]]


class SalesOrderMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    ShipAddress: ShipAddress
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    ItemSalesTaxRef: ItemSalesTaxRef
    IsManuallyClosed: BOOLTYPE
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExchangeRate: FLOATTYPE
    SalesOrderLineMod: SalesOrderLineMod
    SalesOrderLineGroupMod: SalesOrderLineGroupMod


class SalesOrderModRq(TypedDict, total=False):
    SalesOrderMod: SalesOrderMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BillAddressBlock(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE


class SalesOrderLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    Invoiced: QUANTYPE
    IsManuallyClosed: BOOLTYPE
    Other1: STRTYPE
    Other2: STRTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class SalesOrderLineGroupRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    IsPrintItemsInGroup: BOOLTYPE
    TotalAmount: AMTTYPE
    SalesOrderLineRet: Union[SalesOrderLineRet, List[SalesOrderLineRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class SalesOrderRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    BillAddressBlock: BillAddressBlock
    ShipAddress: ShipAddress
    ShipAddressBlock: ShipAddressBlock
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    Subtotal: AMTTYPE
    ItemSalesTaxRef: ItemSalesTaxRef
    SalesTaxPercentage: PERCENTTYPE
    SalesTaxTotal: AMTTYPE
    TotalAmount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    TotalAmountInHomeCurrency: AMTTYPE
    IsManuallyClosed: BOOLTYPE
    IsFullyInvoiced: BOOLTYPE
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExternalGUID: GUIDTYPE
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]
    SalesOrderLineRet: SalesOrderLineRet
    SalesOrderLineGroupRet: SalesOrderLineGroupRet
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class SalesOrderModRs(TypedDict, total=False):
    SalesOrderRet: SalesOrderRet
    ErrorRecovery: ErrorRecovery


class ChargeQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    PaidStatus: PaidStatus
    IncludeLinkedTxns: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ChargeQueryRs(TypedDict, total=False):
    ChargeRet: Union[ChargeRet, List[ChargeRet]]


class VehicleMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    Desc: STRTYPE


class VehicleModRq(TypedDict, total=False):
    VehicleMod: VehicleMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class VehicleRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    Desc: STRTYPE


class VehicleModRs(TypedDict, total=False):
    VehicleRet: VehicleRet
    ErrorRecovery: ErrorRecovery


class VehicleRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class VehicleMileageAdd(TypedDict, total=False):
    VehicleRef: VehicleRef
    CustomerRef: CustomerRef
    ItemRef: ItemRef
    ClassRef: ClassRef
    TripStartDate: DATETYPE
    TripEndDate: DATETYPE
    OdometerStart: QUANTYPE
    OdometerEnd: QUANTYPE
    TotalMiles: QUANTYPE
    Notes: STRTYPE
    BillableStatus: BillableStatus


class VehicleMileageAddRq(TypedDict, total=False):
    VehicleMileageAdd: VehicleMileageAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class VehicleMileageRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    VehicleRef: VehicleRef
    CustomerRef: CustomerRef
    ItemRef: ItemRef
    ClassRef: ClassRef
    TripStartDate: DATETYPE
    TripEndDate: DATETYPE
    OdometerStart: QUANTYPE
    OdometerEnd: QUANTYPE
    TotalMiles: QUANTYPE
    Notes: STRTYPE
    BillableStatus: BillableStatus
    StandardMileageRate: PERCENTTYPE
    StandardMileageTotalAmount: AMTTYPE
    BillableRate: PRICETYPE
    BillableAmount: AMTTYPE


class VehicleMileageAddRs(TypedDict, total=False):
    VehicleMileageRet: VehicleMileageRet
    ErrorRecovery: ErrorRecovery


class ApplyCheckToTxnAdd(TypedDict, total=False):
    TxnID: IDTYPE
    Amount: AMTTYPE


class ExpenseLineAdd(TypedDict, total=False):
    AccountRef: AccountRef
    Amount: AMTTYPE
    Memo: STRTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    SalesTaxCodeRef: SalesTaxCodeRef
    BillableStatus: BillableStatus
    SalesRepRef: SalesRepRef
    DataExt: Union[DataExt, List[DataExt]]


class ItemLineAdd(TypedDict, total=False):
    ItemRef: ItemRef
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    Cost: PRICETYPE
    Amount: AMTTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    SalesTaxCodeRef: SalesTaxCodeRef
    BillableStatus: BillableStatus
    OverrideItemAccountRef: OverrideItemAccountRef
    SalesRepRef: SalesRepRef
    DataExt: Union[DataExt, List[DataExt]]


class ItemGroupLineAdd(TypedDict, total=False):
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    DataExt: Union[DataExt, List[DataExt]]


class CheckAdd(TypedDict, total=False):
    AccountRef: AccountRef
    PayeeEntityRef: PayeeEntityRef
    RefNumber: STRTYPE
    TxnDate: DATETYPE
    Memo: STRTYPE
    Address: Address
    IsToBePrinted: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    ApplyCheckToTxnAdd: Union[ApplyCheckToTxnAdd, List[ApplyCheckToTxnAdd]]
    ExpenseLineAdd: Union[ExpenseLineAdd, List[ExpenseLineAdd]]
    ItemLineAdd: ItemLineAdd
    ItemGroupLineAdd: ItemGroupLineAdd


class CheckAddRq(TypedDict, total=False):
    CheckAdd: CheckAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CheckRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    AccountRef: AccountRef
    PayeeEntityRef: PayeeEntityRef
    RefNumber: STRTYPE
    TxnDate: DATETYPE
    Amount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    AmountInHomeCurrency: AMTTYPE
    Memo: STRTYPE
    Address: Address
    AddressBlock: AddressBlock
    IsToBePrinted: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExternalGUID: GUIDTYPE
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]
    ExpenseLineRet: Union[ExpenseLineRet, List[ExpenseLineRet]]
    ItemLineRet: ItemLineRet
    ItemGroupLineRet: ItemGroupLineRet
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class CheckAddRs(TypedDict, total=False):
    CheckRet: CheckRet
    ErrorRecovery: ErrorRecovery


class PriceLevelQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ItemRef: ItemRef
    CurrencyFilter: CurrencyFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class PriceLevelPerItemRet(TypedDict, total=False):
    ItemRef: ItemRef
    CustomPrice: PRICETYPE
    CustomPricePercent: PERCENTTYPE


class PriceLevelRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    PriceLevelType: PriceLevelType
    PriceLevelFixedPercentage: PERCENTTYPE
    PriceLevelPerItemRet: Union[PriceLevelPerItemRet, List[PriceLevelPerItemRet]]
    CurrencyRef: CurrencyRef


class PriceLevelQueryRs(TypedDict, total=False):
    PriceLevelRet: Union[PriceLevelRet, List[PriceLevelRet]]


class BillQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    PaidStatus: PaidStatus
    IncludeLineItems: BOOLTYPE
    IncludeLinkedTxns: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class BillRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    VendorRef: VendorRef
    VendorAddress: VendorAddress
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    DueDate: DATETYPE
    AmountDue: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    AmountDueInHomeCurrency: AMTTYPE
    RefNumber: STRTYPE
    TermsRef: TermsRef
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    IsPaid: BOOLTYPE
    ExternalGUID: GUIDTYPE
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]
    ExpenseLineRet: Union[ExpenseLineRet, List[ExpenseLineRet]]
    ItemLineRet: ItemLineRet
    ItemGroupLineRet: ItemGroupLineRet
    OpenAmount: AMTTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class BillQueryRs(TypedDict, total=False):
    BillRet: Union[BillRet, List[BillRet]]


class ItemSubtotalQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemSubtotalQueryRs(TypedDict, total=False):
    ItemSubtotalRet: Union[ItemSubtotalRet, List[ItemSubtotalRet]]


class EstimateLineAdd(TypedDict, total=False):
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    OptionForPriceRuleConflict: OptionForPriceRuleConflict
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SalesTaxCodeRef: SalesTaxCodeRef
    MarkupRate: PRICETYPE
    MarkupRatePercent: PERCENTTYPE
    PriceLevelRef: PriceLevelRef
    OverrideItemAccountRef: OverrideItemAccountRef
    Other1: STRTYPE
    Other2: STRTYPE
    DataExt: Union[DataExt, List[DataExt]]


class EstimateLineGroupAdd(TypedDict, total=False):
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    DataExt: Union[DataExt, List[DataExt]]


class EstimateAdd(TypedDict, total=False):
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    ShipAddress: ShipAddress
    IsActive: BOOLTYPE
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ItemSalesTaxRef: ItemSalesTaxRef
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    EstimateLineAdd: EstimateLineAdd
    EstimateLineGroupAdd: EstimateLineGroupAdd


class EstimateAddRq(TypedDict, total=False):
    EstimateAdd: EstimateAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class EstimateLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SalesTaxCodeRef: SalesTaxCodeRef
    MarkupRate: PRICETYPE
    MarkupRatePercent: PERCENTTYPE
    Other1: STRTYPE
    Other2: STRTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class EstimateLineGroupRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    IsPrintItemsInGroup: BOOLTYPE
    TotalAmount: AMTTYPE
    EstimateLineRet: Union[EstimateLineRet, List[EstimateLineRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class EstimateRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    BillAddressBlock: BillAddressBlock
    ShipAddress: ShipAddress
    ShipAddressBlock: ShipAddressBlock
    IsActive: BOOLTYPE
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    Subtotal: AMTTYPE
    ItemSalesTaxRef: ItemSalesTaxRef
    SalesTaxPercentage: PERCENTTYPE
    SalesTaxTotal: AMTTYPE
    TotalAmount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    TotalAmountInHomeCurrency: AMTTYPE
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExternalGUID: GUIDTYPE
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]
    EstimateLineRet: EstimateLineRet
    EstimateLineGroupRet: EstimateLineGroupRet
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class EstimateAddRs(TypedDict, total=False):
    EstimateRet: EstimateRet
    ErrorRecovery: ErrorRecovery


class ToDoQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    DoneStatus: DoneStatus
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ToDoQueryRs(TypedDict, total=False):
    ToDoRet: Union[ToDoRet, List[ToDoRet]]


class DataExtDefDelRq(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtName: STRTYPE


class DataExtDefDelRet(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtName: STRTYPE
    TimeDeleted: DATETIMETYPE


class DataExtDefDelRs(TypedDict, total=False):
    DataExtDefDelRet: DataExtDefDelRet
    ErrorRecovery: ErrorRecovery


class JobTypeAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef


class JobTypeAddRq(TypedDict, total=False):
    JobTypeAdd: JobTypeAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class JobTypeRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef
    Sublevel: INTTYPE


class JobTypeAddRs(TypedDict, total=False):
    JobTypeRet: JobTypeRet
    ErrorRecovery: ErrorRecovery


class QuantityAdjustment(TypedDict, total=False):
    NewQuantity: QUANTYPE
    QuantityDifference: QUANTYPE
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    InventorySiteLocationRef: InventorySiteLocationRef


class ValueAdjustment(TypedDict, total=False):
    NewQuantity: QUANTYPE
    QuantityDifference: QUANTYPE
    NewValue: AMTTYPE
    ValueDifference: AMTTYPE


class SerialNumberAdjustment(TypedDict, total=False):
    AddSerialNumber: STRTYPE
    RemoveSerialNumber: STRTYPE
    InventorySiteLocationRef: InventorySiteLocationRef


class LotNumberAdjustment(TypedDict, total=False):
    LotNumber: STRTYPE
    CountAdjustment: INTTYPE
    InventorySiteLocationRef: InventorySiteLocationRef


class InventoryAdjustmentLineAdd(TypedDict, total=False):
    ItemRef: ItemRef
    QuantityAdjustment: QuantityAdjustment
    ValueAdjustment: ValueAdjustment
    SerialNumberAdjustment: SerialNumberAdjustment
    LotNumberAdjustment: LotNumberAdjustment


class InventoryAdjustmentAdd(TypedDict, total=False):
    AccountRef: AccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    InventorySiteRef: InventorySiteRef
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    Memo: STRTYPE
    ExternalGUID: GUIDTYPE
    InventoryAdjustmentLineAdd: Union[InventoryAdjustmentLineAdd, List[InventoryAdjustmentLineAdd]]


class InventoryAdjustmentAddRq(TypedDict, total=False):
    InventoryAdjustmentAdd: InventoryAdjustmentAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class InventoryAdjustmentLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    SerialNumber: STRTYPE
    SerialNumberAddedOrRemoved: SerialNumberAddedOrRemoved
    LotNumber: STRTYPE
    InventorySiteLocationRef: InventorySiteLocationRef
    QuantityDifference: QUANTYPE
    ValueDifference: AMTTYPE


class InventoryAdjustmentRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    AccountRef: AccountRef
    InventorySiteRef: InventorySiteRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    Memo: STRTYPE
    ExternalGUID: GUIDTYPE
    InventoryAdjustmentLineRet: Union[InventoryAdjustmentLineRet, List[InventoryAdjustmentLineRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class InventoryAdjustmentAddRs(TypedDict, total=False):
    InventoryAdjustmentRet: InventoryAdjustmentRet
    ErrorRecovery: ErrorRecovery


class SalesOrPurchase(TypedDict, total=False):
    Desc: STRTYPE
    Price: PRICETYPE
    PricePercent: PERCENTTYPE
    AccountRef: AccountRef


class ExpenseAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SalesAndPurchase(TypedDict, total=False):
    SalesDesc: STRTYPE
    SalesPrice: PRICETYPE
    IncomeAccountRef: IncomeAccountRef
    PurchaseDesc: STRTYPE
    PurchaseCost: PRICETYPE
    PurchaseTaxCodeRef: PurchaseTaxCodeRef
    ExpenseAccountRef: ExpenseAccountRef
    PrefVendorRef: PrefVendorRef


class ItemServiceAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesOrPurchase: SalesOrPurchase
    SalesAndPurchase: SalesAndPurchase
    ExternalGUID: GUIDTYPE


class ItemServiceAddRq(TypedDict, total=False):
    ItemServiceAdd: ItemServiceAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemServiceRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    Sublevel: INTTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesOrPurchase: SalesOrPurchase
    SalesAndPurchase: SalesAndPurchase
    ExternalGUID: GUIDTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemServiceAddRs(TypedDict, total=False):
    ItemServiceRet: ItemServiceRet
    ErrorRecovery: ErrorRecovery


class ItemFilter(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class SalesTaxPaymentCheckQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    ItemFilter: ItemFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class SalesTaxPaymentCheckQueryRs(TypedDict, total=False):
    SalesTaxPaymentCheckRet: Union[SalesTaxPaymentCheckRet, List[SalesTaxPaymentCheckRet]]


class ShipToAddress(TypedDict, total=False):
    Name: STRTYPE
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE
    City: STRTYPE
    State: STRTYPE
    PostalCode: STRTYPE
    Country: STRTYPE
    Note: STRTYPE
    DefaultShipTo: BOOLTYPE


class ClassFilter(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class ItemDiscountQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemDiscountRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    Sublevel: INTTYPE
    ItemDesc: STRTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    DiscountRate: PRICETYPE
    DiscountRatePercent: PERCENTTYPE
    AccountRef: AccountRef
    ExternalGUID: GUIDTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemDiscountQueryRs(TypedDict, total=False):
    ItemDiscountRet: Union[ItemDiscountRet, List[ItemDiscountRet]]


class ItemGroupLine(TypedDict, total=False):
    ItemRef: ItemRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE


class ItemGroupAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ItemDesc: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    IsPrintItemsInGroup: BOOLTYPE
    ExternalGUID: GUIDTYPE
    ItemGroupLine: Union[ItemGroupLine, List[ItemGroupLine]]


class ItemGroupAddRq(TypedDict, total=False):
    ItemGroupAdd: ItemGroupAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemGroupRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ItemDesc: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    IsPrintItemsInGroup: BOOLTYPE
    SpecialItemType: SpecialItemType
    ExternalGUID: GUIDTYPE
    ItemGroupLine: Union[ItemGroupLine, List[ItemGroupLine]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemGroupAddRs(TypedDict, total=False):
    ItemGroupRet: ItemGroupRet
    ErrorRecovery: ErrorRecovery


class CreditMemoQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeLinkedTxns: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class CreditMemoLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    Other1: STRTYPE
    Other2: STRTYPE
    CreditCardTxnInfo: CreditCardTxnInfo
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class CreditMemoLineGroupRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    IsPrintItemsInGroup: BOOLTYPE
    TotalAmount: AMTTYPE
    CreditMemoLineRet: Union[CreditMemoLineRet, List[CreditMemoLineRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class CreditMemoRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    ARAccountRef: ARAccountRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    BillAddressBlock: BillAddressBlock
    ShipAddress: ShipAddress
    ShipAddressBlock: ShipAddressBlock
    IsPending: BOOLTYPE
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    Subtotal: AMTTYPE
    ItemSalesTaxRef: ItemSalesTaxRef
    SalesTaxPercentage: PERCENTTYPE
    SalesTaxTotal: AMTTYPE
    TotalAmount: AMTTYPE
    CreditRemaining: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    CreditRemainingInHomeCurrency: AMTTYPE
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExternalGUID: GUIDTYPE
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]
    CreditMemoLineRet: CreditMemoLineRet
    CreditMemoLineGroupRet: CreditMemoLineGroupRet
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class CreditMemoQueryRs(TypedDict, total=False):
    CreditMemoRet: Union[CreditMemoRet, List[CreditMemoRet]]


class StandardTermsAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    StdDueDays: INTTYPE
    StdDiscountDays: INTTYPE
    DiscountPct: PERCENTTYPE


class StandardTermsAddRq(TypedDict, total=False):
    StandardTermsAdd: StandardTermsAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class StandardTermsRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    StdDueDays: INTTYPE
    StdDiscountDays: INTTYPE
    DiscountPct: PERCENTTYPE


class StandardTermsAddRs(TypedDict, total=False):
    StandardTermsRet: StandardTermsRet
    ErrorRecovery: ErrorRecovery


class BillingRatePerItem(TypedDict, total=False):
    ItemRef: ItemRef
    CustomRate: PRICETYPE
    CustomRatePercent: PERCENTTYPE
    AdjustPercentage: PERCENTTYPE
    AdjustBillingRateRelativeTo: AdjustBillingRateRelativeTo


class BillingRateAdd(TypedDict, total=False):
    Name: STRTYPE
    FixedBillingRate: PRICETYPE
    BillingRatePerItem: Union[BillingRatePerItem, List[BillingRatePerItem]]


class BillingRateAddRq(TypedDict, total=False):
    BillingRateAdd: BillingRateAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BillingRatePerItemRet(TypedDict, total=False):
    ItemRef: ItemRef
    CustomRate: PRICETYPE
    CustomRatePercent: PERCENTTYPE


class BillingRateRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BillingRateType: BillingRateType
    FixedBillingRate: PRICETYPE
    BillingRatePerItemRet: Union[BillingRatePerItemRet, List[BillingRatePerItemRet]]


class BillingRateAddRs(TypedDict, total=False):
    BillingRateRet: BillingRateRet
    ErrorRecovery: ErrorRecovery


class RateEntry(TypedDict, total=False):
    Rate: PRICETYPE
    EffectiveDate: DATETYPE


class WorkersCompCodeAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    Desc: STRTYPE
    RateEntry: Union[RateEntry, List[RateEntry]]


class WorkersCompCodeAddRq(TypedDict, total=False):
    WorkersCompCodeAdd: WorkersCompCodeAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class RateHistory(TypedDict, total=False):
    Rate: PRICETYPE
    EffectiveDate: DATETYPE


class WorkersCompCodeRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    Desc: STRTYPE
    CurrentRate: PRICETYPE
    CurrentEffectiveDate: DATETYPE
    NextRate: PRICETYPE
    NextEffectiveDate: DATETYPE
    RateHistory: Union[RateHistory, List[RateHistory]]


class WorkersCompCodeAddRs(TypedDict, total=False):
    WorkersCompCodeRet: WorkersCompCodeRet
    ErrorRecovery: ErrorRecovery


class ItemOtherChargeAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesOrPurchase: SalesOrPurchase
    SalesAndPurchase: SalesAndPurchase
    ExternalGUID: GUIDTYPE


class ItemOtherChargeAddRq(TypedDict, total=False):
    ItemOtherChargeAdd: ItemOtherChargeAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemOtherChargeRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    Sublevel: INTTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesOrPurchase: SalesOrPurchase
    SalesAndPurchase: SalesAndPurchase
    SpecialItemType: SpecialItemType
    ExternalGUID: GUIDTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemOtherChargeAddRs(TypedDict, total=False):
    ItemOtherChargeRet: ItemOtherChargeRet
    ErrorRecovery: ErrorRecovery


class BillPaymentCreditCardQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class CreditCardAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class BillPaymentCreditCardRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    PayeeEntityRef: PayeeEntityRef
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    CreditCardAccountRef: CreditCardAccountRef
    Amount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    AmountInHomeCurrency: AMTTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    ExternalGUID: GUIDTYPE
    AppliedToTxnRet: Union[AppliedToTxnRet, List[AppliedToTxnRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class BillPaymentCreditCardQueryRs(TypedDict, total=False):
    BillPaymentCreditCardRet: Union[BillPaymentCreditCardRet, List[BillPaymentCreditCardRet]]


class TermsQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class DateDrivenTermsRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    DayOfMonthDue: INTTYPE
    DueNextMonthDays: INTTYPE
    DiscountDayOfMonth: INTTYPE
    DiscountPct: PERCENTTYPE


class TermsQueryRs(TypedDict, total=False):
    StandardTermsRet: StandardTermsRet
    DateDrivenTermsRet: DateDrivenTermsRet


class ListDisplayAddRq(TypedDict, total=False):
    ListDisplayAddType: ListDisplayAddType


class SalesOrPurchaseMod(TypedDict, total=False):
    Desc: STRTYPE
    Price: PRICETYPE
    PricePercent: PERCENTTYPE
    AccountRef: AccountRef
    ApplyAccountRefToExistingTxns: BOOLTYPE


class SalesAndPurchaseMod(TypedDict, total=False):
    SalesDesc: STRTYPE
    SalesPrice: PRICETYPE
    IncomeAccountRef: IncomeAccountRef
    ApplyIncomeAccountRefToExistingTxns: BOOLTYPE
    PurchaseDesc: STRTYPE
    PurchaseCost: PRICETYPE
    PurchaseTaxCodeRef: PurchaseTaxCodeRef
    ExpenseAccountRef: ExpenseAccountRef
    ApplyExpenseAccountRefToExistingTxns: BOOLTYPE
    PrefVendorRef: PrefVendorRef


class ItemNonInventoryMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    ManufacturerPartNumber: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    ForceUOMChange: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesOrPurchaseMod: SalesOrPurchaseMod
    SalesAndPurchaseMod: SalesAndPurchaseMod


class ItemNonInventoryModRq(TypedDict, total=False):
    ItemNonInventoryMod: ItemNonInventoryMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemNonInventoryRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    Sublevel: INTTYPE
    ManufacturerPartNumber: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesOrPurchase: SalesOrPurchase
    SalesAndPurchase: SalesAndPurchase
    ExternalGUID: GUIDTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemNonInventoryModRs(TypedDict, total=False):
    ItemNonInventoryRet: ItemNonInventoryRet
    ErrorRecovery: ErrorRecovery


class ItemSalesTaxGroupAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ItemDesc: STRTYPE
    ExternalGUID: GUIDTYPE
    ItemSalesTaxRef: Union[ItemSalesTaxRef, List[ItemSalesTaxRef]]


class ItemSalesTaxGroupAddRq(TypedDict, total=False):
    ItemSalesTaxGroupAdd: ItemSalesTaxGroupAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemSalesTaxGroupRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ItemDesc: STRTYPE
    ExternalGUID: GUIDTYPE
    ItemSalesTaxRef: Union[ItemSalesTaxRef, List[ItemSalesTaxRef]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemSalesTaxGroupAddRs(TypedDict, total=False):
    ItemSalesTaxGroupRet: ItemSalesTaxGroupRet
    ErrorRecovery: ErrorRecovery


class ExpenseLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    AccountRef: AccountRef
    Amount: AMTTYPE
    Memo: STRTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    SalesTaxCodeRef: SalesTaxCodeRef
    BillableStatus: BillableStatus
    SalesRepRef: SalesRepRef


class ItemLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Cost: PRICETYPE
    Amount: AMTTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    SalesTaxCodeRef: SalesTaxCodeRef
    BillableStatus: BillableStatus
    OverrideItemAccountRef: OverrideItemAccountRef
    SalesRepRef: SalesRepRef


class ItemGroupLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    ItemLineMod: Union[ItemLineMod, List[ItemLineMod]]


class ItemReceiptMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    VendorRef: VendorRef
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ClearExpenseLines: BOOLTYPE
    ExpenseLineMod: Union[ExpenseLineMod, List[ExpenseLineMod]]
    ClearItemLines: BOOLTYPE
    ItemLineMod: ItemLineMod
    ItemGroupLineMod: ItemGroupLineMod


class ItemReceiptModRq(TypedDict, total=False):
    ItemReceiptMod: ItemReceiptMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemReceiptModRs(TypedDict, total=False):
    ItemReceiptRet: ItemReceiptRet
    ErrorRecovery: ErrorRecovery


class CreditMemoLineAdd(TypedDict, total=False):
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    PriceLevelRef: PriceLevelRef
    ClassRef: ClassRef
    Amount: AMTTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    OverrideItemAccountRef: OverrideItemAccountRef
    Other1: STRTYPE
    Other2: STRTYPE
    CreditCardTxnInfo: CreditCardTxnInfo
    DataExt: Union[DataExt, List[DataExt]]


class CreditMemoLineGroupAdd(TypedDict, total=False):
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    DataExt: Union[DataExt, List[DataExt]]


class CreditMemoAdd(TypedDict, total=False):
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    ARAccountRef: ARAccountRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    ShipAddress: ShipAddress
    IsPending: BOOLTYPE
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    ItemSalesTaxRef: ItemSalesTaxRef
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    CreditMemoLineAdd: CreditMemoLineAdd
    CreditMemoLineGroupAdd: CreditMemoLineGroupAdd


class CreditMemoAddRq(TypedDict, total=False):
    CreditMemoAdd: CreditMemoAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CreditMemoAddRs(TypedDict, total=False):
    CreditMemoRet: CreditMemoRet
    ErrorRecovery: ErrorRecovery


class PayrollSummaryReportQueryRq(TypedDict, total=False):
    PayrollSummaryReportType: PayrollSummaryReportType
    DisplayReport: BOOLTYPE
    ReportPeriod: ReportPeriod
    ReportDateMacro: ReportDateMacro
    ReportAccountFilter: ReportAccountFilter
    ReportEntityFilter: ReportEntityFilter
    ReportItemFilter: ReportItemFilter
    ReportClassFilter: ReportClassFilter
    ReportModifiedDateRangeFilter: ReportModifiedDateRangeFilter
    ReportModifiedDateRangeMacro: ReportModifiedDateRangeMacro
    ReportDetailLevelFilter: ReportDetailLevelFilter
    ReportPostingStatusFilter: ReportPostingStatusFilter
    SummarizeColumnsBy: SummarizeColumnsBy
    IncludeSubcolumns: BOOLTYPE
    ReportCalendar: ReportCalendar
    ReturnRows: ReturnRows
    ReturnColumns: ReturnColumns


class SetCredit(TypedDict, total=False):
    CreditTxnID: IDTYPE
    AppliedAmount: AMTTYPE
    Override: BOOLTYPE


class AppliedToTxnAdd(TypedDict, total=False):
    TxnID: IDTYPE
    PaymentAmount: AMTTYPE
    SetCredit: Union[SetCredit, List[SetCredit]]
    DiscountAmount: AMTTYPE
    DiscountAccountRef: DiscountAccountRef
    DiscountClassRef: DiscountClassRef


class ReceivePaymentAdd(TypedDict, total=False):
    CustomerRef: CustomerRef
    ARAccountRef: ARAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    TotalAmount: AMTTYPE
    ExchangeRate: FLOATTYPE
    PaymentMethodRef: PaymentMethodRef
    Memo: STRTYPE
    DepositToAccountRef: DepositToAccountRef
    CreditCardTxnInfo: CreditCardTxnInfo
    ExternalGUID: GUIDTYPE
    IsAutoApply: BOOLTYPE
    AppliedToTxnAdd: Union[AppliedToTxnAdd, List[AppliedToTxnAdd]]


class ReceivePaymentAddRq(TypedDict, total=False):
    ReceivePaymentAdd: ReceivePaymentAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ReceivePaymentAddRs(TypedDict, total=False):
    ReceivePaymentRet: ReceivePaymentRet
    ErrorRecovery: ErrorRecovery


class PayrollItemNonWageQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class PayrollItemNonWageRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    NonWageType: NonWageType
    ExpenseAccountRef: ExpenseAccountRef
    LiabilityAccountRef: LiabilityAccountRef


class PayrollItemNonWageQueryRs(TypedDict, total=False):
    PayrollItemNonWageRet: Union[PayrollItemNonWageRet, List[PayrollItemNonWageRet]]


class SalesReceiptLineAdd(TypedDict, total=False):
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    PriceLevelRef: PriceLevelRef
    ClassRef: ClassRef
    Amount: AMTTYPE
    OptionForPriceRuleConflict: OptionForPriceRuleConflict
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    OverrideItemAccountRef: OverrideItemAccountRef
    Other1: STRTYPE
    Other2: STRTYPE
    CreditCardTxnInfo: CreditCardTxnInfo
    DataExt: Union[DataExt, List[DataExt]]


class SalesReceiptLineGroupAdd(TypedDict, total=False):
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    DataExt: Union[DataExt, List[DataExt]]


class SalesReceiptAdd(TypedDict, total=False):
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    ShipAddress: ShipAddress
    IsPending: BOOLTYPE
    CheckNumber: STRTYPE
    PaymentMethodRef: PaymentMethodRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    FOB: STRTYPE
    ItemSalesTaxRef: ItemSalesTaxRef
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    DepositToAccountRef: DepositToAccountRef
    CreditCardTxnInfo: CreditCardTxnInfo
    Other: STRTYPE
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    SalesReceiptLineAdd: SalesReceiptLineAdd
    SalesReceiptLineGroupAdd: SalesReceiptLineGroupAdd


class SalesReceiptAddRq(TypedDict, total=False):
    SalesReceiptAdd: SalesReceiptAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesReceiptLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    Other1: STRTYPE
    Other2: STRTYPE
    CreditCardTxnInfo: CreditCardTxnInfo
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class SalesReceiptLineGroupRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    IsPrintItemsInGroup: BOOLTYPE
    TotalAmount: AMTTYPE
    SalesReceiptLineRet: Union[SalesReceiptLineRet, List[SalesReceiptLineRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class SalesReceiptRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    BillAddressBlock: BillAddressBlock
    ShipAddress: ShipAddress
    ShipAddressBlock: ShipAddressBlock
    IsPending: BOOLTYPE
    CheckNumber: STRTYPE
    PaymentMethodRef: PaymentMethodRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    FOB: STRTYPE
    Subtotal: AMTTYPE
    ItemSalesTaxRef: ItemSalesTaxRef
    SalesTaxPercentage: PERCENTTYPE
    SalesTaxTotal: AMTTYPE
    TotalAmount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    TotalAmountInHomeCurrency: AMTTYPE
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    DepositToAccountRef: DepositToAccountRef
    CreditCardTxnInfo: CreditCardTxnInfo
    Other: STRTYPE
    ExternalGUID: GUIDTYPE
    SalesReceiptLineRet: SalesReceiptLineRet
    SalesReceiptLineGroupRet: SalesReceiptLineGroupRet
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class SalesReceiptAddRs(TypedDict, total=False):
    SalesReceiptRet: SalesReceiptRet
    ErrorRecovery: ErrorRecovery


class GeneralSummaryReportQueryRq(TypedDict, total=False):
    GeneralSummaryReportType: GeneralSummaryReportType
    DisplayReport: BOOLTYPE
    ReportPeriod: ReportPeriod
    ReportDateMacro: ReportDateMacro
    ReportAccountFilter: ReportAccountFilter
    ReportEntityFilter: ReportEntityFilter
    ReportItemFilter: ReportItemFilter
    ReportClassFilter: ReportClassFilter
    ReportTxnTypeFilter: ReportTxnTypeFilter
    ReportModifiedDateRangeFilter: ReportModifiedDateRangeFilter
    ReportModifiedDateRangeMacro: ReportModifiedDateRangeMacro
    ReportDetailLevelFilter: ReportDetailLevelFilter
    ReportPostingStatusFilter: ReportPostingStatusFilter
    SummarizeColumnsBy: SummarizeColumnsBy
    IncludeSubcolumns: BOOLTYPE
    ReportCalendar: ReportCalendar
    ReturnRows: ReturnRows
    ReturnColumns: ReturnColumns
    ReportBasis: ReportBasis


class ShipMethodAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE


class ShipMethodAddRq(TypedDict, total=False):
    ShipMethodAdd: ShipMethodAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ShipMethodRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE


class ShipMethodAddRs(TypedDict, total=False):
    ShipMethodRet: ShipMethodRet
    ErrorRecovery: ErrorRecovery


class ItemPurchaseTaxRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SalesTaxCodeMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    IsTaxable: BOOLTYPE
    Desc: STRTYPE
    ItemPurchaseTaxRef: ItemPurchaseTaxRef
    ItemSalesTaxRef: ItemSalesTaxRef


class SalesTaxCodeModRq(TypedDict, total=False):
    SalesTaxCodeMod: SalesTaxCodeMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesTaxCodeRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    IsTaxable: BOOLTYPE
    Desc: STRTYPE
    ItemPurchaseTaxRef: ItemPurchaseTaxRef
    ItemSalesTaxRef: ItemSalesTaxRef


class SalesTaxCodeModRs(TypedDict, total=False):
    SalesTaxCodeRet: SalesTaxCodeRet
    ErrorRecovery: ErrorRecovery


class ItemDiscountMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    ItemDesc: STRTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    DiscountRate: PRICETYPE
    DiscountRatePercent: PERCENTTYPE
    AccountRef: AccountRef
    ApplyAccountRefToExistingTxns: BOOLTYPE


class ItemDiscountModRq(TypedDict, total=False):
    ItemDiscountMod: ItemDiscountMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemDiscountModRs(TypedDict, total=False):
    ItemDiscountRet: ItemDiscountRet
    ErrorRecovery: ErrorRecovery


class CreditCardChargeAdd(TypedDict, total=False):
    AccountRef: AccountRef
    PayeeEntityRef: PayeeEntityRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    ExpenseLineAdd: Union[ExpenseLineAdd, List[ExpenseLineAdd]]
    ItemLineAdd: ItemLineAdd
    ItemGroupLineAdd: ItemGroupLineAdd


class CreditCardChargeAddRq(TypedDict, total=False):
    CreditCardChargeAdd: CreditCardChargeAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CreditCardChargeRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    AccountRef: AccountRef
    PayeeEntityRef: PayeeEntityRef
    TxnDate: DATETYPE
    Amount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    AmountInHomeCurrency: AMTTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExternalGUID: GUIDTYPE
    ExpenseLineRet: Union[ExpenseLineRet, List[ExpenseLineRet]]
    ItemLineRet: ItemLineRet
    ItemGroupLineRet: ItemGroupLineRet
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class CreditCardChargeAddRs(TypedDict, total=False):
    CreditCardChargeRet: CreditCardChargeRet
    ErrorRecovery: ErrorRecovery


class SalesReceiptQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class SalesReceiptQueryRs(TypedDict, total=False):
    SalesReceiptRet: Union[SalesReceiptRet, List[SalesReceiptRet]]


class VendorTypeQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class VendorTypeRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef
    Sublevel: INTTYPE


class VendorTypeQueryRs(TypedDict, total=False):
    VendorTypeRet: Union[VendorTypeRet, List[VendorTypeRet]]


class VehicleQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class VehicleQueryRs(TypedDict, total=False):
    VehicleRet: Union[VehicleRet, List[VehicleRet]]


class BillingRateQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ItemRef: ItemRef
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BillingRateQueryRs(TypedDict, total=False):
    BillingRateRet: Union[BillingRateRet, List[BillingRateRet]]


class VendorCreditMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    VendorRef: VendorRef
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ClearExpenseLines: BOOLTYPE
    ExpenseLineMod: Union[ExpenseLineMod, List[ExpenseLineMod]]
    ClearItemLines: BOOLTYPE
    ItemLineMod: ItemLineMod
    ItemGroupLineMod: ItemGroupLineMod


class VendorCreditModRq(TypedDict, total=False):
    VendorCreditMod: VendorCreditMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class VendorCreditRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    VendorRef: VendorRef
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    CreditAmount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    CreditAmountInHomeCurrency: AMTTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExternalGUID: GUIDTYPE
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]
    ExpenseLineRet: Union[ExpenseLineRet, List[ExpenseLineRet]]
    ItemLineRet: ItemLineRet
    ItemGroupLineRet: ItemGroupLineRet
    OpenAmount: AMTTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class VendorCreditModRs(TypedDict, total=False):
    VendorCreditRet: VendorCreditRet
    ErrorRecovery: ErrorRecovery


class SiteFilter(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]


class ItemSiteFilter(TypedDict, total=False):
    ItemFilter: ItemFilter
    SiteFilter: SiteFilter


class ItemSitesQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    ItemTypeFilter: ItemTypeFilter
    ItemSiteFilter: ItemSiteFilter
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemInventoryRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ItemSitesRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    ItemInventoryAssemblyRef: ItemInventoryAssemblyRef
    ItemInventoryRef: ItemInventoryRef
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    ReorderLevel: QUANTYPE
    QuantityOnHand: QUANTYPE
    QuantityOnPurchaseOrders: QUANTYPE
    QuantityOnSalesOrders: QUANTYPE
    QuantityToBeBuiltByPendingBuildTxns: QUANTYPE
    QuantityRequiredByPendingBuildTxns: QUANTYPE
    QuantityOnPendingTransfers: QUANTYPE
    AssemblyBuildPoint: QUANTYPE


class ItemSitesQueryRs(TypedDict, total=False):
    ItemSitesRet: Union[ItemSitesRet, List[ItemSitesRet]]


class ItemInventoryAssemblyLine(TypedDict, total=False):
    ItemInventoryRef: ItemInventoryRef
    Quantity: QUANTYPE


class ItemInventoryAssemblyAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    ManufacturerPartNumber: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesDesc: STRTYPE
    SalesPrice: PRICETYPE
    IncomeAccountRef: IncomeAccountRef
    PurchaseDesc: STRTYPE
    PurchaseCost: PRICETYPE
    PurchaseTaxCodeRef: PurchaseTaxCodeRef
    COGSAccountRef: COGSAccountRef
    PrefVendorRef: PrefVendorRef
    AssetAccountRef: AssetAccountRef
    BuildPoint: QUANTYPE
    Max: QUANTYPE
    QuantityOnHand: QUANTYPE
    TotalValue: AMTTYPE
    InventoryDate: DATETYPE
    ExternalGUID: GUIDTYPE
    ItemInventoryAssemblyLine: Union[ItemInventoryAssemblyLine, List[ItemInventoryAssemblyLine]]


class ItemInventoryAssemblyAddRq(TypedDict, total=False):
    ItemInventoryAssemblyAdd: ItemInventoryAssemblyAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemInventoryAssemblyRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    Sublevel: INTTYPE
    ManufacturerPartNumber: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesDesc: STRTYPE
    SalesPrice: PRICETYPE
    IncomeAccountRef: IncomeAccountRef
    PurchaseDesc: STRTYPE
    PurchaseCost: PRICETYPE
    PurchaseTaxCodeRef: PurchaseTaxCodeRef
    COGSAccountRef: COGSAccountRef
    PrefVendorRef: PrefVendorRef
    AssetAccountRef: AssetAccountRef
    BuildPoint: QUANTYPE
    Max: QUANTYPE
    QuantityOnHand: QUANTYPE
    AverageCost: PRICETYPE
    QuantityOnOrder: QUANTYPE
    QuantityOnSalesOrder: QUANTYPE
    ExternalGUID: GUIDTYPE
    ItemInventoryAssemblyLine: Union[ItemInventoryAssemblyLine, List[ItemInventoryAssemblyLine]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemInventoryAssemblyAddRs(TypedDict, total=False):
    ItemInventoryAssemblyRet: ItemInventoryAssemblyRet
    ErrorRecovery: ErrorRecovery


class TxnDisplayModRq(TypedDict, total=False):
    TxnDisplayModType: TxnDisplayModType
    TxnID: IDTYPE


class StandardTermsQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class StandardTermsQueryRs(TypedDict, total=False):
    StandardTermsRet: Union[StandardTermsRet, List[StandardTermsRet]]


class BillPaymentCheckQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class BillPaymentCheckRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    PayeeEntityRef: PayeeEntityRef
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    BankAccountRef: BankAccountRef
    Amount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    AmountInHomeCurrency: AMTTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    Address: Address
    AddressBlock: AddressBlock
    IsToBePrinted: BOOLTYPE
    ExternalGUID: GUIDTYPE
    AppliedToTxnRet: Union[AppliedToTxnRet, List[AppliedToTxnRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class BillPaymentCheckQueryRs(TypedDict, total=False):
    BillPaymentCheckRet: Union[BillPaymentCheckRet, List[BillPaymentCheckRet]]


class ItemQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class FixedAssetSalesInfo(TypedDict, total=False):
    SalesDesc: STRTYPE
    SalesDate: DATETYPE
    SalesPrice: PRICETYPE
    SalesExpense: PRICETYPE


class ItemFixedAssetRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    AcquiredAs: AcquiredAs
    PurchaseDesc: STRTYPE
    PurchaseDate: DATETYPE
    PurchaseCost: PRICETYPE
    VendorOrPayeeName: STRTYPE
    AssetAccountRef: AssetAccountRef
    FixedAssetSalesInfo: FixedAssetSalesInfo
    AssetDesc: STRTYPE
    Location: STRTYPE
    PONumber: STRTYPE
    SerialNumber: STRTYPE
    WarrantyExpDate: DATETYPE
    Notes: STRTYPE
    AssetNumber: STRTYPE
    CostBasis: AMTTYPE
    YearEndAccumulatedDepreciation: AMTTYPE
    YearEndBookValue: AMTTYPE
    ExternalGUID: GUIDTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemPaymentRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ItemDesc: STRTYPE
    DepositToAccountRef: DepositToAccountRef
    PaymentMethodRef: PaymentMethodRef
    ExternalGUID: GUIDTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class TaxVendorRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SalesTaxReturnLineRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ItemSalesTaxRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCodeValue: STRTYPE
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ItemDesc: STRTYPE
    TaxRate: PERCENTTYPE
    TaxVendorRef: TaxVendorRef
    SalesTaxReturnLineRef: SalesTaxReturnLineRef
    ExternalGUID: GUIDTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ItemQueryRs(TypedDict, total=False):
    ItemServiceRet: ItemServiceRet
    ItemNonInventoryRet: ItemNonInventoryRet
    ItemOtherChargeRet: ItemOtherChargeRet
    ItemInventoryRet: ItemInventoryRet
    ItemInventoryAssemblyRet: ItemInventoryAssemblyRet
    ItemFixedAssetRet: ItemFixedAssetRet
    ItemSubtotalRet: ItemSubtotalRet
    ItemDiscountRet: ItemDiscountRet
    ItemPaymentRet: ItemPaymentRet
    ItemSalesTaxRet: ItemSalesTaxRet
    ItemSalesTaxGroupRet: ItemSalesTaxGroupRet
    ItemGroupRet: ItemGroupRet


class ItemInventoryAssemblyQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemInventoryAssemblyQueryRs(TypedDict, total=False):
    ItemInventoryAssemblyRet: Union[ItemInventoryAssemblyRet, List[ItemInventoryAssemblyRet]]


class TransactionModifiedDateRangeFilter(TypedDict, total=False):
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    DateMacro: DateMacro


class TransactionDateRangeFilter(TypedDict, total=False):
    FromTxnDate: DATETYPE
    ToTxnDate: DATETYPE
    DateMacro: DateMacro


class TransactionEntityFilter(TypedDict, total=False):
    EntityTypeFilter: EntityTypeFilter
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class TransactionAccountFilter(TypedDict, total=False):
    AccountTypeFilter: AccountTypeFilter
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class TransactionItemFilter(TypedDict, total=False):
    ItemTypeFilter: ItemTypeFilter
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class TransactionClassFilter(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ListIDWithChildren: IDTYPE
    FullNameWithChildren: STRTYPE


class TransactionTypeFilter(TypedDict, total=False):
    TxnTypeFilter: Union[TxnTypeFilter, List[TxnTypeFilter]]


class TransactionQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    MaxReturned: INTTYPE
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    TransactionModifiedDateRangeFilter: TransactionModifiedDateRangeFilter
    TransactionDateRangeFilter: TransactionDateRangeFilter
    TransactionEntityFilter: TransactionEntityFilter
    TransactionAccountFilter: TransactionAccountFilter
    TransactionItemFilter: TransactionItemFilter
    TransactionClassFilter: TransactionClassFilter
    TransactionTypeFilter: TransactionTypeFilter
    TransactionDetailLevelFilter: TransactionDetailLevelFilter
    TransactionPostingStatusFilter: TransactionPostingStatusFilter
    TransactionPaidStatusFilter: TransactionPaidStatusFilter
    CurrencyFilter: CurrencyFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TransactionRet(TypedDict, total=False):
    TxnType: TxnType
    TxnID: IDTYPE
    TxnLineID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EntityRef: EntityRef
    AccountRef: AccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Amount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    AmountInHomeCurrency: AMTTYPE
    Memo: STRTYPE


class TransactionQueryRs(TypedDict, total=False):
    TransactionRet: Union[TransactionRet, List[TransactionRet]]


class SalesTaxPayableQueryRq(TypedDict, total=False):
    AsOfDate: DATETYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesTaxPayableLineRet(TypedDict, total=False):
    ItemSalesTaxRef: ItemSalesTaxRef
    Amount: AMTTYPE


class SalesTaxPayableRet(TypedDict, total=False):
    PayeeEntityRef: PayeeEntityRef
    Amount: AMTTYPE
    SalesTaxPayableLineRet: Union[SalesTaxPayableLineRet, List[SalesTaxPayableLineRet]]


class SalesTaxPayableQueryRs(TypedDict, total=False):
    SalesTaxPayableRet: Union[SalesTaxPayableRet, List[SalesTaxPayableRet]]


class BuildAssemblyQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    ItemFilter: ItemFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    PendingStatus: PendingStatus
    IncludeComponentLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class BuildAssemblyQueryRs(TypedDict, total=False):
    BuildAssemblyRet: Union[BuildAssemblyRet, List[BuildAssemblyRet]]


class AccountMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef
    AccountType: AccountType
    AccountNumber: STRTYPE
    BankNumber: STRTYPE
    Desc: STRTYPE
    OpenBalance: AMTTYPE
    OpenBalanceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    TaxLineID: INTTYPE
    CurrencyRef: CurrencyRef


class AccountModRq(TypedDict, total=False):
    AccountMod: AccountMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TaxLineInfoRet(TypedDict, total=False):
    TaxLineID: INTTYPE
    TaxLineName: STRTYPE


class AccountRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef
    Sublevel: INTTYPE
    AccountType: AccountType
    SpecialAccountType: SpecialAccountType
    IsTaxAccount: BOOLTYPE
    AccountNumber: STRTYPE
    BankNumber: STRTYPE
    Desc: STRTYPE
    Balance: AMTTYPE
    TotalBalance: AMTTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    TaxLineInfoRet: TaxLineInfoRet
    CashFlowClassification: CashFlowClassification
    CurrencyRef: CurrencyRef
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class AccountModRs(TypedDict, total=False):
    AccountRet: AccountRet
    ErrorRecovery: ErrorRecovery


class SupervisorRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class EmployeeAddress(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    City: STRTYPE
    State: STRTYPE
    PostalCode: STRTYPE


class ItemPaymentMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ItemDesc: STRTYPE
    DepositToAccountRef: DepositToAccountRef
    PaymentMethodRef: PaymentMethodRef


class ItemPaymentModRq(TypedDict, total=False):
    ItemPaymentMod: ItemPaymentMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemPaymentModRs(TypedDict, total=False):
    ItemPaymentRet: ItemPaymentRet
    ErrorRecovery: ErrorRecovery


class DateDrivenTermsAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    DayOfMonthDue: INTTYPE
    DueNextMonthDays: INTTYPE
    DiscountDayOfMonth: INTTYPE
    DiscountPct: PERCENTTYPE


class DateDrivenTermsAddRq(TypedDict, total=False):
    DateDrivenTermsAdd: DateDrivenTermsAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class DateDrivenTermsAddRs(TypedDict, total=False):
    DateDrivenTermsRet: DateDrivenTermsRet
    ErrorRecovery: ErrorRecovery


class ItemSalesTaxMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ItemDesc: STRTYPE
    TaxRate: PERCENTTYPE
    TaxVendorRef: TaxVendorRef
    SalesTaxReturnLineRef: SalesTaxReturnLineRef


class ItemSalesTaxModRq(TypedDict, total=False):
    ItemSalesTaxMod: ItemSalesTaxMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemSalesTaxModRs(TypedDict, total=False):
    ItemSalesTaxRet: ItemSalesTaxRet
    ErrorRecovery: ErrorRecovery


class BillPaymentCheckAdd(TypedDict, total=False):
    PayeeEntityRef: PayeeEntityRef
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    BankAccountRef: BankAccountRef
    IsToBePrinted: BOOLTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    AppliedToTxnAdd: Union[AppliedToTxnAdd, List[AppliedToTxnAdd]]


class BillPaymentCheckAddRq(TypedDict, total=False):
    BillPaymentCheckAdd: BillPaymentCheckAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BillPaymentCheckAddRs(TypedDict, total=False):
    BillPaymentCheckRet: BillPaymentCheckRet
    ErrorRecovery: ErrorRecovery


class ParentSiteRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SiteAddress(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE
    City: STRTYPE
    State: STRTYPE
    PostalCode: STRTYPE
    Country: STRTYPE


class InventorySiteMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    ParentSiteRef: ParentSiteRef
    SiteDesc: STRTYPE
    Contact: STRTYPE
    Phone: STRTYPE
    Fax: STRTYPE
    Email: STRTYPE
    SiteAddress: SiteAddress


class InventorySiteModRq(TypedDict, total=False):
    InventorySiteMod: InventorySiteMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SiteAddressBlock(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE


class InventorySiteRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    ParentSiteRef: ParentSiteRef
    IsDefaultSite: BOOLTYPE
    SiteDesc: STRTYPE
    Contact: STRTYPE
    Phone: STRTYPE
    Fax: STRTYPE
    Email: STRTYPE
    SiteAddress: SiteAddress
    SiteAddressBlock: SiteAddressBlock


class InventorySiteModRs(TypedDict, total=False):
    InventorySiteRet: InventorySiteRet
    ErrorRecovery: ErrorRecovery


class TemplateQueryRq(TypedDict, total=False):
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TemplateRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    TemplateType: TemplateType


class TemplateQueryRs(TypedDict, total=False):
    TemplateRet: Union[TemplateRet, List[TemplateRet]]


class CreditCardCreditAdd(TypedDict, total=False):
    AccountRef: AccountRef
    PayeeEntityRef: PayeeEntityRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    ExpenseLineAdd: Union[ExpenseLineAdd, List[ExpenseLineAdd]]
    ItemLineAdd: ItemLineAdd
    ItemGroupLineAdd: ItemGroupLineAdd


class CreditCardCreditAddRq(TypedDict, total=False):
    CreditCardCreditAdd: CreditCardCreditAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CreditCardCreditRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    AccountRef: AccountRef
    PayeeEntityRef: PayeeEntityRef
    TxnDate: DATETYPE
    Amount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    AmountInHomeCurrency: AMTTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExternalGUID: GUIDTYPE
    ExpenseLineRet: Union[ExpenseLineRet, List[ExpenseLineRet]]
    ItemLineRet: ItemLineRet
    ItemGroupLineRet: ItemGroupLineRet
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class CreditCardCreditAddRs(TypedDict, total=False):
    CreditCardCreditRet: CreditCardCreditRet
    ErrorRecovery: ErrorRecovery


class SalesOrderQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeLinkedTxns: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class SalesOrderQueryRs(TypedDict, total=False):
    SalesOrderRet: Union[SalesOrderRet, List[SalesOrderRet]]


class SalesRepEntityRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SalesRepAdd(TypedDict, total=False):
    Initial: STRTYPE
    IsActive: BOOLTYPE
    SalesRepEntityRef: SalesRepEntityRef


class SalesRepAddRq(TypedDict, total=False):
    SalesRepAdd: SalesRepAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesRepRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Initial: STRTYPE
    IsActive: BOOLTYPE
    SalesRepEntityRef: SalesRepEntityRef


class SalesRepAddRs(TypedDict, total=False):
    SalesRepRet: SalesRepRet
    ErrorRecovery: ErrorRecovery


class MappingAccount(TypedDict, total=False):
    AccountRef: AccountRef
    ForceMapping: BOOLTYPE


class CategoryAccountMappingMod(TypedDict, total=False):
    MappingCategory: MappingCategory
    MappingAccount: Union[MappingAccount, List[MappingAccount]]
    Threshold: AMTTYPE


class Form1099CategoryAccountMappingMod(TypedDict, total=False):
    IsFiling1099Misc: BOOLTYPE
    CategoryAccountMappingMod: Union[CategoryAccountMappingMod, List[CategoryAccountMappingMod]]


class Form1099CategoryAccountMappingModRq(TypedDict, total=False):
    Form1099CategoryAccountMappingMod: Form1099CategoryAccountMappingMod


class CategoryAccountMapping(TypedDict, total=False):
    MappingCategory: MappingCategory
    AccountRef: Union[AccountRef, List[AccountRef]]
    Threshold: AMTTYPE


class Form1099CategoryAccountMappingRet(TypedDict, total=False):
    IsFiling1099Misc: BOOLTYPE
    CategoryAccountMapping: Union[CategoryAccountMapping, List[CategoryAccountMapping]]


class Form1099CategoryAccountMappingModRs(TypedDict, total=False):
    Form1099CategoryAccountMappingRet: Form1099CategoryAccountMappingRet


class SalesRepQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesRepQueryRs(TypedDict, total=False):
    SalesRepRet: Union[SalesRepRet, List[SalesRepRet]]


class InventorySiteQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class InventorySiteQueryRs(TypedDict, total=False):
    InventorySiteRet: Union[InventorySiteRet, List[InventorySiteRet]]


class ClassQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ClassQueryRs(TypedDict, total=False):
    ClassRet: Union[ClassRet, List[ClassRet]]


class ListObjRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class DataExtMod(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtName: STRTYPE
    ListDataExtType: ListDataExtType
    ListObjRef: ListObjRef
    TxnDataExtType: TxnDataExtType
    TxnID: IDTYPE
    TxnLineID: IDTYPE
    OtherDataExtType: OtherDataExtType
    DataExtValue: STRTYPE


class DataExtModRq(TypedDict, total=False):
    DataExtMod: DataExtMod


class DataExtModRs(TypedDict, total=False):
    DataExtRet: DataExtRet
    ErrorRecovery: ErrorRecovery


class TaxAgencyVendorRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class SalesTaxReturnLineQueryRq(TypedDict, total=False):
    TaxAgencyVendorRef: Union[TaxAgencyVendorRef, List[TaxAgencyVendorRef]]


class SalesTaxReturnLineRet(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE
    LineType: LineType


class SalesTaxReturnLineQueryRs(TypedDict, total=False):
    SalesTaxReturnLineRet: Union[SalesTaxReturnLineRet, List[SalesTaxReturnLineRet]]


class PriceLevelPerItem(TypedDict, total=False):
    ItemRef: ItemRef
    CustomPrice: PRICETYPE
    CustomPricePercent: PERCENTTYPE
    AdjustPercentage: PERCENTTYPE
    AdjustRelativeTo: AdjustRelativeTo


class PriceLevelMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    PriceLevelFixedPercentage: PERCENTTYPE
    PriceLevelPerItem: Union[PriceLevelPerItem, List[PriceLevelPerItem]]
    CurrencyRef: CurrencyRef


class PriceLevelModRq(TypedDict, total=False):
    PriceLevelMod: PriceLevelMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class PriceLevelModRs(TypedDict, total=False):
    PriceLevelRet: PriceLevelRet
    ErrorRecovery: ErrorRecovery


class DataEventRecoveryInfoQueryRq(TypedDict, total=False):
    SubscriberID: GUIDTYPE


class DataEventRecoveryInfoRet(TypedDict, total=False):
    SubscriberID: GUIDTYPE
    DataEventRecoveryTime: DATETIMETYPE


class DataEventRecoveryInfoQueryRs(TypedDict, total=False):
    DataEventRecoveryInfoRet: DataEventRecoveryInfoRet


class LeadQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    Name: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CashBackInfoAdd(TypedDict, total=False):
    AccountRef: AccountRef
    Memo: STRTYPE
    Amount: AMTTYPE


class OverrideClassRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class DepositLineAdd(TypedDict, total=False):
    PaymentTxnID: IDTYPE
    PaymentTxnLineID: IDTYPE
    OverrideMemo: STRTYPE
    OverrideCheckNumber: STRTYPE
    OverrideClassRef: OverrideClassRef
    EntityRef: EntityRef
    AccountRef: AccountRef
    Memo: STRTYPE
    CheckNumber: STRTYPE
    PaymentMethodRef: PaymentMethodRef
    ClassRef: ClassRef
    Amount: AMTTYPE


class DepositAdd(TypedDict, total=False):
    TxnDate: DATETYPE
    DepositToAccountRef: DepositToAccountRef
    Memo: STRTYPE
    CashBackInfoAdd: CashBackInfoAdd
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    DepositLineAdd: Union[DepositLineAdd, List[DepositLineAdd]]


class DepositAddRq(TypedDict, total=False):
    DepositAdd: DepositAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CashBackInfoRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    AccountRef: AccountRef
    Memo: STRTYPE
    Amount: AMTTYPE


class DepositLineRet(TypedDict, total=False):
    TxnType: TxnType
    TxnID: IDTYPE
    TxnLineID: IDTYPE
    PaymentTxnLineID: IDTYPE
    EntityRef: EntityRef
    AccountRef: AccountRef
    Memo: STRTYPE
    CheckNumber: STRTYPE
    PaymentMethodRef: PaymentMethodRef
    ClassRef: ClassRef
    Amount: AMTTYPE


class DepositRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    TxnDate: DATETYPE
    DepositToAccountRef: DepositToAccountRef
    Memo: STRTYPE
    DepositTotal: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    DepositTotalInHomeCurrency: AMTTYPE
    CashBackInfoRet: CashBackInfoRet
    ExternalGUID: GUIDTYPE
    DepositLineRet: Union[DepositLineRet, List[DepositLineRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class DepositAddRs(TypedDict, total=False):
    DepositRet: DepositRet
    ErrorRecovery: ErrorRecovery


class FromInventorySiteRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ToInventorySiteRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class FromInventorySiteLocationRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class ToInventorySiteLocationRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class TransferInventoryLineAdd(TypedDict, total=False):
    ItemRef: ItemRef
    FromInventorySiteLocationRef: FromInventorySiteLocationRef
    ToInventorySiteLocationRef: ToInventorySiteLocationRef
    QuantityToTransfer: QUANTYPE
    SerialNumber: STRTYPE
    LotNumber: STRTYPE


class TransferInventoryAdd(TypedDict, total=False):
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    FromInventorySiteRef: FromInventorySiteRef
    ToInventorySiteRef: ToInventorySiteRef
    Memo: STRTYPE
    ExternalGUID: GUIDTYPE
    TransferInventoryLineAdd: Union[TransferInventoryLineAdd, List[TransferInventoryLineAdd]]


class TransferInventoryAddRq(TypedDict, total=False):
    TransferInventoryAdd: TransferInventoryAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TransferInventoryLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    FromInventorySiteLocationRef: FromInventorySiteLocationRef
    ToInventorySiteLocationRef: ToInventorySiteLocationRef
    QuantityTransferred: QUANTYPE
    SerialNumber: STRTYPE
    LotNumber: STRTYPE


class TransferInventoryRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    FromInventorySiteRef: FromInventorySiteRef
    ToInventorySiteRef: ToInventorySiteRef
    Memo: STRTYPE
    ExternalGUID: GUIDTYPE
    TransferInventoryLineRet: Union[TransferInventoryLineRet, List[TransferInventoryLineRet]]


class TransferInventoryAddRs(TypedDict, total=False):
    TransferInventoryRet: TransferInventoryRet
    ErrorRecovery: ErrorRecovery


class DateDrivenTermsQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class DateDrivenTermsQueryRs(TypedDict, total=False):
    DateDrivenTermsRet: Union[DateDrivenTermsRet, List[DateDrivenTermsRet]]


class BillMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    VendorRef: VendorRef
    VendorAddress: VendorAddress
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    DueDate: DATETYPE
    RefNumber: STRTYPE
    TermsRef: TermsRef
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ClearExpenseLines: BOOLTYPE
    ExpenseLineMod: Union[ExpenseLineMod, List[ExpenseLineMod]]
    ClearItemLines: BOOLTYPE
    ItemLineMod: ItemLineMod
    ItemGroupLineMod: ItemGroupLineMod


class BillModRq(TypedDict, total=False):
    BillMod: BillMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BillModRs(TypedDict, total=False):
    BillRet: BillRet
    ErrorRecovery: ErrorRecovery


class BillToPayQueryRq(TypedDict, total=False):
    PayeeEntityRef: PayeeEntityRef
    APAccountRef: APAccountRef
    DueDate: DATETYPE
    CurrencyFilter: CurrencyFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BillToPay(TypedDict, total=False):
    TxnID: IDTYPE
    TxnType: TxnType
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    DueDate: DATETYPE
    AmountDue: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    AmountDueInHomeCurrency: AMTTYPE


class CreditToApply(TypedDict, total=False):
    TxnID: IDTYPE
    TxnType: TxnType
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    CreditRemaining: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    CreditRemainingInHomeCurrency: AMTTYPE


class BillToPayRet(TypedDict, total=False):
    BillToPay: BillToPay
    CreditToApply: CreditToApply


class BillToPayQueryRs(TypedDict, total=False):
    BillToPayRet: Union[BillToPayRet, List[BillToPayRet]]


class TransferQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TransferQueryRs(TypedDict, total=False):
    TransferRet: Union[TransferRet, List[TransferRet]]


class ARRefundCreditCardQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class RefundFromAccountRef(TypedDict, total=False):
    ListID: IDTYPE
    FullName: STRTYPE


class RefundAppliedToTxnRet(TypedDict, total=False):
    TxnID: IDTYPE
    TxnType: TxnType
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    CreditRemaining: AMTTYPE
    RefundAmount: AMTTYPE
    CreditRemainingInHomeCurrency: AMTTYPE
    RefundAmountInHomeCurrency: AMTTYPE


class ARRefundCreditCardRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    CustomerRef: CustomerRef
    RefundFromAccountRef: RefundFromAccountRef
    ARAccountRef: ARAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    TotalAmount: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    TotalAmountInHomeCurrency: AMTTYPE
    Address: Address
    AddressBlock: AddressBlock
    PaymentMethodRef: PaymentMethodRef
    Memo: STRTYPE
    CreditCardTxnInfo: CreditCardTxnInfo
    ExternalGUID: GUIDTYPE
    RefundAppliedToTxnRet: Union[RefundAppliedToTxnRet, List[RefundAppliedToTxnRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class ARRefundCreditCardQueryRs(TypedDict, total=False):
    ARRefundCreditCardRet: Union[ARRefundCreditCardRet, List[ARRefundCreditCardRet]]


class InvoiceQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    PaidStatus: PaidStatus
    IncludeLineItems: BOOLTYPE
    IncludeLinkedTxns: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class InvoiceLineRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    Other1: STRTYPE
    Other2: STRTYPE
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class InvoiceLineGroupRet(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    IsPrintItemsInGroup: BOOLTYPE
    TotalAmount: AMTTYPE
    InvoiceLineRet: Union[InvoiceLineRet, List[InvoiceLineRet]]
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class InvoiceRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    ARAccountRef: ARAccountRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    BillAddressBlock: BillAddressBlock
    ShipAddress: ShipAddress
    ShipAddressBlock: ShipAddressBlock
    IsPending: BOOLTYPE
    IsFinanceCharge: BOOLTYPE
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    Subtotal: AMTTYPE
    ItemSalesTaxRef: ItemSalesTaxRef
    SalesTaxPercentage: PERCENTTYPE
    SalesTaxTotal: AMTTYPE
    AppliedAmount: AMTTYPE
    BalanceRemaining: AMTTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    BalanceRemainingInHomeCurrency: AMTTYPE
    Memo: STRTYPE
    IsPaid: BOOLTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    SuggestedDiscountAmount: AMTTYPE
    SuggestedDiscountDate: DATETYPE
    Other: STRTYPE
    ExternalGUID: GUIDTYPE
    LinkedTxn: Union[LinkedTxn, List[LinkedTxn]]
    InvoiceLineRet: InvoiceLineRet
    InvoiceLineGroupRet: InvoiceLineGroupRet
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class InvoiceQueryRs(TypedDict, total=False):
    InvoiceRet: Union[InvoiceRet, List[InvoiceRet]]


class ItemAssembliesCanBuildQueryRq(TypedDict, total=False):
    ItemInventoryAssemblyRef: ItemInventoryAssemblyRef
    TxnDate: DATETYPE


class ItemAssembliesCanBuildRet(TypedDict, total=False):
    ItemInventoryAssemblyRef: ItemInventoryAssemblyRef
    TxnDate: DATETYPE
    QuantityCanBuild: QUANTYPE


class ItemAssembliesCanBuildQueryRs(TypedDict, total=False):
    ItemAssembliesCanBuildRet: ItemAssembliesCanBuildRet


class ItemFixedAssetAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    AcquiredAs: AcquiredAs
    PurchaseDesc: STRTYPE
    PurchaseDate: DATETYPE
    PurchaseCost: PRICETYPE
    VendorOrPayeeName: STRTYPE
    AssetAccountRef: AssetAccountRef
    FixedAssetSalesInfo: FixedAssetSalesInfo
    AssetDesc: STRTYPE
    Location: STRTYPE
    PONumber: STRTYPE
    SerialNumber: STRTYPE
    WarrantyExpDate: DATETYPE
    Notes: STRTYPE
    AssetNumber: STRTYPE
    CostBasis: AMTTYPE
    YearEndAccumulatedDepreciation: AMTTYPE
    YearEndBookValue: AMTTYPE
    ExternalGUID: GUIDTYPE


class ItemFixedAssetAddRq(TypedDict, total=False):
    ItemFixedAssetAdd: ItemFixedAssetAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemFixedAssetAddRs(TypedDict, total=False):
    ItemFixedAssetRet: ItemFixedAssetRet
    ErrorRecovery: ErrorRecovery


class CurrencyFormat(TypedDict, total=False):
    ThousandSeparator: ThousandSeparator
    ThousandSeparatorGrouping: ThousandSeparatorGrouping
    DecimalPlaces: DecimalPlaces
    DecimalSeparator: DecimalSeparator


class CurrencyAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    CurrencyCode: STRTYPE
    CurrencyFormat: CurrencyFormat


class CurrencyAddRq(TypedDict, total=False):
    CurrencyAdd: CurrencyAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CurrencyRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    CurrencyCode: STRTYPE
    CurrencyFormat: CurrencyFormat
    IsUserDefinedCurrency: BOOLTYPE
    ExchangeRate: FLOATTYPE
    AsOfDate: DATETYPE


class CurrencyAddRs(TypedDict, total=False):
    CurrencyRet: CurrencyRet
    ErrorRecovery: ErrorRecovery


class JournalDebitLine(TypedDict, total=False):
    TxnLineID: IDTYPE
    AccountRef: AccountRef
    Amount: AMTTYPE
    Memo: STRTYPE
    EntityRef: EntityRef
    ClassRef: ClassRef
    ItemSalesTaxRef: ItemSalesTaxRef
    BillableStatus: BillableStatus


class JournalCreditLine(TypedDict, total=False):
    TxnLineID: IDTYPE
    AccountRef: AccountRef
    Amount: AMTTYPE
    Memo: STRTYPE
    EntityRef: EntityRef
    ClassRef: ClassRef
    ItemSalesTaxRef: ItemSalesTaxRef
    BillableStatus: BillableStatus


class JournalEntryAdd(TypedDict, total=False):
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    IsAdjustment: BOOLTYPE
    IsHomeCurrencyAdjustment: BOOLTYPE
    IsAmountsEnteredInHomeCurrency: BOOLTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    JournalDebitLine: JournalDebitLine
    JournalCreditLine: JournalCreditLine


class JournalEntryAddRq(TypedDict, total=False):
    JournalEntryAdd: JournalEntryAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class JournalEntryRet(TypedDict, total=False):
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    TxnNumber: INTTYPE
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    IsAdjustment: BOOLTYPE
    IsHomeCurrencyAdjustment: BOOLTYPE
    IsAmountsEnteredInHomeCurrency: BOOLTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    JournalDebitLine: JournalDebitLine
    JournalCreditLine: JournalCreditLine
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class JournalEntryAddRs(TypedDict, total=False):
    JournalEntryRet: JournalEntryRet
    ErrorRecovery: ErrorRecovery


class LinkToTxn(TypedDict, total=False):
    TxnID: IDTYPE
    TxnLineID: IDTYPE


class InvoiceLineAdd(TypedDict, total=False):
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    PriceLevelRef: PriceLevelRef
    ClassRef: ClassRef
    Amount: AMTTYPE
    OptionForPriceRuleConflict: OptionForPriceRuleConflict
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    OverrideItemAccountRef: OverrideItemAccountRef
    Other1: STRTYPE
    Other2: STRTYPE
    LinkToTxn: LinkToTxn
    DataExt: Union[DataExt, List[DataExt]]


class InvoiceLineGroupAdd(TypedDict, total=False):
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    DataExt: Union[DataExt, List[DataExt]]


class InvoiceAdd(TypedDict, total=False):
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    ARAccountRef: ARAccountRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    ShipAddress: ShipAddress
    IsPending: BOOLTYPE
    IsFinanceCharge: BOOLTYPE
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    ItemSalesTaxRef: ItemSalesTaxRef
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    LinkToTxnID: Union[IDTYPE, List[IDTYPE]]
    SetCredit: Union[SetCredit, List[SetCredit]]
    InvoiceLineAdd: InvoiceLineAdd
    InvoiceLineGroupAdd: InvoiceLineGroupAdd


class InvoiceAddRq(TypedDict, total=False):
    InvoiceAdd: InvoiceAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class InvoiceAddRs(TypedDict, total=False):
    InvoiceRet: InvoiceRet
    ErrorRecovery: ErrorRecovery


class TransferInventoryQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    SiteFilter: SiteFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TransferInventoryQueryRs(TypedDict, total=False):
    TransferInventoryRet: Union[TransferInventoryRet, List[TransferInventoryRet]]


class ShipMethodQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ShipMethodQueryRs(TypedDict, total=False):
    ShipMethodRet: Union[ShipMethodRet, List[ShipMethodRet]]


class BuildAssemblyAdd(TypedDict, total=False):
    ItemInventoryAssemblyRef: ItemInventoryAssemblyRef
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    QuantityToBuild: QUANTYPE
    MarkPendingIfRequired: BOOLTYPE
    ExternalGUID: GUIDTYPE


class BuildAssemblyAddRq(TypedDict, total=False):
    BuildAssemblyAdd: BuildAssemblyAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BuildAssemblyAddRs(TypedDict, total=False):
    BuildAssemblyRet: BuildAssemblyRet
    ErrorRecovery: ErrorRecovery


class ItemInventoryAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    ManufacturerPartNumber: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesDesc: STRTYPE
    SalesPrice: PRICETYPE
    IncomeAccountRef: IncomeAccountRef
    PurchaseDesc: STRTYPE
    PurchaseCost: PRICETYPE
    PurchaseTaxCodeRef: PurchaseTaxCodeRef
    COGSAccountRef: COGSAccountRef
    PrefVendorRef: PrefVendorRef
    AssetAccountRef: AssetAccountRef
    ReorderPoint: QUANTYPE
    Max: QUANTYPE
    QuantityOnHand: QUANTYPE
    TotalValue: AMTTYPE
    InventoryDate: DATETYPE
    ExternalGUID: GUIDTYPE


class ItemInventoryAddRq(TypedDict, total=False):
    ItemInventoryAdd: ItemInventoryAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemInventoryAddRs(TypedDict, total=False):
    ItemInventoryRet: ItemInventoryRet
    ErrorRecovery: ErrorRecovery


class OtherNameQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class OtherNameQueryRs(TypedDict, total=False):
    OtherNameRet: Union[OtherNameRet, List[OtherNameRet]]


class JobTypeQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class JobTypeQueryRs(TypedDict, total=False):
    JobTypeRet: Union[JobTypeRet, List[JobTypeRet]]


class DataExtDefMod(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtName: STRTYPE
    DataExtNewName: STRTYPE
    AssignToObject: Union[AssignToObject, List[AssignToObject]]
    RemoveFromObject: Union[RemoveFromObject, List[RemoveFromObject]]
    DataExtListRequire: BOOLTYPE
    DataExtTxnRequire: BOOLTYPE
    DataExtFormatString: STRTYPE


class DataExtDefModRq(TypedDict, total=False):
    DataExtDefMod: DataExtDefMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class DataExtDefModRs(TypedDict, total=False):
    DataExtDefRet: DataExtDefRet
    ErrorRecovery: ErrorRecovery


class ItemServiceQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemServiceQueryRs(TypedDict, total=False):
    ItemServiceRet: Union[ItemServiceRet, List[ItemServiceRet]]


class OtherNameMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    CompanyName: STRTYPE
    Salutation: STRTYPE
    FirstName: STRTYPE
    MiddleName: STRTYPE
    LastName: STRTYPE
    OtherNameAddress: OtherNameAddress
    Phone: STRTYPE
    AltPhone: STRTYPE
    Fax: STRTYPE
    Email: STRTYPE
    Contact: STRTYPE
    AltContact: STRTYPE
    AccountNumber: STRTYPE
    Notes: STRTYPE


class OtherNameModRq(TypedDict, total=False):
    OtherNameMod: OtherNameMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class OtherNameModRs(TypedDict, total=False):
    OtherNameRet: OtherNameRet
    ErrorRecovery: ErrorRecovery


class ClassMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef


class ClassModRq(TypedDict, total=False):
    ClassMod: ClassMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ClassModRs(TypedDict, total=False):
    ClassRet: ClassRet
    ErrorRecovery: ErrorRecovery


class ToDoMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Notes: STRTYPE
    IsActive: BOOLTYPE
    Type: Type
    Priority: Priority
    CustomerRef: CustomerRef
    EmployeeRef: EmployeeRef
    LeadRef: LeadRef
    VendorRef: VendorRef
    IsDone: BOOLTYPE
    ReminderDate: DATETYPE
    ReminderTime: TIMEINTERVALTYPE


class ToDoModRq(TypedDict, total=False):
    ToDoMod: ToDoMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ToDoModRs(TypedDict, total=False):
    ToDoRet: ToDoRet
    ErrorRecovery: ErrorRecovery


class ChargeAdd(TypedDict, total=False):
    CustomerRef: CustomerRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    ItemRef: ItemRef
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    Rate: PRICETYPE
    OptionForPriceRuleConflict: OptionForPriceRuleConflict
    Amount: AMTTYPE
    Desc: STRTYPE
    ARAccountRef: ARAccountRef
    ClassRef: ClassRef
    BilledDate: DATETYPE
    DueDate: DATETYPE
    OverrideItemAccountRef: OverrideItemAccountRef
    ExternalGUID: GUIDTYPE


class ChargeAddRq(TypedDict, total=False):
    ChargeAdd: ChargeAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ChargeAddRs(TypedDict, total=False):
    ChargeRet: ChargeRet
    ErrorRecovery: ErrorRecovery


class TimeReportQueryRq(TypedDict, total=False):
    TimeReportType: TimeReportType
    DisplayReport: BOOLTYPE
    ReportPeriod: ReportPeriod
    ReportDateMacro: ReportDateMacro
    ReportEntityFilter: ReportEntityFilter
    ReportItemFilter: ReportItemFilter
    ReportClassFilter: ReportClassFilter
    SummarizeColumnsBy: SummarizeColumnsBy
    IncludeColumn: Union[IncludeColumn, List[IncludeColumn]]
    IncludeSubcolumns: BOOLTYPE
    ReportCalendar: ReportCalendar
    ReturnRows: ReturnRows
    ReturnColumns: ReturnColumns


class TimeTrackingAdd(TypedDict, total=False):
    TxnDate: DATETYPE
    EntityRef: EntityRef
    CustomerRef: CustomerRef
    ItemServiceRef: ItemServiceRef
    Duration: TIMEINTERVALTYPE
    ClassRef: ClassRef
    PayrollItemWageRef: PayrollItemWageRef
    Notes: STRTYPE
    BillableStatus: BillableStatus
    IsBillable: BOOLTYPE
    ExternalGUID: GUIDTYPE


class TimeTrackingAddRq(TypedDict, total=False):
    TimeTrackingAdd: TimeTrackingAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TimeTrackingAddRs(TypedDict, total=False):
    TimeTrackingRet: TimeTrackingRet
    ErrorRecovery: ErrorRecovery


class ItemSubtotalMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ItemDesc: STRTYPE


class ItemSubtotalModRq(TypedDict, total=False):
    ItemSubtotalMod: ItemSubtotalMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemSubtotalModRs(TypedDict, total=False):
    ItemSubtotalRet: ItemSubtotalRet
    ErrorRecovery: ErrorRecovery


class SalesTaxPaymentCheckLineAdd(TypedDict, total=False):
    ItemSalesTaxRef: ItemSalesTaxRef
    Amount: AMTTYPE


class SalesTaxPaymentCheckAdd(TypedDict, total=False):
    PayeeEntityRef: PayeeEntityRef
    TxnDate: DATETYPE
    BankAccountRef: BankAccountRef
    IsToBePrinted: BOOLTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    Address: Address
    ExternalGUID: GUIDTYPE
    SalesTaxPaymentCheckLineAdd: Union[SalesTaxPaymentCheckLineAdd, List[SalesTaxPaymentCheckLineAdd]]


class SalesTaxPaymentCheckAddRq(TypedDict, total=False):
    SalesTaxPaymentCheckAdd: SalesTaxPaymentCheckAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesTaxPaymentCheckAddRs(TypedDict, total=False):
    SalesTaxPaymentCheckRet: SalesTaxPaymentCheckRet
    ErrorRecovery: ErrorRecovery


class BarCodeQueryRq(TypedDict, total=False):
    BarCodeValue: Union[STRTYPE, List[STRTYPE]]


class BarCodeRet(TypedDict, total=False):
    ListType: ListType
    ListID: IDTYPE
    FullName: STRTYPE


class BarCodeQueryRs(TypedDict, total=False):
    BarCodeRet: Union[BarCodeRet, List[BarCodeRet]]


class TransferMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    TxnDate: DATETYPE
    TransferFromAccountRef: TransferFromAccountRef
    TransferToAccountRef: TransferToAccountRef
    ClassRef: ClassRef
    Amount: AMTTYPE
    Memo: STRTYPE


class TransferModRq(TypedDict, total=False):
    TransferMod: TransferMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TransferModRs(TypedDict, total=False):
    TransferRet: TransferRet


class PayrollItemWageQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class PayrollItemWageRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    WageType: WageType
    ExpenseAccountRef: ExpenseAccountRef


class PayrollItemWageQueryRs(TypedDict, total=False):
    PayrollItemWageRet: Union[PayrollItemWageRet, List[PayrollItemWageRet]]


class ItemInventoryQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemInventoryQueryRs(TypedDict, total=False):
    ItemInventoryRet: Union[ItemInventoryRet, List[ItemInventoryRet]]


class EstimateQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeLinkedTxns: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class EstimateQueryRs(TypedDict, total=False):
    EstimateRet: Union[EstimateRet, List[EstimateRet]]


class PurchaseOrderLineAdd(TypedDict, total=False):
    ItemRef: ItemRef
    ManufacturerPartNumber: STRTYPE
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    Rate: PRICETYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    InventorySiteLocationRef: InventorySiteLocationRef
    CustomerRef: CustomerRef
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    OverrideItemAccountRef: OverrideItemAccountRef
    Other1: STRTYPE
    Other2: STRTYPE
    DataExt: Union[DataExt, List[DataExt]]


class PurchaseOrderLineGroupAdd(TypedDict, total=False):
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    InventorySiteLocationRef: InventorySiteLocationRef
    DataExt: Union[DataExt, List[DataExt]]


class PurchaseOrderAdd(TypedDict, total=False):
    VendorRef: VendorRef
    ClassRef: ClassRef
    InventorySiteRef: InventorySiteRef
    ShipToEntityRef: ShipToEntityRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    VendorAddress: VendorAddress
    ShipAddress: ShipAddress
    TermsRef: TermsRef
    DueDate: DATETYPE
    ExpectedDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    FOB: STRTYPE
    Memo: STRTYPE
    VendorMsg: STRTYPE
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    Other1: STRTYPE
    Other2: STRTYPE
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    PurchaseOrderLineAdd: PurchaseOrderLineAdd
    PurchaseOrderLineGroupAdd: PurchaseOrderLineGroupAdd


class PurchaseOrderAddRq(TypedDict, total=False):
    PurchaseOrderAdd: PurchaseOrderAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class PurchaseOrderAddRs(TypedDict, total=False):
    PurchaseOrderRet: PurchaseOrderRet
    ErrorRecovery: ErrorRecovery


class UnitOfMeasureSetAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    UnitOfMeasureType: UnitOfMeasureType
    BaseUnit: BaseUnit
    RelatedUnit: Union[RelatedUnit, List[RelatedUnit]]
    DefaultUnit: Union[DefaultUnit, List[DefaultUnit]]


class UnitOfMeasureSetAddRq(TypedDict, total=False):
    UnitOfMeasureSetAdd: UnitOfMeasureSetAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class UnitOfMeasureSetAddRs(TypedDict, total=False):
    UnitOfMeasureSetRet: UnitOfMeasureSetRet
    ErrorRecovery: ErrorRecovery


class CreditCardChargeQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class CreditCardChargeQueryRs(TypedDict, total=False):
    CreditCardChargeRet: Union[CreditCardChargeRet, List[CreditCardChargeRet]]


class PurchaseOrderQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeLinkedTxns: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class PurchaseOrderQueryRs(TypedDict, total=False):
    PurchaseOrderRet: Union[PurchaseOrderRet, List[PurchaseOrderRet]]


class CreditCardCreditQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class CreditCardCreditQueryRs(TypedDict, total=False):
    CreditCardCreditRet: Union[CreditCardCreditRet, List[CreditCardCreditRet]]


class MergeFrom(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE


class MergeTo(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE


class ListMergeRq(TypedDict, total=False):
    ListMergeType: ListMergeType
    MergeFrom: MergeFrom
    MergeTo: MergeTo
    SameShipAddrOk: BOOLTYPE


class MergedFrom(TypedDict, total=False):
    ListID: IDTYPE
    TimeDeleted: DATETIMETYPE
    FullName: STRTYPE


class MergedTo(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    FullName: STRTYPE


class ListMergeRs(TypedDict, total=False):
    ListMergeType: ListMergeType
    MergedFrom: MergedFrom
    MergedTo: MergedTo


class ApplyCheckToTxnMod(TypedDict, total=False):
    TxnID: IDTYPE
    Amount: AMTTYPE


class CheckMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    AccountRef: AccountRef
    PayeeEntityRef: PayeeEntityRef
    RefNumber: STRTYPE
    TxnDate: DATETYPE
    Memo: STRTYPE
    Address: Address
    IsToBePrinted: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ApplyCheckToTxnMod: Union[ApplyCheckToTxnMod, List[ApplyCheckToTxnMod]]
    ClearExpenseLines: BOOLTYPE
    ExpenseLineMod: Union[ExpenseLineMod, List[ExpenseLineMod]]
    ClearItemLines: BOOLTYPE
    ItemLineMod: ItemLineMod
    ItemGroupLineMod: ItemGroupLineMod


class CheckModRq(TypedDict, total=False):
    CheckMod: CheckMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CheckModRs(TypedDict, total=False):
    CheckRet: CheckRet
    ErrorRecovery: ErrorRecovery


class PayrollItemWageAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    WageType: WageType
    ExpenseAccountRef: ExpenseAccountRef


class PayrollItemWageAddRq(TypedDict, total=False):
    PayrollItemWageAdd: PayrollItemWageAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class PayrollItemWageAddRs(TypedDict, total=False):
    PayrollItemWageRet: PayrollItemWageRet


class EstimateLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    ClassRef: ClassRef
    Amount: AMTTYPE
    OptionForPriceRuleConflict: OptionForPriceRuleConflict
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SalesTaxCodeRef: SalesTaxCodeRef
    MarkupRate: PRICETYPE
    MarkupRatePercent: PERCENTTYPE
    PriceLevelRef: PriceLevelRef
    Other1: STRTYPE
    Other2: STRTYPE


class EstimateLineGroupMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    EstimateLineMod: Union[EstimateLineMod, List[EstimateLineMod]]


class EstimateMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    ShipAddress: ShipAddress
    IsActive: BOOLTYPE
    CreateChangeOrder: BOOLTYPE
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ItemSalesTaxRef: ItemSalesTaxRef
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExchangeRate: FLOATTYPE
    EstimateLineMod: EstimateLineMod
    EstimateLineGroupMod: EstimateLineGroupMod


class EstimateModRq(TypedDict, total=False):
    EstimateMod: EstimateMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class EstimateModRs(TypedDict, total=False):
    EstimateRet: EstimateRet
    ErrorRecovery: ErrorRecovery


class DataEventRecoveryInfoDelRq(TypedDict, total=False):
    SubscriberID: GUIDTYPE


class IncludeListMetaData(TypedDict, total=False):
    IncludeMaxCapacity: BOOLTYPE


class HostQueryRq(TypedDict, total=False):
    IncludeListMetaData: IncludeListMetaData
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class AccountMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class BillingRateMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class ClassMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class CustomerMsgMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class CustomerTypeMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class EntityMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class ItemMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class JobTypeMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class PaymentMethodMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class PayrollItemMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class PriceLevelMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class SalesRepMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class SalesTaxCodeMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class ShipMethodMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class TemplateMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class TermsMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class ToDoMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class VehicleMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class VendorTypeMetaData(TypedDict, total=False):
    MaxCapacity: INTTYPE


class ListMetaData(TypedDict, total=False):
    AccountMetaData: AccountMetaData
    BillingRateMetaData: BillingRateMetaData
    ClassMetaData: ClassMetaData
    CustomerMsgMetaData: CustomerMsgMetaData
    CustomerTypeMetaData: CustomerTypeMetaData
    EntityMetaData: EntityMetaData
    ItemMetaData: ItemMetaData
    JobTypeMetaData: JobTypeMetaData
    PaymentMethodMetaData: PaymentMethodMetaData
    PayrollItemMetaData: PayrollItemMetaData
    PriceLevelMetaData: PriceLevelMetaData
    SalesRepMetaData: SalesRepMetaData
    SalesTaxCodeMetaData: SalesTaxCodeMetaData
    ShipMethodMetaData: ShipMethodMetaData
    TemplateMetaData: TemplateMetaData
    TermsMetaData: TermsMetaData
    ToDoMetaData: ToDoMetaData
    VehicleMetaData: VehicleMetaData
    VendorTypeMetaData: VendorTypeMetaData


class HostRet(TypedDict, total=False):
    ProductName: STRTYPE
    MajorVersion: STRTYPE
    MinorVersion: STRTYPE
    Country: STRTYPE
    SupportedQBXMLVersion: Union[STRTYPE, List[STRTYPE]]
    IsAutomaticLogin: BOOLTYPE
    QBFileMode: QBFileMode
    ListMetaData: ListMetaData


class HostQueryRs(TypedDict, total=False):
    HostRet: HostRet


class BudgetSummaryReportQueryRq(TypedDict, total=False):
    BudgetSummaryReportType: BudgetSummaryReportType
    DisplayReport: BOOLTYPE
    FiscalYear: INTTYPE
    BudgetCriterion: BudgetCriterion
    ReportPeriod: ReportPeriod
    ReportDateMacro: ReportDateMacro
    ReportClassFilter: ReportClassFilter
    SummarizeBudgetColumnsBy: SummarizeBudgetColumnsBy
    SummarizeBudgetRowsBy: SummarizeBudgetRowsBy


class VendorTypeAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef


class VendorTypeAddRq(TypedDict, total=False):
    VendorTypeAdd: VendorTypeAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class VendorTypeAddRs(TypedDict, total=False):
    VendorTypeRet: VendorTypeRet
    ErrorRecovery: ErrorRecovery


class SalesOrderLineAdd(TypedDict, total=False):
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    PriceLevelRef: PriceLevelRef
    ClassRef: ClassRef
    Amount: AMTTYPE
    OptionForPriceRuleConflict: OptionForPriceRuleConflict
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    IsManuallyClosed: BOOLTYPE
    Other1: STRTYPE
    Other2: STRTYPE
    DataExt: Union[DataExt, List[DataExt]]


class SalesOrderLineGroupAdd(TypedDict, total=False):
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    DataExt: Union[DataExt, List[DataExt]]


class SalesOrderAdd(TypedDict, total=False):
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    ShipAddress: ShipAddress
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    ItemSalesTaxRef: ItemSalesTaxRef
    IsManuallyClosed: BOOLTYPE
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    SalesOrderLineAdd: SalesOrderLineAdd
    SalesOrderLineGroupAdd: SalesOrderLineGroupAdd


class SalesOrderAddRq(TypedDict, total=False):
    SalesOrderAdd: SalesOrderAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesOrderAddRs(TypedDict, total=False):
    SalesOrderRet: SalesOrderRet
    ErrorRecovery: ErrorRecovery


class VehicleAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    Desc: STRTYPE


class VehicleAddRq(TypedDict, total=False):
    VehicleAdd: VehicleAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class VehicleAddRs(TypedDict, total=False):
    VehicleRet: VehicleRet
    ErrorRecovery: ErrorRecovery


class ItemSalesTaxGroupQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemSalesTaxGroupQueryRs(TypedDict, total=False):
    ItemSalesTaxGroupRet: Union[ItemSalesTaxGroupRet, List[ItemSalesTaxGroupRet]]


class ItemPaymentQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemPaymentQueryRs(TypedDict, total=False):
    ItemPaymentRet: Union[ItemPaymentRet, List[ItemPaymentRet]]


class ItemGroupMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ItemDesc: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    ForceUOMChange: BOOLTYPE
    IsPrintItemsInGroup: BOOLTYPE
    ClearItemsInGroup: BOOLTYPE
    ItemGroupLine: Union[ItemGroupLine, List[ItemGroupLine]]


class ItemGroupModRq(TypedDict, total=False):
    ItemGroupMod: ItemGroupMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemGroupModRs(TypedDict, total=False):
    ItemGroupRet: ItemGroupRet
    ErrorRecovery: ErrorRecovery


class EntityQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class WorkersCompCodeMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    Desc: STRTYPE
    RateEntry: Union[RateEntry, List[RateEntry]]


class WorkersCompCodeModRq(TypedDict, total=False):
    WorkersCompCodeMod: WorkersCompCodeMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class WorkersCompCodeModRs(TypedDict, total=False):
    WorkersCompCodeRet: WorkersCompCodeRet
    ErrorRecovery: ErrorRecovery


class CompanyActivityQueryRq(TypedDict, total=False):
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CompanyActivityRet(TypedDict, total=False):
    LastRestoreTime: DATETIMETYPE
    LastCondenseTime: DATETIMETYPE


class CompanyActivityQueryRs(TypedDict, total=False):
    CompanyActivityRet: CompanyActivityRet


class PaymentMethodAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    PaymentMethodType: PaymentMethodType


class PaymentMethodAddRq(TypedDict, total=False):
    PaymentMethodAdd: PaymentMethodAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class PaymentMethodRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    PaymentMethodType: PaymentMethodType


class PaymentMethodAddRs(TypedDict, total=False):
    PaymentMethodRet: PaymentMethodRet
    ErrorRecovery: ErrorRecovery


class InventoryAdjustmentLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    CountAdjustment: INTTYPE
    InventorySiteLocationRef: InventorySiteLocationRef
    QuantityDifference: QUANTYPE
    ValueDifference: AMTTYPE


class InventoryAdjustmentMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    AccountRef: AccountRef
    InventorySiteRef: InventorySiteRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    Memo: STRTYPE
    InventoryAdjustmentLineMod: Union[InventoryAdjustmentLineMod, List[InventoryAdjustmentLineMod]]


class InventoryAdjustmentModRq(TypedDict, total=False):
    InventoryAdjustmentMod: InventoryAdjustmentMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class InventoryAdjustmentModRs(TypedDict, total=False):
    InventoryAdjustmentRet: InventoryAdjustmentRet
    ErrorRecovery: ErrorRecovery


class ItemServiceMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    ForceUOMChange: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesOrPurchaseMod: SalesOrPurchaseMod
    SalesAndPurchaseMod: SalesAndPurchaseMod


class ItemServiceModRq(TypedDict, total=False):
    ItemServiceMod: ItemServiceMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemServiceModRs(TypedDict, total=False):
    ItemServiceRet: ItemServiceRet
    ErrorRecovery: ErrorRecovery


class BillPaymentCreditCardAdd(TypedDict, total=False):
    PayeeEntityRef: PayeeEntityRef
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    CreditCardAccountRef: CreditCardAccountRef
    RefNumber: STRTYPE
    Memo: STRTYPE
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    AppliedToTxnAdd: Union[AppliedToTxnAdd, List[AppliedToTxnAdd]]


class BillPaymentCreditCardAddRq(TypedDict, total=False):
    BillPaymentCreditCardAdd: BillPaymentCreditCardAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BillPaymentCreditCardAddRs(TypedDict, total=False):
    BillPaymentCreditCardRet: BillPaymentCreditCardRet
    ErrorRecovery: ErrorRecovery


class SalesReceiptLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    PriceLevelRef: PriceLevelRef
    ClassRef: ClassRef
    Amount: AMTTYPE
    OptionForPriceRuleConflict: OptionForPriceRuleConflict
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    OverrideItemAccountRef: OverrideItemAccountRef
    Other1: STRTYPE
    Other2: STRTYPE


class SalesReceiptLineGroupMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    SalesReceiptLineMod: Union[SalesReceiptLineMod, List[SalesReceiptLineMod]]


class SalesReceiptMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    ShipAddress: ShipAddress
    IsPending: BOOLTYPE
    CheckNumber: STRTYPE
    PaymentMethodRef: PaymentMethodRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    FOB: STRTYPE
    ItemSalesTaxRef: ItemSalesTaxRef
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    DepositToAccountRef: DepositToAccountRef
    Other: STRTYPE
    ExchangeRate: FLOATTYPE
    SalesReceiptLineMod: SalesReceiptLineMod
    SalesReceiptLineGroupMod: SalesReceiptLineGroupMod


class SalesReceiptModRq(TypedDict, total=False):
    SalesReceiptMod: SalesReceiptMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesReceiptModRs(TypedDict, total=False):
    SalesReceiptRet: SalesReceiptRet
    ErrorRecovery: ErrorRecovery


class CustomerTypeAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef


class CustomerTypeAddRq(TypedDict, total=False):
    CustomerTypeAdd: CustomerTypeAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CustomerTypeRet(TypedDict, total=False):
    ListID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    FullName: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef
    Sublevel: INTTYPE


class CustomerTypeAddRs(TypedDict, total=False):
    CustomerTypeRet: CustomerTypeRet
    ErrorRecovery: ErrorRecovery


class CreditCardChargeMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    AccountRef: AccountRef
    PayeeEntityRef: PayeeEntityRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ClearExpenseLines: BOOLTYPE
    ExpenseLineMod: Union[ExpenseLineMod, List[ExpenseLineMod]]
    ClearItemLines: BOOLTYPE
    ItemLineMod: ItemLineMod
    ItemGroupLineMod: ItemGroupLineMod


class CreditCardChargeModRq(TypedDict, total=False):
    CreditCardChargeMod: CreditCardChargeMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CreditCardChargeModRs(TypedDict, total=False):
    CreditCardChargeRet: CreditCardChargeRet
    ErrorRecovery: ErrorRecovery


class ItemDiscountAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    ItemDesc: STRTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    DiscountRate: PRICETYPE
    DiscountRatePercent: PERCENTTYPE
    AccountRef: AccountRef
    ExternalGUID: GUIDTYPE


class ItemDiscountAddRq(TypedDict, total=False):
    ItemDiscountAdd: ItemDiscountAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemDiscountAddRs(TypedDict, total=False):
    ItemDiscountRet: ItemDiscountRet
    ErrorRecovery: ErrorRecovery


class SalesTaxCodeAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    IsTaxable: BOOLTYPE
    Desc: STRTYPE
    ItemPurchaseTaxRef: ItemPurchaseTaxRef
    ItemSalesTaxRef: ItemSalesTaxRef


class SalesTaxCodeAddRq(TypedDict, total=False):
    SalesTaxCodeAdd: SalesTaxCodeAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesTaxCodeAddRs(TypedDict, total=False):
    SalesTaxCodeRet: SalesTaxCodeRet
    ErrorRecovery: ErrorRecovery


class CreditMemoLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    PriceLevelRef: PriceLevelRef
    ClassRef: ClassRef
    Amount: AMTTYPE
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    OverrideItemAccountRef: OverrideItemAccountRef
    Other1: STRTYPE
    Other2: STRTYPE


class CreditMemoLineGroupMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    CreditMemoLineMod: Union[CreditMemoLineMod, List[CreditMemoLineMod]]


class CreditMemoMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    ARAccountRef: ARAccountRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    ShipAddress: ShipAddress
    IsPending: BOOLTYPE
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    ItemSalesTaxRef: ItemSalesTaxRef
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExchangeRate: FLOATTYPE
    CreditMemoLineMod: CreditMemoLineMod
    CreditMemoLineGroupMod: CreditMemoLineGroupMod


class CreditMemoModRq(TypedDict, total=False):
    CreditMemoMod: CreditMemoMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CreditMemoModRs(TypedDict, total=False):
    CreditMemoRet: CreditMemoRet
    ErrorRecovery: ErrorRecovery


class ItemReceiptAdd(TypedDict, total=False):
    VendorRef: VendorRef
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    LinkToTxnID: Union[IDTYPE, List[IDTYPE]]
    ExpenseLineAdd: Union[ExpenseLineAdd, List[ExpenseLineAdd]]
    ItemLineAdd: ItemLineAdd
    ItemGroupLineAdd: ItemGroupLineAdd


class ItemReceiptAddRq(TypedDict, total=False):
    ItemReceiptAdd: ItemReceiptAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemReceiptAddRs(TypedDict, total=False):
    ItemReceiptRet: ItemReceiptRet
    ErrorRecovery: ErrorRecovery


class ItemOtherChargeMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesOrPurchaseMod: SalesOrPurchaseMod
    SalesAndPurchaseMod: SalesAndPurchaseMod


class ItemOtherChargeModRq(TypedDict, total=False):
    ItemOtherChargeMod: ItemOtherChargeMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemOtherChargeModRs(TypedDict, total=False):
    ItemOtherChargeRet: ItemOtherChargeRet
    ErrorRecovery: ErrorRecovery


class ItemNonInventoryAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ParentRef: ParentRef
    ClassRef: ClassRef
    ManufacturerPartNumber: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesOrPurchase: SalesOrPurchase
    SalesAndPurchase: SalesAndPurchase
    ExternalGUID: GUIDTYPE


class ItemNonInventoryAddRq(TypedDict, total=False):
    ItemNonInventoryAdd: ItemNonInventoryAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemNonInventoryAddRs(TypedDict, total=False):
    ItemNonInventoryRet: ItemNonInventoryRet
    ErrorRecovery: ErrorRecovery


class ItemSalesTaxGroupMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ItemDesc: STRTYPE
    ItemSalesTaxRef: Union[ItemSalesTaxRef, List[ItemSalesTaxRef]]


class ItemSalesTaxGroupModRq(TypedDict, total=False):
    ItemSalesTaxGroupMod: ItemSalesTaxGroupMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemSalesTaxGroupModRs(TypedDict, total=False):
    ItemSalesTaxGroupRet: ItemSalesTaxGroupRet
    ErrorRecovery: ErrorRecovery


class ListDisplayModRq(TypedDict, total=False):
    ListDisplayModType: ListDisplayModType
    ListID: IDTYPE


class TotalBalanceFilter(TypedDict, total=False):
    Operator: Operator
    Amount: AMTTYPE


class VendorQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    TotalBalanceFilter: TotalBalanceFilter
    CurrencyFilter: CurrencyFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class CreditCardTxnInputInfoMod(TypedDict, total=False):
    CreditCardNumber: STRTYPE
    ExpirationMonth: INTTYPE
    ExpirationYear: INTTYPE
    NameOnCard: STRTYPE
    CreditCardAddress: STRTYPE
    CreditCardPostalCode: STRTYPE
    CommercialCardCode: STRTYPE
    TransactionMode: TransactionMode
    CreditCardTxnType: CreditCardTxnType


class CreditCardTxnResultInfoMod(TypedDict, total=False):
    ResultCode: INTTYPE
    ResultMessage: STRTYPE
    CreditCardTransID: STRTYPE
    MerchantAccountNumber: STRTYPE
    AuthorizationCode: STRTYPE
    AVSStreet: AVSStreet
    AVSZip: AVSZip
    CardSecurityCodeMatch: CardSecurityCodeMatch
    ReconBatchID: STRTYPE
    PaymentGroupingCode: INTTYPE
    PaymentStatus: PaymentStatus
    TxnAuthorizationTime: DATETIMETYPE
    TxnAuthorizationStamp: INTTYPE
    ClientTransID: STRTYPE


class CreditCardTxnInfoMod(TypedDict, total=False):
    CreditCardTxnInputInfoMod: CreditCardTxnInputInfoMod
    CreditCardTxnResultInfoMod: CreditCardTxnResultInfoMod


class AppliedToTxnMod(TypedDict, total=False):
    TxnID: IDTYPE
    PaymentAmount: AMTTYPE
    SetCredit: Union[SetCredit, List[SetCredit]]
    DiscountAmount: AMTTYPE
    DiscountAccountRef: DiscountAccountRef
    DiscountClassRef: DiscountClassRef


class ReceivePaymentMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    CustomerRef: CustomerRef
    ARAccountRef: ARAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    TotalAmount: AMTTYPE
    ExchangeRate: FLOATTYPE
    PaymentMethodRef: PaymentMethodRef
    Memo: STRTYPE
    DepositToAccountRef: DepositToAccountRef
    CreditCardTxnInfoMod: CreditCardTxnInfoMod
    AppliedToTxnMod: Union[AppliedToTxnMod, List[AppliedToTxnMod]]


class ReceivePaymentModRq(TypedDict, total=False):
    ReceivePaymentMod: ReceivePaymentMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ReceivePaymentModRs(TypedDict, total=False):
    ReceivePaymentRet: ReceivePaymentRet
    ErrorRecovery: ErrorRecovery


class ItemOtherChargeQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemOtherChargeQueryRs(TypedDict, total=False):
    ItemOtherChargeRet: Union[ItemOtherChargeRet, List[ItemOtherChargeRet]]


class VehicleMileageQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class VehicleMileageQueryRs(TypedDict, total=False):
    VehicleMileageRet: Union[VehicleMileageRet, List[VehicleMileageRet]]


class DataExtDel(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtName: STRTYPE
    ListDataExtType: ListDataExtType
    ListObjRef: ListObjRef
    TxnDataExtType: TxnDataExtType
    TxnID: IDTYPE
    TxnLineID: IDTYPE
    OtherDataExtType: OtherDataExtType


class DataExtDelRq(TypedDict, total=False):
    DataExtDel: DataExtDel


class DataExtDelRet(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtName: STRTYPE
    ListDataExtType: ListDataExtType
    ListObjRef: ListObjRef
    TxnDataExtType: TxnDataExtType
    TxnID: IDTYPE
    TxnLineID: IDTYPE
    OtherDataExtType: OtherDataExtType
    TimeDeleted: DATETIMETYPE


class DataExtDelRs(TypedDict, total=False):
    DataExtDelRet: DataExtDelRet
    ErrorRecovery: ErrorRecovery


class AgingReportQueryRq(TypedDict, total=False):
    AgingReportType: AgingReportType
    DisplayReport: BOOLTYPE
    ReportPeriod: ReportPeriod
    ReportDateMacro: ReportDateMacro
    ReportAccountFilter: ReportAccountFilter
    ReportEntityFilter: ReportEntityFilter
    ReportItemFilter: ReportItemFilter
    ReportClassFilter: ReportClassFilter
    ReportTxnTypeFilter: ReportTxnTypeFilter
    ReportModifiedDateRangeFilter: ReportModifiedDateRangeFilter
    ReportModifiedDateRangeMacro: ReportModifiedDateRangeMacro
    ReportDetailLevelFilter: ReportDetailLevelFilter
    ReportPostingStatusFilter: ReportPostingStatusFilter
    IncludeColumn: Union[IncludeColumn, List[IncludeColumn]]
    IncludeAccounts: IncludeAccounts
    ReportAgingAsOf: ReportAgingAsOf


class PaymentMethodQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    PaymentMethodType: Union[PaymentMethodType, List[PaymentMethodType]]
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class PaymentMethodQueryRs(TypedDict, total=False):
    PaymentMethodRet: Union[PaymentMethodRet, List[PaymentMethodRet]]


class CurrencyQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CurrencyQueryRs(TypedDict, total=False):
    CurrencyRet: Union[CurrencyRet, List[CurrencyRet]]


class AccountAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    ParentRef: ParentRef
    AccountType: AccountType
    AccountNumber: STRTYPE
    BankNumber: STRTYPE
    Desc: STRTYPE
    OpenBalance: AMTTYPE
    OpenBalanceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    TaxLineID: INTTYPE
    CurrencyRef: CurrencyRef


class AccountAddRq(TypedDict, total=False):
    AccountAdd: AccountAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class AccountAddRs(TypedDict, total=False):
    AccountRet: AccountRet
    ErrorRecovery: ErrorRecovery


class VendorCreditAdd(TypedDict, total=False):
    VendorRef: VendorRef
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    ExpenseLineAdd: Union[ExpenseLineAdd, List[ExpenseLineAdd]]
    ItemLineAdd: ItemLineAdd
    ItemGroupLineAdd: ItemGroupLineAdd


class VendorCreditAddRq(TypedDict, total=False):
    VendorCreditAdd: VendorCreditAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class VendorCreditAddRs(TypedDict, total=False):
    VendorCreditRet: VendorCreditRet
    ErrorRecovery: ErrorRecovery


class ItemInventoryAssemblyMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ParentRef: ParentRef
    ManufacturerPartNumber: STRTYPE
    UnitOfMeasureSetRef: UnitOfMeasureSetRef
    ForceUOMChange: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    SalesDesc: STRTYPE
    SalesPrice: PRICETYPE
    IncomeAccountRef: IncomeAccountRef
    ApplyIncomeAccountRefToExistingTxns: BOOLTYPE
    PurchaseDesc: STRTYPE
    PurchaseCost: PRICETYPE
    PurchaseTaxCodeRef: PurchaseTaxCodeRef
    COGSAccountRef: COGSAccountRef
    PrefVendorRef: PrefVendorRef
    AssetAccountRef: AssetAccountRef
    BuildPoint: QUANTYPE
    Max: QUANTYPE
    ClearItemsInGroup: BOOLTYPE
    ItemInventoryAssemblyLine: Union[ItemInventoryAssemblyLine, List[ItemInventoryAssemblyLine]]


class ItemInventoryAssemblyModRq(TypedDict, total=False):
    ItemInventoryAssemblyMod: ItemInventoryAssemblyMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemInventoryAssemblyModRs(TypedDict, total=False):
    ItemInventoryAssemblyRet: ItemInventoryAssemblyRet
    ErrorRecovery: ErrorRecovery


class CustomerQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    TotalBalanceFilter: TotalBalanceFilter
    CurrencyFilter: CurrencyFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class CheckQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeLinkedTxns: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class CheckQueryRs(TypedDict, total=False):
    CheckRet: Union[CheckRet, List[CheckRet]]


class DepositQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class DepositQueryRs(TypedDict, total=False):
    DepositRet: Union[DepositRet, List[DepositRet]]


class CustomerTypeQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CustomerTypeQueryRs(TypedDict, total=False):
    CustomerTypeRet: Union[CustomerTypeRet, List[CustomerTypeRet]]


class TxnDisplayAddRq(TypedDict, total=False):
    TxnDisplayAddType: TxnDisplayAddType
    EntityRef: EntityRef


class ListDelRq(TypedDict, total=False):
    ListDelType: ListDelType
    ListID: IDTYPE


class ListDelRs(TypedDict, total=False):
    ListDelType: ListDelType
    ListID: IDTYPE
    TimeDeleted: DATETIMETYPE
    FullName: STRTYPE


class TxnDeletedQueryRq(TypedDict, total=False):
    TxnDelType: Union[TxnDelType, List[TxnDelType]]
    DeletedDateRangeFilter: DeletedDateRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TxnDeletedRet(TypedDict, total=False):
    TxnDelType: TxnDelType
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeDeleted: DATETIMETYPE
    RefNumber: STRTYPE


class TxnDeletedQueryRs(TypedDict, total=False):
    TxnDeletedRet: Union[TxnDeletedRet, List[TxnDeletedRet]]


class WorkersCompCodeQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    FromEffectiveDate: DATETYPE
    ToEffectiveDate: DATETYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class WorkersCompCodeQueryRs(TypedDict, total=False):
    WorkersCompCodeRet: Union[WorkersCompCodeRet, List[WorkersCompCodeRet]]


class ItemGroupQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemGroupQueryRs(TypedDict, total=False):
    ItemGroupRet: Union[ItemGroupRet, List[ItemGroupRet]]


class ItemSalesTaxQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemSalesTaxQueryRs(TypedDict, total=False):
    ItemSalesTaxRet: Union[ItemSalesTaxRet, List[ItemSalesTaxRet]]


class CreditCardCreditMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    AccountRef: AccountRef
    PayeeEntityRef: PayeeEntityRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ClearExpenseLines: BOOLTYPE
    ExpenseLineMod: Union[ExpenseLineMod, List[ExpenseLineMod]]
    ClearItemLines: BOOLTYPE
    ItemLineMod: ItemLineMod
    ItemGroupLineMod: ItemGroupLineMod


class CreditCardCreditModRq(TypedDict, total=False):
    CreditCardCreditMod: CreditCardCreditMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CreditCardCreditModRs(TypedDict, total=False):
    CreditCardCreditRet: CreditCardCreditRet
    ErrorRecovery: ErrorRecovery


class SalesRepMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Initial: STRTYPE
    IsActive: BOOLTYPE
    SalesRepEntityRef: SalesRepEntityRef


class SalesRepModRq(TypedDict, total=False):
    SalesRepMod: SalesRepMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesRepModRs(TypedDict, total=False):
    SalesRepRet: SalesRepRet
    ErrorRecovery: ErrorRecovery


class ClearedStatusMod(TypedDict, total=False):
    TxnID: IDTYPE
    TxnLineID: IDTYPE
    ClearedStatus: ClearedStatus


class ClearedStatusModRq(TypedDict, total=False):
    ClearedStatusMod: ClearedStatusMod


class InventorySiteAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    ParentSiteRef: ParentSiteRef
    SiteDesc: STRTYPE
    Contact: STRTYPE
    Phone: STRTYPE
    Fax: STRTYPE
    Email: STRTYPE
    SiteAddress: SiteAddress


class InventorySiteAddRq(TypedDict, total=False):
    InventorySiteAdd: InventorySiteAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class InventorySiteAddRs(TypedDict, total=False):
    InventorySiteRet: InventorySiteRet
    ErrorRecovery: ErrorRecovery


class CompanyQueryRq(TypedDict, total=False):
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class LegalAddress(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE
    City: STRTYPE
    State: STRTYPE
    PostalCode: STRTYPE
    Country: STRTYPE
    Note: STRTYPE


class CompanyAddressForCustomer(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE
    City: STRTYPE
    State: STRTYPE
    PostalCode: STRTYPE
    Country: STRTYPE
    Note: STRTYPE


class CompanyAddressBlockForCustomer(TypedDict, total=False):
    Addr1: STRTYPE
    Addr2: STRTYPE
    Addr3: STRTYPE
    Addr4: STRTYPE
    Addr5: STRTYPE


class Service(TypedDict, total=False):
    Name: STRTYPE
    Domain: STRTYPE
    ServiceStatus: ServiceStatus


class SubscribedServices(TypedDict, total=False):
    Service: Union[Service, List[Service]]


class AccountantCopy(TypedDict, total=False):
    AccountantCopyExists: BOOLTYPE
    DividingDate: DATETYPE


class CompanyRet(TypedDict, total=False):
    IsSampleCompany: BOOLTYPE
    CompanyName: STRTYPE
    LegalCompanyName: STRTYPE
    Address: Address
    AddressBlock: AddressBlock
    LegalAddress: LegalAddress
    CompanyAddressForCustomer: CompanyAddressForCustomer
    CompanyAddressBlockForCustomer: CompanyAddressBlockForCustomer
    Phone: STRTYPE
    Fax: STRTYPE
    Email: STRTYPE
    CompanyWebSite: STRTYPE
    FirstMonthFiscalYear: FirstMonthFiscalYear
    FirstMonthIncomeTaxYear: FirstMonthIncomeTaxYear
    CompanyType: STRTYPE
    EIN: STRTYPE
    SSN: STRTYPE
    TaxForm: TaxForm
    SubscribedServices: SubscribedServices
    AccountantCopy: AccountantCopy
    DataExtRet: Union[DataExtRet, List[DataExtRet]]


class CompanyQueryRs(TypedDict, total=False):
    CompanyRet: CompanyRet


class ItemPaymentAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ItemDesc: STRTYPE
    DepositToAccountRef: DepositToAccountRef
    PaymentMethodRef: PaymentMethodRef
    ExternalGUID: GUIDTYPE


class ItemPaymentAddRq(TypedDict, total=False):
    ItemPaymentAdd: ItemPaymentAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemPaymentAddRs(TypedDict, total=False):
    ItemPaymentRet: ItemPaymentRet
    ErrorRecovery: ErrorRecovery


class ItemSalesTaxAdd(TypedDict, total=False):
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    ItemDesc: STRTYPE
    TaxRate: PERCENTTYPE
    TaxVendorRef: TaxVendorRef
    SalesTaxReturnLineRef: SalesTaxReturnLineRef
    ExternalGUID: GUIDTYPE


class ItemSalesTaxAddRq(TypedDict, total=False):
    ItemSalesTaxAdd: ItemSalesTaxAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemSalesTaxAddRs(TypedDict, total=False):
    ItemSalesTaxRet: ItemSalesTaxRet
    ErrorRecovery: ErrorRecovery


class SpecialAccountAdd(TypedDict, total=False):
    SpecialAccountType: SpecialAccountType
    CurrencyRef: CurrencyRef


class SpecialAccountAddRq(TypedDict, total=False):
    SpecialAccountAdd: SpecialAccountAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SpecialAccountAddRs(TypedDict, total=False):
    AccountRet: AccountRet
    ErrorRecovery: ErrorRecovery


class Form1099CategoryAccountMappingQueryRq(TypedDict, total=False):
    MappingCategory: Union[MappingCategory, List[MappingCategory]]


class Form1099CategoryAccountMappingQueryRs(TypedDict, total=False):
    Form1099CategoryAccountMappingRet: Form1099CategoryAccountMappingRet


class BillPaymentCheckMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    TxnDate: DATETYPE
    BankAccountRef: BankAccountRef
    Amount: AMTTYPE
    ExchangeRate: FLOATTYPE
    IsToBePrinted: BOOLTYPE
    RefNumber: STRTYPE
    Memo: STRTYPE
    AppliedToTxnMod: Union[AppliedToTxnMod, List[AppliedToTxnMod]]


class BillPaymentCheckModRq(TypedDict, total=False):
    BillPaymentCheckMod: BillPaymentCheckMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BillPaymentCheckModRs(TypedDict, total=False):
    BillPaymentCheckRet: BillPaymentCheckRet
    ErrorRecovery: ErrorRecovery


class ItemNonInventoryQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemNonInventoryQueryRs(TypedDict, total=False):
    ItemNonInventoryRet: Union[ItemNonInventoryRet, List[ItemNonInventoryRet]]


class RefundAppliedToTxnAdd(TypedDict, total=False):
    TxnID: IDTYPE
    RefundAmount: AMTTYPE


class ARRefundCreditCardAdd(TypedDict, total=False):
    CustomerRef: CustomerRef
    RefundFromAccountRef: RefundFromAccountRef
    ARAccountRef: ARAccountRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    Address: Address
    PaymentMethodRef: PaymentMethodRef
    Memo: STRTYPE
    CreditCardTxnInfo: CreditCardTxnInfo
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    RefundAppliedToTxnAdd: Union[RefundAppliedToTxnAdd, List[RefundAppliedToTxnAdd]]


class ARRefundCreditCardAddRq(TypedDict, total=False):
    ARRefundCreditCardAdd: ARRefundCreditCardAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ARRefundCreditCardAddRs(TypedDict, total=False):
    ARRefundCreditCardRet: ARRefundCreditCardRet
    ErrorRecovery: ErrorRecovery


class TxnDelRq(TypedDict, total=False):
    TxnDelType: TxnDelType
    TxnID: IDTYPE


class TxnDelRs(TypedDict, total=False):
    TxnDelType: TxnDelType
    TxnID: IDTYPE
    TimeDeleted: DATETIMETYPE
    RefNumber: STRTYPE
    ErrorRecovery: ErrorRecovery


class TransferInventoryLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    FromInventorySiteLocationRef: FromInventorySiteLocationRef
    ToInventorySiteLocationRef: ToInventorySiteLocationRef
    QuantityToTransfer: QUANTYPE
    SerialNumber: STRTYPE
    LotNumber: STRTYPE


class TransferInventoryMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    FromInventorySiteRef: FromInventorySiteRef
    ToInventorySiteRef: ToInventorySiteRef
    Memo: STRTYPE
    TransferInventoryLineMod: Union[TransferInventoryLineMod, List[TransferInventoryLineMod]]


class TransferInventoryModRq(TypedDict, total=False):
    TransferInventoryMod: TransferInventoryMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class TransferInventoryModRs(TypedDict, total=False):
    TransferInventoryRet: TransferInventoryRet
    ErrorRecovery: ErrorRecovery


class CashBackInfoMod(TypedDict, total=False):
    AccountRef: AccountRef
    Memo: STRTYPE
    Amount: AMTTYPE


class DepositLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    PaymentTxnID: IDTYPE
    PaymentTxnLineID: IDTYPE
    OverrideMemo: STRTYPE
    OverrideCheckNumber: STRTYPE
    OverrideClassRef: OverrideClassRef
    EntityRef: EntityRef
    AccountRef: AccountRef
    Memo: STRTYPE
    CheckNumber: STRTYPE
    PaymentMethodRef: PaymentMethodRef
    ClassRef: ClassRef
    Amount: AMTTYPE


class DepositMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    TxnDate: DATETYPE
    DepositToAccountRef: DepositToAccountRef
    Memo: STRTYPE
    CashBackInfoMod: CashBackInfoMod
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    DepositLineMod: Union[DepositLineMod, List[DepositLineMod]]


class DepositModRq(TypedDict, total=False):
    DepositMod: DepositMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class DepositModRs(TypedDict, total=False):
    DepositRet: DepositRet
    ErrorRecovery: ErrorRecovery


class ItemFixedAssetQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    ClassFilter: ClassFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class ItemFixedAssetQueryRs(TypedDict, total=False):
    ItemFixedAssetRet: Union[ItemFixedAssetRet, List[ItemFixedAssetRet]]


class AccountQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    AccountType: Union[AccountType, List[AccountType]]
    CurrencyFilter: CurrencyFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class AccountQueryRs(TypedDict, total=False):
    AccountRet: Union[AccountRet, List[AccountRet]]


class TxnVoidRq(TypedDict, total=False):
    TxnVoidType: TxnVoidType
    TxnID: IDTYPE


class TxnVoidRs(TypedDict, total=False):
    TxnVoidType: TxnVoidType
    TxnID: IDTYPE
    TimeCreated: DATETIMETYPE
    TimeModified: DATETIMETYPE
    RefNumber: STRTYPE
    ErrorRecovery: ErrorRecovery


class SpecialItemAdd(TypedDict, total=False):
    SpecialItemType: SpecialItemType
    BarCode: BarCode
    ExternalGUID: GUIDTYPE


class SpecialItemAddRq(TypedDict, total=False):
    SpecialItemAdd: SpecialItemAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SpecialItemAddRs(TypedDict, total=False):
    ItemOtherChargeRet: ItemOtherChargeRet
    ItemSubtotalRet: ItemSubtotalRet
    ItemGroupRet: ItemGroupRet


class DataExtAdd(TypedDict, total=False):
    OwnerID: GUIDTYPE
    DataExtName: STRTYPE
    ListDataExtType: ListDataExtType
    ListObjRef: ListObjRef
    TxnDataExtType: TxnDataExtType
    TxnID: IDTYPE
    TxnLineID: IDTYPE
    OtherDataExtType: OtherDataExtType
    DataExtValue: STRTYPE


class DataExtAddRq(TypedDict, total=False):
    DataExtAdd: DataExtAdd


class DataExtAddRs(TypedDict, total=False):
    DataExtRet: DataExtRet
    ErrorRecovery: ErrorRecovery


class PriceLevelAdd(TypedDict, total=False):
    Name: STRTYPE
    IsActive: BOOLTYPE
    PriceLevelFixedPercentage: PERCENTTYPE
    PriceLevelPerItem: Union[PriceLevelPerItem, List[PriceLevelPerItem]]
    CurrencyRef: CurrencyRef


class PriceLevelAddRq(TypedDict, total=False):
    PriceLevelAdd: PriceLevelAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class PriceLevelAddRs(TypedDict, total=False):
    PriceLevelRet: PriceLevelRet
    ErrorRecovery: ErrorRecovery


class JobReportQueryRq(TypedDict, total=False):
    JobReportType: JobReportType
    DisplayReport: BOOLTYPE
    ReportPeriod: ReportPeriod
    ReportDateMacro: ReportDateMacro
    ReportAccountFilter: ReportAccountFilter
    ReportEntityFilter: ReportEntityFilter
    ReportItemFilter: ReportItemFilter
    ReportClassFilter: ReportClassFilter
    ReportTxnTypeFilter: ReportTxnTypeFilter
    ReportModifiedDateRangeFilter: ReportModifiedDateRangeFilter
    ReportModifiedDateRangeMacro: ReportModifiedDateRangeMacro
    ReportDetailLevelFilter: ReportDetailLevelFilter
    ReportPostingStatusFilter: ReportPostingStatusFilter
    SummarizeColumnsBy: SummarizeColumnsBy
    IncludeSubcolumns: BOOLTYPE


class InventoryAdjustmentQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    ItemFilter: ItemFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class InventoryAdjustmentQueryRs(TypedDict, total=False):
    InventoryAdjustmentRet: Union[InventoryAdjustmentRet, List[InventoryAdjustmentRet]]


class JournalLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    JournalLineType: JournalLineType
    AccountRef: AccountRef
    Amount: AMTTYPE
    Memo: STRTYPE
    EntityRef: EntityRef
    ClassRef: ClassRef
    ItemSalesTaxRef: ItemSalesTaxRef
    BillableStatus: BillableStatus


class JournalEntryMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    IsAdjustment: BOOLTYPE
    IsAmountsEnteredInHomeCurrency: BOOLTYPE
    CurrencyRef: CurrencyRef
    ExchangeRate: FLOATTYPE
    JournalLineMod: Union[JournalLineMod, List[JournalLineMod]]


class JournalEntryModRq(TypedDict, total=False):
    JournalEntryMod: JournalEntryMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class JournalEntryModRs(TypedDict, total=False):
    JournalEntryRet: JournalEntryRet
    ErrorRecovery: ErrorRecovery


class FixedAssetSalesInfoMod(TypedDict, total=False):
    SalesDesc: STRTYPE
    SalesDate: DATETYPE
    SalesPrice: PRICETYPE
    SalesExpense: PRICETYPE


class ItemFixedAssetMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    BarCode: BarCode
    IsActive: BOOLTYPE
    ClassRef: ClassRef
    AcquiredAs: AcquiredAs
    PurchaseDesc: STRTYPE
    PurchaseDate: DATETYPE
    PurchaseCost: PRICETYPE
    VendorOrPayeeName: STRTYPE
    AssetAccountRef: AssetAccountRef
    FixedAssetSalesInfoMod: FixedAssetSalesInfoMod
    AssetDesc: STRTYPE
    Location: STRTYPE
    PONumber: STRTYPE
    SerialNumber: STRTYPE
    WarrantyExpDate: DATETYPE
    Notes: STRTYPE
    AssetNumber: STRTYPE
    CostBasis: AMTTYPE
    YearEndAccumulatedDepreciation: AMTTYPE
    YearEndBookValue: AMTTYPE


class ItemFixedAssetModRq(TypedDict, total=False):
    ItemFixedAssetMod: ItemFixedAssetMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class ItemFixedAssetModRs(TypedDict, total=False):
    ItemFixedAssetRet: ItemFixedAssetRet
    ErrorRecovery: ErrorRecovery


class CurrencyMod(TypedDict, total=False):
    ListID: IDTYPE
    EditSequence: STRTYPE
    Name: STRTYPE
    IsActive: BOOLTYPE
    CurrencyCode: STRTYPE
    CurrencyFormat: CurrencyFormat


class CurrencyModRq(TypedDict, total=False):
    CurrencyMod: CurrencyMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CurrencyModRs(TypedDict, total=False):
    CurrencyRet: CurrencyRet
    ErrorRecovery: ErrorRecovery


class InvoiceLineMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemRef: ItemRef
    Desc: STRTYPE
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    Rate: PRICETYPE
    RatePercent: PERCENTTYPE
    PriceLevelRef: PriceLevelRef
    ClassRef: ClassRef
    Amount: AMTTYPE
    OptionForPriceRuleConflict: OptionForPriceRuleConflict
    InventorySiteRef: InventorySiteRef
    InventorySiteLocationRef: InventorySiteLocationRef
    SerialNumber: STRTYPE
    LotNumber: STRTYPE
    ServiceDate: DATETYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    OverrideItemAccountRef: OverrideItemAccountRef
    Other1: STRTYPE
    Other2: STRTYPE


class InvoiceLineGroupMod(TypedDict, total=False):
    TxnLineID: IDTYPE
    ItemGroupRef: ItemGroupRef
    Quantity: QUANTYPE
    UnitOfMeasure: STRTYPE
    OverrideUOMSetRef: OverrideUOMSetRef
    InvoiceLineMod: Union[InvoiceLineMod, List[InvoiceLineMod]]


class InvoiceMod(TypedDict, total=False):
    TxnID: IDTYPE
    EditSequence: STRTYPE
    CustomerRef: CustomerRef
    ClassRef: ClassRef
    ARAccountRef: ARAccountRef
    TemplateRef: TemplateRef
    TxnDate: DATETYPE
    RefNumber: STRTYPE
    BillAddress: BillAddress
    ShipAddress: ShipAddress
    IsPending: BOOLTYPE
    PONumber: STRTYPE
    TermsRef: TermsRef
    DueDate: DATETYPE
    SalesRepRef: SalesRepRef
    FOB: STRTYPE
    ShipDate: DATETYPE
    ShipMethodRef: ShipMethodRef
    ItemSalesTaxRef: ItemSalesTaxRef
    Memo: STRTYPE
    CustomerMsgRef: CustomerMsgRef
    IsToBePrinted: BOOLTYPE
    IsToBeEmailed: BOOLTYPE
    IsTaxIncluded: BOOLTYPE
    CustomerSalesTaxCodeRef: CustomerSalesTaxCodeRef
    Other: STRTYPE
    ExchangeRate: FLOATTYPE
    SetCredit: Union[SetCredit, List[SetCredit]]
    InvoiceLineMod: InvoiceLineMod
    InvoiceLineGroupMod: InvoiceLineGroupMod


class InvoiceModRq(TypedDict, total=False):
    InvoiceMod: InvoiceMod
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class InvoiceModRs(TypedDict, total=False):
    InvoiceRet: InvoiceRet
    ErrorRecovery: ErrorRecovery


class CustomSummaryReportQueryRq(TypedDict, total=False):
    CustomSummaryReportType: CustomSummaryReportType
    DisplayReport: BOOLTYPE
    ReportPeriod: ReportPeriod
    ReportDateMacro: ReportDateMacro
    ReportAccountFilter: ReportAccountFilter
    ReportEntityFilter: ReportEntityFilter
    ReportItemFilter: ReportItemFilter
    ReportClassFilter: ReportClassFilter
    ReportTxnTypeFilter: ReportTxnTypeFilter
    ReportModifiedDateRangeFilter: ReportModifiedDateRangeFilter
    ReportModifiedDateRangeMacro: ReportModifiedDateRangeMacro
    ReportDetailLevelFilter: ReportDetailLevelFilter
    ReportPostingStatusFilter: ReportPostingStatusFilter
    SummarizeColumnsBy: SummarizeColumnsBy
    SummarizeRowsBy: SummarizeRowsBy
    IncludeSubcolumns: BOOLTYPE
    ReportCalendar: ReportCalendar
    ReturnRows: ReturnRows
    ReturnColumns: ReturnColumns
    ReportBasis: ReportBasis


class CustomerMsgQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class CustomerMsgQueryRs(TypedDict, total=False):
    CustomerMsgRet: Union[CustomerMsgRet, List[CustomerMsgRet]]


class BillAdd(TypedDict, total=False):
    VendorRef: VendorRef
    VendorAddress: VendorAddress
    APAccountRef: APAccountRef
    TxnDate: DATETYPE
    DueDate: DATETYPE
    RefNumber: STRTYPE
    TermsRef: TermsRef
    Memo: STRTYPE
    IsTaxIncluded: BOOLTYPE
    SalesTaxCodeRef: SalesTaxCodeRef
    ExchangeRate: FLOATTYPE
    ExternalGUID: GUIDTYPE
    LinkToTxnID: Union[IDTYPE, List[IDTYPE]]
    ExpenseLineAdd: Union[ExpenseLineAdd, List[ExpenseLineAdd]]
    ItemLineAdd: ItemLineAdd
    ItemGroupLineAdd: ItemGroupLineAdd


class BillAddRq(TypedDict, total=False):
    BillAdd: BillAdd
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class BillAddRs(TypedDict, total=False):
    BillRet: BillRet
    ErrorRecovery: ErrorRecovery


class JournalEntryQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class JournalEntryQueryRs(TypedDict, total=False):
    JournalEntryRet: Union[JournalEntryRet, List[JournalEntryRet]]


class CustomDetailReportQueryRq(TypedDict, total=False):
    CustomDetailReportType: CustomDetailReportType
    DisplayReport: BOOLTYPE
    ReportPeriod: ReportPeriod
    ReportDateMacro: ReportDateMacro
    ReportAccountFilter: ReportAccountFilter
    ReportEntityFilter: ReportEntityFilter
    ReportItemFilter: ReportItemFilter
    ReportClassFilter: ReportClassFilter
    ReportTxnTypeFilter: ReportTxnTypeFilter
    ReportModifiedDateRangeFilter: ReportModifiedDateRangeFilter
    ReportModifiedDateRangeMacro: ReportModifiedDateRangeMacro
    ReportDetailLevelFilter: ReportDetailLevelFilter
    ReportPostingStatusFilter: ReportPostingStatusFilter
    SummarizeRowsBy: SummarizeRowsBy
    IncludeColumn: Union[IncludeColumn, List[IncludeColumn]]
    IncludeAccounts: IncludeAccounts
    ReportOpenBalanceAsOf: ReportOpenBalanceAsOf
    ReportBasis: ReportBasis


class VendorCreditQueryRq(TypedDict, total=False):
    TxnID: Union[IDTYPE, List[IDTYPE]]
    RefNumber: Union[STRTYPE, List[STRTYPE]]
    RefNumberCaseSensitive: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ModifiedDateRangeFilter: ModifiedDateRangeFilter
    TxnDateRangeFilter: TxnDateRangeFilter
    EntityFilter: EntityFilter
    AccountFilter: AccountFilter
    RefNumberFilter: RefNumberFilter
    RefNumberRangeFilter: RefNumberRangeFilter
    CurrencyFilter: CurrencyFilter
    IncludeLineItems: BOOLTYPE
    IncludeLinkedTxns: BOOLTYPE
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class VendorCreditQueryRs(TypedDict, total=False):
    VendorCreditRet: Union[VendorCreditRet, List[VendorCreditRet]]


class SalesTaxCodeQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]


class SalesTaxCodeQueryRs(TypedDict, total=False):
    SalesTaxCodeRet: Union[SalesTaxCodeRet, List[SalesTaxCodeRet]]


class EmployeeQueryRq(TypedDict, total=False):
    ListID: Union[IDTYPE, List[IDTYPE]]
    FullName: Union[STRTYPE, List[STRTYPE]]
    MaxReturned: INTTYPE
    ActiveStatus: ActiveStatus
    FromModifiedDate: DATETIMETYPE
    ToModifiedDate: DATETIMETYPE
    NameFilter: NameFilter
    NameRangeFilter: NameRangeFilter
    IncludeRetElement: Union[STRTYPE, List[STRTYPE]]
    OwnerID: Union[GUIDTYPE, List[GUIDTYPE]]


class PayrollDetailReportQueryRq(TypedDict, total=False):
    PayrollDetailReportType: PayrollDetailReportType
    DisplayReport: BOOLTYPE
    ReportPeriod: ReportPeriod
    ReportDateMacro: ReportDateMacro
    ReportAccountFilter: ReportAccountFilter
    ReportEntityFilter: ReportEntityFilter
    ReportItemFilter: ReportItemFilter
    ReportClassFilter: ReportClassFilter
    ReportModifiedDateRangeFilter: ReportModifiedDateRangeFilter
    ReportModifiedDateRangeMacro: ReportModifiedDateRangeMacro
    ReportDetailLevelFilter: ReportDetailLevelFilter
    ReportPostingStatusFilter: ReportPostingStatusFilter
    SummarizeRowsBy: SummarizeRowsBy
    IncludeColumn: Union[IncludeColumn, List[IncludeColumn]]
    IncludeAccounts: IncludeAccounts
    ReportOpenBalanceAsOf: ReportOpenBalanceAsOf


class QBXMLMsgsRq(TypedDict, total=False):
    CustomerMsgAddRq: Optional[Union[CustomerMsgAddRq, List[CustomerMsgAddRq]]]
    ItemSubtotalAddRq: Optional[Union[ItemSubtotalAddRq, List[ItemSubtotalAddRq]]]
    SalesTaxPaymentCheckModRq: Optional[Union[SalesTaxPaymentCheckModRq, List[SalesTaxPaymentCheckModRq]]]
    TimeTrackingModRq: Optional[Union[TimeTrackingModRq, List[TimeTrackingModRq]]]
    ChargeModRq: Optional[Union[ChargeModRq, List[ChargeModRq]]]
    PurchaseOrderModRq: Optional[Union[PurchaseOrderModRq, List[PurchaseOrderModRq]]]
    ItemReceiptQueryRq: Optional[Union[ItemReceiptQueryRq, List[ItemReceiptQueryRq]]]
    TransferAddRq: Optional[Union[TransferAddRq, List[TransferAddRq]]]
    TimeTrackingQueryRq: Optional[Union[TimeTrackingQueryRq, List[TimeTrackingQueryRq]]]
    ItemInventoryModRq: Optional[Union[ItemInventoryModRq, List[ItemInventoryModRq]]]
    BuildAssemblyModRq: Optional[Union[BuildAssemblyModRq, List[BuildAssemblyModRq]]]
    GeneralDetailReportQueryRq: Optional[Union[GeneralDetailReportQueryRq, List[GeneralDetailReportQueryRq]]]
    ListDeletedQueryRq: Optional[Union[ListDeletedQueryRq, List[ListDeletedQueryRq]]]
    ToDoAddRq: Optional[Union[ToDoAddRq, List[ToDoAddRq]]]
    ReceivePaymentQueryRq: Optional[Union[ReceivePaymentQueryRq, List[ReceivePaymentQueryRq]]]
    PreferencesQueryRq: Optional[Union[PreferencesQueryRq, List[PreferencesQueryRq]]]
    ClassAddRq: Optional[Union[ClassAddRq, List[ClassAddRq]]]
    DataExtDefAddRq: Optional[Union[DataExtDefAddRq, List[DataExtDefAddRq]]]
    OtherNameAddRq: Optional[Union[OtherNameAddRq, List[OtherNameAddRq]]]
    ReceivePaymentToDepositQueryRq: Optional[Union[ReceivePaymentToDepositQueryRq, List[ReceivePaymentToDepositQueryRq]]]
    UnitOfMeasureSetQueryRq: Optional[Union[UnitOfMeasureSetQueryRq, List[UnitOfMeasureSetQueryRq]]]
    DataExtDefQueryRq: Optional[Union[DataExtDefQueryRq, List[DataExtDefQueryRq]]]
    SalesOrderModRq: Optional[Union[SalesOrderModRq, List[SalesOrderModRq]]]
    ChargeQueryRq: Optional[Union[ChargeQueryRq, List[ChargeQueryRq]]]
    VehicleModRq: Optional[Union[VehicleModRq, List[VehicleModRq]]]
    VehicleMileageAddRq: Optional[Union[VehicleMileageAddRq, List[VehicleMileageAddRq]]]
    CheckAddRq: Optional[Union[CheckAddRq, List[CheckAddRq]]]
    PriceLevelQueryRq: Optional[Union[PriceLevelQueryRq, List[PriceLevelQueryRq]]]
    BillQueryRq: Optional[Union[BillQueryRq, List[BillQueryRq]]]
    ItemSubtotalQueryRq: Optional[Union[ItemSubtotalQueryRq, List[ItemSubtotalQueryRq]]]
    EstimateAddRq: Optional[Union[EstimateAddRq, List[EstimateAddRq]]]
    ToDoQueryRq: Optional[Union[ToDoQueryRq, List[ToDoQueryRq]]]
    DataExtDefDelRq: Optional[Union[DataExtDefDelRq, List[DataExtDefDelRq]]]
    JobTypeAddRq: Optional[Union[JobTypeAddRq, List[JobTypeAddRq]]]
    InventoryAdjustmentAddRq: Optional[Union[InventoryAdjustmentAddRq, List[InventoryAdjustmentAddRq]]]
    ItemServiceAddRq: Optional[Union[ItemServiceAddRq, List[ItemServiceAddRq]]]
    SalesTaxPaymentCheckQueryRq: Optional[Union[SalesTaxPaymentCheckQueryRq, List[SalesTaxPaymentCheckQueryRq]]]
    ItemDiscountQueryRq: Optional[Union[ItemDiscountQueryRq, List[ItemDiscountQueryRq]]]
    ItemGroupAddRq: Optional[Union[ItemGroupAddRq, List[ItemGroupAddRq]]]
    CreditMemoQueryRq: Optional[Union[CreditMemoQueryRq, List[CreditMemoQueryRq]]]
    StandardTermsAddRq: Optional[Union[StandardTermsAddRq, List[StandardTermsAddRq]]]
    BillingRateAddRq: Optional[Union[BillingRateAddRq, List[BillingRateAddRq]]]
    WorkersCompCodeAddRq: Optional[Union[WorkersCompCodeAddRq, List[WorkersCompCodeAddRq]]]
    ItemOtherChargeAddRq: Optional[Union[ItemOtherChargeAddRq, List[ItemOtherChargeAddRq]]]
    BillPaymentCreditCardQueryRq: Optional[Union[BillPaymentCreditCardQueryRq, List[BillPaymentCreditCardQueryRq]]]
    TermsQueryRq: Optional[Union[TermsQueryRq, List[TermsQueryRq]]]
    ListDisplayAddRq: Optional[Union[ListDisplayAddRq, List[ListDisplayAddRq]]]
    ItemNonInventoryModRq: Optional[Union[ItemNonInventoryModRq, List[ItemNonInventoryModRq]]]
    ItemSalesTaxGroupAddRq: Optional[Union[ItemSalesTaxGroupAddRq, List[ItemSalesTaxGroupAddRq]]]
    ItemReceiptModRq: Optional[Union[ItemReceiptModRq, List[ItemReceiptModRq]]]
    CreditMemoAddRq: Optional[Union[CreditMemoAddRq, List[CreditMemoAddRq]]]
    PayrollSummaryReportQueryRq: Optional[Union[PayrollSummaryReportQueryRq, List[PayrollSummaryReportQueryRq]]]
    ReceivePaymentAddRq: Optional[Union[ReceivePaymentAddRq, List[ReceivePaymentAddRq]]]
    PayrollItemNonWageQueryRq: Optional[Union[PayrollItemNonWageQueryRq, List[PayrollItemNonWageQueryRq]]]
    SalesReceiptAddRq: Optional[Union[SalesReceiptAddRq, List[SalesReceiptAddRq]]]
    GeneralSummaryReportQueryRq: Optional[Union[GeneralSummaryReportQueryRq, List[GeneralSummaryReportQueryRq]]]
    ShipMethodAddRq: Optional[Union[ShipMethodAddRq, List[ShipMethodAddRq]]]
    SalesTaxCodeModRq: Optional[Union[SalesTaxCodeModRq, List[SalesTaxCodeModRq]]]
    ItemDiscountModRq: Optional[Union[ItemDiscountModRq, List[ItemDiscountModRq]]]
    CreditCardChargeAddRq: Optional[Union[CreditCardChargeAddRq, List[CreditCardChargeAddRq]]]
    SalesReceiptQueryRq: Optional[Union[SalesReceiptQueryRq, List[SalesReceiptQueryRq]]]
    VendorTypeQueryRq: Optional[Union[VendorTypeQueryRq, List[VendorTypeQueryRq]]]
    VehicleQueryRq: Optional[Union[VehicleQueryRq, List[VehicleQueryRq]]]
    BillingRateQueryRq: Optional[Union[BillingRateQueryRq, List[BillingRateQueryRq]]]
    VendorCreditModRq: Optional[Union[VendorCreditModRq, List[VendorCreditModRq]]]
    ItemSitesQueryRq: Optional[Union[ItemSitesQueryRq, List[ItemSitesQueryRq]]]
    ItemInventoryAssemblyAddRq: Optional[Union[ItemInventoryAssemblyAddRq, List[ItemInventoryAssemblyAddRq]]]
    TxnDisplayModRq: Optional[Union[TxnDisplayModRq, List[TxnDisplayModRq]]]
    StandardTermsQueryRq: Optional[Union[StandardTermsQueryRq, List[StandardTermsQueryRq]]]
    BillPaymentCheckQueryRq: Optional[Union[BillPaymentCheckQueryRq, List[BillPaymentCheckQueryRq]]]
    ItemQueryRq: Optional[Union[ItemQueryRq, List[ItemQueryRq]]]
    ItemInventoryAssemblyQueryRq: Optional[Union[ItemInventoryAssemblyQueryRq, List[ItemInventoryAssemblyQueryRq]]]
    TransactionQueryRq: Optional[Union[TransactionQueryRq, List[TransactionQueryRq]]]
    SalesTaxPayableQueryRq: Optional[Union[SalesTaxPayableQueryRq, List[SalesTaxPayableQueryRq]]]
    BuildAssemblyQueryRq: Optional[Union[BuildAssemblyQueryRq, List[BuildAssemblyQueryRq]]]
    AccountModRq: Optional[Union[AccountModRq, List[AccountModRq]]]
    ItemPaymentModRq: Optional[Union[ItemPaymentModRq, List[ItemPaymentModRq]]]
    DateDrivenTermsAddRq: Optional[Union[DateDrivenTermsAddRq, List[DateDrivenTermsAddRq]]]
    ItemSalesTaxModRq: Optional[Union[ItemSalesTaxModRq, List[ItemSalesTaxModRq]]]
    BillPaymentCheckAddRq: Optional[Union[BillPaymentCheckAddRq, List[BillPaymentCheckAddRq]]]
    InventorySiteModRq: Optional[Union[InventorySiteModRq, List[InventorySiteModRq]]]
    TemplateQueryRq: Optional[Union[TemplateQueryRq, List[TemplateQueryRq]]]
    CreditCardCreditAddRq: Optional[Union[CreditCardCreditAddRq, List[CreditCardCreditAddRq]]]
    SalesOrderQueryRq: Optional[Union[SalesOrderQueryRq, List[SalesOrderQueryRq]]]
    SalesRepAddRq: Optional[Union[SalesRepAddRq, List[SalesRepAddRq]]]
    Form1099CategoryAccountMappingModRq: Optional[Union[Form1099CategoryAccountMappingModRq, List[Form1099CategoryAccountMappingModRq]]]
    SalesRepQueryRq: Optional[Union[SalesRepQueryRq, List[SalesRepQueryRq]]]
    InventorySiteQueryRq: Optional[Union[InventorySiteQueryRq, List[InventorySiteQueryRq]]]
    ClassQueryRq: Optional[Union[ClassQueryRq, List[ClassQueryRq]]]
    DataExtModRq: Optional[Union[DataExtModRq, List[DataExtModRq]]]
    SalesTaxReturnLineQueryRq: Optional[Union[SalesTaxReturnLineQueryRq, List[SalesTaxReturnLineQueryRq]]]
    PriceLevelModRq: Optional[Union[PriceLevelModRq, List[PriceLevelModRq]]]
    DataEventRecoveryInfoQueryRq: Optional[Union[DataEventRecoveryInfoQueryRq, List[DataEventRecoveryInfoQueryRq]]]
    LeadQueryRq: Optional[Union[LeadQueryRq, List[LeadQueryRq]]]
    DepositAddRq: Optional[Union[DepositAddRq, List[DepositAddRq]]]
    TransferInventoryAddRq: Optional[Union[TransferInventoryAddRq, List[TransferInventoryAddRq]]]
    DateDrivenTermsQueryRq: Optional[Union[DateDrivenTermsQueryRq, List[DateDrivenTermsQueryRq]]]
    BillModRq: Optional[Union[BillModRq, List[BillModRq]]]
    BillToPayQueryRq: Optional[Union[BillToPayQueryRq, List[BillToPayQueryRq]]]
    TransferQueryRq: Optional[Union[TransferQueryRq, List[TransferQueryRq]]]
    ARRefundCreditCardQueryRq: Optional[Union[ARRefundCreditCardQueryRq, List[ARRefundCreditCardQueryRq]]]
    InvoiceQueryRq: Optional[Union[InvoiceQueryRq, List[InvoiceQueryRq]]]
    ItemAssembliesCanBuildQueryRq: Optional[Union[ItemAssembliesCanBuildQueryRq, List[ItemAssembliesCanBuildQueryRq]]]
    ItemFixedAssetAddRq: Optional[Union[ItemFixedAssetAddRq, List[ItemFixedAssetAddRq]]]
    CurrencyAddRq: Optional[Union[CurrencyAddRq, List[CurrencyAddRq]]]
    JournalEntryAddRq: Optional[Union[JournalEntryAddRq, List[JournalEntryAddRq]]]
    InvoiceAddRq: Optional[Union[InvoiceAddRq, List[InvoiceAddRq]]]
    TransferInventoryQueryRq: Optional[Union[TransferInventoryQueryRq, List[TransferInventoryQueryRq]]]
    ShipMethodQueryRq: Optional[Union[ShipMethodQueryRq, List[ShipMethodQueryRq]]]
    BuildAssemblyAddRq: Optional[Union[BuildAssemblyAddRq, List[BuildAssemblyAddRq]]]
    ItemInventoryAddRq: Optional[Union[ItemInventoryAddRq, List[ItemInventoryAddRq]]]
    OtherNameQueryRq: Optional[Union[OtherNameQueryRq, List[OtherNameQueryRq]]]
    JobTypeQueryRq: Optional[Union[JobTypeQueryRq, List[JobTypeQueryRq]]]
    DataExtDefModRq: Optional[Union[DataExtDefModRq, List[DataExtDefModRq]]]
    ItemServiceQueryRq: Optional[Union[ItemServiceQueryRq, List[ItemServiceQueryRq]]]
    OtherNameModRq: Optional[Union[OtherNameModRq, List[OtherNameModRq]]]
    ClassModRq: Optional[Union[ClassModRq, List[ClassModRq]]]
    ToDoModRq: Optional[Union[ToDoModRq, List[ToDoModRq]]]
    ChargeAddRq: Optional[Union[ChargeAddRq, List[ChargeAddRq]]]
    TimeReportQueryRq: Optional[Union[TimeReportQueryRq, List[TimeReportQueryRq]]]
    TimeTrackingAddRq: Optional[Union[TimeTrackingAddRq, List[TimeTrackingAddRq]]]
    ItemSubtotalModRq: Optional[Union[ItemSubtotalModRq, List[ItemSubtotalModRq]]]
    SalesTaxPaymentCheckAddRq: Optional[Union[SalesTaxPaymentCheckAddRq, List[SalesTaxPaymentCheckAddRq]]]
    BarCodeQueryRq: Optional[Union[BarCodeQueryRq, List[BarCodeQueryRq]]]
    TransferModRq: Optional[Union[TransferModRq, List[TransferModRq]]]
    PayrollItemWageQueryRq: Optional[Union[PayrollItemWageQueryRq, List[PayrollItemWageQueryRq]]]
    ItemInventoryQueryRq: Optional[Union[ItemInventoryQueryRq, List[ItemInventoryQueryRq]]]
    EstimateQueryRq: Optional[Union[EstimateQueryRq, List[EstimateQueryRq]]]
    PurchaseOrderAddRq: Optional[Union[PurchaseOrderAddRq, List[PurchaseOrderAddRq]]]
    UnitOfMeasureSetAddRq: Optional[Union[UnitOfMeasureSetAddRq, List[UnitOfMeasureSetAddRq]]]
    CreditCardChargeQueryRq: Optional[Union[CreditCardChargeQueryRq, List[CreditCardChargeQueryRq]]]
    PurchaseOrderQueryRq: Optional[Union[PurchaseOrderQueryRq, List[PurchaseOrderQueryRq]]]
    CreditCardCreditQueryRq: Optional[Union[CreditCardCreditQueryRq, List[CreditCardCreditQueryRq]]]
    ListMergeRq: Optional[Union[ListMergeRq, List[ListMergeRq]]]
    CheckModRq: Optional[Union[CheckModRq, List[CheckModRq]]]
    PayrollItemWageAddRq: Optional[Union[PayrollItemWageAddRq, List[PayrollItemWageAddRq]]]
    EstimateModRq: Optional[Union[EstimateModRq, List[EstimateModRq]]]
    DataEventRecoveryInfoDelRq: Optional[Union[DataEventRecoveryInfoDelRq, List[DataEventRecoveryInfoDelRq]]]
    HostQueryRq: Optional[Union[HostQueryRq, List[HostQueryRq]]]
    BudgetSummaryReportQueryRq: Optional[Union[BudgetSummaryReportQueryRq, List[BudgetSummaryReportQueryRq]]]
    VendorTypeAddRq: Optional[Union[VendorTypeAddRq, List[VendorTypeAddRq]]]
    SalesOrderAddRq: Optional[Union[SalesOrderAddRq, List[SalesOrderAddRq]]]
    VehicleAddRq: Optional[Union[VehicleAddRq, List[VehicleAddRq]]]
    ItemSalesTaxGroupQueryRq: Optional[Union[ItemSalesTaxGroupQueryRq, List[ItemSalesTaxGroupQueryRq]]]
    ItemPaymentQueryRq: Optional[Union[ItemPaymentQueryRq, List[ItemPaymentQueryRq]]]
    ItemGroupModRq: Optional[Union[ItemGroupModRq, List[ItemGroupModRq]]]
    EntityQueryRq: Optional[Union[EntityQueryRq, List[EntityQueryRq]]]
    WorkersCompCodeModRq: Optional[Union[WorkersCompCodeModRq, List[WorkersCompCodeModRq]]]
    CompanyActivityQueryRq: Optional[Union[CompanyActivityQueryRq, List[CompanyActivityQueryRq]]]
    PaymentMethodAddRq: Optional[Union[PaymentMethodAddRq, List[PaymentMethodAddRq]]]
    InventoryAdjustmentModRq: Optional[Union[InventoryAdjustmentModRq, List[InventoryAdjustmentModRq]]]
    ItemServiceModRq: Optional[Union[ItemServiceModRq, List[ItemServiceModRq]]]
    BillPaymentCreditCardAddRq: Optional[Union[BillPaymentCreditCardAddRq, List[BillPaymentCreditCardAddRq]]]
    SalesReceiptModRq: Optional[Union[SalesReceiptModRq, List[SalesReceiptModRq]]]
    CustomerTypeAddRq: Optional[Union[CustomerTypeAddRq, List[CustomerTypeAddRq]]]
    CreditCardChargeModRq: Optional[Union[CreditCardChargeModRq, List[CreditCardChargeModRq]]]
    ItemDiscountAddRq: Optional[Union[ItemDiscountAddRq, List[ItemDiscountAddRq]]]
    SalesTaxCodeAddRq: Optional[Union[SalesTaxCodeAddRq, List[SalesTaxCodeAddRq]]]
    CreditMemoModRq: Optional[Union[CreditMemoModRq, List[CreditMemoModRq]]]
    ItemReceiptAddRq: Optional[Union[ItemReceiptAddRq, List[ItemReceiptAddRq]]]
    ItemOtherChargeModRq: Optional[Union[ItemOtherChargeModRq, List[ItemOtherChargeModRq]]]
    ItemNonInventoryAddRq: Optional[Union[ItemNonInventoryAddRq, List[ItemNonInventoryAddRq]]]
    ItemSalesTaxGroupModRq: Optional[Union[ItemSalesTaxGroupModRq, List[ItemSalesTaxGroupModRq]]]
    ListDisplayModRq: Optional[Union[ListDisplayModRq, List[ListDisplayModRq]]]
    VendorQueryRq: Optional[Union[VendorQueryRq, List[VendorQueryRq]]]
    ReceivePaymentModRq: Optional[Union[ReceivePaymentModRq, List[ReceivePaymentModRq]]]
    ItemOtherChargeQueryRq: Optional[Union[ItemOtherChargeQueryRq, List[ItemOtherChargeQueryRq]]]
    VehicleMileageQueryRq: Optional[Union[VehicleMileageQueryRq, List[VehicleMileageQueryRq]]]
    DataExtDelRq: Optional[Union[DataExtDelRq, List[DataExtDelRq]]]
    AgingReportQueryRq: Optional[Union[AgingReportQueryRq, List[AgingReportQueryRq]]]
    PaymentMethodQueryRq: Optional[Union[PaymentMethodQueryRq, List[PaymentMethodQueryRq]]]
    CurrencyQueryRq: Optional[Union[CurrencyQueryRq, List[CurrencyQueryRq]]]
    AccountAddRq: Optional[Union[AccountAddRq, List[AccountAddRq]]]
    VendorCreditAddRq: Optional[Union[VendorCreditAddRq, List[VendorCreditAddRq]]]
    ItemInventoryAssemblyModRq: Optional[Union[ItemInventoryAssemblyModRq, List[ItemInventoryAssemblyModRq]]]
    CustomerQueryRq: Optional[Union[CustomerQueryRq, List[CustomerQueryRq]]]
    CheckQueryRq: Optional[Union[CheckQueryRq, List[CheckQueryRq]]]
    DepositQueryRq: Optional[Union[DepositQueryRq, List[DepositQueryRq]]]
    CustomerTypeQueryRq: Optional[Union[CustomerTypeQueryRq, List[CustomerTypeQueryRq]]]
    TxnDisplayAddRq: Optional[Union[TxnDisplayAddRq, List[TxnDisplayAddRq]]]
    ListDelRq: Optional[Union[ListDelRq, List[ListDelRq]]]
    TxnDeletedQueryRq: Optional[Union[TxnDeletedQueryRq, List[TxnDeletedQueryRq]]]
    WorkersCompCodeQueryRq: Optional[Union[WorkersCompCodeQueryRq, List[WorkersCompCodeQueryRq]]]
    ItemGroupQueryRq: Optional[Union[ItemGroupQueryRq, List[ItemGroupQueryRq]]]
    ItemSalesTaxQueryRq: Optional[Union[ItemSalesTaxQueryRq, List[ItemSalesTaxQueryRq]]]
    CreditCardCreditModRq: Optional[Union[CreditCardCreditModRq, List[CreditCardCreditModRq]]]
    SalesRepModRq: Optional[Union[SalesRepModRq, List[SalesRepModRq]]]
    ClearedStatusModRq: Optional[Union[ClearedStatusModRq, List[ClearedStatusModRq]]]
    InventorySiteAddRq: Optional[Union[InventorySiteAddRq, List[InventorySiteAddRq]]]
    CompanyQueryRq: Optional[Union[CompanyQueryRq, List[CompanyQueryRq]]]
    ItemPaymentAddRq: Optional[Union[ItemPaymentAddRq, List[ItemPaymentAddRq]]]
    ItemSalesTaxAddRq: Optional[Union[ItemSalesTaxAddRq, List[ItemSalesTaxAddRq]]]
    SpecialAccountAddRq: Optional[Union[SpecialAccountAddRq, List[SpecialAccountAddRq]]]
    Form1099CategoryAccountMappingQueryRq: Optional[Union[Form1099CategoryAccountMappingQueryRq, List[Form1099CategoryAccountMappingQueryRq]]]
    BillPaymentCheckModRq: Optional[Union[BillPaymentCheckModRq, List[BillPaymentCheckModRq]]]
    ItemNonInventoryQueryRq: Optional[Union[ItemNonInventoryQueryRq, List[ItemNonInventoryQueryRq]]]
    ARRefundCreditCardAddRq: Optional[Union[ARRefundCreditCardAddRq, List[ARRefundCreditCardAddRq]]]
    TxnDelRq: Optional[Union[TxnDelRq, List[TxnDelRq]]]
    TransferInventoryModRq: Optional[Union[TransferInventoryModRq, List[TransferInventoryModRq]]]
    DepositModRq: Optional[Union[DepositModRq, List[DepositModRq]]]
    ItemFixedAssetQueryRq: Optional[Union[ItemFixedAssetQueryRq, List[ItemFixedAssetQueryRq]]]
    AccountQueryRq: Optional[Union[AccountQueryRq, List[AccountQueryRq]]]
    TxnVoidRq: Optional[Union[TxnVoidRq, List[TxnVoidRq]]]
    SpecialItemAddRq: Optional[Union[SpecialItemAddRq, List[SpecialItemAddRq]]]
    DataExtAddRq: Optional[Union[DataExtAddRq, List[DataExtAddRq]]]
    PriceLevelAddRq: Optional[Union[PriceLevelAddRq, List[PriceLevelAddRq]]]
    JobReportQueryRq: Optional[Union[JobReportQueryRq, List[JobReportQueryRq]]]
    InventoryAdjustmentQueryRq: Optional[Union[InventoryAdjustmentQueryRq, List[InventoryAdjustmentQueryRq]]]
    JournalEntryModRq: Optional[Union[JournalEntryModRq, List[JournalEntryModRq]]]
    ItemFixedAssetModRq: Optional[Union[ItemFixedAssetModRq, List[ItemFixedAssetModRq]]]
    CurrencyModRq: Optional[Union[CurrencyModRq, List[CurrencyModRq]]]
    InvoiceModRq: Optional[Union[InvoiceModRq, List[InvoiceModRq]]]
    CustomSummaryReportQueryRq: Optional[Union[CustomSummaryReportQueryRq, List[CustomSummaryReportQueryRq]]]
    CustomerMsgQueryRq: Optional[Union[CustomerMsgQueryRq, List[CustomerMsgQueryRq]]]
    BillAddRq: Optional[Union[BillAddRq, List[BillAddRq]]]
    JournalEntryQueryRq: Optional[Union[JournalEntryQueryRq, List[JournalEntryQueryRq]]]
    CustomDetailReportQueryRq: Optional[Union[CustomDetailReportQueryRq, List[CustomDetailReportQueryRq]]]
    VendorCreditQueryRq: Optional[Union[VendorCreditQueryRq, List[VendorCreditQueryRq]]]
    SalesTaxCodeQueryRq: Optional[Union[SalesTaxCodeQueryRq, List[SalesTaxCodeQueryRq]]]
    EmployeeQueryRq: Optional[Union[EmployeeQueryRq, List[EmployeeQueryRq]]]
    PayrollDetailReportQueryRq: Optional[Union[PayrollDetailReportQueryRq, List[PayrollDetailReportQueryRq]]]


class QBXMLMsgsRs(TypedDict, total=False):
    CustomerMsgAddRs: Optional[Union[CustomerMsgAddRs, List[CustomerMsgAddRs]]]
    ItemSubtotalAddRs: Optional[Union[ItemSubtotalAddRs, List[ItemSubtotalAddRs]]]
    SalesTaxPaymentCheckModRs: Optional[Union[SalesTaxPaymentCheckModRs, List[SalesTaxPaymentCheckModRs]]]
    TimeTrackingModRs: Optional[Union[TimeTrackingModRs, List[TimeTrackingModRs]]]
    ChargeModRs: Optional[Union[ChargeModRs, List[ChargeModRs]]]
    PurchaseOrderModRs: Optional[Union[PurchaseOrderModRs, List[PurchaseOrderModRs]]]
    ItemReceiptQueryRs: Optional[Union[ItemReceiptQueryRs, List[ItemReceiptQueryRs]]]
    TransferAddRs: Optional[Union[TransferAddRs, List[TransferAddRs]]]
    TimeTrackingQueryRs: Optional[Union[TimeTrackingQueryRs, List[TimeTrackingQueryRs]]]
    ItemInventoryModRs: Optional[Union[ItemInventoryModRs, List[ItemInventoryModRs]]]
    BuildAssemblyModRs: Optional[Union[BuildAssemblyModRs, List[BuildAssemblyModRs]]]
    ListDeletedQueryRs: Optional[Union[ListDeletedQueryRs, List[ListDeletedQueryRs]]]
    ToDoAddRs: Optional[Union[ToDoAddRs, List[ToDoAddRs]]]
    ReceivePaymentQueryRs: Optional[Union[ReceivePaymentQueryRs, List[ReceivePaymentQueryRs]]]
    PreferencesQueryRs: Optional[Union[PreferencesQueryRs, List[PreferencesQueryRs]]]
    ClassAddRs: Optional[Union[ClassAddRs, List[ClassAddRs]]]
    DataExtDefAddRs: Optional[Union[DataExtDefAddRs, List[DataExtDefAddRs]]]
    OtherNameAddRs: Optional[Union[OtherNameAddRs, List[OtherNameAddRs]]]
    ReceivePaymentToDepositQueryRs: Optional[Union[ReceivePaymentToDepositQueryRs, List[ReceivePaymentToDepositQueryRs]]]
    UnitOfMeasureSetQueryRs: Optional[Union[UnitOfMeasureSetQueryRs, List[UnitOfMeasureSetQueryRs]]]
    DataExtDefQueryRs: Optional[Union[DataExtDefQueryRs, List[DataExtDefQueryRs]]]
    SalesOrderModRs: Optional[Union[SalesOrderModRs, List[SalesOrderModRs]]]
    ChargeQueryRs: Optional[Union[ChargeQueryRs, List[ChargeQueryRs]]]
    VehicleModRs: Optional[Union[VehicleModRs, List[VehicleModRs]]]
    VehicleMileageAddRs: Optional[Union[VehicleMileageAddRs, List[VehicleMileageAddRs]]]
    CheckAddRs: Optional[Union[CheckAddRs, List[CheckAddRs]]]
    PriceLevelQueryRs: Optional[Union[PriceLevelQueryRs, List[PriceLevelQueryRs]]]
    BillQueryRs: Optional[Union[BillQueryRs, List[BillQueryRs]]]
    ItemSubtotalQueryRs: Optional[Union[ItemSubtotalQueryRs, List[ItemSubtotalQueryRs]]]
    EstimateAddRs: Optional[Union[EstimateAddRs, List[EstimateAddRs]]]
    ToDoQueryRs: Optional[Union[ToDoQueryRs, List[ToDoQueryRs]]]
    DataExtDefDelRs: Optional[Union[DataExtDefDelRs, List[DataExtDefDelRs]]]
    JobTypeAddRs: Optional[Union[JobTypeAddRs, List[JobTypeAddRs]]]
    InventoryAdjustmentAddRs: Optional[Union[InventoryAdjustmentAddRs, List[InventoryAdjustmentAddRs]]]
    ItemServiceAddRs: Optional[Union[ItemServiceAddRs, List[ItemServiceAddRs]]]
    SalesTaxPaymentCheckQueryRs: Optional[Union[SalesTaxPaymentCheckQueryRs, List[SalesTaxPaymentCheckQueryRs]]]
    ItemDiscountQueryRs: Optional[Union[ItemDiscountQueryRs, List[ItemDiscountQueryRs]]]
    ItemGroupAddRs: Optional[Union[ItemGroupAddRs, List[ItemGroupAddRs]]]
    CreditMemoQueryRs: Optional[Union[CreditMemoQueryRs, List[CreditMemoQueryRs]]]
    StandardTermsAddRs: Optional[Union[StandardTermsAddRs, List[StandardTermsAddRs]]]
    BillingRateAddRs: Optional[Union[BillingRateAddRs, List[BillingRateAddRs]]]
    WorkersCompCodeAddRs: Optional[Union[WorkersCompCodeAddRs, List[WorkersCompCodeAddRs]]]
    ItemOtherChargeAddRs: Optional[Union[ItemOtherChargeAddRs, List[ItemOtherChargeAddRs]]]
    BillPaymentCreditCardQueryRs: Optional[Union[BillPaymentCreditCardQueryRs, List[BillPaymentCreditCardQueryRs]]]
    TermsQueryRs: Optional[Union[TermsQueryRs, List[TermsQueryRs]]]
    ItemNonInventoryModRs: Optional[Union[ItemNonInventoryModRs, List[ItemNonInventoryModRs]]]
    ItemSalesTaxGroupAddRs: Optional[Union[ItemSalesTaxGroupAddRs, List[ItemSalesTaxGroupAddRs]]]
    ItemReceiptModRs: Optional[Union[ItemReceiptModRs, List[ItemReceiptModRs]]]
    CreditMemoAddRs: Optional[Union[CreditMemoAddRs, List[CreditMemoAddRs]]]
    ReceivePaymentAddRs: Optional[Union[ReceivePaymentAddRs, List[ReceivePaymentAddRs]]]
    PayrollItemNonWageQueryRs: Optional[Union[PayrollItemNonWageQueryRs, List[PayrollItemNonWageQueryRs]]]
    SalesReceiptAddRs: Optional[Union[SalesReceiptAddRs, List[SalesReceiptAddRs]]]
    ShipMethodAddRs: Optional[Union[ShipMethodAddRs, List[ShipMethodAddRs]]]
    SalesTaxCodeModRs: Optional[Union[SalesTaxCodeModRs, List[SalesTaxCodeModRs]]]
    ItemDiscountModRs: Optional[Union[ItemDiscountModRs, List[ItemDiscountModRs]]]
    CreditCardChargeAddRs: Optional[Union[CreditCardChargeAddRs, List[CreditCardChargeAddRs]]]
    SalesReceiptQueryRs: Optional[Union[SalesReceiptQueryRs, List[SalesReceiptQueryRs]]]
    VendorTypeQueryRs: Optional[Union[VendorTypeQueryRs, List[VendorTypeQueryRs]]]
    VehicleQueryRs: Optional[Union[VehicleQueryRs, List[VehicleQueryRs]]]
    BillingRateQueryRs: Optional[Union[BillingRateQueryRs, List[BillingRateQueryRs]]]
    VendorCreditModRs: Optional[Union[VendorCreditModRs, List[VendorCreditModRs]]]
    ItemSitesQueryRs: Optional[Union[ItemSitesQueryRs, List[ItemSitesQueryRs]]]
    ItemInventoryAssemblyAddRs: Optional[Union[ItemInventoryAssemblyAddRs, List[ItemInventoryAssemblyAddRs]]]
    StandardTermsQueryRs: Optional[Union[StandardTermsQueryRs, List[StandardTermsQueryRs]]]
    BillPaymentCheckQueryRs: Optional[Union[BillPaymentCheckQueryRs, List[BillPaymentCheckQueryRs]]]
    ItemQueryRs: Optional[Union[ItemQueryRs, List[ItemQueryRs]]]
    ItemInventoryAssemblyQueryRs: Optional[Union[ItemInventoryAssemblyQueryRs, List[ItemInventoryAssemblyQueryRs]]]
    TransactionQueryRs: Optional[Union[TransactionQueryRs, List[TransactionQueryRs]]]
    SalesTaxPayableQueryRs: Optional[Union[SalesTaxPayableQueryRs, List[SalesTaxPayableQueryRs]]]
    BuildAssemblyQueryRs: Optional[Union[BuildAssemblyQueryRs, List[BuildAssemblyQueryRs]]]
    AccountModRs: Optional[Union[AccountModRs, List[AccountModRs]]]
    ItemPaymentModRs: Optional[Union[ItemPaymentModRs, List[ItemPaymentModRs]]]
    DateDrivenTermsAddRs: Optional[Union[DateDrivenTermsAddRs, List[DateDrivenTermsAddRs]]]
    ItemSalesTaxModRs: Optional[Union[ItemSalesTaxModRs, List[ItemSalesTaxModRs]]]
    BillPaymentCheckAddRs: Optional[Union[BillPaymentCheckAddRs, List[BillPaymentCheckAddRs]]]
    InventorySiteModRs: Optional[Union[InventorySiteModRs, List[InventorySiteModRs]]]
    TemplateQueryRs: Optional[Union[TemplateQueryRs, List[TemplateQueryRs]]]
    CreditCardCreditAddRs: Optional[Union[CreditCardCreditAddRs, List[CreditCardCreditAddRs]]]
    SalesOrderQueryRs: Optional[Union[SalesOrderQueryRs, List[SalesOrderQueryRs]]]
    SalesRepAddRs: Optional[Union[SalesRepAddRs, List[SalesRepAddRs]]]
    Form1099CategoryAccountMappingModRs: Optional[Union[Form1099CategoryAccountMappingModRs, List[Form1099CategoryAccountMappingModRs]]]
    SalesRepQueryRs: Optional[Union[SalesRepQueryRs, List[SalesRepQueryRs]]]
    InventorySiteQueryRs: Optional[Union[InventorySiteQueryRs, List[InventorySiteQueryRs]]]
    ClassQueryRs: Optional[Union[ClassQueryRs, List[ClassQueryRs]]]
    DataExtModRs: Optional[Union[DataExtModRs, List[DataExtModRs]]]
    SalesTaxReturnLineQueryRs: Optional[Union[SalesTaxReturnLineQueryRs, List[SalesTaxReturnLineQueryRs]]]
    PriceLevelModRs: Optional[Union[PriceLevelModRs, List[PriceLevelModRs]]]
    DataEventRecoveryInfoQueryRs: Optional[Union[DataEventRecoveryInfoQueryRs, List[DataEventRecoveryInfoQueryRs]]]
    DepositAddRs: Optional[Union[DepositAddRs, List[DepositAddRs]]]
    TransferInventoryAddRs: Optional[Union[TransferInventoryAddRs, List[TransferInventoryAddRs]]]
    DateDrivenTermsQueryRs: Optional[Union[DateDrivenTermsQueryRs, List[DateDrivenTermsQueryRs]]]
    BillModRs: Optional[Union[BillModRs, List[BillModRs]]]
    BillToPayQueryRs: Optional[Union[BillToPayQueryRs, List[BillToPayQueryRs]]]
    TransferQueryRs: Optional[Union[TransferQueryRs, List[TransferQueryRs]]]
    ARRefundCreditCardQueryRs: Optional[Union[ARRefundCreditCardQueryRs, List[ARRefundCreditCardQueryRs]]]
    InvoiceQueryRs: Optional[Union[InvoiceQueryRs, List[InvoiceQueryRs]]]
    ItemAssembliesCanBuildQueryRs: Optional[Union[ItemAssembliesCanBuildQueryRs, List[ItemAssembliesCanBuildQueryRs]]]
    ItemFixedAssetAddRs: Optional[Union[ItemFixedAssetAddRs, List[ItemFixedAssetAddRs]]]
    CurrencyAddRs: Optional[Union[CurrencyAddRs, List[CurrencyAddRs]]]
    JournalEntryAddRs: Optional[Union[JournalEntryAddRs, List[JournalEntryAddRs]]]
    InvoiceAddRs: Optional[Union[InvoiceAddRs, List[InvoiceAddRs]]]
    TransferInventoryQueryRs: Optional[Union[TransferInventoryQueryRs, List[TransferInventoryQueryRs]]]
    ShipMethodQueryRs: Optional[Union[ShipMethodQueryRs, List[ShipMethodQueryRs]]]
    BuildAssemblyAddRs: Optional[Union[BuildAssemblyAddRs, List[BuildAssemblyAddRs]]]
    ItemInventoryAddRs: Optional[Union[ItemInventoryAddRs, List[ItemInventoryAddRs]]]
    OtherNameQueryRs: Optional[Union[OtherNameQueryRs, List[OtherNameQueryRs]]]
    JobTypeQueryRs: Optional[Union[JobTypeQueryRs, List[JobTypeQueryRs]]]
    DataExtDefModRs: Optional[Union[DataExtDefModRs, List[DataExtDefModRs]]]
    ItemServiceQueryRs: Optional[Union[ItemServiceQueryRs, List[ItemServiceQueryRs]]]
    OtherNameModRs: Optional[Union[OtherNameModRs, List[OtherNameModRs]]]
    ClassModRs: Optional[Union[ClassModRs, List[ClassModRs]]]
    ToDoModRs: Optional[Union[ToDoModRs, List[ToDoModRs]]]
    ChargeAddRs: Optional[Union[ChargeAddRs, List[ChargeAddRs]]]
    TimeTrackingAddRs: Optional[Union[TimeTrackingAddRs, List[TimeTrackingAddRs]]]
    ItemSubtotalModRs: Optional[Union[ItemSubtotalModRs, List[ItemSubtotalModRs]]]
    SalesTaxPaymentCheckAddRs: Optional[Union[SalesTaxPaymentCheckAddRs, List[SalesTaxPaymentCheckAddRs]]]
    BarCodeQueryRs: Optional[Union[BarCodeQueryRs, List[BarCodeQueryRs]]]
    TransferModRs: Optional[Union[TransferModRs, List[TransferModRs]]]
    PayrollItemWageQueryRs: Optional[Union[PayrollItemWageQueryRs, List[PayrollItemWageQueryRs]]]
    ItemInventoryQueryRs: Optional[Union[ItemInventoryQueryRs, List[ItemInventoryQueryRs]]]
    EstimateQueryRs: Optional[Union[EstimateQueryRs, List[EstimateQueryRs]]]
    PurchaseOrderAddRs: Optional[Union[PurchaseOrderAddRs, List[PurchaseOrderAddRs]]]
    UnitOfMeasureSetAddRs: Optional[Union[UnitOfMeasureSetAddRs, List[UnitOfMeasureSetAddRs]]]
    CreditCardChargeQueryRs: Optional[Union[CreditCardChargeQueryRs, List[CreditCardChargeQueryRs]]]
    PurchaseOrderQueryRs: Optional[Union[PurchaseOrderQueryRs, List[PurchaseOrderQueryRs]]]
    CreditCardCreditQueryRs: Optional[Union[CreditCardCreditQueryRs, List[CreditCardCreditQueryRs]]]
    ListMergeRs: Optional[Union[ListMergeRs, List[ListMergeRs]]]
    CheckModRs: Optional[Union[CheckModRs, List[CheckModRs]]]
    PayrollItemWageAddRs: Optional[Union[PayrollItemWageAddRs, List[PayrollItemWageAddRs]]]
    EstimateModRs: Optional[Union[EstimateModRs, List[EstimateModRs]]]
    HostQueryRs: Optional[Union[HostQueryRs, List[HostQueryRs]]]
    VendorTypeAddRs: Optional[Union[VendorTypeAddRs, List[VendorTypeAddRs]]]
    SalesOrderAddRs: Optional[Union[SalesOrderAddRs, List[SalesOrderAddRs]]]
    VehicleAddRs: Optional[Union[VehicleAddRs, List[VehicleAddRs]]]
    ItemSalesTaxGroupQueryRs: Optional[Union[ItemSalesTaxGroupQueryRs, List[ItemSalesTaxGroupQueryRs]]]
    ItemPaymentQueryRs: Optional[Union[ItemPaymentQueryRs, List[ItemPaymentQueryRs]]]
    ItemGroupModRs: Optional[Union[ItemGroupModRs, List[ItemGroupModRs]]]
    WorkersCompCodeModRs: Optional[Union[WorkersCompCodeModRs, List[WorkersCompCodeModRs]]]
    CompanyActivityQueryRs: Optional[Union[CompanyActivityQueryRs, List[CompanyActivityQueryRs]]]
    PaymentMethodAddRs: Optional[Union[PaymentMethodAddRs, List[PaymentMethodAddRs]]]
    InventoryAdjustmentModRs: Optional[Union[InventoryAdjustmentModRs, List[InventoryAdjustmentModRs]]]
    ItemServiceModRs: Optional[Union[ItemServiceModRs, List[ItemServiceModRs]]]
    BillPaymentCreditCardAddRs: Optional[Union[BillPaymentCreditCardAddRs, List[BillPaymentCreditCardAddRs]]]
    SalesReceiptModRs: Optional[Union[SalesReceiptModRs, List[SalesReceiptModRs]]]
    CustomerTypeAddRs: Optional[Union[CustomerTypeAddRs, List[CustomerTypeAddRs]]]
    CreditCardChargeModRs: Optional[Union[CreditCardChargeModRs, List[CreditCardChargeModRs]]]
    ItemDiscountAddRs: Optional[Union[ItemDiscountAddRs, List[ItemDiscountAddRs]]]
    SalesTaxCodeAddRs: Optional[Union[SalesTaxCodeAddRs, List[SalesTaxCodeAddRs]]]
    CreditMemoModRs: Optional[Union[CreditMemoModRs, List[CreditMemoModRs]]]
    ItemReceiptAddRs: Optional[Union[ItemReceiptAddRs, List[ItemReceiptAddRs]]]
    ItemOtherChargeModRs: Optional[Union[ItemOtherChargeModRs, List[ItemOtherChargeModRs]]]
    ItemNonInventoryAddRs: Optional[Union[ItemNonInventoryAddRs, List[ItemNonInventoryAddRs]]]
    ItemSalesTaxGroupModRs: Optional[Union[ItemSalesTaxGroupModRs, List[ItemSalesTaxGroupModRs]]]
    ReceivePaymentModRs: Optional[Union[ReceivePaymentModRs, List[ReceivePaymentModRs]]]
    ItemOtherChargeQueryRs: Optional[Union[ItemOtherChargeQueryRs, List[ItemOtherChargeQueryRs]]]
    VehicleMileageQueryRs: Optional[Union[VehicleMileageQueryRs, List[VehicleMileageQueryRs]]]
    DataExtDelRs: Optional[Union[DataExtDelRs, List[DataExtDelRs]]]
    PaymentMethodQueryRs: Optional[Union[PaymentMethodQueryRs, List[PaymentMethodQueryRs]]]
    CurrencyQueryRs: Optional[Union[CurrencyQueryRs, List[CurrencyQueryRs]]]
    AccountAddRs: Optional[Union[AccountAddRs, List[AccountAddRs]]]
    VendorCreditAddRs: Optional[Union[VendorCreditAddRs, List[VendorCreditAddRs]]]
    ItemInventoryAssemblyModRs: Optional[Union[ItemInventoryAssemblyModRs, List[ItemInventoryAssemblyModRs]]]
    CheckQueryRs: Optional[Union[CheckQueryRs, List[CheckQueryRs]]]
    DepositQueryRs: Optional[Union[DepositQueryRs, List[DepositQueryRs]]]
    CustomerTypeQueryRs: Optional[Union[CustomerTypeQueryRs, List[CustomerTypeQueryRs]]]
    ListDelRs: Optional[Union[ListDelRs, List[ListDelRs]]]
    TxnDeletedQueryRs: Optional[Union[TxnDeletedQueryRs, List[TxnDeletedQueryRs]]]
    WorkersCompCodeQueryRs: Optional[Union[WorkersCompCodeQueryRs, List[WorkersCompCodeQueryRs]]]
    ItemGroupQueryRs: Optional[Union[ItemGroupQueryRs, List[ItemGroupQueryRs]]]
    ItemSalesTaxQueryRs: Optional[Union[ItemSalesTaxQueryRs, List[ItemSalesTaxQueryRs]]]
    CreditCardCreditModRs: Optional[Union[CreditCardCreditModRs, List[CreditCardCreditModRs]]]
    SalesRepModRs: Optional[Union[SalesRepModRs, List[SalesRepModRs]]]
    InventorySiteAddRs: Optional[Union[InventorySiteAddRs, List[InventorySiteAddRs]]]
    CompanyQueryRs: Optional[Union[CompanyQueryRs, List[CompanyQueryRs]]]
    ItemPaymentAddRs: Optional[Union[ItemPaymentAddRs, List[ItemPaymentAddRs]]]
    ItemSalesTaxAddRs: Optional[Union[ItemSalesTaxAddRs, List[ItemSalesTaxAddRs]]]
    SpecialAccountAddRs: Optional[Union[SpecialAccountAddRs, List[SpecialAccountAddRs]]]
    Form1099CategoryAccountMappingQueryRs: Optional[Union[Form1099CategoryAccountMappingQueryRs, List[Form1099CategoryAccountMappingQueryRs]]]
    BillPaymentCheckModRs: Optional[Union[BillPaymentCheckModRs, List[BillPaymentCheckModRs]]]
    ItemNonInventoryQueryRs: Optional[Union[ItemNonInventoryQueryRs, List[ItemNonInventoryQueryRs]]]
    ARRefundCreditCardAddRs: Optional[Union[ARRefundCreditCardAddRs, List[ARRefundCreditCardAddRs]]]
    TxnDelRs: Optional[Union[TxnDelRs, List[TxnDelRs]]]
    TransferInventoryModRs: Optional[Union[TransferInventoryModRs, List[TransferInventoryModRs]]]
    DepositModRs: Optional[Union[DepositModRs, List[DepositModRs]]]
    ItemFixedAssetQueryRs: Optional[Union[ItemFixedAssetQueryRs, List[ItemFixedAssetQueryRs]]]
    AccountQueryRs: Optional[Union[AccountQueryRs, List[AccountQueryRs]]]
    TxnVoidRs: Optional[Union[TxnVoidRs, List[TxnVoidRs]]]
    SpecialItemAddRs: Optional[Union[SpecialItemAddRs, List[SpecialItemAddRs]]]
    DataExtAddRs: Optional[Union[DataExtAddRs, List[DataExtAddRs]]]
    PriceLevelAddRs: Optional[Union[PriceLevelAddRs, List[PriceLevelAddRs]]]
    InventoryAdjustmentQueryRs: Optional[Union[InventoryAdjustmentQueryRs, List[InventoryAdjustmentQueryRs]]]
    JournalEntryModRs: Optional[Union[JournalEntryModRs, List[JournalEntryModRs]]]
    ItemFixedAssetModRs: Optional[Union[ItemFixedAssetModRs, List[ItemFixedAssetModRs]]]
    CurrencyModRs: Optional[Union[CurrencyModRs, List[CurrencyModRs]]]
    InvoiceModRs: Optional[Union[InvoiceModRs, List[InvoiceModRs]]]
    CustomerMsgQueryRs: Optional[Union[CustomerMsgQueryRs, List[CustomerMsgQueryRs]]]
    BillAddRs: Optional[Union[BillAddRs, List[BillAddRs]]]
    JournalEntryQueryRs: Optional[Union[JournalEntryQueryRs, List[JournalEntryQueryRs]]]
    VendorCreditQueryRs: Optional[Union[VendorCreditQueryRs, List[VendorCreditQueryRs]]]
    SalesTaxCodeQueryRs: Optional[Union[SalesTaxCodeQueryRs, List[SalesTaxCodeQueryRs]]]
