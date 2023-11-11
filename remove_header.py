#!/usr/bin/env python3

import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Table):
        content = pf.stringify(elem)
        if 'Email :' in content and 'Mobile :' in content:
            return []  # Return an empty list to remove this element

        # This function will be used to wrap text in Div and convert to Para for proper HTML structure
        def wrap_in_div(text, class_name):
            return pf.Div(pf.Para(pf.Str(text)), classes=[class_name])

        divs = []
        for row in elem.content:
            if len(row.content) >= 2:
                cells = row.content

                organization = pf.stringify(cells[0].content[0]).strip()
                location = pf.stringify(cells[0].content[1]).strip()
                organization_div = wrap_in_div(organization, 'resume-organization')
                location_div = wrap_in_div(location, 'resume-location')

                sub_divs = []
                for subcell in cells[1:]:
                    title = pf.stringify(subcell.content[0]).strip()
                    timeframe = pf.stringify(subcell.content[1]).strip()
                    title_div = wrap_in_div(title, 'resume-title')
                    timeframe_div = wrap_in_div(timeframe, 'resume-timeframe')
                    sub_divs.append(title_div)
                    sub_divs.append(timeframe_div)
                entry_div = pf.Div(organization_div, location_div, *sub_divs, classes=['resume-header-entry'])
                divs.append(entry_div)

        return divs

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == '__main__':
    main()

