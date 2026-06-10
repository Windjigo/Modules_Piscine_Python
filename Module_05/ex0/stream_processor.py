from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.list = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        try:
            return (self.list.pop(0))
        except Exception:
            print("Trying to output from nothing")
            return ((0, "empty"))


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        x = 0
        y = 0
        try:
            for i in str(data):
                if (i in "0123456789"):
                    y += 1
                if (i in "0123456789.-[], "):
                    x += 1
            if (x == len(str(data)) and y >= 1):
                return (True)
            else:
                return (False)
        except Exception as obj:
            print(obj)
            return False

    def ingest(self, data: float | int | List[float | int]) -> None:
        try:
            x = 0
            if not self.validate(data):
                raise Exception("Improper numeric data")
            data2 = str(data).replace("[", "")
            data2 = str(data2).replace("]", "")
            for i in str(data2).split(", "):
                self.list += [(x, i)]
                x += 1
        except Exception as obj:
            print("Got exception:", obj)

    def output(self) -> tuple[int, str]:
        return super().output()


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            a = NumericProcessor()
            b = LogProcessor()
            if (a.validate(data) is True):
                return (False)
            if (b.validate(data) is True):
                return (False)
            return (True)
        except Exception as obj:
            print(obj)
            return False

    def ingest(self, data: str | List[str]) -> None:
        try:
            x = 0
            if not self.validate(data):
                raise Exception("Improper textual data")
            data = str(data).replace("[", "")
            data = str(data).replace("]", "")
            for i in str(data).split(", "):
                self.list += [(x, i)]
                x += 1
        except Exception as obj:
            print("Got exception:", obj)

    def output(self) -> tuple[int, str]:
        return super().output()


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            if (type(data) is list):
                for i in data:
                    if (type(i) is not dict):
                        return (False)
                return (True)
            return (type(data) is dict)
        except Exception as obj:
            print(obj)
            return False

    def ingest(self, data: dict | list[dict]) -> None:
        try:
            x = 0
            values = ""
            if not self.validate(data):
                raise Exception("Improper dictionary")
            if (type(data) is list):
                for i in data:
                    for v in i.values():
                        if (values != ""):
                            values += ": "
                        values += v
                    self.list += [(x, values)]
                    values = ""
                    x += 1
            elif (type(data) is dict):
                for v in data.values():
                    if (values != ""):
                        values += ": "
                    values += v
                self.list += [(x, values)]
        except Exception as obj:
            print("Got exception:", obj)

    def output(self) -> tuple[int, str]:
        return super().output()


def main():
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    a = NumericProcessor()
    print("Trying to validate input '42':", a.validate('42'))
    print("Trying to validate input 'Hello':",  a.validate('Hello'))
    print("Test invalid ingestion of string 'foo' \
without prior validation:")
    a.ingest("foo")
    print("Processing data: [1, 2, 3, 4, 5]")
    a.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(0, 3):
        b = a.output()
        print("Numeric value", b[0], ":", b[1])

    print("\nTesting Text Processor...")
    b = TextProcessor()
    print("Trying to validate input '42':", b.validate('42'))
    print("Processing data: ['Hello', 'Nexus', 'World']")
    b.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 2 value...")
    for i in range(0, 2):
        c = b.output()
        print("Text value", c[0], ":", c[1])

    print("\nTesting Log Processor...")
    c = LogProcessor()
    print("Trying to validate input 'Hello':", c.validate('Hello'))
    print("Processing data: [{'log_level': 'NOTICE', \
'log_message': 'Connection to server'}, {'log_level': \
'ERROR', 'log_message': 'Unauthorized access!!'}]")
    c.ingest([{'log_level': 'NOTICE', 'log_message':
               'Connection to server'},
              {'log_level': 'ERROR', 'log_message':
               'Unauthorized access!!'}])
    print("Extracting 2 values...")
    for i in range(0, 2):
        d = c.output()
        print("Log entry", d[0], ":", d[1])


if __name__ == "__main__":
    main()
