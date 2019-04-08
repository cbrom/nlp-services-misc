#/bin/usr/env python
import sys
sys.path.insert(0, 'service')
sys.path.insert(0, 'service_spec')

from server import *

if __name__ == "__main__":
    server = get_server()
    server.start()
    print("Server has started on port:", "50051")
    _ONE_DAY = 86400
    try:
        while True:
            time.sleep(_ONE_DAY)
    except KeyboardInterrupt:
        server.stop(1)
