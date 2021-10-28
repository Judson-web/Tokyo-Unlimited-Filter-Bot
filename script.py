class Script(object):

    START_MSG = """<b>𝘏𝘦𝘭𝘭𝘰 {},
𝘐𝘮 𝘢 𝘴𝘪𝘮𝘱𝘭𝘦 𝘣𝘰𝘵 𝘸𝘩𝘪𝘤𝘩 𝘪𝘴 𝘥𝘦𝘴𝘪𝘨𝘯𝘦𝘥 𝘢𝘯𝘥 𝘣𝘶𝘪𝘭𝘵 𝘧𝘰𝘳 𝘢𝘥𝘥𝘪𝘯𝘨 𝘧𝘪𝘭𝘵𝘦𝘳𝘴 𝘪𝘯 𝘢𝘯𝘺 𝘨𝘳𝘰𝘶𝘱.𝘏𝘪𝘵 /help 𝘧𝘰𝘳 𝘮𝘰𝘳𝘦 𝘪𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯.
"""


    HELP_MSG = """
<i>**What is a filter bot?**</i>

<b>A bot were group admins can set replies for a particular keyword and the bot will automatically send preset replies whenever that keyword enountered in the chat.</b>

<b>Usual commands:</b>

/start - Check if I'm alive!
/help - Command help!
/about - Something about me!

<b>Filter Commands;</b>

<code>/add name reply</code>  -  Add filter for name

<code>/del name</code>  -  Delete filter

<code>/delall</code>  -  Delete entire filters (Group Owner Only!)

<code>/viewfilters</code>  -  List all filters in chat

<b>Connection Commands;</b>

<code>/connect groupid</code>  -  Connect your group to my PM. You can also simply use,
<code>/connect</code> in groups.

<code>/connections</code>  -  Manage your connections.

<b>Extras;</b>

/status  -  Shows current status of your bot (Auth User Only)

/id  -  Shows ID information

<code>/info userid</code>  -  Shows User Information. Use <code>/info</code> as reply to some message for their details!

"""


    ABOUT_MSG = """<b>**🙋🏻‍♂️ 𝘏𝘦𝘭𝘭𝘰**,
    
⭕️<b>My Name :</b> Filter Bot</b>

⭕️<b>Creater :</b>  <a href="https://t.me/VAMPIRE_KING_NO_1">ƬЄƦƦƠƦ MƖƇƘЄƳ</a>

⭕️<b>Credits :</b> Everyone in this journey ☺️

⭕️<b>Language :</b> <code>Python3</code>

⭕️<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 
"""
    
    FILTERS_MSG = """<b>**Filters:**,

<b>Filter is the feature were users can set automated replies for a particular keyword and the bot will respond whenever a keyword is found the message</b>

<b>**NOTE:**</b>
<b>1. bot should have admin privillage in order to reply filters in a chat.</b>
<b>2. only admins can add filters in a chat.<b/>
<b>3. filters does support all the telegram markdowns, medias and buttons.</b>
<b>4. alert buttons are also supported with a limit of 64 characters.</b>
<b>5. there are some easter eggs, try to find it out.</b>

<b>**Commands and Usage:**</b>
<code>/add</code>   - add a filter
<code>/view</code> - list all the filters of a chat
<code>/del</code>  - delete a specific filter (separate keywords with spaces for deleting multiple filters at a time)
<code>/delall</code> - delete the whole filters in a chat (chat owner only)
"""
    
    
