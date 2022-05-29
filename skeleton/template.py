from const import TEXT_PH, MAIN_HOST

HOME = {
    'id': "home",
    'text': "Select an option",
    'keyboard_type': "reply",
    'keyboard': [
        [["New Mezmur", MAIN_HOST+"mezmurs/new/"]],
        [["Browse"], ["Search"]],
        [["Setting"], ["Help"]],
        [["Contact Us"], ["About"]]
    ],
    'return_call': 0
}

ADD_NEW = {
    'id': "add new",
    'text': "⚠️This page is not ready yet ⚠",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
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
        [["<~", "prev"], ["~>", "next"]]
    ],
    'return_call': 2
}

BROWSE_LYRICS = {
    'id': "browse",
    'text': f"""
[ {TEXT_PH} ]
~~~   ~~~   ~~~
{TEXT_PH}
~~~   ~~~   ~~~

{TEXT_PH}
""",
    'keyboard_type': "inline",
    'keyboard': [
        [TEXT_PH]
    ],
    'return_call': 2
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

SETTING = {
    'id': "setting",
    'text': "⚠️This page is not ready yet ⚠",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]]
    ],
    'return_call': None
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
