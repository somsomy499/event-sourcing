"""Append-only event store."""
from typing import List, Dict, Any
from datetime import datetime

class EventStore:
    def __init__(self):
        self.events = []
        
    def append(self, aggregate_id, event_type, data):
        self.events.append({
            "aggregate_id": aggregate_id,
            "event_type": event_type,
            "data": data,
            "version": len(self.events) + 1,
            "timestamp": datetime.utcnow().isoformat(),
        })
        
    def get_events(self, aggregate_id):
        return [e for e in self.events if e["aggregate_id"] == aggregate_id]
