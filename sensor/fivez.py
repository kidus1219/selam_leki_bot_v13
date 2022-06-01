from skeleton import template
from skeleton.view import View


def home(update, _):
    return View(template.HELP).printer(update.effective_chat.id)
