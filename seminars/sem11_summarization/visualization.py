from IPython.core.display import display, HTML
def css_styling(path_to_css='./custom.css'):
    
    styles = open(path_to_css,'r').read()
    return HTML(styles)


def make_html(sent_tokenized_text,extracted_sentences):
    result_html = '<body>'
    for sentence in sent_tokenized_text:
        if sentence in extracted_sentences:
            result_html += '<p class="highlighted_text"> {0}.</p>'.format(sentence.replace('\n', '<br>'))
        else:
            result_html += ' {0}'.format(sentence)#'<p class="raw_text"> {0}.</p>'.format(sentence.replace('\n', '<br>'))
    return result_html + '</body>'


def highlight_sentences(sent_tokenized_text,summary_sentences):
    display(HTML(make_html(sent_tokenized_text,summary_sentences)))