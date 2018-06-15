# README

## != To review

- Probably use an `aside` over `blockquote` if not a direct quote?
    - Is the `blockquote` just for **[ACTUAL QUOTES](https://quinnlabs.com/articles/pullquotes-blockquotes-and-asides-in-html5/)**?
    - `<aside class="aside-error"></aside>`
        - Can be removed without reducing the meaning of the content
    - Or `<figure>`?

```
<aside class="aside aside-standout">
  <p class="aside-Passage">
    Always make comparisons <b class="aside-Border">explicit</b>
  </p>
</aside>
```

```
<aside class=aside aside-thumbnail">
  <p class="aside-Passage">
    <i class="aside-thumbnail">lightbulb</i> This is an exciting idea!</i>
  </p>
</aside>
```

```
<aside class="aside aside-with-notes">
  <p class="aside-Passage">
    A fancy note with a <b class="aside-Border">standout note</b>
  </p>
  <footer class="aside-Footer">
    <p class="aside-Gotcha">This is a note with something</p>
  </footer>
</aside>
```

```
<aside class="aside aside-split">
  <p class="aside-Passage">Col 1</p>
  <p class="aside-Passage">Col 2</p>
</aside>
```


View the current [HTML element reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) (may need to revise occasionally)


## Multifile reference

http://marked2app.com/help/Multi-File_Documents.html


## Visual presentation

- `b`: underlined stressed
- `i`: technical details, names, places, translation
- `mark`:
    - highlighted for reference purposes, due to its relevance in another context
        - i.e: inside a `q` or a `blockquote` to highlight pertinent passages
    - relevant to a users current activity:
        - i.e: search term, misspelled words, selected content in a web app
- `span`:
    - Blocks of content to be visually styled with css

## Importance

- `strong`: stressed, of strong importance
    - Does not change the meaning of the sentence
- `em`: stressed, emphasis on the word or sentence
    - Changes the meaning of the sentence (Cats _are_ cute)
    - Verbal stress
    - [possibly] to compare and contrast in context
- `q`: inline quotations
- `blockquote`: long form (block) quotations
    - `blockquote` > `mark`:
      - Highlight interesting parts of original text
  - `blockquote` > `b`:
      - Highlight errors or gotchas
      - `blockquote` > `b` > `mark`
  - `blockquote` > `i`:
      - Italics (!= do we need?)
- [`cite`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite): A book, research paper, essay or reference to source material
    - Can be used within a paragraph
    - [Debatable])https://stackoverflow.com/questions/5460356/html5-block-quote-with-author): Can be used within a `blockquote`
    - Could also use a `footer` in the `blockquote` with a `cite` for the source (author or work)
    - Possibly use a `<a href="#" rel="author">` tag for the author
        - Basically *no one fucking knows*

## Image sizes

`A4` @ `300ppi` = `2480 x 3508`
`A4` @ `72ppi` = `595 x 842`
