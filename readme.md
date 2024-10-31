# Python Concatenation Performance Test

This is a performace test to show the efficiency of different concatennation methods used in Python. The current version of the test includes two parts:

1. Test of combing two string variables into one.
2. Test of combing 19 (words + punctuations) string variables into one.

## Test Result

| Method Used | Time Consumed for 2 Variables (s) | Time Consumed for 19 Variables (s) |
| :---: | :---: | :---: |
| + | 2.392548899999383 | 29.571498500001326 |
| join | 4.323850400000083 | 8.194372099998873 |
| f-String | 3.68403810000018 | 9.566135800001575 |
| format | 6.365032500001689 | 23.20330599999943 |

Disclamer 1: Test results could differ across different platforms with machines having different performance.

Disclamer 2: Testing methods definitely need further improvements. Any advice on improving/expanding my test is welcomed.
