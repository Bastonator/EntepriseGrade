import json
from channels.generic.websocket import AsyncWebsocketConsumer
from typing import Dict, Any
from uuid import UUID


def convert_uuids(data):
    """Recursively convert UUIDs to strings in dicts/lists."""

    if isinstance(data, dict):
        return {k: convert_uuids(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_uuids(v) for v in data]
    elif isinstance(data, UUID):
        return str(data)
    return data


class PatientConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Add this connection to the "patients" group
        await self.channel_layer.group_add("patients", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("patients", self.channel_name)

    # Handler for messages sent to the group
    async def patient_update(self, event: Dict[str, Any]):
        safe_patient = convert_uuids(event["patient"])

        await self.send(text_data=json.dumps({
            "type": "patient_update",
            "patient": safe_patient,
        }))