import jester, asyncdispatch
from controllers/SampleController import SampleController

router main_router:
  get "/": resp SampleController.index()
  get "/fib/@num/":
    resp SampleController.fib(@"num"), "application/json"

# runForever()

proc main() =
  let port = 8002.Port
  let settings = newSettings(port=port)
  var jester = initJester(main_router, settings=settings)
  jester.serve()

when isMainModule:
  main()