from typing import Dict, List

searchReplaceDict: Dict[str, str] = {
    r'{"resistor-array-board":"RA001"}': r'{"resistor-array-board":""}',
    r'{"resistor-array-board":"RA002"}': r'{"resistor-array-board":""}',
    r'{"resistor-array-board":"RA003"}': r'{"resistor-array-board":""}',

#     r'{"resistor-array-board":"1"}': r'{"resistor-array-board":"RA001"}',
#     r'{"resistor-array-board":"2"}': r'{"resistor-array-board":"RA002"}',
#     r'{"resistor-array-board":"3"}': r'{"resistor-array-board":"RA003"}',
}

BaseDir: str = "C:/Users/Matt Dion/Dropbox/Squidstat Calibrations/Squidstat customer records"

filePathFilters_inclusive: List[str] = [
        "Plus1782",
        "Plus1783",
        "Plus1784",
        "Plus1785",
        "Plus1786",
        "Plus1787",
        "Plus1788",
        "Plus1789",
]

filePathFilters_exclusive: List[str] = [
        ".csv",
        "QCTests_AC",
        "microOhm",
]