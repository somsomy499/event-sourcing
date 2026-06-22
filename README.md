# Event Sourcing Framework 📝

Event sourcing with CQRS, versioning, snapshots, and replay.

## Features

- **Event Store**: Append-only with versioning
- **Aggregates**: Domain-driven design patterns
- **CQRS**: Separate read/write models
- **Snapshots**: Periodic state snapshots for fast replay
- **Projections**: Real-time materialized views

## Quick Start

```python
from event_sourcing import EventStore, Aggregate

store = EventStore()

class Order(Aggregate):
    def apply_order_created(self, event):
        self.total = event.data["total"]
```

## License

MIT