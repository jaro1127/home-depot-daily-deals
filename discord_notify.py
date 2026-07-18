import os
from datetime import datetime

from discord_webhook import DiscordWebhook, DiscordEmbed


def send_notification(categories, matching_keywords=None):
    webhook = DiscordWebhook(url=os.environ["DISCORD_WEBHOOK"])

    embed = DiscordEmbed(
        title="🟧 Home Depot Daily Deals",
        color="F96302"
    )

    embed.set_description(
        f"**{datetime.now().strftime('%A, %B %d, %Y')}**"
    )

    embed.add_embed_field(
        name="Today's Featured Categories",
        value="\n".join(f"• {c}" for c in categories),
        inline=False,
    )

    if matching_keywords:
        embed.add_embed_field(
            name="🔥 Watch List Matches",
            value="\n".join(f"• {m}" for m in matching_keywords),
            inline=False,
        )

    embed.add_embed_field(
        name="Link",
        value="https://www.homedepot.com/daily-deals",
        inline=False,
    )

    webhook.add_embed(embed)
    webhook.execute()
