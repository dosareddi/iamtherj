from logic import eventlines
from renderers import item_renderers

# Get the new timeline renderer given the timeline id.
# Arguments:
#   timeline_id: integer.
# Returns:
#   TimelineRenderer object if timeline exists, None otherwise.
def get_timeline_renderer(timeline_id):
  timeline = eventlines.get_timeline(timeline_id)
  if not timeline:
    return None

  events = []
  for event in timeline.events:
    events.append(item_renderers.EventRenderer(
      event.name, event.description, event.start_time, event.end_time))
    
  return item_renderers.TimelineRenderer(
    timeline.name, timeline.description, 
    timeline.start_time, timeline.end_time, events)


