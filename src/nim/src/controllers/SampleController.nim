# import strutils
from strutils import parseInt
include ../services/domain_services/SampleService

proc index*(): string =
  return "hello"

proc fib*(num: string): string =
  let new_num = num.parseInt
  let data = SampleService().fib(new_num)
  return $data # $…JsonNodeを文字列にする
