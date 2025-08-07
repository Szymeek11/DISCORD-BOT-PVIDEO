import discord
from datetime import datetime as d
from w import w


def m(k, ka):
    async def on_message(w):
        if w.author.bot or w.channel.id != ka:
            return
        z = w.content.lower()
        if any(q in z for q in k):
            e = discord.Embed(
                title="PUREVIDEO | Jak pobrać aplikację?",
                description=(
                    "**Kroki do pobrania:**\n\n"
                    "1️⃣ Wejdź na stronę: https://majusss.github.io\n"
                    "2️⃣ Kliknij przycisk **Sprawdź wydania**\n"
                    "3️⃣ Przejdź do zakładki **Deweloperskie**\n"
                    "4️⃣ Wybierz najnowszą wersję\n"
                    "5️⃣ Przewiń niżej i pobierz aplikację z sekcji **Artifacts**"
                ),
                color=0xc800ff,
            )
            e.set_footer(text=f"PUREVIDEO • FILMY I SERIALE • {d.now().strftime('%d-%m-%Y')}")
            e.set_image(url="https://media.discordapp.net/attachments/1402383493765529742/1402891583241584671/image.png?ex=68959019&is=68943e99&hm=cbc3922c7f37ef3e99d79db09b241dbf897d1a77ab7eb83b394734a334e3d4f5&=&format=webp&quality=lossless")
            await w.channel.send(embed=e)
    return on_message
