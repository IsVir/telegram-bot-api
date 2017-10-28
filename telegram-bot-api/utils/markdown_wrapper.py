def markdown_wrapper(text: str, style: str, url: str=None, user_id: int=None) -> str:
    """
    Use this to styling message
    :param style: Set bold, italic, url, user_link, inline_code, code_block
    :param url: Use it if chosen style url
    :param user_id: Use it if chosen style user_link
    :return:
    """
    if style == 'bold':
        result = '*%s*' % text
    elif style == 'italic':
        result = '_%s_' % text
    elif style == 'url':
        result = '[%s](%s)' % (text, url)
    elif style == 'user_link':
        result = '[%s](tg://user?id=%s)' % (text, user_id)
    elif style == 'inline_code':
        result = '`%s`' % text
    elif style == 'code_block':
        result = '```block_language %s```' % text
    else:
        result = text

    return result
