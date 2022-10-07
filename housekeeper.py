import sys
import json
import importlib

def main():
    lines = sys.argv[1]
    data = json.loads(lines)
    mod = importlib.import_module('workers.{}'.format(data["worker"]))
    worker = mod.Worker(data)
    res = worker.run(data)
    print(json.dumps(res))
    sys.stdout.flush()

if __name__ == "__main__":
    main()