from enum import Enum
from pyspark.errors import *
class PySparkErrors(Enum):
    AnalysisException = AnalysisException(message="Failed to analyze a SQL query plan.")
    TempTableAlreadyExistsException = TempTableAlreadyExistsException(message="Failed to create temp view since it is already exists.")
    ParseException = ParseException(message="Failed to parse a SQL command.")
    IllegalArgumentException = IllegalArgumentException(message="Passed an illegal or inappropriate argument.")
    ArithmeticException = ArithmeticException(message="Arithmetic exception thrown from Spark with an error class.")
    UnsupportedOperationException = UnsupportedOperationException(message="Unsupported operation exception thrown from Spark with an error class.")
    ArrayIndexOutOfBoundsException = ArrayIndexOutOfBoundsException(message="Array index out of bounds exception thrown from Spark with an error class.")
    DateTimeException = DateTimeException(message="Datetime exception thrown from Spark with an error class.")
    NumberFormatException = NumberFormatException(message="Number format exception thrown from Spark with an error class.")
    StreamingQueryException = StreamingQueryException(message="Exception that stopped a `StreamingQuery`.")
    QueryExecutionException = QueryExecutionException(message="Failed to execute a query.")
    PythonException = PythonException(message="Exceptions thrown from Python workers.")
    SparkRuntimeException = SparkRuntimeException(message="Runtime exception thrown from Spark with an error class.")
    SparkUpgradeException = SparkUpgradeException(message="Exception thrown because of Spark upgrade.")
    UnknownException = UnknownException(message="None of the above exceptions.")
    PySparkValueError = PySparkValueError(message="ValueError.")
    PySparkTypeError = PySparkTypeError(message="TypeError.")
    PySparkAttributeError = PySparkAttributeError(message="AttributeError.")
    PySparkRuntimeError = PySparkRuntimeError(message="RuntimeError.")
    PySparkAssertionError = PySparkAssertionError(message="AssertionError.")
    PySparkNotImplementedError = PySparkNotImplementedError(message="NotImplementedError.")




error_list = ["AnalysisException","ParseException","StreamingQueryException","PythonException","UnknownException"]

for element in error_list:
    print(PySparkErrors[element].value)

