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
    CustomerMsgAddRq: Union[CustomerMsgAddRq, List[CustomerMsgAddRq]]
    ItemSubtotalAddRq: Union[ItemSubtotalAddRq, List[ItemSubtotalAddRq]]
    SalesTaxPaymentCheckModRq: Union[SalesTaxPaymentCheckModRq, List[SalesTaxPaymentCheckModRq]]
    TimeTrackingModRq: Union[TimeTrackingModRq, List[TimeTrackingModRq]]
    ChargeModRq: Union[ChargeModRq, List[ChargeModRq]]
    PurchaseOrderModRq: Union[PurchaseOrderModRq, List[PurchaseOrderModRq]]
    ItemReceiptQueryRq: Union[ItemReceiptQueryRq, List[ItemReceiptQueryRq]]
    TransferAddRq: Union[TransferAddRq, List[TransferAddRq]]
    TimeTrackingQueryRq: Union[TimeTrackingQueryRq, List[TimeTrackingQueryRq]]
    ItemInventoryModRq: Union[ItemInventoryModRq, List[ItemInventoryModRq]]
    BuildAssemblyModRq: Union[BuildAssemblyModRq, List[BuildAssemblyModRq]]
    GeneralDetailReportQueryRq: Union[GeneralDetailReportQueryRq, List[GeneralDetailReportQueryRq]]
    ListDeletedQueryRq: Union[ListDeletedQueryRq, List[ListDeletedQueryRq]]
    ToDoAddRq: Union[ToDoAddRq, List[ToDoAddRq]]
    ReceivePaymentQueryRq: Union[ReceivePaymentQueryRq, List[ReceivePaymentQueryRq]]
    PreferencesQueryRq: Union[PreferencesQueryRq, List[PreferencesQueryRq]]
    ClassAddRq: Union[ClassAddRq, List[ClassAddRq]]
    DataExtDefAddRq: Union[DataExtDefAddRq, List[DataExtDefAddRq]]
    OtherNameAddRq: Union[OtherNameAddRq, List[OtherNameAddRq]]
    ReceivePaymentToDepositQueryRq: Union[ReceivePaymentToDepositQueryRq, List[ReceivePaymentToDepositQueryRq]]
    UnitOfMeasureSetQueryRq: Union[UnitOfMeasureSetQueryRq, List[UnitOfMeasureSetQueryRq]]
    DataExtDefQueryRq: Union[DataExtDefQueryRq, List[DataExtDefQueryRq]]
    SalesOrderModRq: Union[SalesOrderModRq, List[SalesOrderModRq]]
    ChargeQueryRq: Union[ChargeQueryRq, List[ChargeQueryRq]]
    VehicleModRq: Union[VehicleModRq, List[VehicleModRq]]
    VehicleMileageAddRq: Union[VehicleMileageAddRq, List[VehicleMileageAddRq]]
    CheckAddRq: Union[CheckAddRq, List[CheckAddRq]]
    PriceLevelQueryRq: Union[PriceLevelQueryRq, List[PriceLevelQueryRq]]
    BillQueryRq: Union[BillQueryRq, List[BillQueryRq]]
    ItemSubtotalQueryRq: Union[ItemSubtotalQueryRq, List[ItemSubtotalQueryRq]]
    EstimateAddRq: Union[EstimateAddRq, List[EstimateAddRq]]
    ToDoQueryRq: Union[ToDoQueryRq, List[ToDoQueryRq]]
    DataExtDefDelRq: Union[DataExtDefDelRq, List[DataExtDefDelRq]]
    JobTypeAddRq: Union[JobTypeAddRq, List[JobTypeAddRq]]
    InventoryAdjustmentAddRq: Union[InventoryAdjustmentAddRq, List[InventoryAdjustmentAddRq]]
    ItemServiceAddRq: Union[ItemServiceAddRq, List[ItemServiceAddRq]]
    SalesTaxPaymentCheckQueryRq: Union[SalesTaxPaymentCheckQueryRq, List[SalesTaxPaymentCheckQueryRq]]
    ItemDiscountQueryRq: Union[ItemDiscountQueryRq, List[ItemDiscountQueryRq]]
    ItemGroupAddRq: Union[ItemGroupAddRq, List[ItemGroupAddRq]]
    CreditMemoQueryRq: Union[CreditMemoQueryRq, List[CreditMemoQueryRq]]
    StandardTermsAddRq: Union[StandardTermsAddRq, List[StandardTermsAddRq]]
    BillingRateAddRq: Union[BillingRateAddRq, List[BillingRateAddRq]]
    WorkersCompCodeAddRq: Union[WorkersCompCodeAddRq, List[WorkersCompCodeAddRq]]
    ItemOtherChargeAddRq: Union[ItemOtherChargeAddRq, List[ItemOtherChargeAddRq]]
    BillPaymentCreditCardQueryRq: Union[BillPaymentCreditCardQueryRq, List[BillPaymentCreditCardQueryRq]]
    TermsQueryRq: Union[TermsQueryRq, List[TermsQueryRq]]
    ListDisplayAddRq: Union[ListDisplayAddRq, List[ListDisplayAddRq]]
    ItemNonInventoryModRq: Union[ItemNonInventoryModRq, List[ItemNonInventoryModRq]]
    ItemSalesTaxGroupAddRq: Union[ItemSalesTaxGroupAddRq, List[ItemSalesTaxGroupAddRq]]
    ItemReceiptModRq: Union[ItemReceiptModRq, List[ItemReceiptModRq]]
    CreditMemoAddRq: Union[CreditMemoAddRq, List[CreditMemoAddRq]]
    PayrollSummaryReportQueryRq: Union[PayrollSummaryReportQueryRq, List[PayrollSummaryReportQueryRq]]
    ReceivePaymentAddRq: Union[ReceivePaymentAddRq, List[ReceivePaymentAddRq]]
    PayrollItemNonWageQueryRq: Union[PayrollItemNonWageQueryRq, List[PayrollItemNonWageQueryRq]]
    SalesReceiptAddRq: Union[SalesReceiptAddRq, List[SalesReceiptAddRq]]
    GeneralSummaryReportQueryRq: Union[GeneralSummaryReportQueryRq, List[GeneralSummaryReportQueryRq]]
    ShipMethodAddRq: Union[ShipMethodAddRq, List[ShipMethodAddRq]]
    SalesTaxCodeModRq: Union[SalesTaxCodeModRq, List[SalesTaxCodeModRq]]
    ItemDiscountModRq: Union[ItemDiscountModRq, List[ItemDiscountModRq]]
    CreditCardChargeAddRq: Union[CreditCardChargeAddRq, List[CreditCardChargeAddRq]]
    SalesReceiptQueryRq: Union[SalesReceiptQueryRq, List[SalesReceiptQueryRq]]
    VendorTypeQueryRq: Union[VendorTypeQueryRq, List[VendorTypeQueryRq]]
    VehicleQueryRq: Union[VehicleQueryRq, List[VehicleQueryRq]]
    BillingRateQueryRq: Union[BillingRateQueryRq, List[BillingRateQueryRq]]
    VendorCreditModRq: Union[VendorCreditModRq, List[VendorCreditModRq]]
    ItemSitesQueryRq: Union[ItemSitesQueryRq, List[ItemSitesQueryRq]]
    ItemInventoryAssemblyAddRq: Union[ItemInventoryAssemblyAddRq, List[ItemInventoryAssemblyAddRq]]
    TxnDisplayModRq: Union[TxnDisplayModRq, List[TxnDisplayModRq]]
    StandardTermsQueryRq: Union[StandardTermsQueryRq, List[StandardTermsQueryRq]]
    BillPaymentCheckQueryRq: Union[BillPaymentCheckQueryRq, List[BillPaymentCheckQueryRq]]
    ItemQueryRq: Union[ItemQueryRq, List[ItemQueryRq]]
    ItemInventoryAssemblyQueryRq: Union[ItemInventoryAssemblyQueryRq, List[ItemInventoryAssemblyQueryRq]]
    TransactionQueryRq: Union[TransactionQueryRq, List[TransactionQueryRq]]
    SalesTaxPayableQueryRq: Union[SalesTaxPayableQueryRq, List[SalesTaxPayableQueryRq]]
    BuildAssemblyQueryRq: Union[BuildAssemblyQueryRq, List[BuildAssemblyQueryRq]]
    AccountModRq: Union[AccountModRq, List[AccountModRq]]
    ItemPaymentModRq: Union[ItemPaymentModRq, List[ItemPaymentModRq]]
    DateDrivenTermsAddRq: Union[DateDrivenTermsAddRq, List[DateDrivenTermsAddRq]]
    ItemSalesTaxModRq: Union[ItemSalesTaxModRq, List[ItemSalesTaxModRq]]
    BillPaymentCheckAddRq: Union[BillPaymentCheckAddRq, List[BillPaymentCheckAddRq]]
    InventorySiteModRq: Union[InventorySiteModRq, List[InventorySiteModRq]]
    TemplateQueryRq: Union[TemplateQueryRq, List[TemplateQueryRq]]
    CreditCardCreditAddRq: Union[CreditCardCreditAddRq, List[CreditCardCreditAddRq]]
    SalesOrderQueryRq: Union[SalesOrderQueryRq, List[SalesOrderQueryRq]]
    SalesRepAddRq: Union[SalesRepAddRq, List[SalesRepAddRq]]
    Form1099CategoryAccountMappingModRq: Union[Form1099CategoryAccountMappingModRq, List[Form1099CategoryAccountMappingModRq]]
    SalesRepQueryRq: Union[SalesRepQueryRq, List[SalesRepQueryRq]]
    InventorySiteQueryRq: Union[InventorySiteQueryRq, List[InventorySiteQueryRq]]
    ClassQueryRq: Union[ClassQueryRq, List[ClassQueryRq]]
    DataExtModRq: Union[DataExtModRq, List[DataExtModRq]]
    SalesTaxReturnLineQueryRq: Union[SalesTaxReturnLineQueryRq, List[SalesTaxReturnLineQueryRq]]
    PriceLevelModRq: Union[PriceLevelModRq, List[PriceLevelModRq]]
    DataEventRecoveryInfoQueryRq: Union[DataEventRecoveryInfoQueryRq, List[DataEventRecoveryInfoQueryRq]]
    LeadQueryRq: Union[LeadQueryRq, List[LeadQueryRq]]
    DepositAddRq: Union[DepositAddRq, List[DepositAddRq]]
    TransferInventoryAddRq: Union[TransferInventoryAddRq, List[TransferInventoryAddRq]]
    DateDrivenTermsQueryRq: Union[DateDrivenTermsQueryRq, List[DateDrivenTermsQueryRq]]
    BillModRq: Union[BillModRq, List[BillModRq]]
    BillToPayQueryRq: Union[BillToPayQueryRq, List[BillToPayQueryRq]]
    TransferQueryRq: Union[TransferQueryRq, List[TransferQueryRq]]
    ARRefundCreditCardQueryRq: Union[ARRefundCreditCardQueryRq, List[ARRefundCreditCardQueryRq]]
    InvoiceQueryRq: Union[InvoiceQueryRq, List[InvoiceQueryRq]]
    ItemAssembliesCanBuildQueryRq: Union[ItemAssembliesCanBuildQueryRq, List[ItemAssembliesCanBuildQueryRq]]
    ItemFixedAssetAddRq: Union[ItemFixedAssetAddRq, List[ItemFixedAssetAddRq]]
    CurrencyAddRq: Union[CurrencyAddRq, List[CurrencyAddRq]]
    JournalEntryAddRq: Union[JournalEntryAddRq, List[JournalEntryAddRq]]
    InvoiceAddRq: Union[InvoiceAddRq, List[InvoiceAddRq]]
    TransferInventoryQueryRq: Union[TransferInventoryQueryRq, List[TransferInventoryQueryRq]]
    ShipMethodQueryRq: Union[ShipMethodQueryRq, List[ShipMethodQueryRq]]
    BuildAssemblyAddRq: Union[BuildAssemblyAddRq, List[BuildAssemblyAddRq]]
    ItemInventoryAddRq: Union[ItemInventoryAddRq, List[ItemInventoryAddRq]]
    OtherNameQueryRq: Union[OtherNameQueryRq, List[OtherNameQueryRq]]
    JobTypeQueryRq: Union[JobTypeQueryRq, List[JobTypeQueryRq]]
    DataExtDefModRq: Union[DataExtDefModRq, List[DataExtDefModRq]]
    ItemServiceQueryRq: Union[ItemServiceQueryRq, List[ItemServiceQueryRq]]
    OtherNameModRq: Union[OtherNameModRq, List[OtherNameModRq]]
    ClassModRq: Union[ClassModRq, List[ClassModRq]]
    ToDoModRq: Union[ToDoModRq, List[ToDoModRq]]
    ChargeAddRq: Union[ChargeAddRq, List[ChargeAddRq]]
    TimeReportQueryRq: Union[TimeReportQueryRq, List[TimeReportQueryRq]]
    TimeTrackingAddRq: Union[TimeTrackingAddRq, List[TimeTrackingAddRq]]
    ItemSubtotalModRq: Union[ItemSubtotalModRq, List[ItemSubtotalModRq]]
    SalesTaxPaymentCheckAddRq: Union[SalesTaxPaymentCheckAddRq, List[SalesTaxPaymentCheckAddRq]]
    BarCodeQueryRq: Union[BarCodeQueryRq, List[BarCodeQueryRq]]
    TransferModRq: Union[TransferModRq, List[TransferModRq]]
    PayrollItemWageQueryRq: Union[PayrollItemWageQueryRq, List[PayrollItemWageQueryRq]]
    ItemInventoryQueryRq: Union[ItemInventoryQueryRq, List[ItemInventoryQueryRq]]
    EstimateQueryRq: Union[EstimateQueryRq, List[EstimateQueryRq]]
    PurchaseOrderAddRq: Union[PurchaseOrderAddRq, List[PurchaseOrderAddRq]]
    UnitOfMeasureSetAddRq: Union[UnitOfMeasureSetAddRq, List[UnitOfMeasureSetAddRq]]
    CreditCardChargeQueryRq: Union[CreditCardChargeQueryRq, List[CreditCardChargeQueryRq]]
    PurchaseOrderQueryRq: Union[PurchaseOrderQueryRq, List[PurchaseOrderQueryRq]]
    CreditCardCreditQueryRq: Union[CreditCardCreditQueryRq, List[CreditCardCreditQueryRq]]
    ListMergeRq: Union[ListMergeRq, List[ListMergeRq]]
    CheckModRq: Union[CheckModRq, List[CheckModRq]]
    PayrollItemWageAddRq: Union[PayrollItemWageAddRq, List[PayrollItemWageAddRq]]
    EstimateModRq: Union[EstimateModRq, List[EstimateModRq]]
    DataEventRecoveryInfoDelRq: Union[DataEventRecoveryInfoDelRq, List[DataEventRecoveryInfoDelRq]]
    HostQueryRq: Union[HostQueryRq, List[HostQueryRq]]
    BudgetSummaryReportQueryRq: Union[BudgetSummaryReportQueryRq, List[BudgetSummaryReportQueryRq]]
    VendorTypeAddRq: Union[VendorTypeAddRq, List[VendorTypeAddRq]]
    SalesOrderAddRq: Union[SalesOrderAddRq, List[SalesOrderAddRq]]
    VehicleAddRq: Union[VehicleAddRq, List[VehicleAddRq]]
    ItemSalesTaxGroupQueryRq: Union[ItemSalesTaxGroupQueryRq, List[ItemSalesTaxGroupQueryRq]]
    ItemPaymentQueryRq: Union[ItemPaymentQueryRq, List[ItemPaymentQueryRq]]
    ItemGroupModRq: Union[ItemGroupModRq, List[ItemGroupModRq]]
    EntityQueryRq: Union[EntityQueryRq, List[EntityQueryRq]]
    WorkersCompCodeModRq: Union[WorkersCompCodeModRq, List[WorkersCompCodeModRq]]
    CompanyActivityQueryRq: Union[CompanyActivityQueryRq, List[CompanyActivityQueryRq]]
    PaymentMethodAddRq: Union[PaymentMethodAddRq, List[PaymentMethodAddRq]]
    InventoryAdjustmentModRq: Union[InventoryAdjustmentModRq, List[InventoryAdjustmentModRq]]
    ItemServiceModRq: Union[ItemServiceModRq, List[ItemServiceModRq]]
    BillPaymentCreditCardAddRq: Union[BillPaymentCreditCardAddRq, List[BillPaymentCreditCardAddRq]]
    SalesReceiptModRq: Union[SalesReceiptModRq, List[SalesReceiptModRq]]
    CustomerTypeAddRq: Union[CustomerTypeAddRq, List[CustomerTypeAddRq]]
    CreditCardChargeModRq: Union[CreditCardChargeModRq, List[CreditCardChargeModRq]]
    ItemDiscountAddRq: Union[ItemDiscountAddRq, List[ItemDiscountAddRq]]
    SalesTaxCodeAddRq: Union[SalesTaxCodeAddRq, List[SalesTaxCodeAddRq]]
    CreditMemoModRq: Union[CreditMemoModRq, List[CreditMemoModRq]]
    ItemReceiptAddRq: Union[ItemReceiptAddRq, List[ItemReceiptAddRq]]
    ItemOtherChargeModRq: Union[ItemOtherChargeModRq, List[ItemOtherChargeModRq]]
    ItemNonInventoryAddRq: Union[ItemNonInventoryAddRq, List[ItemNonInventoryAddRq]]
    ItemSalesTaxGroupModRq: Union[ItemSalesTaxGroupModRq, List[ItemSalesTaxGroupModRq]]
    ListDisplayModRq: Union[ListDisplayModRq, List[ListDisplayModRq]]
    VendorQueryRq: Union[VendorQueryRq, List[VendorQueryRq]]
    ReceivePaymentModRq: Union[ReceivePaymentModRq, List[ReceivePaymentModRq]]
    ItemOtherChargeQueryRq: Union[ItemOtherChargeQueryRq, List[ItemOtherChargeQueryRq]]
    VehicleMileageQueryRq: Union[VehicleMileageQueryRq, List[VehicleMileageQueryRq]]
    DataExtDelRq: Union[DataExtDelRq, List[DataExtDelRq]]
    AgingReportQueryRq: Union[AgingReportQueryRq, List[AgingReportQueryRq]]
    PaymentMethodQueryRq: Union[PaymentMethodQueryRq, List[PaymentMethodQueryRq]]
    CurrencyQueryRq: Union[CurrencyQueryRq, List[CurrencyQueryRq]]
    AccountAddRq: Union[AccountAddRq, List[AccountAddRq]]
    VendorCreditAddRq: Union[VendorCreditAddRq, List[VendorCreditAddRq]]
    ItemInventoryAssemblyModRq: Union[ItemInventoryAssemblyModRq, List[ItemInventoryAssemblyModRq]]
    CustomerQueryRq: Union[CustomerQueryRq, List[CustomerQueryRq]]
    CheckQueryRq: Union[CheckQueryRq, List[CheckQueryRq]]
    DepositQueryRq: Union[DepositQueryRq, List[DepositQueryRq]]
    CustomerTypeQueryRq: Union[CustomerTypeQueryRq, List[CustomerTypeQueryRq]]
    TxnDisplayAddRq: Union[TxnDisplayAddRq, List[TxnDisplayAddRq]]
    ListDelRq: Union[ListDelRq, List[ListDelRq]]
    TxnDeletedQueryRq: Union[TxnDeletedQueryRq, List[TxnDeletedQueryRq]]
    WorkersCompCodeQueryRq: Union[WorkersCompCodeQueryRq, List[WorkersCompCodeQueryRq]]
    ItemGroupQueryRq: Union[ItemGroupQueryRq, List[ItemGroupQueryRq]]
    ItemSalesTaxQueryRq: Union[ItemSalesTaxQueryRq, List[ItemSalesTaxQueryRq]]
    CreditCardCreditModRq: Union[CreditCardCreditModRq, List[CreditCardCreditModRq]]
    SalesRepModRq: Union[SalesRepModRq, List[SalesRepModRq]]
    ClearedStatusModRq: Union[ClearedStatusModRq, List[ClearedStatusModRq]]
    InventorySiteAddRq: Union[InventorySiteAddRq, List[InventorySiteAddRq]]
    CompanyQueryRq: Union[CompanyQueryRq, List[CompanyQueryRq]]
    ItemPaymentAddRq: Union[ItemPaymentAddRq, List[ItemPaymentAddRq]]
    ItemSalesTaxAddRq: Union[ItemSalesTaxAddRq, List[ItemSalesTaxAddRq]]
    SpecialAccountAddRq: Union[SpecialAccountAddRq, List[SpecialAccountAddRq]]
    Form1099CategoryAccountMappingQueryRq: Union[Form1099CategoryAccountMappingQueryRq, List[Form1099CategoryAccountMappingQueryRq]]
    BillPaymentCheckModRq: Union[BillPaymentCheckModRq, List[BillPaymentCheckModRq]]
    ItemNonInventoryQueryRq: Union[ItemNonInventoryQueryRq, List[ItemNonInventoryQueryRq]]
    ARRefundCreditCardAddRq: Union[ARRefundCreditCardAddRq, List[ARRefundCreditCardAddRq]]
    TxnDelRq: Union[TxnDelRq, List[TxnDelRq]]
    TransferInventoryModRq: Union[TransferInventoryModRq, List[TransferInventoryModRq]]
    DepositModRq: Union[DepositModRq, List[DepositModRq]]
    ItemFixedAssetQueryRq: Union[ItemFixedAssetQueryRq, List[ItemFixedAssetQueryRq]]
    AccountQueryRq: Union[AccountQueryRq, List[AccountQueryRq]]
    TxnVoidRq: Union[TxnVoidRq, List[TxnVoidRq]]
    SpecialItemAddRq: Union[SpecialItemAddRq, List[SpecialItemAddRq]]
    DataExtAddRq: Union[DataExtAddRq, List[DataExtAddRq]]
    PriceLevelAddRq: Union[PriceLevelAddRq, List[PriceLevelAddRq]]
    JobReportQueryRq: Union[JobReportQueryRq, List[JobReportQueryRq]]
    InventoryAdjustmentQueryRq: Union[InventoryAdjustmentQueryRq, List[InventoryAdjustmentQueryRq]]
    JournalEntryModRq: Union[JournalEntryModRq, List[JournalEntryModRq]]
    ItemFixedAssetModRq: Union[ItemFixedAssetModRq, List[ItemFixedAssetModRq]]
    CurrencyModRq: Union[CurrencyModRq, List[CurrencyModRq]]
    InvoiceModRq: Union[InvoiceModRq, List[InvoiceModRq]]
    CustomSummaryReportQueryRq: Union[CustomSummaryReportQueryRq, List[CustomSummaryReportQueryRq]]
    CustomerMsgQueryRq: Union[CustomerMsgQueryRq, List[CustomerMsgQueryRq]]
    BillAddRq: Union[BillAddRq, List[BillAddRq]]
    JournalEntryQueryRq: Union[JournalEntryQueryRq, List[JournalEntryQueryRq]]
    CustomDetailReportQueryRq: Union[CustomDetailReportQueryRq, List[CustomDetailReportQueryRq]]
    VendorCreditQueryRq: Union[VendorCreditQueryRq, List[VendorCreditQueryRq]]
    SalesTaxCodeQueryRq: Union[SalesTaxCodeQueryRq, List[SalesTaxCodeQueryRq]]
    EmployeeQueryRq: Union[EmployeeQueryRq, List[EmployeeQueryRq]]
    PayrollDetailReportQueryRq: Union[PayrollDetailReportQueryRq, List[PayrollDetailReportQueryRq]]


class QBXMLMsgsRs(TypedDict, total=False):
    CustomerMsgAddRs: Union[CustomerMsgAddRs, List[CustomerMsgAddRs]]
    ItemSubtotalAddRs: Union[ItemSubtotalAddRs, List[ItemSubtotalAddRs]]
    SalesTaxPaymentCheckModRs: Union[SalesTaxPaymentCheckModRs, List[SalesTaxPaymentCheckModRs]]
    TimeTrackingModRs: Union[TimeTrackingModRs, List[TimeTrackingModRs]]
    ChargeModRs: Union[ChargeModRs, List[ChargeModRs]]
    PurchaseOrderModRs: Union[PurchaseOrderModRs, List[PurchaseOrderModRs]]
    ItemReceiptQueryRs: Union[ItemReceiptQueryRs, List[ItemReceiptQueryRs]]
    TransferAddRs: Union[TransferAddRs, List[TransferAddRs]]
    TimeTrackingQueryRs: Union[TimeTrackingQueryRs, List[TimeTrackingQueryRs]]
    ItemInventoryModRs: Union[ItemInventoryModRs, List[ItemInventoryModRs]]
    BuildAssemblyModRs: Union[BuildAssemblyModRs, List[BuildAssemblyModRs]]
    ListDeletedQueryRs: Union[ListDeletedQueryRs, List[ListDeletedQueryRs]]
    ToDoAddRs: Union[ToDoAddRs, List[ToDoAddRs]]
    ReceivePaymentQueryRs: Union[ReceivePaymentQueryRs, List[ReceivePaymentQueryRs]]
    PreferencesQueryRs: Union[PreferencesQueryRs, List[PreferencesQueryRs]]
    ClassAddRs: Union[ClassAddRs, List[ClassAddRs]]
    DataExtDefAddRs: Union[DataExtDefAddRs, List[DataExtDefAddRs]]
    OtherNameAddRs: Union[OtherNameAddRs, List[OtherNameAddRs]]
    ReceivePaymentToDepositQueryRs: Union[ReceivePaymentToDepositQueryRs, List[ReceivePaymentToDepositQueryRs]]
    UnitOfMeasureSetQueryRs: Union[UnitOfMeasureSetQueryRs, List[UnitOfMeasureSetQueryRs]]
    DataExtDefQueryRs: Union[DataExtDefQueryRs, List[DataExtDefQueryRs]]
    SalesOrderModRs: Union[SalesOrderModRs, List[SalesOrderModRs]]
    ChargeQueryRs: Union[ChargeQueryRs, List[ChargeQueryRs]]
    VehicleModRs: Union[VehicleModRs, List[VehicleModRs]]
    VehicleMileageAddRs: Union[VehicleMileageAddRs, List[VehicleMileageAddRs]]
    CheckAddRs: Union[CheckAddRs, List[CheckAddRs]]
    PriceLevelQueryRs: Union[PriceLevelQueryRs, List[PriceLevelQueryRs]]
    BillQueryRs: Union[BillQueryRs, List[BillQueryRs]]
    ItemSubtotalQueryRs: Union[ItemSubtotalQueryRs, List[ItemSubtotalQueryRs]]
    EstimateAddRs: Union[EstimateAddRs, List[EstimateAddRs]]
    ToDoQueryRs: Union[ToDoQueryRs, List[ToDoQueryRs]]
    DataExtDefDelRs: Union[DataExtDefDelRs, List[DataExtDefDelRs]]
    JobTypeAddRs: Union[JobTypeAddRs, List[JobTypeAddRs]]
    InventoryAdjustmentAddRs: Union[InventoryAdjustmentAddRs, List[InventoryAdjustmentAddRs]]
    ItemServiceAddRs: Union[ItemServiceAddRs, List[ItemServiceAddRs]]
    SalesTaxPaymentCheckQueryRs: Union[SalesTaxPaymentCheckQueryRs, List[SalesTaxPaymentCheckQueryRs]]
    ItemDiscountQueryRs: Union[ItemDiscountQueryRs, List[ItemDiscountQueryRs]]
    ItemGroupAddRs: Union[ItemGroupAddRs, List[ItemGroupAddRs]]
    CreditMemoQueryRs: Union[CreditMemoQueryRs, List[CreditMemoQueryRs]]
    StandardTermsAddRs: Union[StandardTermsAddRs, List[StandardTermsAddRs]]
    BillingRateAddRs: Union[BillingRateAddRs, List[BillingRateAddRs]]
    WorkersCompCodeAddRs: Union[WorkersCompCodeAddRs, List[WorkersCompCodeAddRs]]
    ItemOtherChargeAddRs: Union[ItemOtherChargeAddRs, List[ItemOtherChargeAddRs]]
    BillPaymentCreditCardQueryRs: Union[BillPaymentCreditCardQueryRs, List[BillPaymentCreditCardQueryRs]]
    TermsQueryRs: Union[TermsQueryRs, List[TermsQueryRs]]
    ItemNonInventoryModRs: Union[ItemNonInventoryModRs, List[ItemNonInventoryModRs]]
    ItemSalesTaxGroupAddRs: Union[ItemSalesTaxGroupAddRs, List[ItemSalesTaxGroupAddRs]]
    ItemReceiptModRs: Union[ItemReceiptModRs, List[ItemReceiptModRs]]
    CreditMemoAddRs: Union[CreditMemoAddRs, List[CreditMemoAddRs]]
    ReceivePaymentAddRs: Union[ReceivePaymentAddRs, List[ReceivePaymentAddRs]]
    PayrollItemNonWageQueryRs: Union[PayrollItemNonWageQueryRs, List[PayrollItemNonWageQueryRs]]
    SalesReceiptAddRs: Union[SalesReceiptAddRs, List[SalesReceiptAddRs]]
    ShipMethodAddRs: Union[ShipMethodAddRs, List[ShipMethodAddRs]]
    SalesTaxCodeModRs: Union[SalesTaxCodeModRs, List[SalesTaxCodeModRs]]
    ItemDiscountModRs: Union[ItemDiscountModRs, List[ItemDiscountModRs]]
    CreditCardChargeAddRs: Union[CreditCardChargeAddRs, List[CreditCardChargeAddRs]]
    SalesReceiptQueryRs: Union[SalesReceiptQueryRs, List[SalesReceiptQueryRs]]
    VendorTypeQueryRs: Union[VendorTypeQueryRs, List[VendorTypeQueryRs]]
    VehicleQueryRs: Union[VehicleQueryRs, List[VehicleQueryRs]]
    BillingRateQueryRs: Union[BillingRateQueryRs, List[BillingRateQueryRs]]
    VendorCreditModRs: Union[VendorCreditModRs, List[VendorCreditModRs]]
    ItemSitesQueryRs: Union[ItemSitesQueryRs, List[ItemSitesQueryRs]]
    ItemInventoryAssemblyAddRs: Union[ItemInventoryAssemblyAddRs, List[ItemInventoryAssemblyAddRs]]
    StandardTermsQueryRs: Union[StandardTermsQueryRs, List[StandardTermsQueryRs]]
    BillPaymentCheckQueryRs: Union[BillPaymentCheckQueryRs, List[BillPaymentCheckQueryRs]]
    ItemQueryRs: Union[ItemQueryRs, List[ItemQueryRs]]
    ItemInventoryAssemblyQueryRs: Union[ItemInventoryAssemblyQueryRs, List[ItemInventoryAssemblyQueryRs]]
    TransactionQueryRs: Union[TransactionQueryRs, List[TransactionQueryRs]]
    SalesTaxPayableQueryRs: Union[SalesTaxPayableQueryRs, List[SalesTaxPayableQueryRs]]
    BuildAssemblyQueryRs: Union[BuildAssemblyQueryRs, List[BuildAssemblyQueryRs]]
    AccountModRs: Union[AccountModRs, List[AccountModRs]]
    ItemPaymentModRs: Union[ItemPaymentModRs, List[ItemPaymentModRs]]
    DateDrivenTermsAddRs: Union[DateDrivenTermsAddRs, List[DateDrivenTermsAddRs]]
    ItemSalesTaxModRs: Union[ItemSalesTaxModRs, List[ItemSalesTaxModRs]]
    BillPaymentCheckAddRs: Union[BillPaymentCheckAddRs, List[BillPaymentCheckAddRs]]
    InventorySiteModRs: Union[InventorySiteModRs, List[InventorySiteModRs]]
    TemplateQueryRs: Union[TemplateQueryRs, List[TemplateQueryRs]]
    CreditCardCreditAddRs: Union[CreditCardCreditAddRs, List[CreditCardCreditAddRs]]
    SalesOrderQueryRs: Union[SalesOrderQueryRs, List[SalesOrderQueryRs]]
    SalesRepAddRs: Union[SalesRepAddRs, List[SalesRepAddRs]]
    Form1099CategoryAccountMappingModRs: Union[Form1099CategoryAccountMappingModRs, List[Form1099CategoryAccountMappingModRs]]
    SalesRepQueryRs: Union[SalesRepQueryRs, List[SalesRepQueryRs]]
    InventorySiteQueryRs: Union[InventorySiteQueryRs, List[InventorySiteQueryRs]]
    ClassQueryRs: Union[ClassQueryRs, List[ClassQueryRs]]
    DataExtModRs: Union[DataExtModRs, List[DataExtModRs]]
    SalesTaxReturnLineQueryRs: Union[SalesTaxReturnLineQueryRs, List[SalesTaxReturnLineQueryRs]]
    PriceLevelModRs: Union[PriceLevelModRs, List[PriceLevelModRs]]
    DataEventRecoveryInfoQueryRs: Union[DataEventRecoveryInfoQueryRs, List[DataEventRecoveryInfoQueryRs]]
    DepositAddRs: Union[DepositAddRs, List[DepositAddRs]]
    TransferInventoryAddRs: Union[TransferInventoryAddRs, List[TransferInventoryAddRs]]
    DateDrivenTermsQueryRs: Union[DateDrivenTermsQueryRs, List[DateDrivenTermsQueryRs]]
    BillModRs: Union[BillModRs, List[BillModRs]]
    BillToPayQueryRs: Union[BillToPayQueryRs, List[BillToPayQueryRs]]
    TransferQueryRs: Union[TransferQueryRs, List[TransferQueryRs]]
    ARRefundCreditCardQueryRs: Union[ARRefundCreditCardQueryRs, List[ARRefundCreditCardQueryRs]]
    InvoiceQueryRs: Union[InvoiceQueryRs, List[InvoiceQueryRs]]
    ItemAssembliesCanBuildQueryRs: Union[ItemAssembliesCanBuildQueryRs, List[ItemAssembliesCanBuildQueryRs]]
    ItemFixedAssetAddRs: Union[ItemFixedAssetAddRs, List[ItemFixedAssetAddRs]]
    CurrencyAddRs: Union[CurrencyAddRs, List[CurrencyAddRs]]
    JournalEntryAddRs: Union[JournalEntryAddRs, List[JournalEntryAddRs]]
    InvoiceAddRs: Union[InvoiceAddRs, List[InvoiceAddRs]]
    TransferInventoryQueryRs: Union[TransferInventoryQueryRs, List[TransferInventoryQueryRs]]
    ShipMethodQueryRs: Union[ShipMethodQueryRs, List[ShipMethodQueryRs]]
    BuildAssemblyAddRs: Union[BuildAssemblyAddRs, List[BuildAssemblyAddRs]]
    ItemInventoryAddRs: Union[ItemInventoryAddRs, List[ItemInventoryAddRs]]
    OtherNameQueryRs: Union[OtherNameQueryRs, List[OtherNameQueryRs]]
    JobTypeQueryRs: Union[JobTypeQueryRs, List[JobTypeQueryRs]]
    DataExtDefModRs: Union[DataExtDefModRs, List[DataExtDefModRs]]
    ItemServiceQueryRs: Union[ItemServiceQueryRs, List[ItemServiceQueryRs]]
    OtherNameModRs: Union[OtherNameModRs, List[OtherNameModRs]]
    ClassModRs: Union[ClassModRs, List[ClassModRs]]
    ToDoModRs: Union[ToDoModRs, List[ToDoModRs]]
    ChargeAddRs: Union[ChargeAddRs, List[ChargeAddRs]]
    TimeTrackingAddRs: Union[TimeTrackingAddRs, List[TimeTrackingAddRs]]
    ItemSubtotalModRs: Union[ItemSubtotalModRs, List[ItemSubtotalModRs]]
    SalesTaxPaymentCheckAddRs: Union[SalesTaxPaymentCheckAddRs, List[SalesTaxPaymentCheckAddRs]]
    BarCodeQueryRs: Union[BarCodeQueryRs, List[BarCodeQueryRs]]
    TransferModRs: Union[TransferModRs, List[TransferModRs]]
    PayrollItemWageQueryRs: Union[PayrollItemWageQueryRs, List[PayrollItemWageQueryRs]]
    ItemInventoryQueryRs: Union[ItemInventoryQueryRs, List[ItemInventoryQueryRs]]
    EstimateQueryRs: Union[EstimateQueryRs, List[EstimateQueryRs]]
    PurchaseOrderAddRs: Union[PurchaseOrderAddRs, List[PurchaseOrderAddRs]]
    UnitOfMeasureSetAddRs: Union[UnitOfMeasureSetAddRs, List[UnitOfMeasureSetAddRs]]
    CreditCardChargeQueryRs: Union[CreditCardChargeQueryRs, List[CreditCardChargeQueryRs]]
    PurchaseOrderQueryRs: Union[PurchaseOrderQueryRs, List[PurchaseOrderQueryRs]]
    CreditCardCreditQueryRs: Union[CreditCardCreditQueryRs, List[CreditCardCreditQueryRs]]
    ListMergeRs: Union[ListMergeRs, List[ListMergeRs]]
    CheckModRs: Union[CheckModRs, List[CheckModRs]]
    PayrollItemWageAddRs: Union[PayrollItemWageAddRs, List[PayrollItemWageAddRs]]
    EstimateModRs: Union[EstimateModRs, List[EstimateModRs]]
    HostQueryRs: Union[HostQueryRs, List[HostQueryRs]]
    VendorTypeAddRs: Union[VendorTypeAddRs, List[VendorTypeAddRs]]
    SalesOrderAddRs: Union[SalesOrderAddRs, List[SalesOrderAddRs]]
    VehicleAddRs: Union[VehicleAddRs, List[VehicleAddRs]]
    ItemSalesTaxGroupQueryRs: Union[ItemSalesTaxGroupQueryRs, List[ItemSalesTaxGroupQueryRs]]
    ItemPaymentQueryRs: Union[ItemPaymentQueryRs, List[ItemPaymentQueryRs]]
    ItemGroupModRs: Union[ItemGroupModRs, List[ItemGroupModRs]]
    WorkersCompCodeModRs: Union[WorkersCompCodeModRs, List[WorkersCompCodeModRs]]
    CompanyActivityQueryRs: Union[CompanyActivityQueryRs, List[CompanyActivityQueryRs]]
    PaymentMethodAddRs: Union[PaymentMethodAddRs, List[PaymentMethodAddRs]]
    InventoryAdjustmentModRs: Union[InventoryAdjustmentModRs, List[InventoryAdjustmentModRs]]
    ItemServiceModRs: Union[ItemServiceModRs, List[ItemServiceModRs]]
    BillPaymentCreditCardAddRs: Union[BillPaymentCreditCardAddRs, List[BillPaymentCreditCardAddRs]]
    SalesReceiptModRs: Union[SalesReceiptModRs, List[SalesReceiptModRs]]
    CustomerTypeAddRs: Union[CustomerTypeAddRs, List[CustomerTypeAddRs]]
    CreditCardChargeModRs: Union[CreditCardChargeModRs, List[CreditCardChargeModRs]]
    ItemDiscountAddRs: Union[ItemDiscountAddRs, List[ItemDiscountAddRs]]
    SalesTaxCodeAddRs: Union[SalesTaxCodeAddRs, List[SalesTaxCodeAddRs]]
    CreditMemoModRs: Union[CreditMemoModRs, List[CreditMemoModRs]]
    ItemReceiptAddRs: Union[ItemReceiptAddRs, List[ItemReceiptAddRs]]
    ItemOtherChargeModRs: Union[ItemOtherChargeModRs, List[ItemOtherChargeModRs]]
    ItemNonInventoryAddRs: Union[ItemNonInventoryAddRs, List[ItemNonInventoryAddRs]]
    ItemSalesTaxGroupModRs: Union[ItemSalesTaxGroupModRs, List[ItemSalesTaxGroupModRs]]
    ReceivePaymentModRs: Union[ReceivePaymentModRs, List[ReceivePaymentModRs]]
    ItemOtherChargeQueryRs: Union[ItemOtherChargeQueryRs, List[ItemOtherChargeQueryRs]]
    VehicleMileageQueryRs: Union[VehicleMileageQueryRs, List[VehicleMileageQueryRs]]
    DataExtDelRs: Union[DataExtDelRs, List[DataExtDelRs]]
    PaymentMethodQueryRs: Union[PaymentMethodQueryRs, List[PaymentMethodQueryRs]]
    CurrencyQueryRs: Union[CurrencyQueryRs, List[CurrencyQueryRs]]
    AccountAddRs: Union[AccountAddRs, List[AccountAddRs]]
    VendorCreditAddRs: Union[VendorCreditAddRs, List[VendorCreditAddRs]]
    ItemInventoryAssemblyModRs: Union[ItemInventoryAssemblyModRs, List[ItemInventoryAssemblyModRs]]
    CheckQueryRs: Union[CheckQueryRs, List[CheckQueryRs]]
    DepositQueryRs: Union[DepositQueryRs, List[DepositQueryRs]]
    CustomerTypeQueryRs: Union[CustomerTypeQueryRs, List[CustomerTypeQueryRs]]
    ListDelRs: Union[ListDelRs, List[ListDelRs]]
    TxnDeletedQueryRs: Union[TxnDeletedQueryRs, List[TxnDeletedQueryRs]]
    WorkersCompCodeQueryRs: Union[WorkersCompCodeQueryRs, List[WorkersCompCodeQueryRs]]
    ItemGroupQueryRs: Union[ItemGroupQueryRs, List[ItemGroupQueryRs]]
    ItemSalesTaxQueryRs: Union[ItemSalesTaxQueryRs, List[ItemSalesTaxQueryRs]]
    CreditCardCreditModRs: Union[CreditCardCreditModRs, List[CreditCardCreditModRs]]
    SalesRepModRs: Union[SalesRepModRs, List[SalesRepModRs]]
    InventorySiteAddRs: Union[InventorySiteAddRs, List[InventorySiteAddRs]]
    CompanyQueryRs: Union[CompanyQueryRs, List[CompanyQueryRs]]
    ItemPaymentAddRs: Union[ItemPaymentAddRs, List[ItemPaymentAddRs]]
    ItemSalesTaxAddRs: Union[ItemSalesTaxAddRs, List[ItemSalesTaxAddRs]]
    SpecialAccountAddRs: Union[SpecialAccountAddRs, List[SpecialAccountAddRs]]
    Form1099CategoryAccountMappingQueryRs: Union[Form1099CategoryAccountMappingQueryRs, List[Form1099CategoryAccountMappingQueryRs]]
    BillPaymentCheckModRs: Union[BillPaymentCheckModRs, List[BillPaymentCheckModRs]]
    ItemNonInventoryQueryRs: Union[ItemNonInventoryQueryRs, List[ItemNonInventoryQueryRs]]
    ARRefundCreditCardAddRs: Union[ARRefundCreditCardAddRs, List[ARRefundCreditCardAddRs]]
    TxnDelRs: Union[TxnDelRs, List[TxnDelRs]]
    TransferInventoryModRs: Union[TransferInventoryModRs, List[TransferInventoryModRs]]
    DepositModRs: Union[DepositModRs, List[DepositModRs]]
    ItemFixedAssetQueryRs: Union[ItemFixedAssetQueryRs, List[ItemFixedAssetQueryRs]]
    AccountQueryRs: Union[AccountQueryRs, List[AccountQueryRs]]
    TxnVoidRs: Union[TxnVoidRs, List[TxnVoidRs]]
    SpecialItemAddRs: Union[SpecialItemAddRs, List[SpecialItemAddRs]]
    DataExtAddRs: Union[DataExtAddRs, List[DataExtAddRs]]
    PriceLevelAddRs: Union[PriceLevelAddRs, List[PriceLevelAddRs]]
    InventoryAdjustmentQueryRs: Union[InventoryAdjustmentQueryRs, List[InventoryAdjustmentQueryRs]]
    JournalEntryModRs: Union[JournalEntryModRs, List[JournalEntryModRs]]
    ItemFixedAssetModRs: Union[ItemFixedAssetModRs, List[ItemFixedAssetModRs]]
    CurrencyModRs: Union[CurrencyModRs, List[CurrencyModRs]]
    InvoiceModRs: Union[InvoiceModRs, List[InvoiceModRs]]
    CustomerMsgQueryRs: Union[CustomerMsgQueryRs, List[CustomerMsgQueryRs]]
    BillAddRs: Union[BillAddRs, List[BillAddRs]]
    JournalEntryQueryRs: Union[JournalEntryQueryRs, List[JournalEntryQueryRs]]
    VendorCreditQueryRs: Union[VendorCreditQueryRs, List[VendorCreditQueryRs]]
    SalesTaxCodeQueryRs: Union[SalesTaxCodeQueryRs, List[SalesTaxCodeQueryRs]]
