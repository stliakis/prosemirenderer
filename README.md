Python prosemirror to HTML or plain text renderer

### Installation

`pip install git+https://github.com/stliakis/prosemirenderer.git --upgrade`

or add the following to your requirements.txt

`git+ssh://git@github.com/stliakis/prosemirenderer.git`

### Usage(Prosemirror->HTML)

The following will render the prosemirror json to HTML

```python
from prosemirenderer.renderers import ProseMirror2HTML

ProseMirror2HTML().render(
    prosemirror_document
)

```

#### Generated HTML

```html
<h2>Heading</h2><p>list</p>
<ul>
    <li><p>1</p></li>
    <li><p>2</p></li>
</ul>
<p></p>
<p>
    <strong>strong text</strong>
</p>
```

### Usage(Prosemirror->Plain text)

The following will render the prosemirror json to plain text

```python
from prosemirenderer.renderers import ProseMirror2Plain

ProseMirror2Plain().render(
    prosemirror_document
)

```

#### Generated Plain text

```html
Heading
list

  • 1
  • 2

strong text

```

```python
prosemirror_document = {
    "type": "doc",
    "content": [
        {
            "type": "heading",
            "attrs": {
                "level": 2
            },
            "content": [
                {
                    "type": "text",
                    "text": "Heading"
                }
            ]
        },
        {
            "type": "paragraph",
            "content": [
                {
                    "type": "text",
                    "text": "list"
                }
            ]
        },
        {
            "type": "bullet_list",
            "content": [
                {
                    "type": "list_item",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "1"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "list_item",
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "2"
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "type": "paragraph"
        },
        {
            "type": "paragraph",
            "content": [
                {
                    "type": "text",
                    "marks": [
                        {
                            "type": "bold"
                        }
                    ],
                    "text": "strong text"
                }
            ]
        }
    ]
}

```
