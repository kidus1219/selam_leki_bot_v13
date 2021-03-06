from const import TEXT_PH, MAIN_HOST

HOME = {
    'id': "home",
    'text': f"{TEXT_PH}",
    'keyboard_type': "reply",
    'keyboard': [
        [["πNew Mezmur", MAIN_HOST+"mezmurs/new/"]],
        [["πBrowse"], ["πSearch", MAIN_HOST+"mezmurs/search"]],
        [["π₯Profile"], ["βοΈHelp"]],
        [["π₯Contact Us"], ["π Leaderboard"]],
        [["βΉοΈAbout"]]
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
αααͺ: {TEXT_PH}
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["β Submit"], TEXT_PH],
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
ββββββββββββ
αααͺ: {TEXT_PH}
""",
    'keyboard_type': "inline",
    'keyboard': [
        #[["β­οΈAdd to Favorite", "add_to_fav"], TEXT_PH],
        [TEXT_PH],
        [["Back", "back"]]
    ],
    'return_call': 21
}

SEARCH = {
    'id': "search",
    'text': "β οΈThis page is not ready yet β ",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
}

PROFILE = {
    'id': "setting",
    'text': f"""
π₯<b>PROFILE</b>
βββββββββββββββββ
<b>NAME</b> :  <code>{TEXT_PH}</code>

<b>LANG</b> :  <code>{TEXT_PH}</code>

<b>STAR</b> :  <code>{TEXT_PH}</code>π

<b>MY_MEZMURS</b> : <code>{TEXT_PH} Mezmurs</code>

""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': 4
}
"""
βββββββββββββββββ

To <b>EDIT</b> or See <b>Details</b>
<code>press their corresponding label</code>
βββββββββββββββββ
"""
PROFILE_UNREGISTERD = {
    'id': "setting",
    'text': f"""
<b>PROFILE</b>
βββββββββββββββββ
<b>You have to REGISTER first!</b>

<code>clicking the button below to register</code>
βββββββββββββββββ
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["REGISTER", "contact"],["Back"]]
    ],
    'return_call': 4
}

HELP = {
    'id': "help",
    'text': "β οΈThis page is not ready yet β ",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
}

CONTACT_US = {
    'id': "contact us",
    'text': "π©ASK Support\nπ¨Give Us Feedback\nπ₯Report A Bug\nusing @The_Beloved_Disciple",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
}

ABOUT = {
    'id': "about",
    'text': """
β αα₯αα α΅αα΅α αα­ααααα΅

π»ββββββββββββββββββββπ»

β ααα α© αα° α αα²α΅ α΅ααα α°αα? α²αα£ αα­ α₯α αα­α α΅α΅αα΅α α ααα΅ αα±α΅ αα₯α­α€αα α°αα ααͺ α₯α α°ααα³α α£αα΅ααα α αα¨α α’

π»ββββββββββββββββββββπ»

β α₯α·α α¨α₯α΅α«α±α αα α¨α°αα αα½ α αα αααα΅ αα±α΅α α°ααα³ α₯αα²α α αα½ "... α¨αα¬ ααα? α΅ααα΅ αα α«αα°αααα... "

π»ββββββββββββββββββββπ»

β α₯αα α΅ααα΅ αα α₯α.. αα¬α α ααα α© αα α°αα ααͺ α₯ααα³ααα’
αα α°ααα³α½α α£ αα΅ααα½α α£ αα³α΄α«α½α α α₯α­α· α₯α» α α«α ααα’
αΆα­α«αα αα αα΅α΅ α€αα¬α α ααα° αα­α₯ αα³α΄α "... ααα¨α α¨αα«α΅αα ααα αα₯αα΄ αα΅αα΅α α¨αα³α΅α°ααͺααΈα α ααΊ αα½... " α₯αα³α α₯αα αα΅αα΅α α£ αα΅ααα α¨α‘α­αα α₯αα΅ α°αα¨α.. α¨α°αα°α° αα΅ααα΅ α₯αα²αααα α°α΅α α₯α«α°α¨αα ααα΅α΅α΅ α₯αα΄ α₯ααα­α£αα::



π₯ββββββββββββββββββββπ₯
α°α°α« α  @The_Beloved_Disciple
π₯ββββββββββββββββββββπ₯
    
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
βββββββββββββββββ
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
ββββββββββββββββββββ
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
ββββββββββββββββββββ

""",
    'keyboard_type': "inline",
    'keyboard': [
        [["Amharic", "am"], ["English", "eng"]]
    ],
    'return_call': 41
}