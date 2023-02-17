from  multiprocessing import Process, Manager
import time
from Events import register_event, dispatch_event


def print_event():
    print("Event was triggered!")

def register_events(events: dict):
    register_event(events, "test", print_event)

def dispatch_events(events: dict):
    dispatch_event(events, "test")


if __name__ == "__main__":
    shared_events = Manager().dict()

    proc_reg = Process(target=register_events, args=(shared_events,))
    proc_dis = Process(target=dispatch_events, args=(shared_events,))

    # Register event before dispatching
    proc_reg.start()
    time.sleep(0.1)
    proc_dis.start()

    # join() => "wait for this [thread/process] to complete"
    proc_reg.join()
    proc_dis.join()



    print('Outside proc:', shared_events)