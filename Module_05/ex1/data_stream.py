from typing import Any, List
from abc import ABC, abstractmethod, ABCMeta


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
            print("\n!!!Trying to output from nothing!!!")
            return ((0, "empty"))


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.x = 0

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
            if not self.validate(data):
                raise Exception("Improper numeric data")
            data2 = str(data).replace("[", "")
            data2 = str(data).replace("]", "")
            for i in str(data2).split(", "):
                self.list += [(self.x, i)]
                self.x += 1
        except Exception as obj:
            print("Got exception:", obj)

    def output(self) -> tuple[int, str]:
        return super().output()


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.x = 0

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
            if not self.validate(data):
                raise Exception("Improper textual data")
            data = str(data).replace("[", "")
            data = str(data).replace("]", "")
            data = str(data).replace("'", "")
            for i in str(data).split(", "):
                self.list += [(self.x, i)]
                self.x += 1
        except Exception as obj:
            print("Got exception:", obj)

    def output(self) -> tuple[int, str]:
        return super().output()


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        self.x = 0

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
            values = ""
            if not self.validate(data):
                raise Exception("Improper dictionary")
            if (type(data) is list):
                for i in data:
                    for v in i.values():
                        if (values != ""):
                            values += ": "
                        values += v
                    self.list += [(self.x, values)]
                    self.x += 1
                    values = ""
            elif (type(data) is dict):
                for v in data.values():
                    if (values != ""):
                        values += ": "
                    values += v
                self.list += [(self.x, values)]
        except Exception as obj:
            print("Got exception:", obj)

    def output(self) -> tuple[int, str]:
        return super().output()


class Datastream():
    def __init__(self):
        self.processors = []
        self.stats = [0, 0, 0]

    def register_processor(self, proc: DataProcessor) -> None:
        if (type(proc) is ABCMeta):
            self.processors += [proc()]

    def process_stream(self, stream: list[Any]) -> None:
        for x in stream:
            try:
                count = 0
                for y in self.processors:
                    if (y.validate(x) is True):
                        to_compare = len(y.list)
                        count += 1
                        y.ingest(x)
                        if (type(y) is NumericProcessor):
                            self.stats[0] += len(y.list) - to_compare
                        if (type(y) is TextProcessor):
                            self.stats[1] += len(y.list) - to_compare
                        if (type(y) is LogProcessor):
                            self.stats[2] += len(y.list) - to_compare
                if (count == 0):
                    raise TypeError("DataStream error- Can't process \
element in stream:")
            except Exception as obj:
                print(obj, x)

    def print_processors_stats(self) -> None:
        for i in self.processors:
            if (type(i) is NumericProcessor):
                print(f"Numeric Processor: total {self.stats[0]} \
items processed, remaining {len(i.list)} on processor")
            if (type(i) is TextProcessor):
                print(f"Text Processor: total {self.stats[1]} items\
processed, remaining {len(i.list)} on processor")
            if (type(i) is LogProcessor):
                print(f"Log Processor: total {self.stats[2]} items\
processed, remaining {len(i.list)} on processor")
        if (len(self.processors) == 0):
            print("No processor found")
        if (self.stats == [0, 0, 0]):
            print("No data offered")


def main():
    a = Datastream()
    print("=== Code Nexus- Data Stream ===\n")
    print("Initialize Data Stream...")
    print("== DataStream statistics ==")
    a.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    a.register_processor(NumericProcessor)
    print("Send first batch of data on stream: \
['Hello world', [3.14,-1, 2.71], [{'log_level': 'WARNING', \
'log_message': 'Telnet access! Use ssh instead'}, {'log_level': \
'INFO', 'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]")
    a.process_stream(['Hello world', [3.14, -1, 2.71],
                      [{'log_level': 'WARNING',
                        'log_message': 'Telnet access! Use ssh instead'},
                       {'log_level': 'INFO', 'log_message':
                        'User wil is connected'}],
                      42, ['Hi', 'five']])
    print("== DataStream statistics ==")
    a.print_processors_stats()
    print("\nRegistering other data processors")
    a.register_processor(TextProcessor)
    a.register_processor(LogProcessor)
    print("Send the same batch again")
    a.process_stream(['Hello world', [3.14, -1, 2.71],
                      [{'log_level': 'WARNING',
                        'log_message': 'Telnet access! Use ssh instead'},
                       {'log_level': 'INFO', 'log_message':
                        'User wil is connected'}],
                      42, ['Hi', 'five']])
    print("== DataStream statistics ==")
    a.print_processors_stats()
    print("\nConsume some elements from the data processors: \
Numeric 3, Text 2, Log 1")
    for i in range(3):
        a.processors[0].list.pop(0)
    for i in range(2):
        a.processors[1].list.pop(0)
    a.processors[2].list.pop(0)
    print("== DataStream statistics ==")
    a.print_processors_stats()


if __name__ == "__main__":
    main()
