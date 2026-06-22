class Aggregate:
    def __init__(self):
        self.version = 0
        self.pending_events = []
        
    def apply(self, event):
        handler = getattr(self, f"apply_{event['event_type']}", None)
        if handler:
            handler(event)
            self.version += 1
            
    def _emit(self, event_type, data):
        self.pending_events.append({"event_type": event_type, "data": data})
