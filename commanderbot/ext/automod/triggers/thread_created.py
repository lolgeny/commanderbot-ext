from dataclasses import dataclass
from typing import TypeVar

from commanderbot.ext.automod import events
from commanderbot.ext.automod.automod_trigger import AutomodTrigger
from commanderbot.ext.automod.triggers.abc.thread_base import ThreadBase
from commanderbot.lib import JsonObject

ST = TypeVar("ST")


@dataclass
class ThreadCreated(ThreadBase):
    """
    Fires when an `on_thread_join` event is received without already being a member.

    See: https://discordpy.readthedocs.io/en/master/api.html#discord.on_thread_join

    Attributes
    ----------
    parent_channels
        The parent channels to match against. If empty, all channels will match.
    """

    event_types = (events.ThreadCreated,)


def create_trigger(data: JsonObject) -> AutomodTrigger:
    return ThreadCreated.from_data(data)
