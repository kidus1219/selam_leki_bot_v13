from const import TEXT_PH, MAIN_HOST

HOME = {
    'id': "home",
    'text': f"{TEXT_PH}",
    'keyboard_type': "reply",
    'keyboard': [
        [["📝New Mezmur", MAIN_HOST+"mezmurs/new/"]],
        [["📖Browse"], ["🔍Search", MAIN_HOST+"mezmurs/search"]],
        [["👥Profile"], ["⁉️Help"]],
        [["📥Contact Us"], ["🎖 Leaderboard"]],
        [["ℹ️About"]]
    ],
    'return_call': 0
}

REVIEW_MEZMUR = {
    'id': "browse",
    'text': f"""
~~~   ~~~   ~~~
{TEXT_PH}
~~~   ~~~   ~~~

{TEXT_PH}


~~~   ~~~   ~~~
ዘማሪ: {TEXT_PH}
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["✅ Submit"], TEXT_PH],
        [["Back"]]
    ],
    'return_call': 1
}

BROWSE_TITLE = {
    'id': "browse",
    'text': f"{TEXT_PH}",
    'keyboard_type': "inline",
    'keyboard': [
        [["<~", "prev"], ["~>", "next"]],
        [["Back", "back"]]
    ],
    'return_call': 2
}

BROWSE_LYRICS = {
    'id': "browse",
    'text': f"""
[ {TEXT_PH} ]   <code>{TEXT_PH}</code>
~~~   ~~~   ~~~
{TEXT_PH}
~~~   ~~~   ~~~

{TEXT_PH}
————————————
ዘማሪ: {TEXT_PH}
""",
    'keyboard_type': "inline",
    'keyboard': [
        #[["⭐️Add to Favorite", "add_to_fav"], TEXT_PH],
        [TEXT_PH],
        [["Back", "back"]]
    ],
    'return_call': 21
}

SEARCH = {
    'id': "search",
    'text': "⚠️This page is not ready yet ⚠",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
}

PROFILE = {
    'id': "setting",
    'text': f"""
👥<b>PROFILE</b>
—————————————————
<b>NAME</b> :  <code>{TEXT_PH}</code>

<b>LANG</b> :  <code>{TEXT_PH}</code>

<b>STAR</b> :  <code>{TEXT_PH}</code>🎖

<b>MY_MEZMURS</b> : <code>{TEXT_PH} Mezmurs</code>

""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': 4
}
"""
—————————————————

To <b>EDIT</b> or See <b>Details</b>
<code>press their corresponding label</code>
—————————————————
"""
PROFILE_UNREGISTERD = {
    'id': "setting",
    'text': f"""
<b>PROFILE</b>
—————————————————
<b>You have to REGISTER first!</b>

<code>clicking the button below to register</code>
—————————————————
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["REGISTER", "contact"],["Back"]]
    ],
    'return_call': 4
}

HELP = {
    'id': "help",
    'text': "⚠️This page is not ready yet ⚠",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
}

CONTACT_US = {
    'id': "contact us",
    'text': "🟩ASK Support\n🟨Give Us Feedback\n🟥Report A Bug\nusing @The_Beloved_Disciple",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
}

ABOUT = {
    'id': "about",
    'text': """
● ወእንዘ ትፈትል ወርቀወሜላት

🔻————————————————————🔻

● መልአኩ ወደ አንዲት ድንግል ተልኮ ሲመጣ ሐር እና ወርቅ ስትፈትል አገኛት ቅዱስ ገብርኤልም ሰላም ለኪ ብሎ ሰላምታን ፣ምስጋናን አቀረበ።

🔻————————————————————🔻

● እሷም የብስራቱን ቃል ከተቀበለች በኃላ መንፈስ ቅዱስን ተሞልታ እንዲህ አለች "... ከዛሬ ጀምሮ ትውልድ ሁሉ ያመሰግኑኛል... "

🔻————————————————————🔻

● እኛም ትውልድ ነን እና.. ዛሬም በመልአኩ ቃል ሰላም ለኪ እንላታለን።
ግና ሰላምታችን ፣ ምስጋናችን ፣ ውዳሴያችን በእርሷ ብቻ አያበቃም።
ሶርያዊው ሊቅ ቅድስ ኤፍሬም በዕለተ ዓርብ ዉዳሴው "... ማሕየዊ የሚያድኑን ለሆኑ ለሥላሴ መስገድን የምታስተምሪላቸው አንቺ ነሽ... " እንዳለ እኛም መስገድን ፣ ምስጋናን ከቡርሃን እናት ተምረን.. የተወደደ መስዋዕት እንዲሆንልን ተስፋ እያደረግን ለቅድስት ሥላሴ እናቀርባለን::



🟥————————————————————🟥
ተሰራ በ @The_Beloved_Disciple
🟥————————————————————🟥
    
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
}

JUST_BACK = {
    'id': "just back",
    'text': f"{TEXT_PH}",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
}

Loading = {
    'id': "Loading",
    'text': "Loading...",
    'keyboard_type': "remove",
    'keyboard': None,
    'return_call': None
}


ACCEPT_SINGLE_VALUE = {
    'id': "accept single value",
    'text': f"""
>> Enter and Send <b>{TEXT_PH}</b>
—————————————————
<code>Press Cancel to Discard</code>
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Cancel"]]
    ],
    'return_call': 1234
}

CONFIRM_INPUT = {
    'id': "confirm input",
    'text': f"""
>><b>{TEXT_PH}</b>
<code>Is This What You Entered?</code>
————————————————————
""",
    'keyboard_type': "inline",
    'keyboard': [
        [["Yes", "y"], ["No", "n"]]
    ],
    'return_call': None
}

SET_LANG = {
    'id': "confirm input",
    'text': f"""
<code>Choose Your Language</code>
————————————————————

""",
    'keyboard_type': "inline",
    'keyboard': [
        [["Amharic", "am"], ["English", "eng"]]
    ],
    'return_call': 41
}