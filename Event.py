

def register_event(events: dict, event: str, func: callable):
    handlers = events.get(event)

    if handlers is None:
        events[event] = [func]
    else:
        handlers.append(func)

    print("Register:", events)

def dispatch_event(events: dict, event: str):
    handlers = events.get(event)

    print("Handlers:", handlers)
    print('Dispatch:', events)

    if handlers is None:
        raise ValueError(f"Event {event} not found")

    for handler in handlers:
        handler()