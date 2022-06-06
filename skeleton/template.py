from const import TEXT_PH, MAIN_HOST

HOME = {
    'id': "home",
    'text': f"{TEXT_PH}",
    'keyboard_type': "reply",
    'keyboard': [
        [["📝New Mezmur", MAIN_HOST+"mezmurs/new/"]],
        [["📖Browse"], ["🔍Search", MAIN_HOST+"mezmurs/search"]],
        [["👥Profile"], ["⁉️Help"]],
        [["📥Contact Us"], ["ℹ️About"]],
        #[["ℹ️About"]]
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

—————————————————

To <b>EDIT</b> or See <b>Details</b>
<code>press their corresponding label</code>
—————————————————
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': 4
}

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
    'text': "⚠️This page is not ready yet ⚠",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
}

ABOUT = {
    'id': "about",
    'text': "⚠️This page is not ready yet ⚠",
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