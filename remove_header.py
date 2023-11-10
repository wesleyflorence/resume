#!/usr/bin/env python3

import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Table):
        content = pf.stringify(elem)
        if 'Email :' in content and 'Mobile :' in content:
            return []  # Return an empty list to remove this element

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == '__main__':
    main()

