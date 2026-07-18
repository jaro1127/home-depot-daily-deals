import os
from discord_webhook import DiscordWebhook, DiscordEmbed


def send_notification(categories, matching_keywords=None):
    webhook_url = os.environ["DISCORD_WEBHOOK"]

    webhook = DiscordWebhook(url=webhook_url)

    embed = DiscordEmbed(
        title="🟧 Home Depot Daily Deals",
        description="Today's featured categories",
        color="F96302",  # Home Depot orange
    )

    for category in categories:
        embed.add_embed_field(
            name="",
            value=f"• {category}",
            inline=False,
        )

    if matching_keywords:
        embed.add_embed_field(
            name="🔥 Watch List Match",
            value="\n".join(f"• {k}" for k in matching_keywords),
            inline=False,
        )

    embed.set_footer(text="https://www.homedepot.com/daily-deals")

    webhook.add_embed(embed)
    webhook.execute()
