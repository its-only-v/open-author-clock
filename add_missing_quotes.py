#!/usr/bin/env python3
import json

# Read the existing data
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Get existing times to avoid duplicates
existing_times = set()
for entry in data:
    existing_times.add(entry['time'])

# Missing times that need quotes
missing_times = [
    "00:22", "01:02", "01:03", "01:05", "01:07", "01:13", "01:14", "01:18", "01:19", "01:21",
    "01:28", "01:31", "01:34", "01:35", "01:36", "01:37", "01:39", "01:41", "01:42", "01:43",
    "01:45", "01:47", "01:48", "01:49", "01:52", "01:53", "01:55", "01:56", "01:58", "01:59",
    "02:03", "02:04", "02:06", "02:08", "02:09", "02:11", "02:14", "02:16", "02:19", "02:23",
    "02:29", "02:34", "02:38", "02:39", "02:41", "02:42", "02:44", "02:48", "02:49", "02:51",
    "02:52", "02:53", "02:54", "02:57", "03:02", "03:03", "03:06", "03:08", "03:09", "03:11",
    "03:12", "03:13", "03:16", "03:18", "03:22", "03:23", "03:24", "03:26", "03:27", "03:29",
    "03:31", "03:32", "03:48", "03:52", "03:53", "03:56", "03:59", "04:09", "04:10", "04:13",
    "04:19", "04:20", "04:21", "04:24", "04:26", "04:27", "04:28", "04:29", "04:33", "04:39",
    "04:42", "04:44", "04:49", "04:51", "04:52", "04:53", "04:56", "04:59", "05:07", "05:17",
    "05:19", "05:21", "05:22", "05:24", "05:29", "05:32", "05:33", "05:36", "05:39", "05:42",
    "05:44", "05:47", "05:48", "05:49", "05:51", "05:53", "05:54", "05:56", "05:59", "06:01",
    "06:03", "06:04", "06:06", "06:07", "06:09", "06:11", "06:12", "06:14", "06:16", "06:18",
    "06:21", "06:22", "06:23", "06:24", "06:26", "06:28", "06:31", "06:34", "06:38", "06:39",
    "06:41", "06:42", "06:44", "06:47", "06:48", "06:51", "06:52", "06:53", "06:54", "06:56",
    "06:57", "06:58", "07:01", "07:04", "07:07", "07:11", "07:16", "07:18", "07:21", "07:22",
    "07:23", "07:24", "07:26", "07:28", "07:31", "07:32", "07:33", "07:37", "07:38", "07:40",
    "07:41", "07:43", "07:44", "07:47", "07:48", "07:49", "07:52", "07:54", "07:57", "07:58",
    "08:02", "08:05", "08:06", "08:07", "08:08", "08:13", "08:14", "08:18", "08:21", "08:22",
    "08:24", "08:25", "08:31", "08:34", "08:36", "08:38", "08:42", "08:46", "08:48", "08:49",
    "08:51", "08:53", "09:01", "09:06", "09:08", "09:09", "09:10", "09:12", "09:14", "09:16",
    "09:17", "09:18", "09:19", "09:24", "09:25", "09:26", "09:29", "09:31", "09:34", "09:38",
    "09:39", "09:41", "09:43", "09:44", "09:46", "09:48", "09:49", "09:51", "09:56", "09:57",
    "10:06", "10:08", "10:09", "10:19", "10:24", "10:28", "10:33", "10:34", "10:35", "10:39",
    "10:41", "10:42", "10:44", "10:46", "10:51", "10:52", "10:54", "10:56", "10:57", "10:58",
    "10:59", "11:02", "11:04", "11:13", "11:16", "11:18", "11:21", "11:22", "11:23", "11:24",
    "11:26", "11:28", "11:33", "11:37", "11:39", "11:41", "11:43", "11:44", "11:46", "11:48",
    "11:49", "11:53", "12:06", "12:09", "12:16", "12:18", "12:19", "12:21", "12:26", "12:27",
    "12:29", "12:31", "12:34", "12:37", "12:38", "12:39", "12:41", "12:47", "12:48", "12:51",
    "12:56", "12:57", "13:07", "13:11", "13:12", "13:14", "13:19", "13:21", "13:22", "13:27",
    "13:28", "13:29", "13:31", "13:36", "13:38", "13:40", "13:41", "13:43", "13:46", "13:51",
    "13:52", "13:53", "14:03", "14:07", "14:08", "14:09", "14:11", "14:12", "14:14", "14:15",
    "14:17", "14:18", "14:21", "14:23", "14:24", "14:25", "14:26", "14:27", "14:29", "14:31",
    "14:33", "14:34", "14:35", "14:37", "14:38", "14:42", "14:43", "14:44", "14:46", "14:47",
    "14:48", "14:49", "14:51", "14:52", "14:54", "14:57", "14:59", "15:02", "15:06", "15:11",
    "15:12", "15:17", "15:18", "15:19", "15:21", "15:22", "15:24", "15:26", "15:28", "15:31",
    "15:34", "15:36", "15:38", "15:43", "15:46", "15:47", "15:48", "15:52", "16:27", "16:36",
    "16:38", "16:41", "16:44", "17:07", "17:08", "17:09", "17:11", "17:13", "17:16", "17:17",
    "17:22", "17:24", "17:26", "17:27", "17:28", "17:29", "17:31", "17:32", "17:34", "17:35",
    "17:36", "17:41", "17:44", "17:47", "17:49", "17:51", "17:52", "17:56", "18:01", "18:02",
    "18:06", "18:07", "18:09", "18:11", "18:14", "18:16", "18:17", "18:18", "18:19", "18:23",
    "18:24", "18:27", "18:28", "18:29", "18:37", "18:38", "18:39", "18:42", "18:43", "18:44",
    "18:46", "18:48", "18:52", "18:54", "19:03", "19:05", "19:06", "19:07", "19:09", "19:13",
    "19:18", "19:26", "19:27", "19:28", "19:31", "19:33", "19:34", "19:36", "19:37", "19:38",
    "19:41", "19:43", "19:44", "19:46", "19:47", "19:48", "19:51", "20:08", "20:09", "20:11",
    "20:12", "20:13", "20:19", "20:22", "20:26", "20:28", "20:31", "20:34", "20:38", "20:39",
    "20:47", "20:48", "20:51", "20:52", "20:54", "21:06", "21:07", "21:08", "21:10", "21:13",
    "21:14", "21:19", "21:21", "21:26", "21:27", "21:29", "21:33", "21:37", "21:39", "21:40",
    "21:41", "21:43", "21:44", "21:46", "21:48", "21:49", "21:51", "21:52", "21:54", "21:55",
    "21:56", "22:01", "22:04", "22:07", "22:09", "22:13", "22:16", "22:19", "22:22", "22:23",
    "22:28", "22:34", "22:36", "22:37", "22:38", "22:39", "22:42", "22:43", "22:51", "22:52",
    "22:53", "22:54", "22:56", "22:57", "23:01", "23:04", "23:06", "23:09", "23:13", "23:14",
    "23:17", "23:21", "23:23", "23:24", "23:28", "23:29", "23:37", "23:38"
]

# Sample quotes from the fictional books
quotes_pool = [
    # Metatext: Rebound by Iosefa Elgin
    {
        "quote": "At {time}, I closed the volume and wondered if perhaps true wisdom lies not in seeking the Metatext, but in understanding why it was hidden from us.",
        "title": "Metatext: Rebound",
        "author": "Iosefa Elgin"
    },
    {
        "quote": "The church bells tolled {time} as I transcribed another lost passage. Each word felt like heresy, each line a step further from salvation.",
        "title": "Metatext: Rebound",
        "author": "Iosefa Elgin"
    },
    {
        "quote": "It was {time} when I discovered the fragment describing Deneir's first doubt. No wonder they excommunicated me for seeking such truths.",
        "title": "Metatext: Rebound",
        "author": "Iosefa Elgin"
    },
    {
        "quote": "By {time}, I had catalogued seventeen contradictions in the official doctrine. The Metatext held answers they feared.",
        "title": "Metatext: Rebound",
        "author": "Iosefa Elgin"
    },
    {
        "quote": "The candle burned low, marking {time}, as I pieced together forbidden knowledge that would cost me everything.",
        "title": "Metatext: Rebound",
        "author": "Iosefa Elgin"
    },

    # The Parables of Dawnmaster Vaseid
    {
        "quote": "At {time}, Dawnmaster Vaseid raised his battleaxe high, and Lathander's light gleamed from its edge like the breaking dawn.",
        "title": "The Parables of Dawnmaster Vaseid",
        "author": "Church of Lathander"
    },
    {
        "quote": "The Blood shone with unbreakable radiance at {time}, reducing the Sharran horde to dust for us to sift from this now-holy ground.",
        "title": "The Parables of Dawnmaster Vaseid",
        "author": "Church of Lathander"
    },
    {
        "quote": "It was {time} when we finished encasing His Blood within steel—to be wielded as a most righteous cudgel against those who sit in shadow.",
        "title": "The Parables of Dawnmaster Vaseid",
        "author": "Church of Lathander"
    },
    {
        "quote": "By {time}, our simple chapel had begun its transformation into a great monastery, blessed by the light of the Morning Lord.",
        "title": "The Parables of Dawnmaster Vaseid",
        "author": "Church of Lathander"
    },
    {
        "quote": "At {time}, His light singed away the mistakes of the past, leading us toward a more fortuitous dawn indeed.",
        "title": "The Parables of Dawnmaster Vaseid",
        "author": "Church of Lathander"
    },

    # A Brush with Evil: On Hags
    {
        "quote": "It was {time} when the Green Hag first spoke to me, her words honeyed poison that I mistook for wisdom.",
        "title": "A Brush with Evil: On Hags",
        "author": "Elizabeth M. Soot"
    },
    {
        "quote": "At {time}, I realized the terrible truth: I had come to love her. That was when I knew I was truly lost.",
        "title": "A Brush with Evil: On Hags",
        "author": "Elizabeth M. Soot"
    },
    {
        "quote": "The clock read {time} in that darkened cell, where I spent two years learning what evil truly meant.",
        "title": "A Brush with Evil: On Hags",
        "author": "Elizabeth M. Soot"
    },
    {
        "quote": "By {time}, I had escaped her clutches, but I knew the coven would never forgive even the smallest of slights.",
        "title": "A Brush with Evil: On Hags",
        "author": "Elizabeth M. Soot"
    },
    {
        "quote": "At {time}, I penned these words: if you encounter a hag, do not think yourself clever. Run. And pray she does not follow.",
        "title": "A Brush with Evil: On Hags",
        "author": "Elizabeth M. Soot"
    },

    # The World in the Walls
    {
        "quote": "The clock in the hall struck {time} as Martin discovered the hidden door that would lead them all to Fillory.",
        "title": "The World in the Walls",
        "author": "Christopher Plover"
    },
    {
        "quote": "At {time}, Jane pressed her ear to the wall and heard the distant sound of silver bells from another world.",
        "title": "The World in the Walls",
        "author": "Christopher Plover"
    },
    {
        "quote": "It was {time} when the children first stepped through the grandfather clock and into a land of eternal summer.",
        "title": "The World in the Walls",
        "author": "Christopher Plover"
    },
    {
        "quote": "By {time}, they had walked the length of the great hall three times, searching for the passage back to Fillory.",
        "title": "The World in the Walls",
        "author": "Christopher Plover"
    },
    {
        "quote": "The old house creaked at {time}, and Martin knew it was calling them back to the world hidden in its walls.",
        "title": "The World in the Walls",
        "author": "Christopher Plover"
    },

    # The Girl Who Told Time
    {
        "quote": "At precisely {time}, Fiona announced that the great battle would begin, for she could see time itself like threads of gold.",
        "title": "The Girl Who Told Time",
        "author": "Christopher Plover"
    },
    {
        "quote": "It was {time} when Fiona first realized her gift was also a curse—to know the future but be powerless to change it.",
        "title": "The Girl Who Told Time",
        "author": "Christopher Plover"
    },
    {
        "quote": "The clock tower chimed {time}, but Fiona knew it was wrong. Time in Fillory bent to no earthly measurement.",
        "title": "The Girl Who Told Time",
        "author": "Christopher Plover"
    },
    {
        "quote": "By {time}, Fiona had seen tomorrow arrive three times, each version more troubling than the last.",
        "title": "The Girl Who Told Time",
        "author": "Christopher Plover"
    },
    {
        "quote": "At {time}, she told them what would come to pass, and though they believed her, they could not prevent it.",
        "title": "The Girl Who Told Time",
        "author": "Christopher Plover"
    },

    # The Flying Forest
    {
        "quote": "The trees lifted from the earth at {time}, their roots trailing through the clouds like ancient fingers.",
        "title": "The Flying Forest",
        "author": "Christopher Plover"
    },
    {
        "quote": "At {time}, Rupert climbed to the highest branch and saw the whole of Fillory spread beneath him like a living map.",
        "title": "The Flying Forest",
        "author": "Christopher Plover"
    },
    {
        "quote": "It was {time} when the forest began its migration, drifting north toward the Frozen Wastes as it did every century.",
        "title": "The Flying Forest",
        "author": "Christopher Plover"
    },
    {
        "quote": "By {time}, they had built a treehouse among the floating oaks, suspended between earth and sky.",
        "title": "The Flying Forest",
        "author": "Christopher Plover"
    },
    {
        "quote": "At {time}, the wind changed direction, and the flying forest turned back toward home.",
        "title": "The Flying Forest",
        "author": "Christopher Plover"
    },

    # The Secret Sea
    {
        "quote": "At {time}, the tide revealed stairs carved into the cliff face, descending into waters that held impossible depths.",
        "title": "The Secret Sea",
        "author": "Christopher Plover"
    },
    {
        "quote": "It was {time} when Helen discovered the underwater kingdom, where mer-people sang songs that could reshape memory.",
        "title": "The Secret Sea",
        "author": "Christopher Plover"
    },
    {
        "quote": "By {time}, they had sailed beyond the edge of the map, where the Secret Sea gave way to stranger waters still.",
        "title": "The Secret Sea",
        "author": "Christopher Plover"
    },
    {
        "quote": "The ship's bell rang {time}, though beneath the waves, all hours felt the same—eternal twilight and pressure.",
        "title": "The Secret Sea",
        "author": "Christopher Plover"
    },
    {
        "quote": "At {time}, they dove beneath the surface and found the city of glass that rose from the ocean floor.",
        "title": "The Secret Sea",
        "author": "Christopher Plover"
    },

    # The Wandering Dune
    {
        "quote": "The great dune crested the horizon at {time}, moving with the patience of geological time.",
        "title": "The Wandering Dune",
        "author": "Christopher Plover"
    },
    {
        "quote": "At {time}, Julia found the door half-buried in sand, leading to chambers that had waited centuries to be discovered.",
        "title": "The Wandering Dune",
        "author": "Christopher Plover"
    },
    {
        "quote": "It was {time} when they realized the dune was alive, conscious in ways that defied understanding.",
        "title": "The Wandering Dune",
        "author": "Christopher Plover"
    },
    {
        "quote": "By {time}, the desert had swallowed the old road completely, and the wandering dune moved ever onward.",
        "title": "The Wandering Dune",
        "author": "Christopher Plover"
    },
    {
        "quote": "At {time}, the sand shifted beneath their feet, revealing treasures from kingdoms that existed before memory.",
        "title": "The Wandering Dune",
        "author": "Christopher Plover"
    },

    # The Tale of the Seven Keys
    {
        "quote": "At {time}, the knight's daughter found the first key, hidden beneath the hearthstone where her father had trained.",
        "title": "The Tale of the Seven Keys",
        "author": "Christopher Plover"
    },
    {
        "quote": "It was {time} when she held the second key aloft, and the door to the Castle at the End of the World began to open.",
        "title": "The Tale of the Seven Keys",
        "author": "Christopher Plover"
    },
    {
        "quote": "By {time}, three keys hung from her belt, each one purchased with a greater sacrifice than the last.",
        "title": "The Tale of the Seven Keys",
        "author": "Christopher Plover"
    },
    {
        "quote": "At {time}, she understood that the seven keys unlocked not doors, but the truth of who she had always been.",
        "title": "The Tale of the Seven Keys",
        "author": "Christopher Plover"
    },
    {
        "quote": "The seventh key turned at {time}, and her father walked free from his prison, pride shining in his eyes.",
        "title": "The Tale of the Seven Keys",
        "author": "Christopher Plover"
    },

    # Practical Exercises for Young Magicians
    {
        "quote": "At {time}, begin the third etude of finger movements, focusing on the precision required for transmutation spells.",
        "title": "Practical Exercises for Young Magicians",
        "author": "Amelia Popper"
    },
    {
        "quote": "Practice the voice exercises precisely at {time}, when the throat is properly warmed but not yet fatigued.",
        "title": "Practical Exercises for Young Magicians",
        "author": "Amelia Popper"
    },
    {
        "quote": "By {time}, the novice should have mastered the seventeen foundational hand positions required for safe spellcasting.",
        "title": "Practical Exercises for Young Magicians",
        "author": "Amelia Popper"
    },
    {
        "quote": "At {time}, attempt the complex gesture sequence detailed in Chapter Seven, but only after proper supervision is arranged.",
        "title": "Practical Exercises for Young Magicians",
        "author": "Amelia Popper"
    },
    {
        "quote": "It was {time} when I first successfully completed Popper's most difficult exercise, feeling magic respond to my will.",
        "title": "Practical Exercises for Young Magicians",
        "author": "Amelia Popper"
    },

    # Poems of the Other Worlds
    {
        "quote": "At {time}, Turner wrote: 'The moon of the fourth world rises purple and slow, casting shadows that whisper of home.'",
        "title": "Poems of the Other Worlds",
        "author": "Ronald Turner"
    },
    {
        "quote": "The clock struck {time} as I read Turner's verse about the realm where time flows backward like a river.",
        "title": "Poems of the Other Worlds",
        "author": "Ronald Turner"
    },
    {
        "quote": "At {time}, his words seemed to open doorways: 'Between the worlds, in spaces undefined, the traveler finds what he left behind.'",
        "title": "Poems of the Other Worlds",
        "author": "Ronald Turner"
    },
    {
        "quote": "It was {time} when Turner penned his final poem, describing worlds beyond counting, each more strange than the last.",
        "title": "Poems of the Other Worlds",
        "author": "Ronald Turner"
    },
    {
        "quote": "By {time}, I had memorized Turner's sonnet about the city that exists simultaneously in seven different planes.",
        "title": "Poems of the Other Worlds",
        "author": "Ronald Turner"
    }
]

def time_to_string(time):
    """Convert time to descriptive string"""
    hour, minute = map(int, time.split(':'))

    if hour == 0 and minute == 0:
        return "midnight"
    elif hour == 12 and minute == 0:
        return "noon"
    elif hour < 12:
        return time + " in the morning"
    elif hour == 12:
        return time + " in the afternoon"
    elif hour < 18:
        return time + " in the afternoon"
    else:
        return time + " in the evening"

# Generate new entries
new_entries = []
for i, time in enumerate(missing_times):
    if time in existing_times:
        continue

    # Cycle through quotes pool
    template = quotes_pool[i % len(quotes_pool)]

    entry = {
        "time": time,
        "timeString": time_to_string(time),
        "quote": template["quote"].replace("{time}", time),
        "title": template["title"],
        "author": template["author"]
    }
    new_entries.append(entry)

# Add new entries to data
data.extend(new_entries)

# Sort by time
def time_to_minutes(time_str):
    hour, minute = map(int, time_str.split(':'))
    return hour * 60 + minute

data.sort(key=lambda x: time_to_minutes(x['time']))

# Write back to file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Added {len(new_entries)} new quotes to data.json")
print(f"Total entries: {len(data)}")
