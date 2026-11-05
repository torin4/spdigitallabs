# Lucide icons (lucide.dev), inline. 24x24, stroke currentColor, width 2.
def _svg(body):
    return ('<svg class="icon" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" '
            'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round">' + body + '</svg>')
ARROW_RIGHT = _svg('<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>')
EXTERNAL = _svg('<path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>')
MAIL = _svg('<path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"/><rect x="2" y="4" width="20" height="16" rx="2"/>')
